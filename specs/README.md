# 📋 Sistema de Especificaciones (`specs/`)

La carpeta `specs/` almacena el histórico formal de cambios, diseños técnicos y evoluciones de **repasaYA**. Funciona como la memoria a largo plazo pública del proyecto para garantizar la trazabilidad de cada cambio significativo.

---

## 📌 Formato y Nomenclatura

Cada especificación sigue el formato:
```text
specs/spec_XXX_<nombre_descriptivo>.md
```
Donde `XXX` es un número secuencial de tres dígitos con ceros a la izquierda (ej. `spec_001_...`, `spec_002_...`).

---

## 📑 Estructura Estándar de una Especificación

Cada archivo debe contener las siguientes secciones:

```markdown
# Spec XXX: [Título de la Especificación]

- **Fecha**: AAAA-MM-DD
- **Estado**: Implementado | En progreso | Propuesto
- **Ámbito**: Contenido | Arquitectura | UI/UX | Infraestructura

---

## 1. Contexto y Motivación
¿Por qué se realiza este cambio o adición?

## 2. Descripción de los Cambios
Detalle de archivos creados, modificados o eliminados.

## 3. Estado de Métricas de Contenido
- Total Preguntas: [Número]
- Total Fichas: [Número]
- Total Asignaturas: [Número]
- Bloques de Material: [Número]

## 4. Verificación y Pruebas
- Resultado de `npm run stats`
- Resultado de `npm run build`
```

---

## 🗂️ Registro de Especificaciones

| ID | Fecha | Título | Ámbito | Estado |
| :--- | :--- | :--- | :--- | :--- |
| [`spec_001`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_001_sistema_metricas_y_especificaciones.md) | 2026-10-09 | Inicialización del Sistema de Especificaciones y Control de Métricas | Infraestructura / Specs | Implementado |
| [`spec_002`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_002_constitucion_y_principios_fundamentales.md) | 2026-10-09 | Constitución y Principios Fundamentales del Proyecto | Gobernanza / Principios | Implementado |
| [`spec_003`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_003_orquestacion_agentes_revision_auditoria.md) | 2026-10-09 | Orquestación Multiagente con Ciclos de Revisión y Auditoría | Arquitectura / Agentes | Implementado |
| [`spec_004`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_004_skill_orquestacion_compleja.md) | 2026-10-09 | Skill de Orquestación para Tareas de Alta Complejidad | Automatización / Skills | Implementado |
| [`spec_005`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_005_orquestacion_concurrente_simultanea.md) | 2026-10-09 | Modelo de Orquestación Concurrente y Simultánea Multiagente | Rendimiento / Paralelismo | Implementado |
| [`spec_006`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_006_scd_auditoria_test_apuntes_y_relaciones.md) | 2026-10-16 | Auditoría de Tests, Apuntes Teóricos y Solucionario de Relaciones de SCD | Contenido / SCD | Implementado |
| [`spec_007`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_007_fft_apuntes_latex.md) | 2026-10-18 | Digitalización, Estructuración LaTeX y Publicación de Apuntes de FFT | Contenido / FFT / LaTeX | Implementado |
| [`spec_008`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_008_scd_justificaciones_apuntes_t2_2_y_guia.md) | 2026-10-22 | Justificaciones de SCD, Apuntes T2-2 y Guía de Examen | Contenido / SCD | Implementado |
| [`spec_009`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_009_scd_extraccion_pdf_y_deduplicacion.md) | 2026-10-28 | Extracción de Tests PDF y Deduplicación en SCD | Contenido / SCD | Implementado |
| [`spec_010`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_010_scd_plantillas_maestras_monitores_semaforos.md) | 2026-10-28 | Plantillas Maestras Universales de Monitores y Semáforos | Contenido / SCD / LaTeX | Implementado |
| [`spec_011`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_011_scd_bloque_prado_50_preguntas.md) | 2026-10-28 | Integración del Bloque Exclusivo «Prado» (50 preguntas) en Tests de SCD | Contenido / SCD | Implementado |
| [`spec_012`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_012_derecho_fiscal_examen_online_supuestos.md) | 2026-11-04 | Incorporación de Derecho Fiscal y Nueva Funcionalidad de Examen Online con Supuestos | Motor de Tests / ADE 5º | Implementado |
| [`spec_013`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/spec_013_derecho_fiscal_renderizado_formulas_katex.md) | 2026-11-04 | Renderizado y Maquetación de Fórmulas Matemáticas con KaTeX en Guías de Estudio | Infraestructura / UI / Fiscal | Implementado |




