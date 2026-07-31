from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import hmac
import os
from uuid import uuid4


@dataclass
class Account:
    card_number: str
    pin_salt: bytes
    pin_hash: bytes
    balance: Decimal
    failed_attempts: int = 0
    blocked: bool = False
    transactions: list[dict] = field(default_factory=list)


class ATM:
    MAX_ATTEMPTS = 3

    def __init__(self):
        self.accounts: dict[str, Account] = {}
        self.active_sessions: set[str] = set()

    @staticmethod
    def _hash_pin(pin: str, salt: bytes) -> bytes:
        return hashlib.pbkdf2_hmac(
            "sha256",
            pin.encode("utf-8"),
            salt,
            100_000
        )

    def register_account(
        self,
        card_number: str,
        pin: str,
        initial_balance
    ) -> None:
        if card_number in self.accounts:
            raise ValueError("The card is already registered.")

        if len(pin) < 4:
            raise ValueError("The PIN must contain at least four characters.")

        salt = os.urandom(16)

        self.accounts[card_number] = Account(
            card_number=card_number,
            pin_salt=salt,
            pin_hash=self._hash_pin(pin, salt),
            balance=Decimal(str(initial_balance))
        )

    def authenticate(self, card_number: str, pin: str) -> bool:
        account = self.accounts.get(card_number)

        if account is None or account.blocked:
            return False

        entered_hash = self._hash_pin(pin, account.pin_salt)

        if hmac.compare_digest(entered_hash, account.pin_hash):
            account.failed_attempts = 0
            self.active_sessions.add(card_number)
            return True

        account.failed_attempts += 1
        self.active_sessions.discard(card_number)

        if account.failed_attempts >= self.MAX_ATTEMPTS:
            account.blocked = True

        return False

    def get_balance(self, card_number: str) -> Decimal:
        account = self._require_active_session(card_number)
        return account.balance

    def withdraw(self, card_number: str, amount) -> dict:
        account = self._require_active_session(card_number)
        withdrawal_amount = Decimal(str(amount))

        if withdrawal_amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero.")

        if withdrawal_amount > account.balance:
            raise ValueError("Insufficient balance.")

        account.balance -= withdrawal_amount

        transaction = {
            "id": str(uuid4()),
            "date": datetime.now(timezone.utc).isoformat(),
            "amount": withdrawal_amount,
            "status": "APPROVED",
            "resulting_balance": account.balance
        }

        account.transactions.append(transaction)
        return transaction

    def get_transactions(self, card_number: str) -> list[dict]:
        account = self._require_active_session(card_number)
        return list(account.transactions)

    def logout(self, card_number: str) -> None:
        self.active_sessions.discard(card_number)

    def _require_active_session(self, card_number: str) -> Account:
        if card_number not in self.active_sessions:
            raise PermissionError("The user must authenticate first.")

        return self.accounts[card_number]