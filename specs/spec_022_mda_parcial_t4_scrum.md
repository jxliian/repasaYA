# Spec 022: MDA · Parcial del Tema 4 (Scrum), 27/11/2026

- **Fecha**: 2026-11-23
- **Estado**: Implementado
- **Ámbito**: Contenido / Metodologías de Desarrollo Ágil

## Contexto
Segunda prueba parcial de teoría de MDA sobre el «Tema 4. Scrum»: viernes 27/11/2026, en grupo (grupos de
prácticas), sin apuntes, una hora como máximo, con preguntas cortas y ejercicios. Fuentes: diapositivas
«Unidad 1 - Desarrollo Ágil de Software. Tema 4 – SCRUM» (104) y «Tema 4 – Elevator Pitch» (11; Sprint 0 y visión).

## Cambios
- `apuntes/MDA/tema4_scrum.tex` → `public/mda/apuntes-tema4-scrum.pdf` (19 págs.). Reutiliza `apuntes/MDA/config/estilo.tex`
  y cambia el pie de página. Cada idea cita su diapositiva (`\diap{N}`), y lo que no está en las diapositivas lleva `\extra`
  (duración del Daily de 15 min según la Guía de Scrum, plantilla de Moore del elevator pitch, valores de la Guía).
- `tipo-test/MDA/build_tema4.py` genera `test-t4-scrum.json` (62), `flashcards-t4-scrum.json` (42), `vf-t4-scrum.json`
  (30) y `preguntas-cortas-t4-scrum.json` (15 preguntas cortas + 10 ejercicios). Opciones barajadas con semilla 2711.
- `apuntes-t4-scrum.json` y `guia-t4-scrum.json` (orden negativo para que salgan antes que el Seminario 2).
- Guía `src/pages/mda/guia-t4.md` (`/mda/guia-t4/`): formato de la prueba, qué entra, ejercicios probables, plan de
  estudio junto al parcial de SCD del 26/11 y cómo organizar el examen en grupo.
- Asignatura: descripción actualizada y `guia` añadida a `materials`.
- `guia-t22.json` de SCD: la descripción decía «plan de 7 días» (ahora son cuatro tardes).

## Notas de contenido
- Duraciones de las reuniones en un Sprint de 4 semanas (diap. 50, imagen): Planning 8 h, Review 4 h, Retrospective 3 h.
- 3 + 3 roles (diap. 16, imagen): cerdos PO/SM/equipo; gallinas user/customer/management.
- `npm run build`: 121 páginas.

## Corrección de aislamiento entre parciales (2026-11-26)
- Añadido `group` opcional en `materialBase` (`src/content.config.ts`) y agrupados los bloques de MDA en `"t4-scrum"` y `"seminario-2"`.
- Corregida la resolución de `testItems`, `vfItems` y `revealItems` en `[material].astro` para que cada página cargue siempre sus propios `items` y solo combine materiales complementarios del mismo `group` (sin mezclar Seminario 2 con Tema 4 Scrum).
- Aislado `localStorage` por grupo (`storageKey`) en `QuizEngine.astro`.
