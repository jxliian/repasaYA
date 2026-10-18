# Spec 007: Digitalización, Estructuración LaTeX y Publicación de Apuntes de FFT

- **Fecha**: 2026-10-18
- **Estado**: Implementado
- **Ámbito**: Contenido / FFT / LaTeX / Grado en Ingeniería Informática (UGR)

---

## 1. Contexto y Motivación
Conversión y digitalización integral a código LaTeX profesional de los apuntes manuscritos completos (120 páginas originales) de la asignatura **Fundamentos Físicos y Tecnológicos (FFT)** (1.º curso, 1.º cuatrimestre, Grado en Ingeniería Informática y Doble Grado DGIIM de la Universidad de Granada, impartida por el profesor Pedro Cartujo).

El objetivo es equiparar los materiales de FFT al estándar de máxima calidad editorial y pedagógica establecido en **Sistemas Concurrentes y Distribuidos (SCD)**:
1. Maquetación limpia, tipografía profesional y cajas didácticas coloreadas (`definicion`, `ley`, `ejemplo`, `aviso`, `metodo`, `ejercicio`).
2. Código LaTeX modularizado por temas (`temas/tema1_...` a `tema7_...`) con compilación automatizada (`compilar.sh`).
3. Integración completa del PDF generado (67 páginas) en la plataforma repasaYA a través de `public/fft/` y colecciones de contenido Astro.
4. Activación de la asignatura de `planned` a `available`.

---

## 2. Descripción de los Cambios

### 2.1. Proyecto LaTeX Modular (`apuntes/FFT/`)
- `apuntes/FFT/config/estilo.tex`: Configuración visual, paquetes matemáticos (`amsmath`, `physics`, `siunitx`, `circuitikz`), paleta cromática (`fftDarkBlue`, `fftPrimary`, `fftAccent`, `fftTeal`, `fftGreen`, `fftOrange`), cajas `tcolorbox` con rotura de página y cabeceras `fancyhdr`.
- `apuntes/FFT/main.tex`: Estructura principal, portada con metadatos de la UGR, índice general e inclusión de capítulos.
- `apuntes/FFT/compilar.sh`: Script ejecutable de doble pasada con `pdflatex` y sincronización automática de `apuntes_fft.pdf`.
- Capítulos temáticos en `apuntes/FFT/temas/`:
  - `tema1_electromagnetismo.tex`: Electrostática (Coulomb, campo $\vec{E}$, Gauss, potencial, condensadores y dieléctricos), Electrodinámica (corriente, Ohm microscópica y macroscópica) y Magnetismo (Lorentz, Biot-Savart, conductores paralelos, Ampère, Faraday-Lenz y autoinducción).
  - `tema2_circuitos_dc.tex`: Elementos activos/pasivos, leyes de Kirchhoff (LCK, LTK), divisores, métodos de nudos y mallas, teoremas de Thévenin, Norton, máxima transferencia de potencia, y régimen transitorio de 1.º orden (RC y RL).
  - `tema3_circuitos_ac.tex`: Régimen permanente sinusoidal, valor eficaz ($V_{rms}$), cálculo fasorial, impedancia compleja ($\mathbf{Z}_R, \mathbf{Z}_L, \mathbf{Z}_C$), potencias en AC ($P, Q, S$, factor de potencia $\cos \theta$, compensación de reactiva) y respuesta en frecuencia (filtros pasivos RC pasa-bajos y pasa-altos).
  - `tema4_diodos_mosfet.tex`: Física de semiconductores, unión PN, modelos lineales del diodo (ideal, $V_\gamma = 0{,}7\ \si{\volt}$, lineal con $r_d$), rectificación de media onda y onda completa, filtro por condensador, y transistor MOSFET (NMOS/PMOS, corte, tríodo, saturación, y cálculo del punto de trabajo $Q$).
  - `tema5_electronica_digital.tex`: Niveles lógicos, márgenes de ruido ($NM_H, NM_L$), abanico de salida (\textit{fan-out}), retardos de propagación, inversor CMOS (funcionamiento y curva VTC) y síntesis de puertas lógicas complejas en tecnología CMOS (redes Pull-Up PMOS y Pull-Down NMOS).
  - `tema6_amplificadores_operacionales.tex`: Op-Amp ideal, cortocircuito virtual, configuraciones lineales (inversor, no inversor, seguidor/buffer, sumador, diferencial, integrador y derivador), comparadores en lazo abierto y conversión A/D y D/A (muestreo, Nyquist, cuantificación y redes R-2R).
  - `tema7_examenes_resueltos.tex`: Solucionario paso a paso de los exámenes parciales y finales oficiales de la UGR (Ampère con 3 hilos paralelos, potencias y nudos en DC, análisis fasorial AC por superposición y transformación de fuentes, síntesis lógica NMOS/CMOS, análisis de diodos ON/OFF y etapas con Op-Amps acoplados).

### 2.2. Integración en repasaYA
- **PDF de Producción**: `public/fft/apuntes-teoria-fft.pdf` (67 páginas, 665 KB).
- **Colección de Materiales**: Creación de `src/content/materials/informatica/fundamentos-fisicos-y-tecnologicos/apuntes.json`.
- **Ficha de Asignatura**: Actualización de `src/content/subjects/informatica/fundamentos-fisicos-y-tecnologicos.md` a `status: available` con material `[apuntes]`.

---

## 3. Estado de Métricas de Contenido
- **Total Preguntas Activas**: 2.622 (1.997 Test, 509 V/F, 116 Ocultas)
- **Total Fichas y Glosarios**: 377 (231 Flashcards, 146 Términos)
- **Total Documentos PDF**: 17 (+1)
- **Total Guías y Recursos**: 5
- **Total Asignaturas**: 64 (16 disponibles, 48 planificadas)
- **Bloques de Material**: 40 (+1)

---

## 4. Verificación y Pruebas
- **Compilación LaTeX**: Doble pasada con `pdflatex` finalizada con código 0, generando `main.pdf` y `apuntes_fft.pdf` (67 páginas).
- **Métricas**: `npm run stats` verificado con incremento exacto a 17 PDFs y 40 bloques.
- **Build Estático**: `npm run build` ejecutado en Astro 6 con 87 páginas generadas en 6.71s y 0 errores de validación Zod.
