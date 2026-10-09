# Spec 004: Skill de Orquestación para Tareas de Alta Complejidad

- **Fecha**: 2026-10-09
- **Estado**: Implementado
- **Ámbito**: Arquitectura de Agentes / Automatización / Skills

---

## 1. Contexto y Motivación

Para escalar la incorporación de contenidos docentes complejos en **repasaYA** (como la extracción y estructuración de exámenes completos en PDF, la generación masiva de bancos de preguntas JSON o refactorizaciones profundas de código), se requiere una habilidad (*skill*) formal que el agente active automáticamente ante tareas de alta complejidad.

Esta especificación formaliza la habilidad `orchestrated-pipeline`, definiendo los umbrales de complejidad que determinan cuándo ejecutar una tarea de forma directa y cuándo desplegar el ciclo completo de cuatro roles: **Coordinador**, **Ejecutor**, **Revisor** y **Auditor**.

---

## 2. Matriz de Umbrales de Complejidad

| Nivel de Complejidad | Ejemplos Típicos | Modo de Operación |
| :--- | :--- | :--- |
| **Baja** | Consultas, dudas sobre el código, corrección de una errata puntual, recuento de métricas | ⚡ **Ejecución Directa** (Rápida y concisa) |
| **Media / Alta** | Extracción de problemas desde PDFs, formateo masivo a JSON de tests o flashcards, refactorización de componentes Astro, cambios en `content.config.ts` | 👥 **Pipeline Orquestado** (Coordinador ➔ Ejecutor ➔ Revisor ➔ Auditor) |

---

## 3. Componentes de la Habilidad

1. **Skill Registrado (`orchestrated-pipeline`)**:
   - Ubicación: [`.agents/skills/orchestrated-pipeline/SKILL.md`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/.agents/skills/orchestrated-pipeline/SKILL.md).
   - Define el flujo de trabajo en 5 fases: Planificación, Ejecución, Revisión, Auditoría y Consolidación.
2. **Garantías de Calidad**:
   - **Legitimidad pedagógica**: Cada pregunta extraída se valida contra el temario oficial de la UGR con justificación razonada obligatoria.
   - **Seguridad técnica**: Verificación de base 0 en arrays, rutas relativas a `public/` para PDFs y respeto al principio de 0 KB JS frameworks en cliente.
   - **Control de publicación**: Verificación de `npm run stats` y `npm run build` previo a cualquier commit.

---

## 4. Estado de Métricas del Contenido

| Métrica | Valor Validado |
| :--- | :--- |
| **Total Preguntas Activas** | **2.622** |
| **Total Fichas y Glosarios** | **377** |
| **Documentos PDF** | **16** |
| **Guías y Recursos** | **5** |
| **Total Asignaturas** | **64** (15 disponibles / 49 planificadas) |
| **Bloques de Material** | **39** |

---

## 5. Verificación y Pruebas

- **Métricas**: `npm run stats` verificado.
- **Compilación estática**: `npm run build` ejecutado y validado (85 páginas generadas).
