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

## Iteración 2 (19/11/2026): contraste con Infomates, diapositivas del tema 1 y banco antiguo
- Fuentes revisadas: `Temario_infomates.pdf` §2.1 (págs. 33–59) y `T1.pdf` diapositiva 1.25. `Apuntes_isma.pdf` solo
  cubre los temas 3 y 4: no aporta nada al 2.2.
- Correcciones de contenido:
  - **Ausencia de interbloqueo = seguridad** en la terminología de Capel (diapositiva 1.25 y clave del Parcial I).
    Corregido en el kit y añadido aviso a la solución del problema 54 (`relacion2.tex`, PDF de relaciones recompilado).
  - **Dekker**: EM y alcanzabilidad; vivacidad y equidad no demostrables (dependen del arbitraje del hardware de
    memoria). Corregidos el kit, la tabla resumen y la pregunta del simulacro.
  - Añadidos: 5ª condición de Knuth (retraso calculable), copia local del turno en Knuth, f(n) = 2^(n−1) − 1 con su
    recurrencia, condición de Dijkstra que incumple cada etapa del refinamiento.
- Simulacro: 7 preguntas nuevas sobre lo anterior y 41 del banco antiguo revisadas (bloque «Exámenes y bancos de otros
  años (revisadas)»). Total 130.
- Banco general (`test.json`): corregidas 6 preguntas (índices 46, 53, 55, 66, 136, 169): opciones duplicadamente
  correctas, «progreso finito», Dekker, guarda de Dijkstra y espera de Peterson N.
- `npm run build` 115 páginas; simulacro probado en Chrome sin errores.

## Iteración 3 (22/11/2026): relación 2-2 con enunciados oficiales y soluciones verificadas
- Kit (`relaciones/SCD/kit_parcial_t22.tex`, 24 págs.): la antigua sección de 9 ejercicios con enunciados propios se
  sustituye por la **relación 2-2 completa** (problemas 54–63 con el enunciado oficial copiado tal cual) más 4
  ejercicios extra de las diapositivas (A–D). Las mismas soluciones reemplazan las del bloque III de
  `relaciones/SCD/temas/relacion2.tex` (PDF de relaciones recompilado, 73 págs.).
- Verificación: verificador exhaustivo de intercalaciones (scratchpad `mc.py`/`ov.py`, no versionado). Resultados:
  55 EM ok + livelock; 56 EM violada; 57 EM ok, intercambiada violada, espera acotada 1 aunque el otro sea lento;
  58 EM ok; 60 EM ok; 61 EM ok, sin la puerta `n[i]:=1` violada, espera acotada 1; 62 EM ok, (b) 0 estados con 2 en
  N−2 y 0 en N−3 (N=4), adelantamientos ilimitados con un proceso lento (N=3,4); 63 guarda `!= enSC`: EM ok y
  livelock (N=2,3), original sin livelock.
- Errores corregidos en las soluciones antiguas: 54 usaba la formulación de libro de las condiciones de Dijkstra
  (con ausencia de inanición) y concluía «correcto en vivacidad individual»; 58 tenía un invariante que no sumaba 1;
  62c afirmaba la cota n(n−1)/2 sin hipótesis de velocidad.
- Apuntes de teoría (`apuntes/SCD/temas/tema2_parte1.tex`, 81 págs.): condiciones de Dijkstra con la formulación de
  las diapositivas (2.3), Dekker sin «completamente correcto», lemas del filtro con la numeración L1–L4 de las
  diapositivas y la cota en turnos con su hipótesis.
- Guía `/scd/guia-t22/`: plan de cuatro tardes de 3 h (22–25/11) y aviso sobre las condiciones de Dijkstra.
- Descripción de la asignatura: 388 preguntas (258 del test general + 130 del simulacro).
- `npm run build`: 115 páginas.
