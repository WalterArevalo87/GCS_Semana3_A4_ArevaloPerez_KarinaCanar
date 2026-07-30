# Modelo de Calidad del Sistema ATM

## 1. Modelo seleccionado

Para evaluar la calidad del sistema de cajero automático se adoptó el modelo de calidad del producto ISO/IEC 25010:2023. De sus características se seleccionaron seis, considerando la operación, seguridad y mantenimiento del sistema ATM.

## 2. Atributos y métricas de calidad

| Atributo | Definición | Métrica verificable | EC relacionados |
|---|---|---|---|
| Adecuación funcional | Capacidad para ejecutar correctamente las funciones requeridas. | El 100 % de las pruebas de autenticación, consulta, retiro y registro debe aprobarse. | `SRS_ATM_v1.md`, `/src`, `/tests` |
| Eficiencia de desempeño | Uso adecuado del tiempo y los recursos durante la operación. | El 95 % de las consultas de saldo y validaciones de retiro debe responder en ≤ 2 segundos. | `SRS_ATM_v1.md`, `/src`, `/tests` |
| Fiabilidad | Capacidad para operar de forma estable y registrar correctamente las transacciones. | Al menos 99 de 100 transacciones simuladas deben finalizar sin errores ni registros duplicados. | `/src`, `/tests`, `/config` |
| Seguridad | Protección de credenciales, transacciones y accesos del usuario. | Debe existir 0 credenciales o PIN almacenados en texto plano y bloquearse el acceso después de 3 intentos fallidos. | `conf.example.json`, `/src`, `/tests` |
| Capacidad de interacción | Facilidad con la que el usuario comprende y utiliza las funciones del ATM. | Al menos 9 de 10 usuarios deben completar un retiro sin ayuda y en un tiempo máximo de 1 minuto. | `SRS_ATM_v1.md`, `/src`, `/tests` |
| Mantenibilidad | Facilidad para analizar, corregir y modificar el sistema sin generar fallos. | La cobertura de pruebas debe ser ≥ 70 % en las funciones críticas y no deben existir pruebas fallidas antes de integrar cambios. | `/src`, `/tests`, `CM_PLAN.md` |

## 3. Métricas clave

### Métrica estrella 1: seguridad de las credenciales

El sistema deberá mantener 0 credenciales o PIN en texto plano y bloquear el acceso después de tres intentos fallidos. Esta métrica es prioritaria porque un acceso no autorizado puede comprometer la información y los fondos del usuario.

### Métrica estrella 2: tiempo de respuesta

El 95 % de las consultas de saldo y validaciones de retiro deberá responder en un tiempo máximo de 2 segundos. Esta métrica permite comprobar que las operaciones frecuentes se procesan con agilidad.

## 4. Validación

Las métricas se comprobarán mediante pruebas funcionales, de rendimiento, seguridad y usabilidad. Los resultados y evidencias deberán conservarse en la carpeta `/tests` y relacionarse con los requisitos definidos en `SRS_ATM_v1.md`.

## 5. Referencia

International Organization for Standardization. (2023). *Systems and software engineering—Systems and software Quality Requirements and Evaluation (SQuaRE)—Product quality model* (ISO/IEC Standard No. 25010:2023). https://www.iso.org/standard/78176.html