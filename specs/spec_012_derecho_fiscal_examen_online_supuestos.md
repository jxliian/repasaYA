# Spec 012: Incorporación de Derecho Fiscal (ADE 5º) y Nueva Funcionalidad de Examen Online con Enunciados de Supuestos Prácticos

- **Fecha**: 2026-11-04
- **Estado**: Implementado
- **Ámbito**: Motor de Exámenes / Arquitectura de Contenidos / Derecho Fiscal (5º ADE / DADE · UGR)

---

## 1. Contexto y Objetivos

1. **Requerimiento del Alumno**:
   - Incorporar la asignatura **Derecho Fiscal** (5º curso, 1º cuatrimestre de ADE / Doble Grado DADE UGR) a la plataforma repasaYA.
   - Desarrollar una **nueva funcionalidad y experiencia en la plataforma**: el simulador de **Examen Online por Supuestos**, que reproduce fielmente el formato del examen oficial:
     - **Enunciado del caso práctico en grande arriba**, con tipografía cómoda, controles de tamaño (+ / -), fijación en pantalla (*sticky*) y plegado.
     - **Preguntas tipo test asociadas inmediatamente debajo**, permitiendo al alumno consultar el supuesto mientras responde cada pregunta de liquidación o calificación jurídica.
     - **Doble modo de realización**:
       - *Modo Examen Online Oficial*: permite seleccionar respuestas, rectificar o desmarcar para dejar en blanco; al finalizar, se pulsa "Corregir Examen" y se aplica la fórmula oficial de penalización de la UGR (cada 3 fallos restan 1 acierto, `-0,33` por fallo), generando un desglose visual con nota sobre 10, aciertos, fallos y justificación legal paso a paso.
       - *Modo Estudio*: corrección inmediata al hacer clic para facilitar el aprendizaje ágil.
   - Publicar la **Guía Maestra del Primer Parcial (9 de Noviembre)** con el mapa de pestañas (*post-its*) para el Código BOE de 1.500 páginas, la resolución canónica de las 16 Cuestiones del Tema 1 (LGT) y los 16 Supuestos Prácticos de clase (IRPF).
   - **Regla estricta de privacidad**: excluir de forma rigurosa cualquier material o apunte personal de compañeros de clase, integrando exclusivamente textos legales oficiales del BOE, enunciados de supuestos prácticos de la asignatura y exámenes oficiales de la universidad.

---

## 2. Nueva Arquitectura del Motor (`QuizEngine.astro` y Esquemas)

1. **Extensión del Esquema Zod (`src/content.config.ts`)**:
   - Incorporación de campos opcionales en `testItem`:
     - `caseId`: Identificador único del caso práctico o examen (`simulacro-9nov`, `examen-2019`, `examen-2020`, `casos-clase-irpf`).
     - `caseTitle`: Título descriptivo para los selectores de casos.
     - `caseStatement`: Texto íntegro del supuesto práctico compartido por las preguntas.

2. **Componente de Examen por Supuestos (`QuizEngine.astro`)**:
   - Pestaña dedicada `📋 Examen Online por Supuestos` con selector dinámico en cuadrícula.
   - Caja de enunciado *Hero Statement* con:
     - Selector de zoom de texto (`A-` / `A+`).
     - Botón de fijación (*Pin / Sticky*) para mantener el enunciado visible durante el desplazamiento vertical.
     - Botón de plegado/desplegado para maximizar espacio.
   - Selector de opciones interactivo con indicador visual de estado (seleccionada, correcta, incorrecta, dejada en blanco).
   - Banner de resultados con desglose de nota según fórmula UGR:
     $$\text{Nota} = \max\left(0, \frac{\text{Aciertos} - 0,33 \times \text{Fallos}}{\text{Total Preguntas}} \times 10\right)$$
   - Retroalimentación formativa y bloque de *Justificación Legal y Resolución Paso a Paso* visible tras la entrega.

3. **Enrutamiento y Detección Automática (`[material].astro`)**:
   - Detección de materiales de supuestos (`isCaseExamMaterial`) para inicializar directamente la vista en `initialTab = 'supuestos'`, sin requerir clics adicionales del usuario.

---

## 3. Catálogo de Contenidos Integrados (Derecho Fiscal)

| Material | Fichero | Cantidad | Descripción |
| :--- | :--- | :--- | :--- |
| **Guía Maestra** | `src/pages/derecho-fiscal/guia.md` & `guia.json` | 1 Guía (480 líneas) | Temario del Parcial (T1 + IRPF), índice de pestañas Código BOE, Cuestiones 1-16 y Supuestos 1-16 resueltos. |
| **Examen Online Supuestos** | `supuestos-examen.json` | **51 preguntas** | 4 Casos: Simulacro 9 Nov (15 q), Ordinario 2019 (10 q), Enero 2020 (10 q) y Seminario Clase 1-16 (16 q). |
| **Banco de Test** | `test.json` | **60 preguntas** | Cuestiones LGT, Contribuyentes, Exenciones, RNTP, Rentas en Especie, Dietas, RNCI e Imputación. |
| **Verdadero / Falso** | `vf.json` | **50 preguntas** | Preguntas trampa de examen con justificación y cita de artículos LIRPF y LGT. |
| **Flashcards** | `flashcards.json` | **48 tarjetas** | Cuantías exactas (0,26 €/km, 53,34 €, 26,67 €, 500 €, 11 €/día, 2% / 1,1% VC), reducciones y reglas. |

**Total de ítems docentes**: 161 preguntas tipo test y V/F + 48 flashcards + 1 Guía Maestra completa.

---

## 4. Archivos Modificados y Creados

- `src/content.config.ts`: Modificado para soportar metadatos de supuestos en colecciones.
- `src/components/QuizEngine.astro`: Implementación del panel de supuestos, toolbar de examen y banner UGR.
- `src/layouts/GuideLayout.astro`: Integración de migas de pan y llamadas a la acción específicas de Derecho Fiscal.
- `src/pages/[degree]/[year]/[semester]/[subject]/[material].astro`: Propagación de `initialTab` y soporte de examen de supuestos.
- `src/content/subjects/ade/derecho-fiscal.md`: Asignatura activada como `available` con descripción y materiales.
- `src/content/materials/ade/derecho-fiscal/guia.json`: Ficha de Guía Maestra.
- `src/content/materials/ade/derecho-fiscal/supuestos-examen.json`: Banco de 51 preguntas estructuradas en 4 casos oficiales.
- `src/content/materials/ade/derecho-fiscal/test.json`: Banco de 60 preguntas tipo test verificadas.
- `src/content/materials/ade/derecho-fiscal/vf.json`: 50 preguntas de V/F con trampas de examen.
- `src/content/materials/ade/derecho-fiscal/flashcards.json`: 48 fichas de estudio rápido.
- `src/pages/derecho-fiscal/guia.md`: Guía de estudio y resolución de prácticas.
- `specs/spec_012_derecho_fiscal_examen_online_supuestos.md`: Esta especificación formal.

---

## 5. Verificación y Calidad

- **Compilación estática Astro**: `npm run build` ejecutado exitosamente generando **103 páginas estáticas** (0 errores, 0 warnings).
- **Rutas verificadas**:
  - `/ade/5/c1/derecho-fiscal/`: Hub de la asignatura con las 5 tarjetas de recursos.
  - `/ade/5/c1/derecho-fiscal/supuestos-examen/`: Simulador de examen online por supuestos con enunciados en grande.
  - `/ade/5/c1/derecho-fiscal/test/`: Banco general de tests.
  - `/ade/5/c1/derecho-fiscal/vf/`: Entrenador de Verdadero/Falso.
  - `/ade/5/c1/derecho-fiscal/flashcards/`: Visor de tarjetas de memoria.
  - `/derecho-fiscal/guia/`: Guía Maestra con índice para el examen y solucionario.
- **Privacidad y cumplimiento**: Confirmada la ausencia total de archivos privados o carpetas de terceros en el repositorio.
