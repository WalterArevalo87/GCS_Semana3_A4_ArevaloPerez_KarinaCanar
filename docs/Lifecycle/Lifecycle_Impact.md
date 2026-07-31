# Impacto del Cambio en el Ciclo de Desarrollo del Sistema ATM

## 1. Cambio seleccionado

Se simuló la solicitud de cambio `CR-001`, orientada a incorporar el requisito no funcional `RNF-PERF-01`: el 95 % de las consultas de saldo y validaciones de retiro deberá responder en un tiempo máximo de 2 segundos bajo condiciones normales de operación.

Este cambio busca mejorar la eficiencia del sistema ATM y establecer un criterio cuantificable que pueda verificarse mediante pruebas.

## 2. Análisis del impacto por fase

| Fase | ¿Qué cambia? | EC afectados | Riesgo si no se controla | Evidencia de validación |
|---|---|---|---|---|
| Requisitos | Se incorpora el requisito `RNF-PERF-01` y su criterio de aceptación. | `SRS_ATM_v1.md`, `Quality_Model.md` | El requisito puede interpretarse de forma diferente y generar retrabajo. | Checklist y revisión del requisito. |
| Diseño | Se definen los puntos donde se medirá el tiempo de respuesta de las operaciones. | `SRS_ATM_v1.md`, `/src`, `conf.example.json` | El diseño podría incluir procesos innecesarios que retrasen las operaciones. | Revisión técnica del flujo de consulta y retiro. |
| Implementación | Se ajusta el procesamiento de consultas y validaciones para cumplir el tiempo establecido. | `/src`, `conf.example.json` | Pueden producirse errores, lentitud o resultados inconsistentes. | Revisión del código y commit asociado al cambio. |
| Pruebas | Se incorpora una prueba que mida el tiempo de respuesta en al menos 100 ejecuciones. | `/tests`, `Quality_Model.md` | No existiría evidencia objetiva de que el requisito se cumple. | Resultado de la prueba y captura de ejecución. |
| Despliegue y mantenimiento | Se registra el cambio y se controla que futuras versiones mantengan el rendimiento esperado. | `CHANGELOG.md`, `/config`, `/tests` | Una actualización posterior podría afectar el rendimiento sin ser detectada. | Historial de commits, registro de cambios y pruebas de regresión. |

## 3. Trazabilidad del cambio

| Elemento | Identificador | Relación |
|---|---|---|
| Solicitud de cambio | `CR-001` | Origina la mejora de rendimiento. |
| Requisito no funcional | `RNF-PERF-01` | Define el tiempo máximo de respuesta. |
| Métrica de calidad | `MC-PERF-01` | Verifica que el 95 % de las operaciones responda en ≤ 2 segundos. |
| Prueba relacionada | `TEST-PERF-01` | Mide el tiempo de respuesta en 100 ejecuciones. |
| Evidencia | Captura de ejecución | Demuestra el resultado obtenido. |

## 4. Criterios de aceptación

El cambio se considerará aprobado cuando:

- El requisito `RNF-PERF-01` esté documentado y sea verificable.
- Se ejecuten al menos 100 consultas o validaciones simuladas.
- Como mínimo, 95 de las 100 operaciones respondan en 2 segundos o menos.
- No se presenten errores ni registros duplicados durante la prueba.
- El cambio quede identificado mediante un commit posterior a la línea base `v1.0`.

## 5. Control del cambio

El análisis se documentará antes de establecer la línea base. Después de crear el tag `v1.0`, el cambio deberá implementarse en los requisitos y pruebas, actualizarse en `CHANGELOG.md` y registrarse mediante un commit independiente. De esta manera podrá demostrarse la diferencia entre la versión aprobada y la modificación posterior.