---
layout: ../../layouts/GuideLayout.astro
title: "Plan para el parcial del tema 2.2 de SCD (26 de noviembre de 2026)"
description: "Qué entra en el examen de algoritmos de exclusión mutua, cómo puntúa (35 preguntas con −0,075 por fallo y 3 ejercicios breves) y un plan de cuatro tardes de 3 horas con el material de repasaYA."
badge: "SCD · Grado en Ingeniería Informática · UGR"
---

# Parcial del tema 2.2: algoritmos de exclusión mutua

> **Jueves 26 de noviembre de 2026, 17:30, aula 0.2.** La convocatoria decía 19 de noviembre, pero el examen se ha cambiado al 26.
> **60 minutos**, individual y sin apuntes ni dispositivos.

Este año la segunda parte del tema 2 tiene examen propio. Entra lo que hay en las diapositivas del 22 de octubre («Sincronización en memoria compartida: exclusión mutua») y en la relación de problemas 2-2 (problemas 54 a 63).

## Cómo es el examen

| Parte | Puntos | Cómo puntúa |
|---|---|---|
| 35 preguntas tipo test | 5,25 | +0,15 por acierto, −0,075 por fallo, 0 en blanco. La parte no baja de 0. |
| 3 ejercicios breves obligatorios | 4,75 | unos 1,6 puntos cada uno |
| Pregunta extra (si la hay) | hasta el 5 % de la nota de teoría | voluntaria |

No hace falta una nota mínima en ninguna parte.

**Cada fallo resta medio acierto.** Si dudas entre dos opciones, contesta (ganas de media). Si dudas entre tres, da igual. Si no has descartado nada, déjala en blanco.

**Reparto de los 60 minutos:** 25 para el test (unos 40 segundos por pregunta, en dos pasadas), 30 para los ejercicios (10 cada uno) y 5 para repasar.

## Qué entra

1. **El problema y las condiciones de Dijkstra.** Seguridad frente a vivacidad, interbloqueo, livelock e inanición. Las cuatro condiciones de las diapositivas y por qué solo dan una solución parcialmente correcta.
2. **Refinamiento sucesivo hasta Dekker.** Qué falla en cada una de las cinco etapas.
3. **Dijkstra y Knuth para N procesos.** Las dos barreras, por qué Dijkstra tiene inanición y cómo la quita el turno circular de Knuth.
4. **Peterson para 2 y para N procesos.** La demostración de exclusión mutua, las etapas, los lemas y la cota n(n−1)/2.
5. **Otros algoritmos de la relación.** Hyman (incorrecto), tickets, anillo, Lamport, `swap` y el cerrojo de capacidad k.
6. **Algoritmos distribuidos.** Ricart-Agrawala (2(n−1) mensajes), Suzuki-Kasami (n mensajes) y la regeneración del testigo de Misra.

## El material

- **[Kit del parcial T2.2](/scd/kit-parcial-t22-scd.pdf)** (PDF, 24 páginas).
  - Secciones 1 a 8: la teoría tal como la pregunta el test.
  - Sección 9: las plantillas para los ejercicios breves.
  - Sección 10: **la relación 2-2 entera**, con los enunciados oficiales de los problemas 54 a 63 tal cual y su solución.
  - Sección 11: cuatro ejercicios extra de las diapositivas.
  - Al final, una tabla resumen.
- **Simulacro parcial T2.2.** 130 preguntas con justificación: 89 nuevas y 41 de exámenes y bancos de otros años, revisadas. Activa **Simulacro de examen** para hacer 35 al azar con la puntuación real y la opción de dejar en blanco. Lo tienes en la página de la asignatura.
- **[Apuntes de teoría](/scd/apuntes-teoria-scd.pdf)**. El tema 2 está corregido con la formulación de las diapositivas.

## Plan: cuatro tardes de 3 horas

Cada tarde tiene teoría, problemas de la relación y test. Con los problemas, intenta tú primero la solución con el reloj (10 minutos, como en el examen) y después compárala con la del kit.

### Domingo 22: el problema, Dijkstra y el refinamiento

| Tiempo | Qué hacer |
|---|---|
| 1 h 15 min | Kit, secciones 1 a 3: táctica, propiedades, condiciones de Dijkstra, refinamiento y Dekker. |
| 45 min | Problemas **54, 55 y 56** (sección 10 del kit). |
| 30 min | Simulacro: bloques «Propiedades y condiciones de Dijkstra» y «Refinamiento sucesivo y Dekker». |
| 30 min | Repasa lo que hayas fallado con las justificaciones. |

### Lunes 23: Dijkstra, Knuth y Peterson

| Tiempo | Qué hacer |
|---|---|
| 1 h | Kit, secciones 4 y 5. Escribe de memoria el código de Peterson para 2 y su demostración de exclusión mutua. |
| 1 h 15 min | Problemas **57, 62 y 63**. |
| 30 min | Simulacro: bloques «Dijkstra y Knuth» y «Peterson». |
| 15 min | Repaso de fallos. |

### Martes 24: el resto de algoritmos y el primer simulacro

| Tiempo | Qué hacer |
|---|---|
| 45 min | Kit, secciones 6 a 8 (otros algoritmos, hardware y distribuidos) y ejercicios extra C y D. |
| 1 h 15 min | Problemas **58, 59, 60 y 61**. |
| 30 min | Primer simulacro completo: 35 preguntas en 25 minutos con **Simulacro de examen** activado. |
| 30 min | Corrige el simulacro y repasa con el modo «Puntos débiles». |

### Miércoles 25: examen de prueba

| Tiempo | Qué hacer |
|---|---|
| 1 h | **Examen de prueba de 60 minutos**: un simulacro de 35 preguntas (25 minutos) y tres problemas de la relación elegidos al azar (30 minutos), sin mirar nada. |
| 45 min | Corrígelo con las soluciones del kit. Lo que falles, vuelve a hacerlo. |
| 45 min | Avisos de abajo, tabla resumen del kit y las tres plantillas. |
| 30 min | Último simulacro. Nada nuevo; después, descansa. |

**Jueves 26 antes del examen:** 20 minutos con la tabla resumen y los avisos. Nada más.

## Avisos: claves corregidas y puntos con trampa

- **Condiciones de Dijkstra.** Las de las diapositivas no son las de los libros. Son estas cuatro:
  1. no suponer nada sobre las instrucciones ni el número de procesos;
  2. ni sobre la velocidad, salvo que no es cero (progreso finito);
  3. quien está fuera de la SC no impide entrar a los demás;
  4. la SC siempre la alcanza alguno de los que esperan.

  Un algoritmo que solo cumple estas cuatro es **parcialmente correcto**: no tiene interbloqueo, pero **puede tener inanición**. Antes los apuntes daban la versión de los libros, con la ausencia de inanición incluida; ya están corregidos.
- **Peterson para N procesos.** En un banco de otros años la respuesta a «máximo de turnos que espera un proceso» es N−1. Según las diapositivas de este curso es **n(n−1)/2**. Es una cota en *turnos*: si un proceso es arbitrariamente lento, los demás pueden adelantarle sin límite (problema 62c). Sin inanición no es lo mismo que espera acotada.
- **Dijkstra con la guarda cambiada a `c[turno] ≠ en_SC`** (problema 63). La clave de otros años decía «pierde corrección (seguridad)». Lo que se pierde es el **progreso** (livelock), y la exclusión mutua se mantiene gracias a la segunda barrera; está comprobado en todas las intercalaciones. Si aparece una opción que hable de progreso o vivacidad, elige esa.
- **Ausencia de interbloqueo.** En las diapositivas del tema 1 de Capel es una propiedad de **seguridad** («nunca ocurrirá que los procesos esperen algo que nunca sucederá»), y así se puntuó en el Parcial I. El *progreso* («algún proceso acabará entrando») sí es de vivacidad. La equidad, según Capel, es de vivacidad.
- **Dekker.** Es la primera solución aceptable (EM y alcanzabilidad), pero su vivacidad y su equidad **no se pueden demostrar**: dependen de cómo arbitre el hardware los accesos simultáneos a memoria. La primera solución sin inanición es la de Knuth.
- **Quinta condición (Knuth).** Poder calcular el retraso máximo de cualquier proceso. Knuth: 2ⁿ⁻¹ − 1 adelantamientos; Peterson: n(n−1)/2 turnos.

Estas correcciones salen de contrastar el material con las diapositivas y con los apuntes de Infomates. Las claves erróneas también se han corregido en el test general de la asignatura.
