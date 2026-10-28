# Spec 009: Extracción, Deduplicación y Ampliación de Tests de SCD desde PDF

- **Fecha**: 2026-10-28
- **Estado**: Implementado
- **Ámbito**: Contenido / SCD (Sistemas Concurrentes y Distribuidos)

---

## 1. Contexto y Objetivos

1. **Recepción del Material de Estudio**:
   - Se suministró el archivo PDF `/home/jxlig0d/Descargas/scdtipotest.pdf` («TIPO TEST SCD – TEMAS 1 Y 2», 16 páginas, compilado por Celia Arroyo Heredia en Wuolah, conteniendo 50 preguntas sin respuestas marcadas).
   - El objetivo principal era extraer todas las preguntas, compararlas exhaustivamente contra el banco activo de 207 preguntas de SCD para descartar repeticiones, e incorporar únicamente aquellas preguntas no existentes garantizando el máximo rigor pedagógico.

2. **Deduplicación Exhaustiva**:
   - Ejecución de análisis algorítmico de coincidencia semántica y textual sobre las 50 preguntas frente a las 207 existentes en `test.json`.
   - **Resultado del análisis**:
     - 48 preguntas correspondían a preguntas ya presentes e integradas en `test.json` con idénticas opciones y justificaciones pedagógicas completas.
     - 1 pregunta (Q27 en el PDF) era una duplicación interna literal de la pregunta 16 del mismo documento.
     - 1 pregunta (Q22 en el PDF) contenía una errata del autor original (se copió el encabezado de la pregunta 32 sobre las opciones correspondientes a la pregunta #207 de la base de datos sobre beneficios de sistemas distribuidos).
     - **Exactamente 1 pregunta nueva (Q32 en el PDF)** no figuraba en la base de datos de test de repasaYA.

3. **Corrección de Errata Previa (Spoiler en Pregunta 155)**:
   - Durante la comparación de la pregunta 48 del PDF frente al banco, se detectó que el enunciado de la pregunta 155 existente contenía un spoiler involuntario («...a menos que se cumpla a = 0?») que desvelaba la opción correcta (`a = 0`). Se aprovechó la ocasión para sanear el enunciado formalmente.

---

## 2. Descripción de los Cambios Implementados

### 2.1. Nueva Pregunta Incorporada (Pregunta 208 en SCD)
- **Tema**: `InfoAdeHub · Temas 1 y 2`
- **Enunciado**: `¿Qué condición de Dijkstra no es esencial para la exclusión mutua?`
- **Opciones**:
  - `[0]` `No hacer suposiciones sobre la velocidad de los procesos.`
  - `[1]` `Cada proceso debe tener un identificador único.`
  - `[2]` `Si un proceso está fuera de la sección crítica, no impide a otros entrar.`
  - `[3]` `Algún proceso en espera debe entrar en la sección crítica.`
  - `[4]` `La concurrencia es siempre determinista.` *(Correcta)*
- **Clave Correcta**: Índice `4` (base 0).
- **Justificación**: Rigurosa y exhaustiva según el Artículo II de la Constitución de repasaYA, analizando el no determinismo inherente a la concurrencia, repasando las cuatro condiciones formales de Dijkstra (1965) y discriminando por qué el identificador único es una premisa de diseño software pero no una propiedad formal intrínseca del problema abstracto de exclusión mutua.

### 2.2. Saneamiento del Enunciado de la Pregunta 155
- **Antes**: `¿Por qué no se puede demostrar la corrección del siguiente fragmento de programa concurrente a menos que se cumpla a = 0?...`
- **Ahora**: `¿Bajo qué condición no se puede demostrar la corrección del siguiente fragmento de programa concurrente a menos que se cumpla?...`
- Se preservan las 5 opciones, la clave correcta (`a = 0`) y la justificación teórica de Owicki-Gries.

### 2.3. Sincronización de Archivos
- `src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/test.json`: 208 preguntas validadas con Zod.
- `tipo-test/SCD/scd.json`: 208 preguntas sincronizadas.
- `tipo-test/SCD/index.html`: Variable `let ALL` actualizada con el nuevo banco completo.
- `.agents/memory/metricas-contenido.md`: Métricas globales actualizadas (+1 pregunta test).
- `.agents/memory/estado-y-roadmap.md`: Catálogo de SCD actualizado a 208 tests.

---

## 3. Verificación y Métricas

- `npm run stats`:
  - Total preguntas activas: `2.623` (antes 2.622).
  - Tipo test: `1.998` (antes 1.997).
- `npm run build`: Ejecutado con éxito (`90 page(s) built in 7.86s`, 0 errores Zod/Astro).
