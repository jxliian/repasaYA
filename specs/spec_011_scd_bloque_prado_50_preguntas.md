# Spec 011: Integración del Bloque Exclusivo «Prado» (50 preguntas) en Tests de SCD

- **Fecha**: 2026-10-28
- **Estado**: Implementado
- **Ámbito**: Contenido Docente / Tests Interactivos / SCD

---

## 1. Contexto y Objetivos

1. **Petición del Alumno**:
   - Incorporar un intento completo de 50 preguntas extraídas directamente de los cuestionarios oficiales de Prado UGR.
   - Crear un **bloque temático específico denominado `Prado`** con exactamente 50 preguntas para permitir al alumno entrenar exclusivamente sobre este conjunto o incluirlo en el modo general.
   - Mantener las preguntas íntegras, con sus 5 opciones y la clave oficial de respuestas de la plataforma docente.

2. **Procesamiento y Enriquecimiento**:
   - Se parseó el volcado textual de Prado asegurando la extracción limpia de las 5 opciones por pregunta mediante segmentación anclada a líneas completas (`(?m)^\s*([a-e])\.\s*$`).
   - Se validó el 100% de las respuestas correctas frente a la retroalimentación de Prado.
   - Se asignaron justificaciones pedagógicas detalladas:
     - 35 preguntas reutilizaron y adaptaron las justificaciones analíticas del banco de SCD.
     - 15 preguntas de nueva incorporación recibieron justificaciones teóricas completas basadas en el temario del Prof. Capel (reentrancia en monitores, semántica SU vs SC, propiedades de seguridad vs vivacidad, olla de salvajes, filósofos comensales, lógica de Hoare).

---

## 2. Archivos Modificados

- `src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/test.json`: 208 $\to$ 258 preguntas (+50 con `tema: "Prado"`).
- `tipo-test/SCD/scd.json`: 208 $\to$ 258 preguntas (+50 con `tema: "Prado"`).
- `tipo-test/SCD/index.html`: Sincronización del array `ALL` para ejecución local/offline con dropdown y banco actualizados.
- `.agents/memory/metricas-contenido.md`: Actualización de métricas globales (2.673 preguntas totales en repasaYA).
- `.agents/memory/estado-y-roadmap.md`: Actualización de catálogo de SCD.

---

## 3. Verificación

- `npm run build` ejecutado y superado con 91 páginas estáticas generadas sin errores de esquema.
- Verificación en `dist/informatica/3/c1/sistemas-concurrentes-y-distribuidos/test/index.html` del chip `Prado` con 50 preguntas.
