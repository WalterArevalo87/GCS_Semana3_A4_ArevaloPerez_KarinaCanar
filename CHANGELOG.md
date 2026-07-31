# Registro de cambios

En este archivo se documentan los cambios relevantes realizados en el proyecto del sistema de cajero automático (ATM).

## [Sin publicar]

### Añadido

- Solicitud de cambio `CR-001` para incorporar un criterio medible de rendimiento.
- Requisito no funcional `RNF-PERF-01` en `docs/SRS/SRS_ATM_v1.md`.
- Métrica `MC-PERF-01` en `docs/Quality/Quality_Model.md`.
- Prueba automatizada `TEST-PERF-01` en `tests/test_atm.py`, mediante la medición individual de 100 operaciones.

### Verificado

- Cumplimiento mínimo de 95 operaciones ejecutadas en un máximo de 2 segundos cada una.
- Ejecución satisfactoria de las 12 pruebas automatizadas.
- Conservación de la línea base `v1.0` sin modificaciones.

## [v1.0] - 2026-07-31

### Añadido

- Plan de Gestión de Configuración.
- Inventario de elementos de configuración.
- Especificación de requisitos funcionales y no funcionales.
- Modelo de calidad basado en ISO/IEC 25010:2023.
- Análisis del impacto de los cambios en el ciclo de desarrollo.
- Código fuente del prototipo ATM.
- Configuración de referencia del sistema.
- Once pruebas automatizadas de autenticación, saldo, retiros, sesiones y seguridad.
- Documentación general del proyecto.
- Línea base identificada mediante el tag `v1.0`.