# Especificación de Requisitos del Sistema ATM

## 1. Propósito

Este documento define los requisitos funcionales y no funcionales de un prototipo de cajero automático (ATM). Su finalidad es establecer el alcance inicial del sistema y facilitar la trazabilidad entre requisitos, código, pruebas y métricas de calidad.

## 2. Alcance

El sistema permitirá autenticar al usuario mediante una tarjeta y un PIN, consultar el saldo disponible, realizar retiros y registrar las transacciones efectuadas. El prototipo no procesará dinero real ni se conectará con redes bancarias externas.

## 3. Actores

| Actor | Responsabilidad |
|---|---|
| Cliente | Se autentica, consulta su saldo y realiza retiros. |
| Administrador | Revisa la configuración y los registros del sistema. |
| Sistema ATM | Valida las operaciones, actualiza el saldo y registra las transacciones. |

## 4. Requisitos funcionales

| ID | Requisito | Criterio de aceptación | Prioridad |
|---|---|---|---|
| `RF-001` | El sistema deberá autenticar al cliente mediante su número de tarjeta y PIN. | El acceso se autoriza únicamente cuando ambos datos sean válidos. | Alta |
| `RF-002` | El sistema deberá bloquear temporalmente el acceso después de tres intentos fallidos consecutivos. | En el cuarto intento, el sistema deberá impedir el ingreso y mostrar un mensaje de bloqueo. | Alta |
| `RF-003` | El sistema deberá permitir al cliente consultar el saldo disponible. | Después de una autenticación válida, se deberá mostrar el saldo correspondiente a la cuenta. | Alta |
| `RF-004` | El sistema deberá permitir retiros cuando exista saldo suficiente. | El retiro se aprobará únicamente si el monto es mayor que cero y no supera el saldo disponible. | Alta |
| `RF-005` | El sistema deberá actualizar el saldo después de aprobar un retiro. | El nuevo saldo deberá ser igual al saldo anterior menos el valor retirado. | Alta |
| `RF-006` | El sistema deberá registrar cada retiro realizado. | El registro deberá contener identificador, fecha, monto, estado y saldo resultante. | Media |

## 5. Requisitos no funcionales

| ID | Atributo | Requisito verificable | Evidencia |
|---|---|---|---|
| `RNF-SEG-01` | Seguridad | El sistema deberá mantener cero PIN o credenciales almacenados en texto plano. | Revisión del código y la configuración. |
| `RNF-SEG-02` | Seguridad | El acceso deberá bloquearse después de tres intentos fallidos consecutivos. | Prueba automatizada de autenticación. |
| `RNF-FIA-01` | Fiabilidad | Al menos 99 de 100 transacciones simuladas deberán finalizar sin errores ni registros duplicados. | Resultado de las pruebas de transacciones. |
| `RNF-USA-01` | Capacidad de interacción | El usuario deberá completar un retiro siguiendo como máximo cinco pasos desde la autenticación. | Revisión del flujo funcional. |
| `RNF-MAN-01` | Mantenibilidad | Las funciones críticas deberán alcanzar una cobertura de pruebas mínima del 70 %. | Reporte de cobertura de pruebas. |

> Nota: el requisito de rendimiento `RNF-PERF-01` se incorporará mediante el cambio controlado `CR-001`, después de establecer la línea base `v1.0`.

## 6. Reglas de negocio

| ID | Regla |
|---|---|
| `RN-001` | El PIN deberá validarse sin almacenarse ni mostrarse en texto plano. |
| `RN-002` | El monto solicitado deberá ser mayor que cero. |
| `RN-003` | No se permitirá retirar un valor superior al saldo disponible. |
| `RN-004` | El saldo se actualizará solamente cuando el retiro sea aprobado. |
| `RN-005` | Cada retiro aprobado deberá generar un único registro de transacción. |

## 7. Trazabilidad inicial

| Requisito | Componente relacionado | Prueba prevista | Métrica de calidad |
|---|---|---|---|
| `RF-001`, `RF-002` | Módulo de autenticación | Prueba de acceso válido, inválido y bloqueo | Cero accesos no autorizados |
| `RF-003` | Módulo de consulta | Prueba de consulta de saldo | 100 % de consultas correctas |
| `RF-004`, `RF-005` | Módulo de retiros | Prueba de retiro válido y saldo insuficiente | 99 de 100 operaciones sin errores |
| `RF-006` | Registro de transacciones | Prueba de registro único | Cero registros duplicados |
| `RNF-MAN-01` | Código fuente y pruebas | Reporte de cobertura | Cobertura mínima del 70 % |

## 8. Control del documento

| Versión | Descripción | Estado |
|---|---|---|
| `1.0` | Definición inicial de requisitos del sistema ATM | Propuesto para línea base |