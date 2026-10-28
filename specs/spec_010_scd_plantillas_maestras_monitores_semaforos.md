# Spec 010: Plantillas Maestras Universales de Monitores y Semáforos para Examen de SCD (Prof. Capel)

- **Fecha**: 2026-10-28
- **Estado**: Implementado
- **Ámbito**: Contenido Docente / Materiales PDF / SCD (Sistemas Concurrentes y Distribuidos)

---

## 1. Contexto y Objetivos

1. **Requerimiento del Alumno**:
   - Disponer de un documento canónico, riguroso e infalible con las plantillas universales para resolver cualquier ejercicio práctico de examen de SCD impartido por el Prof. Manuel I. Capel Tuñón.
   - Soportar con exactitud tanto la implementación oficial en C++ de la UGR (`HoareMonitor`, `CondVar`, `newCondVar()`, `sem_t`) como el pseudocódigo canónico teórico de Hoare y Dijkstra/Andrews.
   - **Requisito de maquetación estricto**: Cada bloque de código y pseudocódigo de cada plantilla debe ubicarse íntegramente en **una sola cara (1 página por plantilla)**, evitando cualquier salto de página que corte el código a la mitad.

2. **Arquitectura del Documento (8 Páginas / 1 Cara por Plantilla)**:
   - **Página 1: Portada y Estrategia Integral**:
     - Las 4 familias de ejercicios de examen de la UGR (Monitores de 2 bandos/aforo, Lectores-Escritores, Paso de Testigo, Handshake asimétrico).
     - Las 4 Reglas de Oro de Capel (herencia, constructor `newCondVar()`, semántica SU vs SC, no liberar mutex en paso de testigo).
     - Tabla de correspondencia sintáctica C++ oficial UGR $\longleftrightarrow$ Pseudocódigo formal Hoare/Dijkstra.
   - **Página 2: Plantilla 1A — Monitor Universal de Dos Bandos / Recursos Incompatibles**:
     - Implementación C++ oficial completa con `HoareMonitor` (Puente, Aseo, Centro 0/1, Olla, Barbería).
     - Transcripción canónica completa en Pseudocódigo formal de Hoare.
   - **Página 3: Diccionario de Adaptación Inmediata y Justificación Teórica**:
     - Tabla de correspondencia para los 5 problemas típicos.
     - Justificación teórica de tres pilares obligatoria para la máxima nota (Invariante de Exclusión Mutua, Ausencia de Deadlock, Semántica SU vs Mesa).
   - **Página 4: Plantilla 1B — Monitor de Lectores--Escritores (Prioridad a Escritores)**:
     - C++ oficial (`HoareMonitor`) y Pseudocódigo en una sola cara.
     - Cascada de lectores y discusión sobre inanición.
   - **Página 5: Plantilla 1C — Monitor con Turno FIFO Estricto (Cuenta Bancaria)**:
     - El problema del Examen 2021 (retiradas grandes vs pequeñas).
     - Patrón de 2 colas (`cola_espera` y `cola_turno`) en C++ y Pseudocódigo en una sola cara.
   - **Página 6: Plantilla 2 — Semáforos con Paso de Testigo (*Passing the Baton*)**:
     - Fundamento de Dijkstra/Andrews para aforos y exclusión compleja con semáforos POSIX en C++ y Pseudocódigo en una sola cara.
     - Regla sagrada de transferencia directa de testigo sin liberar `mutex`.
   - **Página 7: Plantilla 3 — Coordinación Asimétrica entre Procesos ($P_1, P_2, P_3$ / *Handshake*)**:
     - Problema oficial del Examen 2025 en C++ y Pseudocódigo en una sola cara.
     - Técnicas de sincronización 1 a 1 (`sem_h_hecho`, `sem_h_ack`) y apertura permanente (`sem_b_primera`).
   - **Página 8: Tabla de Decisión Rápida en 10 Segundos y Checklist Final de Entrega**:
     - Clasificación según palabras clave del enunciado.
     - Checklist de 6 comprobaciones críticas antes de entregar la hoja.

---

## 2. Archivos Afectados y Generados

- `/home/jxlig0d/Descargas/Plantillas_Maestras_SCD_Examen.pdf`: Copia directa para consulta e impresión del alumno.
- `public/scd/plantillas-maestras-scd.pdf`: PDF integrado en el repositorio para servir estáticamente.
- `relaciones/SCD/plantillas_maestras_scd.tex`: Código fuente en LaTeX compilable con `pdflatex`.
- `src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/plantillas.json`: Ficha de material didáctico registrada en repasaYA.
- `src/pages/scd/guia.md`: Enlace directo de descarga en la guía de estudio de SCD.

---

## 3. Verificación

- Compilación LaTeX limpia (`pdflatex`) resultando en exactamente 8 páginas sin desbordamientos de código ni cortes.
- Auditoría de páginas con `pdfplumber` y `pdftotext` certificando que cada código reside íntegramente en su propia cara.
- `npm run build` superado con 91 rutas estáticas generadas sin errores.
