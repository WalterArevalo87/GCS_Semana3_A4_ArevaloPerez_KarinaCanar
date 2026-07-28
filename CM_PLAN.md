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

### EC-01. Requisitos del sistema
- **Archivo:** `SRS_ATM_v1.md`
- **Ubicación:** `/docs/SRS/`
- **Justificación:** Define los requisitos del sistema ATM. Sus cambios pueden afectar el alcance, el código y las pruebas.
- **Responsable:** Analista / Product Owner.

### EC-02. Modelo de calidad
- **Archivo:** `Quality_Model.md`
- **Ubicación:** `/docs/Quality/`
- **Justificación:** Establece los atributos y métricas utilizados para evaluar la calidad del sistema.
- **Responsable:** QA / Responsable de calidad.

### EC-03. Impacto en el ciclo de vida
- **Archivo:** `Lifecycle_Impact.md`
- **Ubicación:** `/docs/Lifecycle/`
- **Justificación:** Registra cómo afecta un cambio a cada fase del desarrollo.
- **Responsable:** Analista / Líder técnico.

### EC-04. Código fuente
- **Elemento:** Código fuente del ATM
- **Ubicación:** `/src/`
- **Justificación:** Contiene la lógica y las operaciones principales del sistema.
- **Responsable:** Desarrollador.

### EC-05. Pruebas
- **Elemento:** Pruebas del ATM
- **Ubicación:** `/tests/`
- **Justificación:** Permiten comprobar los requisitos y detectar errores o regresiones.
- **Responsable:** QA / Desarrollador.

### EC-06. Configuración
- **Archivo:** `conf.example.json`
- **Ubicación:** `/config/`
- **Justificación:** Define parámetros de red, base de datos, seguridad, auditoría y hardware.
- **Responsable:** DevOps / Desarrollador.

### EC-07. Plan de configuración
- **Archivo:** `CM_PLAN.md`
- **Ubicación:** Raíz del repositorio.
- **Justificación:** Establece las reglas para identificar, versionar y controlar los cambios.
- **Responsable:** Responsable de configuración.

### EC-08. Registro de cambios
- **Archivo:** `CHANGELOG.md`
- **Ubicación:** Raíz del repositorio.
- **Justificación:** Registra la evolución y los cambios realizados en cada versión.
- **Responsable:** Responsable de configuración / Equipo.


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
