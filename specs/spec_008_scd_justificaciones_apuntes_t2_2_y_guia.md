# Spec 008: Auditoría de Justificaciones SCD, Integración del Tema 2-2 en Apuntes y Normalización de la Guía

- **Fecha**: 2026-10-22
- **Estado**: Implementado
- **Ámbito**: Contenido / SCD (Sistemas Concurrentes y Distribuidos)

---

## 1. Contexto y Objetivos

1. **Auditoría Pedagógica del Banco Tipo Test de SCD (207 preguntas)**:
   - Siguiendo el **Artículo II de la Constitución de repasaYA** y la instrucción del usuario, verificar que todas las preguntas tipo test de SCD cuenten con justificaciones razonadas exhaustivas.
   - Cada justificación debe explicar de forma meridiana por qué la opción marcada (`correct`, base 0) es la correcta y refutar individualmente por qué cada uno de los distractores es incorrecto o inválido.
2. **Normalización Tipográfica y Renderizado en la Guía de Estudio (`src/pages/scd/guia.md`)**:
   - Resolver el problema de fórmulas y símbolos no renderizados (`$\implies$`, `$\iff$`, `\land`, `\lor`, `\cap`, cotas matemáticas, etc.), adaptándolos a caracteres estándar Unicode limpios y bloques destacados legibles sin dependencias pesadas de cliente.
3. **Integración Oficial del Tema 2-2 en Apuntes Teóricos (`SCD_T2_2_SPA.pdf`)**:
   - Contrastar los apuntes de teoría de SCD con la presentación oficial del Departamento de LSI (`SCD_T2_2_SPA.pdf`), incorporando la teoría que faltaba: Algoritmo de Dijkstra para $N$ procesos (barreras y traza de inanición), Algoritmo de Knuth para $N$ procesos (retraso acotado $2^{N-1}-1$), Lemas formales del Filtro de Peterson para $N$ procesos (Lemas 1, 2 y 3 sin etapas intermedias vacías, cota de $N(N-1)/2$), y algoritmos distribuidos de exclusión mutua (Ricart-Agrawala, enfoque basado en testigo y algoritmo de regeneración de testigo de Misra con invariante $\text{num\_ping} + \text{num\_pong} = 0$).
   - Recompilar los apuntes de teoría en LaTeX pasando de 75 a 79 páginas y sincronizar `public/scd/apuntes-teoria-scd.pdf`.

---

## 2. Descripción de los Cambios Implementados

### 2.1. Tests de SCD (`test.json`, `scd.json`, `index.html`)
- Despliegue de un pipeline multiagente concurrente (`orchestrated-pipeline`) con 5 subagentes especializados particionando las 207 preguntas:
  - **Worker 0 (0..44)**: Conceptos Básicos, Axiomas de Concurrencia, Lógica de Hoare y Monitores.
  - **Worker 1 (45..89)**: Exclusión Mutua, Spinlocks, Semáforos y Paso de Mensajes.
  - **Worker 2 (90..131)**: Tiempo Real (RMS, EDF, PIP, PCP), Paso de Mensajes avanzado y Examen Parcial I.
  - **Worker 3 (132..169)**: Examen Parcial II e InfoAdeHub Temas 1 y 2.
  - **Worker 4 (170..206)**: InfoAdeHub Temas 3 y 4 y Sistemas Distribuidos.
- El 100% de las 207 preguntas (de 17 con justificación previa a 207) disponen de un desglose analítico completo que detalla la opción correcta y desglosa individualmente las alternativas erróneas.
- Se preservaron las notas de corrección y aclaraciones didácticas de repasaYA en preguntas clave (p. ej. preguntas 1, 13, 66 y 154).

### 2.2. Guía de Estudio de SCD (`src/pages/scd/guia.md`)
- Sustitución de etiquetas LaTeX no interpretadas por el parser Markdown de Astro por caracteres Unicode matemáticos nativos (`⟹`, `⟺`, `≤`, `∧`, `∨`, `∩`, `∅`, `×`).
- Formateo de la fórmula de esperanza matemática en el test y cálculo de penalización (-0,5) en bloques destacados legibles.
- Invariantes y fórmulas formalizados en bloques monospaciados (`np = min(na, nv)`, `0 ≤ dentro ≤ k`, etc.).

### 2.3. Apuntes de Teoría en LaTeX (`apuntes/SCD/`)
- Ampliación sustancial de `apuntes/SCD/temas/tema2_parte1.tex`:
  - **Algoritmo de Dijkstra para N procesos (1965)**: Protocolo de dos barreras, análisis de seguridad y traza detallada del contraejemplo de inanición.
  - **Algoritmo de Knuth (1966)**: Resolución de la inanición mediante comprobación circular y demostración del teorema de cota de espera acotada ($2^{N-1}-1$).
  - **Filtro de Peterson para N procesos**: Formulación rigurosa con demostración de los 3 Lemas de Capel (Filtro, Exclusión Mutua en nivel $N-1$, y Distribución Monótona decreciente que prohíbe etapas intermedias vacías), junto a la cota uniforme de $\frac{N(N-1)}{2}$ adelantamientos.
  - **Algoritmos Distribuidos de Exclusión Mutua**:
    - Ricart-Agrawala con $2(N-1)$ mensajes.
    - Esquemas con testigo y verificación formal del invariante ($\sum \text{token\_presente}_i \le 1$).
    - Algoritmo de regeneración de testigo de Misra (tokens duales ping-pong e invariante $\text{num\_ping} + \text{num\_pong} = 0$).
- Recompilación exitosa con `pdflatex`: documento final ampliado a 79 páginas (`main.pdf`), sincronizado en `public/scd/apuntes-teoria-scd.pdf` y actualizado en `apuntes.json`.

---

## 3. Verificación y Calidad

- **Compilación estática Astro**: `npm run build` ejecutado con éxito (88 páginas generadas, 0 errores de Zod).
- **Compilación LaTeX**: `compilar.sh` ejecutado con éxito sin advertencias críticas de UTF-8 ni errores de listings.
- **Métricas**: `npm run stats` verificado (2.622 preguntas activas, 377 fichas y glosarios, 17 PDFs).
- **PUSH_POLICY**: Cumple con adición/actualización efectiva de contenido docente y con mandato explícito del usuario.
