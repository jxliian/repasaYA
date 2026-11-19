# Spec 021 — SCD: material para el parcial del tema 2.2 (algoritmos de exclusión mutua)

## Contexto
Capel convoca un parcial solo para la segunda parte del tema 2 (algoritmos de exclusión mutua). La convocatoria
dice jueves 19/11/2026, pero se ha cambiado al **jueves 26/11/2026**, 17:30, aula 0.2, 60 minutos. Estructura:
35 preguntas test (5,25 puntos; +0,15 / −0,075 / 0 en blanco; la parte no baja de 0) y 3 ejercicios breves
obligatorios (4,75 puntos). Fuentes: diapositivas «Tema 2. Sincronización en memoria compartida» del 22/10/2026
(`tipo-test/SCD/SCD_T2_2_SPA.pdf`) y relación 2-2, problemas 54–63 (`tipo-test/SCD/scd_t2-2_SPA.pdf`).

## Cambios
- **Simulacro parcial T2.2** (`test-t22.json`): 82 preguntas nuevas de 5 opciones con justificación, en 7 bloques
  (propiedades y condiciones de Dijkstra, refinamiento y Dekker, Dijkstra y Knuth, Peterson 2 y N, Hyman/tickets/
  anillo/Lamport, hardware, distribuidos). Generadas con `tipo-test/SCD/build_test_t22.py` (opciones barajadas con
  semilla fija).
- **Motor de tests**: dos campos opcionales en los materiales `test`:
  - `penalty`: fracción de acierto que resta cada fallo con el descuento activado (0.33 por defecto; 0.5 en T2.2).
    Se usa en el test normal y en el modo de supuestos, y la etiqueta muestra el valor real.
  - `examSize`: añade el modificador «Simulacro de examen» (muestra al azar de ese tamaño, descuento activado y
    botón «Dejar en blanco (0 puntos)», que no suma ni resta y muestra la correcta y la justificación).
- **Kit del parcial T2.2** (`relaciones/SCD/kit_parcial_t22.tex` → `public/scd/kit-parcial-t22-scd.pdf`, 13 págs):
  táctica para los 60 minutos y regla de contestar o dejar en blanco, teoría fiel a las diapositivas, plantillas de
  ejercicios breves, 9 ejercicios resueltos y tabla resumen.
- **Guía** `/scd/guia-t22/` con el formato del examen, qué entra, material y plan de 7 días (19–25/11).
- Descripción de la asignatura actualizada (340 preguntas).

## Decisiones
- Dos claves del banco de otros años contradicen las diapositivas o el código: «máximo de turnos en Peterson N =
  N−1» (las diapositivas dan n(n−1)/2) y «cambiar la guarda de Dijkstra a ≠ en_SC pierde la seguridad» (la EM la
  mantiene la 2ª barrera; se pierde el progreso). El material nuevo sigue a las diapositivas y al código, y avisa de
  la discrepancia en el kit, la guía y la justificación de las preguntas. No se ha tocado el banco antiguo.
- El dato de la espera de Knuth (2^(n−1)−1) no está en las diapositivas: va en el kit marcado como dato clásico y no
  se pregunta en el simulacro.

## Verificación
- `npm run build`: 115 páginas, sin errores.
- Chrome sin cabeza por CDP: simulacro de 35 preguntas, botón en blanco visible y funcional, nota con descuento
  0,5 correcta (8 aciertos, 26 fallos, 1 en blanco → 0), sin errores de consola; guía y hub de la asignatura enlazan
  el material nuevo; el PDF se sirve.
