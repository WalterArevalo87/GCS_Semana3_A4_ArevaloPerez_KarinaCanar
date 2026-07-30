# Sistema de Cajero Automático (ATM)

## Descripción

Este repositorio contiene la estructura inicial de un sistema de cajero automático (ATM), organizado mediante prácticas de Gestión de Configuración de Software. El proyecto contempla documentación, código fuente, pruebas, parámetros de configuración y control de versiones.

## Objetivo

Aplicar procedimientos de identificación, versionamiento y control de cambios sobre los elementos de configuración del sistema ATM, manteniendo la trazabilidad de los aportes realizados por el equipo.

## Alcance

El sistema contempla las siguientes funciones:

- Autenticación del usuario.
- Consulta de saldo.
- Retiro de efectivo.
- Registro de transacciones.
- Control de seguridad y auditoría.
- Configuración de red, base de datos y hardware.

## Estructura del repositorio

- `config/`: parámetros de configuración del sistema.
- `docs/`: requisitos y documentación técnica.
- `src/`: código fuente.
- `tests/`: pruebas del sistema.
- `CM_PLAN.md`: plan de Gestión de Configuración.
- `CHANGELOG.md`: registro de cambios.
- `README.md`: descripción general del proyecto.

## Configuración

El archivo `config/conf.example.json` contiene valores de referencia para la red, la base de datos PostgreSQL, la seguridad, la auditoría y los dispositivos del ATM. No deben almacenarse contraseñas ni credenciales reales en el repositorio.

## Control de versiones

- La rama principal del proyecto es `main`.
- Cada cambio debe registrarse mediante un commit descriptivo.
- Antes de modificar archivos se debe actualizar el repositorio local.
- La primera línea base aprobada se identificará con el tag `v1.0`.
- Los cambios relevantes deberán registrarse en `CHANGELOG.md`.

## Estado del proyecto

En desarrollo.

## Integrantes

- Walter Arévalo Pérez
- Karina Cañar