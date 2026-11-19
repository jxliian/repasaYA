---
layout: ../../layouts/GuideLayout.astro
title: "Plan para el parcial del tema 2.2 de SCD (26 de noviembre de 2026)"
description: "Qué entra en el examen de algoritmos de exclusión mutua, cómo puntúa (35 preguntas con −0,075 por fallo y 3 ejercicios breves) y un plan de 7 días con el material de repasaYA."
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

1. **El problema y las condiciones de Dijkstra.** Seguridad frente a vivacidad, interbloqueo, livelock e inanición. Las cuatro condiciones y por qué solo dan una solución parcialmente correcta.
2. **Refinamiento sucesivo hasta Dekker.** Qué falla en cada una de las cinco etapas.
3. **Dijkstra y Knuth para N procesos.** Las dos barreras, por qué Dijkstra tiene inanición y cómo la quita el turno circular de Knuth.
4. **Peterson para 2 y para N procesos.** La demostración de exclusión mutua, las etapas, los lemas y la cota n(n−1)/2.
5. **Otros algoritmos de la relación.** Hyman (incorrecto), tickets, anillo, Lamport, `swap` y el cerrojo de capacidad k.
6. **Algoritmos distribuidos.** Ricart-Agrawala (2(n−1) mensajes), Suzuki-Kasami (n mensajes) y la regeneración del testigo de Misra.

## El material

- **[Kit del parcial T2.2](/scd/kit-parcial-t22-scd.pdf)** (PDF, 13 páginas). Toda la teoría que pregunta el test, plantillas para los ejercicios breves, 9 ejercicios resueltos y una tabla resumen.
- **Simulacro parcial T2.2.** 82 preguntas nuevas con justificación. Activa **Simulacro de examen** para hacer 35 al azar con la puntuación real y la opción de dejar en blanco. Lo tienes en la página de la asignatura.
- **Relaciones de problemas resueltas.** Los problemas 54 a 63 están resueltos al detalle en el bloque III.

## Plan de 7 días

| Día | Qué hacer |
|---|---|
| **Jueves 19** | Lee las secciones 1 a 3 del kit (táctica, condiciones de Dijkstra, refinamiento y Dekker). Haz el bloque «Propiedades y condiciones de Dijkstra» del simulacro. |
| **Viernes 20** | Secciones 4 y 5 del kit: Dijkstra, Knuth y Peterson. Escribe de memoria el código de Peterson para 2 y su demostración de exclusión mutua. |
| **Sábado 21** | Relación: problemas 55, 56, 57 y 61. Primero intenta tú la traza y después compárala con la solución. |
| **Domingo 22** | Algoritmos distribuidos (sección 8 del kit) y ejercicios resueltos 6 y 7. Bloque «Algoritmos distribuidos» del simulacro. |
| **Lunes 23** | Relación: problemas 58, 59, 60 y 63. Primer simulacro completo de 35 preguntas con el cronómetro en 25 minutos. |
| **Martes 24** | Repasa las preguntas que fallaste (modo «Puntos débiles»). Problemas 54 y 62 de la relación. Segundo simulacro. |
| **Miércoles 25** | Tabla resumen del kit y las tres plantillas. Último simulacro. Nada nuevo: descansa. |

## Dos avisos sobre el banco de otros años

- **Peterson para N procesos.** En un banco de otros años la respuesta a «máximo de turnos que espera un proceso» es N−1. Según las diapositivas de este curso es **n(n−1)/2**.
- **Dijkstra con la guarda cambiada a `c[turno] ≠ en_SC`** (problema 63). La clave de otros años decía «pierde corrección (seguridad)». Razonado sobre el código, la exclusión mutua se mantiene gracias a la segunda barrera y lo que se pierde es el progreso. Si aparece una opción que hable de progreso o vivacidad, elige esa.
