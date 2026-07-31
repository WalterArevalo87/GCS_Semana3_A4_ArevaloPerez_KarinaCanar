Plan de Gestión de Configuración

1. Información general

Proyecto: Sistema de cajero automático (ATM)
Repositorio: GCS_Semana3_A4_ArevaloPerez_KarinaCanar
Rama principal: main
Línea base prevista: v1.0

2. Objetivo

Establecer los criterios para identificar, modificar, versionar y controlar los elementos de configuración del sistema ATM, de manera que cada cambio pueda ser revisado y rastreado durante el desarrollo.

3. Alcance

Este plan comprende los requisitos, la documentación de calidad, el análisis del ciclo de desarrollo, el código fuente, las pruebas, la configuración y los registros de cambios del proyecto.

4. Elementos de configuración

| ID | Archivo o elemento | Ubicación | Justificación | Responsable |
|---|---|---|---|---|
| `EC-01` | `SRS_ATM_v1.md` | `/docs/SRS/` | Define los requisitos del sistema ATM; sus cambios afectan el alcance, el código y las pruebas. | Analista / Product Owner |
| `EC-02` | `Quality_Model.md` | `/docs/Quality/` | Establece los atributos y las métricas utilizadas para evaluar la calidad del sistema. | QA / Responsable de calidad |
| `EC-03` | `Lifecycle_Impact.md` | `/docs/Lifecycle/` | Documenta el impacto de un cambio en cada fase del ciclo de desarrollo. | Analista / Líder técnico |
| `EC-04` | `atm.py` | `/src/` | Contiene la lógica de autenticación, consulta de saldo, retiros y registro de transacciones. | Desarrollador |
| `EC-05` | `test_atm.py` | `/tests/` | Verifica los requisitos funcionales y permite detectar errores o regresiones. | QA / Desarrollador |
| `EC-06` | `conf.example.json` | `/config/` | Define parámetros de red, base de datos, seguridad, auditoría y hardware. | DevOps / Desarrollador |
| `EC-07` | `CM_PLAN.md` | Raíz del repositorio | Establece las reglas para identificar, versionar y controlar los cambios. | Responsable de configuración |
| `EC-08` | `CHANGELOG.md` | Raíz del repositorio | Registra la evolución y los cambios incorporados en cada versión. | Responsable de configuración / Equipo |


5. Reglas de identificación y versionado

Los archivos deberán conservar nombres claros y relacionados con su función.
La rama main contendrá la versión integrada y revisada del proyecto.
Los commits utilizarán mensajes descriptivos, por ejemplo: docs: add configuration items.
El archivo conf.example.json no deberá contener contraseñas ni credenciales reales.
La versión aprobada se identificará mediante el tag v1.0.
Los cambios posteriores a la línea base deberán registrarse en nuevos commits.

6. Control de cambios

Para realizar un cambio se seguirá este procedimiento:

Descargar la versión actualizada del repositorio.
Identificar el requisito y los elementos de configuración afectados.
Modificar únicamente los archivos asignados.
Revisar y probar el cambio realizado.
Registrar el cambio mediante un commit con un mensaje claro.
Publicar el commit en el repositorio remoto.
Actualizar CHANGELOG.md cuando el cambio afecte una funcionalidad o una versión.

7. Responsabilidades
Analista: mantiene actualizados los requisitos y analiza el impacto de los cambios.
Desarrollador: modifica el código fuente y la configuración técnica.
QA: define métricas, ejecuta pruebas y conserva las evidencias.
Responsable de configuración: revisa los commits, controla el historial y crea la línea base.
Equipo: revisa los elementos antes de aprobar la versión v1.0.

8. Línea base

La línea base v1.0 se creará cuando los elementos de configuración estén completos, revisados y publicados. 
Esta versión representará el estado aprobado del proyecto.
Los cambios posteriores deberán generar un nuevo commit y no podrán alterar el tag ya creado.
