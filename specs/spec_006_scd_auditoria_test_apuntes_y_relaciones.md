# Spec 006: Auditoría de Tests, Apuntes Teóricos y Solucionario de Relaciones de SCD

- **Fecha**: 2026-10-16
- **Estado**: Implementado
- **Ámbito**: Contenido / SCD

---

## 1. Contexto y Motivación
Revisión exhaustiva y consolidación de materiales de **Sistemas Concurrentes y Distribuidos (SCD)** (3.º curso del Grado en Ingeniería Informática, UGR) solicitada para:
1. Garantizar la corrección absoluta de las 207 preguntas tipo test, documentando en el JSON cualquier corrección o aclaración didáctica sobre las plantillas originales.
2. Certificar la ausencia de preguntas duplicadas y verificar la estructuración modular por bloques temáticos.
3. Alinear los apuntes de teoría en LaTeX con las diapositivas oficiales del profesor Manuel Capel (`Tema 2-1.pdf`).
4. Resolver íntegramente las dos relaciones oficiales de problemas (Relación 1 de entrelazados y semáforos, y Relación 2 de monitores y sincronización avanzada), unificándolas en un solo documento PDF de referencia.

---

## 2. Descripción de los Cambios

### 2.1. Tests de SCD (`test.json` y `scd.json`)
- **Corrección de Claves**:
  - Pregunta 1: Clave corregida a opción 2 (explosión combinatoria de secuencias de intercalación). Se incorpora nota explícita en `justification`.
  - Pregunta 13: Clave corregida a opción 1 (progreso local como completitud de sección sin interrupción/bloqueo, conforme a la diapositiva 1.14 del temario). Se incorpora nota explícita en `justification`.
  - Pregunta 66: Se añade aclaración didáctica en `justification` sobre la resolución teórica de inanición y bloqueo mutuo en el algoritmo de Dekker frente a la plantilla original de evaluación continua.
- **Deduplicación**: Verificación algorítmica con similitud difusa (Levenshtein); confirmación de 0 preguntas duplicadas sobre el total de 207.

### 2.2. Apuntes de Teoría en LaTeX (`apuntes/SCD/`)
- Integración en `tema2_parte2.tex` de los modelos específicos de las diapositivas de Capel:
  - Monitor Semáforo de Habermann con verificación formal de invariantes ($np = \min(na, nv)$).
  - Regla de Concurrencia de Hoare para monitores (aislamiento y ausencia de interferencia).
  - Patrón *Single Wait* (EU) y colas de condición con prioridad (`c.wait(p)`, `c.min_p()`).
  - Patrón *Barrera Parcial* (Barrera2 con épocas).
- Recompilación a 75 páginas y sincronización de `public/scd/apuntes-teoria-scd.pdf`.

### 2.3. Solucionario de Problemas (`relaciones/SCD/`)
- Creación de `relacion2.tex` resolviendo paso a paso los 17 problemas de la Relación 2 (problemas 37 al 53: monitores Hoare, Lampson-Redell, POSIX, baño compartido, puente con cuotas, caníbales, cuenta bancaria, filósofos, canal $K$, barrera reutilizable y transacciones 2PC).
- Recompilación del PDF unificado de problemas `relaciones-problemas-scd.pdf` alcanzando 61 páginas con 53 problemas explicados y con código C++11.
- Actualización de metadatos en `relaciones.json` y memoria del proyecto.

---

## 3. Estado de Métricas de Contenido
- **Total Preguntas**: 2.622 (1.997 Test, 509 V/F, 116 Ocultas)
- **Total Fichas y Glosarios**: 377 (231 Flashcards, 146 Términos)
- **Total Documentos PDF**: 16
- **Total Asignaturas**: 64 (15 disponibles, 49 planificadas)
- **Bloques de Material**: 39

---

## 4. Verificación y Pruebas
- `npm run stats`: Métricas íntegras y verificadas.
- `npm run build`: 85 páginas generadas exitosamente con salida estática en Astro 6 y 0 errores de esquemas Zod.
