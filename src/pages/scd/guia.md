---
layout: ../../layouts/GuideLayout.astro
title: "Plan de Estudio y Estrategia: Examen Parcial de SCD (29 Octubre 2026)"
description: "Guía intensiva de 7 días, desglose del formato de examen con penalización (-0.5), selección de los ejercicios prácticos clave y estrategia para arrasar con Capel."
badge: "SCD · Grado en Ingeniería Informática / DGIIM · UGR"
---

# Plan de Estudio y Estrategia: Primer Parcial de SCD
### Convocatoria Oficial de Evaluación Continua — Jueves 29 de Octubre de 2026

> **Información Oficial de la Convocatoria (Prof. Manuel I. Capel Tuñón):**  
> 🗓️ **Fecha:** Jueves, 29 de octubre de 2026  
> ⏰ **Horario:** 17:30 a 19:30 horas (duración máxima del examen: **100 minutos**)  
> 📍 **Modalidad:** Presencial e individual  
> 🎯 **Peso en la Calificación Final:** **3,5 puntos sobre 10** de la teoría (Tema 1: 1,2 puntos | Tema 2: 2,3 puntos)

---

## 1. Radiografía y Estructura del Examen

El examen consta de dos bloques independientes que se realizan en un tiempo total de **100 minutos**:

```
                              EXAMEN PARCIAL (100 min · 3,5 puntos)
                                               │
             ┌─────────────────────────────────┴─────────────────────────────────┐
             ▼                                                                   ▼
PARTE 1: CUESTIONARIO TEST (5 opciones)                            PARTE 2: RESOLUCIÓN DE PROBLEMAS
• 1 única respuesta correcta                                      • Se proponen 3 problemas
• ⚠️ PENALIZACIÓN: Cada 2 fallos anulan 1 acierto                  • El estudiante ELIGE y RESUELVE 2
  (Fallo = -0,5 aciertos | Blanco = 0)                            • Código C++11, semáforos, monitores y trazas
```

### El Peso de los Temas: El Tema 2 es Decisivo
* **Tema 1 (1,2 puntos — 34% del examen):** Introducción a la concurrencia, entrelazados, condiciones de Bernstein, grafos de precedencias, lógica de Hoare y teorema de no interferencia de Owicki-Gries.
* **Tema 2 (2,3 puntos — 66% del examen):** Exclusión mutua, algoritmos de memoria compartida (Dekker, Peterson, Lamport, Hyman, Dijkstra), mecanismos hardware (Swap, Test-and-Set), semáforos y monitores (semántica Hoare/SU vs. Mesa/SC).

> 💡 **Conclusión Estratégica:** El Tema 2 vale prácticamente el **doble** que el Tema 1. Quien domine los algoritmos de exclusión mutua y los monitores tiene asegurado el aprobado con holgura.

---

## 2. ¿Empollarse los Tipo Test de Memoria Funciona? Análisis Crítico

> **Tu duda:** *"Tengo pensado leerme profundamente los temas y hacer los tipo test para aprenderlos de memoria súper bien... ¿Eso lo ves bien? Todos los años sube los tipo test a PRADO, bastantes; este año no ha subido... lo que me sugiere que sea igual a los que tengo."*

### La Verdad sobre el Banco de Preguntas de Capel
1. **Es cierto que el banco base se reutiliza:** Capel utiliza un histórico consolidado de preguntas que hemos volcado y verificado en **repasaYA** (las 207 preguntas oficiales de los Temas 1 y 2). El hecho de que este año no haya publicado tests nuevos en PRADO refuerza la hipótesis de que el cuestionario se extraerá de este mismo repertorio histórico.
2. **PERO memorizar a ciegas la letra de la opción (`a, b, c, d, e`) es una trampa mortal:**
   * Capel es célebre por **reordenar las alternativas** o **cambiar una sola palabra** en el enunciado para cazar a quienes memorizan patrones de memoria (por ejemplo, cambiar *"planificación justa"* por *"planificación débilmente justa"*, *"progreso local"* por *"progreso global"*, o sustituir `estado[turno] = pasivo` por `estado[turno] != enSC`).
   * Además, los tests solo cubren una parte del examen: **los problemas valen la mayor parte de la nota** y no se pueden resolver memorizando tests.
3. **La regla matemática de la penalización ($-0,5$ por fallo):**
   * En un test de 5 opciones con penalización de $2 \text{ fallos} = 1 \text{ acierto}$:
     $$\text{Esperanza al azar puro} = \frac{1}{5}(+1) + \frac{4}{5}(-0,5) = 0,2 - 0,4 = \mathbf{-0,20 \text{ (Pérdida neta)}}$$
   * **REGLA DE ORO EN EL EXAMEN:**
     * Si no tienes ni la menor idea $\implies$ **DÉJALA EN BLANCO**.
     * Si dudas entre 4 o 5 opciones $\implies$ **EN BLANCO**.
     * Si has descartado 3 opciones con total seguridad y dudas entre 2 $\implies$ **ARRIESGA** (Esperanza: $\frac{1}{2}(+1) - \frac{1}{2}(0,5) = +0,25$).

### La Estrategia Correcta con los Tests
En vez de memorizar la letra, **aprende la justificación pedagógica**. En el motor de tests de repasaYA, cada una de las 207 preguntas tiene redactada la explicación técnica citando la transparencia exacta de Capel. Cuando hagas el test, pregúntate: *«¿Por qué son falsas las otras 4?»*.

---

## 3. Los Ejercicios Prácticos que DEBES Saber a la Perfección

En la Parte 2 se propondrán **3 problemas y deberás elegir 2**. Capel suele proponer:
1. Un problema de **Algoritmos Software de Exclusión Mutua / Trazas de Intercalación**.
2. Un problema de **Sincronización con Monitores** (Hoare o Mesa).
3. Un problema de **Lógica de Hoare / Semáforos / Paralelización**.

De los **63 problemas resueltos** en el solucionario oficial en PDF de repasaYA, estos son los **intocables** que debes dominar de memoria:

### Grupo 1: Exclusión Mutua en Memoria Compartida (Tema 2-2)
* **Ejercicio 57 (Peterson para 2 procesos):**
  * *Qué saberte:* Demostración de exclusión mutua por contradicción en la variable `turno`.
  * *Pregunta trampa típica:* ¿Qué ocurre si se intercambian las asignaciones `turno := 1-i` y `quiere[i] := true`? *(Respuesta: Se pierde la exclusión mutua).*
  * *Pregunta de memoria débil:* ¿Por qué falla en procesadores modernos sin `std::atomic`? *(Por el buffer de escritura y la reordenación Store-Load).*
* **Ejercicio 56 (Algoritmo de Hyman):**
  * *Qué saberte:* Es el contraejemplo estrella de Capel. Saber dibujar de memoria la **tabla de intercalación** donde $P_0$ supera la espera interna, es suspendido antes de fijar `turno := 0`, y $P_1$ entra a la SC porque ve `turno == 1`, entrando ambos a la SC ($N_{SC}=2$).
* **Ejercicio 55 (Cuarto Intento / Dos indicadores sin turno):**
  * *Qué saberte:* Demostración de que **sí** tiene exclusión mutua, pero adolece de **livelock (bloqueo dinámico)** simétrico en paso síncrono (*lock-step*). Saber explicar cómo la variable de turno en Peterson rompe esta simetría.
* **Ejercicio 62 (Peterson para N procesos — Filtro por niveles):**
  * *Qué saberte:* Demostración del Lema del Filtro ($\le N-L$ procesos en nivel $L$). Justificación de por qué **no** pueden encontrarse 2 procesos en $N-2$ y 0 en $N-3$ (Lema 3 de distribución monótona decreciente).
* **Ejercicio 63 (Dijkstra para N procesos con cambio de guarda):**
  * *Qué saberte:* Por qué cambiar `estado[turno] = pasivo` por `estado[turno] != enSC` **no** rompe la exclusión mutua (la cuida el segundo bucle `for`), pero **destruye completamente el progreso** provocando que los procesos se arrebaten el turno cíclicamente en un livelock infinito.

### Grupo 2: Monitores y Sincronización de Alto Nivel (Tema 2-1 y Relación 2)
* **Ejercicio 40 (Semántica Hoare/SU vs. Mesa/SC):**
  * *Regla de oro:* En semántica **Hoare (Señalar y Espera Urgente)** la condición señalada se cumple de inmediato al despertar $\implies$ se usa **`if (!cond) c.wait()`**. En semántica **Mesa / POSIX (Señalar y Continuar)** otros hilos pueden adelantarse antes de que el despertado tome el cerrojo $\implies$ es obligatorio usar **`while (!cond) c.wait()`**.
* **Ejercicio 43 (El Puente de un solo carril con cupo máximo):**
  * Control de dirección (`sentido_actual`), contador de vehículos cruzando, cola de espera y cupo máximo de 10 coches para evitar inanición de la dirección opuesta.
* **Ejercicio 44 (La Olla de los Caníbales / Salvajes y el Cocinero):**
  * Sincronización clásica productor-consumidor múltiple con un servidor único que duerme mientras la olla tiene comida (`raciones > 0`) y es despertado exclusivamente por el salvaje que encuentra la olla vacía.
* **Ejercicio 42 (Lectores-Escritores con Prioridad):**
  * Saber implementar tanto la versión con prioridad a lectores como la versión con prioridad a escritores (evitando la inanición de solicitudes de modificación).

### Grupo 3: Lógica de Hoare y Concurrencia Básica (Tema 1)
* **Ejercicio 1 (Bucles de incremento concurrentes solapados):**
  * Dos procesos ejecutan $k$ incrementos concurrentes sobre $x$ con lecturas y escrituras en registros independientes. El valor máximo es $2k$ y el mínimo es **$2$** (por solapamiento extremo en la primera y última iteración).
* **Ejercicios 4 y 5 (Condiciones de Bernstein y Paralelización):**
  * $I(S_1) \cap O(S_2) = \emptyset \land O(S_1) \cap I(S_2) = \emptyset \land O(S_1) \cap O(S_2) = \emptyset$. Cómo construir el grafo de precedencias y programarlo con `cobegin / coend` y semáforos binarios.
* **Ejercicios 14 y 20 (Teorema de No Interferencia de Owicki-Gries):**
  * Demostrar que para dos procesos $\{P_1\} S_1 \{Q_1\}$ y $\{P_2\} S_2 \{Q_2\}$, toda aserción intermedia $A$ en la prueba de $P_1$ se preserva ante cualquier asignación $T$ de $P_2$: $\{A \land pre(T)\} T \{A\}$.

---

## 4. Plan de Estudio Intensivo Día a Día (7 Días)

Cronograma optimizado desde hoy hasta el examen:

| Día | Fecha | Bloque Temático | Tareas Prácticas Clave | Material repasaYA |
| :--- | :--- | :--- | :--- | :--- |
| **Día 1** | Jueves 22 Oct | **Tema 1: Concurrencia Básica** | Intercalaciones, bucles de registros (Ej. 1-3), Bernstein y grafos de precedencias (Ej. 4-10). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 4-15) |
| **Día 2** | Viernes 23 Oct | **Tema 1: Lógica de Hoare** | Axiomas de asignación, precondición más débil ($wp$), Owicki-Gries e invariantes (Ej. 14-25). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 16-35) + Test Bloque 1 |
| **Día 3** | Sábado 24 Oct | **Tema 2-2: Exclusión Software** | Condiciones de Dijkstra, Cuarto intento (Ej. 55), Hyman (Ej. 56), Peterson 2 y N (Ej. 57, 62), Dijkstra (Ej. 63). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 61-77) |
| **Día 4** | Domingo 25 Oct | **Tema 2-1: Hardware y Semáforos** | Swap (Ej. 58), Capacidad $k$ (Ej. 59), Semáforos en fase y rondas (Ej. 37-39), Productor-Consumidor. | [PDF Apuntes](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/apuntes-teoria-scd.pdf) (Tema 2-1) + Test Bloque 2 |
| **Día 5** | Lunes 26 Oct | **Tema 2: Monitores Avanzados** | Semántica SU vs SC (Ej. 40), Puente (Ej. 43), Caníbales (Ej. 44), Lectores-Escritores (Ej. 42), Filósofos (Ej. 48). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 45-60) |
| **Día 6** | Martes 27 Oct | **Simulacro y Drill de Test** | Ráfaga de los 207 tests de repasaYA en bloques de 30 preguntas aplicando la penalización real. | [Motor de Tests SCD](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/test.json) |
| **Día 7** | Miércoles 28 Oct | **Repaso de Trampas y Fórmulas** | Repasar tablas de contraejemplos, invariantes formales, límites de Peterson y Habermann. Descanso temprano. | Guía rápida y notas |
| **Día D** | Jueves 29 Oct | **EL EXAMEN (17:30 h)** | Repaso visual 1 hora antes. Ejecutar estrategia de los 100 minutos. | ¡A por el 3,5/3,5! |

---

## 5. Estrategia de Gestión de los 100 Minutos en el Examen

La mayoría de alumnos suspenden o sacan baja nota no por falta de estudio, sino por **mala gestión del reloj**:

```
                       REPARTO TEMPORAL SUGERIDO (100 MINUTOS)
 ┌──────────────────────┬────────────────────────────┬────────────────────────────┬─────────────┐
 │  PARTE 1: TEST       │  PROBLEMA 1 ELEGIDO        │  PROBLEMA 2 ELEGIDO        │  REVISIÓN   │
 │  30 - 35 minutos     │  25 - 30 minutos           │  25 - 30 minutos           │  10 minutos │
 └──────────────────────┴────────────────────────────┴────────────────────────────┴─────────────┘
```

1. **Minutos 0 a 5 — Lectura completa y elección de problemas:**
   * Lee con calma los 3 problemas propuestos.
   * **Descarta de inmediato el que veas más enrevesado** (por ejemplo, si uno pide una prueba formal exhaustiva con Owicki-Gries de muchas ramas y otro es un monitor clásico de puente o caníbales, ve de cabeza a por el monitor).
   * Marca los dos problemas elegidos y no cambies de idea a mitad de examen salvo catástrofe.
2. **Minutos 5 a 35 — Bloque Test:**
   * Haz una primera pasada respondiendo **únicamente las que te sabes al 100%**.
   * En la segunda pasada, analiza aquellas donde dudes entre dos. Aplica la regla: si has descartado 3 opciones con solidez, marca la más fundamentada. Si dudas entre 3 o más, déjala en blanco.
3. **Minutos 35 a 90 — Los 2 Problemas Prácticos (25-30 min cada uno):**
   * *Estructura siempre la respuesta:*
     1. **Declaración de variables compartidas e inicialización.**
     2. **Invariante de seguridad formal** (ej. $0 \le dentro \le k$ o $coches\_norte \times coches\_sur == 0$).
     3. **Código claro en C++11 o pseudocódigo estructurado** con nombres descriptivos.
     4. **Justificación de progreso:** Explica brevemente por qué no hay interbloqueo (*deadlock*) ni inanición (*starvation*).
4. **Minutos 90 a 100 — Control de daños y repaso:**
   * Comprueba que no has marcado opciones dudosas por impulso en el test.
   * Verifica los nombres de variables y que todos los cerrojos/semáforos abiertos tienen su `post()` o `unlock()` correspondiente.

---

## 6. Resumen de Fórmulas y Conceptos Trampa Frecuentes

* **Habermann:** Semáforo como monitor con invariante $np = \min(na, nv)$. Si $na < nv$, la cola de espera tiene $nv - na$ procesos suspendidos.
* **Peterson N procesos:** Cota máxima de espera uniforme $= \frac{N(N-1)}{2}$ adelantamientos.
* **Hoare vs. Mesa:** Señal desplazante (SU) $\implies$ el señalador cede el monitor y el despertado entra sin competencia $\implies$ `if`. Señal no desplazante (SC) $\implies$ el señalador continúa y el despertado va a la cola de listos $\implies$ `while`.
* **Desempate en Tickets:** Tupla lexicográfica $(n[i], i) < (n[j], j) \iff (n[i] < n[j]) \lor (n[i] == n[j] \land i < j)$.
* **Instrucción Swap:** Garantiza exclusión mutua mediante conservación de llaves, pero **NO garantiza equidad ni orden FIFO**.
