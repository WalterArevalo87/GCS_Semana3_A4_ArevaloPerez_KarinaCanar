import unittest

from decimal import Decimal

from src.atm import ATM

from time import perf_counter

class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM()
        self.card_number = "100200300"
        self.pin = "2580"
        self.atm.register_account(
            self.card_number,
            self.pin,
            Decimal("1000.00")
        )

    def test_authenticates_valid_credentials(self):
        result = self.atm.authenticate(self.card_number, self.pin)

        self.assertTrue(result)

    def test_rejects_invalid_pin(self):
        result = self.atm.authenticate(self.card_number, "0000")

        self.assertFalse(result)

    def test_blocks_account_after_three_failed_attempts(self):
        for _ in range(3):
            self.assertFalse(
                self.atm.authenticate(self.card_number, "0000")
            )

        account = self.atm.accounts[self.card_number]

        self.assertTrue(account.blocked)
        self.assertFalse(
            self.atm.authenticate(self.card_number, self.pin)
        )

    def test_requires_authentication_to_check_balance(self):
        with self.assertRaises(PermissionError):
            self.atm.get_balance(self.card_number)

    def test_returns_balance_after_authentication(self):
        self.atm.authenticate(self.card_number, self.pin)

        balance = self.atm.get_balance(self.card_number)

        self.assertEqual(balance, Decimal("1000.00"))

    def test_withdrawal_updates_balance(self):
        self.atm.authenticate(self.card_number, self.pin)

        transaction = self.atm.withdraw(
            self.card_number,
            Decimal("150.00")
        )

        self.assertEqual(
            transaction["resulting_balance"],
            Decimal("850.00")
        )
        self.assertEqual(
            self.atm.get_balance(self.card_number),
            Decimal("850.00")
        )

    def test_withdrawal_creates_single_transaction(self):
        self.atm.authenticate(self.card_number, self.pin)

        self.atm.withdraw(self.card_number, Decimal("100.00"))
        transactions = self.atm.get_transactions(self.card_number)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["status"], "APPROVED")

    def test_rejects_withdrawal_above_available_balance(self):
        self.atm.authenticate(self.card_number, self.pin)

        with self.assertRaises(ValueError):
            self.atm.withdraw(
                self.card_number,
                Decimal("1200.00")
            )

    def test_rejects_non_positive_withdrawal(self):
        self.atm.authenticate(self.card_number, self.pin)

        for amount in (Decimal("0"), Decimal("-10.00")):
            with self.subTest(amount=amount):
                with self.assertRaises(ValueError):
                    self.atm.withdraw(self.card_number, amount)

    def test_logout_invalidates_session(self):
        self.atm.authenticate(self.card_number, self.pin)
        self.atm.logout(self.card_number)

        with self.assertRaises(PermissionError):
            self.atm.get_balance(self.card_number)

    def test_pin_is_not_stored_in_plain_text(self):
        account = self.atm.accounts[self.card_number]

        self.assertFalse(hasattr(account, "pin"))
        self.assertNotEqual(account.pin_hash, self.pin.encode())

    def test_perf_01_completes_95_of_100_operations_within_two_seconds(self):
        self.assertTrue(
            self.atm.authenticate(self.card_number, self.pin)
        )
        response_times = []

        for _ in range(100):
            start_time = perf_counter()
            balance = self.atm.get_balance(self.card_number)
            elapsed_time = perf_counter() - start_time

            response_times.append(elapsed_time)
            self.assertEqual(balance, Decimal("1000.00"))

        operations_within_limit = sum(
            elapsed_time <= 2.0
            for elapsed_time in response_times
        )
        compliance_percentage = (
            operations_within_limit / len(response_times)
        ) * 100

        self.assertEqual(len(response_times), 100)
        self.assertGreaterEqual(
            compliance_percentage,
            95.0,
            (
                f"Solo {operations_within_limit} de 100 operaciones "
                "finalizaron en un máximo de 2 segundos."
            )
        )

if __name__ == "__main__":
    unittest.main()