---
layout: ../../layouts/GuideLayout.astro
title: "Plan de Rescate y Estrategia: Examen Parcial de SCD (29 Octubre 2026)"
description: "Sprint intensivo de emergencia de 4 días (25-29 Oct), desglose del examen con penalización (-0.5), selección de ejercicios indispensables y táctica para arrasar con Capel."
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

## 2. ¿Qué Hacer con la Teoría y el Tipo Test? Análisis Crítico y Táctica

> **Tu situación actual:** *"No he podido estudiar antes y tengo poco tiempo... ¿qué hago con la teoría y el tipo test? ¿Me empoyo las transparencias o hago tests de memoria?"*

### ⚠️ El Error Típico: Leer Diapositivas Pasivamente
Leerse las más de 80 diapositivas teóricas de Capel como una novela a pocos días del examen es una trampa: consume un tiempo vital que necesitas para programar y no fija los conceptos trampa. En este examen, **la teoría se aprende y se consolida haciendo los tests comentados de repasaYA y deduciendo los invariantes de los problemas**.

### La Verdad sobre el Banco de Preguntas de Capel
1. **El banco base se reutiliza:** Capel utiliza un histórico consolidado de preguntas que hemos volcado y verificado en **repasaYA** (las 207 preguntas oficiales de los Temas 1 y 2). Al no haber publicado cuestionarios nuevos en PRADO, las preguntas del examen saldrán en su inmensa mayoría de este banco.
2. **Memorizar letras (`a, b, c, d, e`) a ciegas es suicida:**
   * Capel reordena alternativas y cambia palabras clave para cazar a quienes memorizan patrones (por ejemplo: *"planificación justa"* vs *"débilmente justa"*, *"progreso local"* vs *"progreso global"*, o cambiar una desigualdad en un invariante).
   * **El método correcto:** Haz los tests en repasaYA leyendo la **justificación técnica** que acompaña a cada una de las 207 preguntas. Cada justificación explica por qué la correcta es cierta citando la transparencia exacta y desmonta una a una las otras 4 opciones.
3. **La regla matemática de la penalización (-0,5 por fallo):**
   * En un test de 5 opciones donde **cada 2 fallos anulan 1 acierto**:
     > **Esperanza al azar puro** = ⅕ · (+1) + ⅘ · (-0,5) = 0,2 - 0,4 = **-0,20 (Pérdida neta)**
   * **REGLA DE ORO DE COMBATE EN EL EXAMEN:**
     * Si no tienes certeza alguna ⟹ **EN BLANCO INMEDIATO**.
     * Si dudas entre 4 o 5 opciones ⟹ **EN BLANCO**.
     * Si has descartado 3 opciones con total seguridad y dudas entre 2 ⟹ **ARRIESGA** (Esperanza: ½ · (+1) - ½ · (0,5) = **+0,25**).
   * **Objetivo realista:** Contestar entre 10 y 14 preguntas con seguridad plena, dejar el resto en blanco y garantizar un 2,5 o 3 sobre 3,5 en el bloque test sin autodestruirte con penalizaciones.

---

## 3. Los Ejercicios Prácticos que DEBES Saber Sí o Sí

En la Parte 2 se propondrán **3 problemas y deberás elegir y resolver 2**.  
La terna típica de Capel es:
1. **Problema A:** Algoritmo Software / Hardware de Exclusión Mutua (Tema 2-2).
2. **Problema B:** Monitor de Sincronización Condicional en C++11 (Tema 2-1).
3. **Problema C:** Lógica de Hoare / Owicki-Gries / Paralelización Bernstein (Tema 1).

> 🎯 **Recomendación Estratégica de Elección:**  
> La combinación más rápida, limpia y con menor riesgo de error algebraico es **elegir el Problema B (Monitor) y el Problema A (Exclusión Mutua)**. Deja Hoare/Owicki-Gries como reserva solo si uno de los otros dos viniera con un enunciado excepcionalmente complejo.

De los **63 problemas resueltos** en el solucionario oficial en PDF de repasaYA, estos son los **imprescindibles absolutos**:

### Grupo 1: Exclusión Mutua en Memoria Compartida (Tema 2-2)
* **Ejercicio 57 (Peterson para 2 procesos):**
  * *Qué saberte:* Demostración formal de exclusión mutua por reducción al absurdo en la variable `turno`.
  * *Pregunta trampa:* ¿Qué ocurre si se intercambian las asignaciones `turno := 1-i` y `quiere[i] := true`? *(Respuesta: Se pierde por completo la exclusión mutua).*
  * *Hardware y memoria débil:* ¿Por qué falla en procesadores modernos sin `std::atomic`? *(Por el buffer de escritura y la reordenación Store-Load; requiere secuencialmente consistente).*
* **Ejercicio 56 (Algoritmo de Hyman):**
  * *Qué saberte:* El contraejemplo rey de Capel. Dibujar de memoria la **tabla de intercalación** donde P₀ supera la espera interna, es suspendido antes de fijar `turno := 0`, y P₁ entra a la SC porque ve `turno == 1`, entrando ambos a la vez (`N_sc = 2`).
* **Ejercicio 55 (Cuarto Intento / Dos indicadores sin turno):**
  * *Qué saberte:* Demostración de que **sí** cumple exclusión mutua, pero adolece de **livelock (bloqueo dinámico)** simétrico en paso síncrono (*lock-step*). Explicar cómo la variable de turno en Peterson rompe esta simetría.
* **Ejercicio 62 (Peterson para N procesos — Filtro por niveles):**
  * *Qué saberte:* Los 3 Lemas de Capel: Lema del Filtro (≤ N - L procesos en nivel L), Lema de Exclusión (≤ 1 en nivel N-1) y Lema 3 (distribución monótona sin etapas intermedias vacías). Cota de espera uniforme: **N(N - 1) / 2** adelantamientos.
* **Ejercicio 63 (Dijkstra para N procesos con cambio de guarda):**
  * *Qué saberte:* Por qué cambiar `estado[turno] = pasivo` por `estado[turno] != enSC` **no** rompe la exclusión mutua (la cuida el segundo bucle `for`), pero **destruye el progreso** generando un livelock infinito donde los procesos se roban el turno cíclicamente.
* **Ejercicios 58 y 59 (Instrucción Atómica Swap y Cerrojos de Capacidad k):**
  * *Qué saberte:* Garantía de exclusión mutua por invariante de conservación de llaves atómicas, pero **ausencia de orden FIFO y posible inanición**.

### Grupo 2: Monitores y Sincronización de Alto Nivel (Tema 2-1 y Relación 2)
* **Ejercicio 40 (Semántica Hoare/SU vs. Mesa/SC):**
  * *Regla de oro:* En semántica **Hoare (Señalar y Espera Urgente)** la condición señalada se cumple de inmediato al despertar ⟹ se usa **`if (!cond) c.wait()`**. En semántica **Mesa / POSIX (Señalar y Continuar)** otros hilos pueden adelantarse antes de que el despertado tome el cerrojo ⟹ es obligatorio usar **`while (!cond) c.wait()`**.
* **Ejercicio 43 (El Puente de un solo carril con cupo máximo):**
  * Control de dirección (`sentido_actual`), contador de vehículos cruzando, cola de espera y cupo máximo de 10 coches para alternar sentido y evitar inanición.
* **Ejercicio 44 (La Olla de los Caníbales / Salvajes y el Cocinero):**
  * Sincronización productor-consumidor múltiple con servidor pasivo (el cocinero duerme con `raciones > 0` y es despertado exclusivamente por el salvaje que encuentra la olla vacía).
* **Ejercicio 42 (Lectores-Escritores con Prioridad):**
  * Saber implementar la variante con prioridad a lectores y la variante con prioridad a escritores (bloqueando nuevos lectores si `n_escritores_esperando > 0`).
* **Ejercicio 39 (El Aseo Compartido con Semáforos POSIX):**
  * Exclusión entre hombres y mujeres en el aseo (máximo 5 hombres o 1 mujer) mediante cerrojos multiplexados.
* **Ejercicio 48 (Filósofos Comensales con Monitor):**
  * Prevención de interbloqueo comprobando los estados de los vecinos (`PENSANDO`, `HAMBRIENTO`, `COMIENDO`).

### Grupo 3: Lógica de Hoare y Concurrencia Básica (Tema 1)
* **Ejercicio 1 (Bucles de incremento concurrentes solapados):**
  * Dos procesos ejecutan *k* incrementos concurrentes sobre *x* con lecturas y escrituras en registros independientes. El valor máximo es 2*k* y el mínimo es **2** (por solapamiento extremo en la primera y última iteración).
* **Ejercicios 4 y 5 (Condiciones de Bernstein y Paralelización):**
  * **Condiciones de Bernstein:** `I(S₁) ∩ O(S₂) = ∅ ∧ O(S₁) ∩ I(S₂) = ∅ ∧ O(S₁) ∩ O(S₂) = ∅`. Construcción del grafo de dependencias y código con `cobegin / coend` y semáforos binarios.
* **Ejercicios 14, 15 y 20 (Teorema de No Interferencia de Owicki-Gries):**
  * Demostrar que para dos procesos `{P₁} S₁ {Q₁}` y `{P₂} S₂ {Q₂}`, toda aserción intermedia *A* en la prueba de P₁ se preserva ante cualquier asignación *T* de P₂: `{A ∧ pre(T)} T {A}`.

---

## 4. Plan de Rescate y Estudio Intensivo (Sprint de Emergencia: 4 Días)

Diseñado específicamente para prepararlo con la máxima rentabilidad desde hoy **Domingo 25 de Octubre** hasta el **Jueves 29 de Octubre (17:30 h)**:

```
                    CRONOGRAMA DE COMBATE (4 DÍAS)
  ┌───────────────────────┬───────────────────────┬───────────────────────┬───────────────────────┐
  │ DOMINGO 25 (NOCHE)    │ LUNES 26 (COMPLETO)   │ MARTES 27 (COMPLETO)  │ MIÉRCOLES 28          │
  │ Tema 2-2: Exclusión   │ Tema 2-1: Monitores   │ Tema 1: Hoare & Grafos│ Simulacro Real        │
  │ Software & Hardware   │ y Semáforos           │ + Bernstein           │ y Drill Test Final    │
  └───────────────────────┴───────────────────────┴───────────────────────┴───────────────────────┘
```

| Jornada | Franja Horaria | Bloque y Contenidos Clave | Tareas Prácticas Concretas | Material repasaYA |
| :--- | :--- | :--- | :--- | :--- |
| **Domingo 25 Oct** *(Hoy)* | **19:30 - 23:30** *(4h)* | **Tema 2-2: Exclusión Mutua Software y Hardware** | • Dominar la traza de Hyman (Ej. 56) y el livelock del Cuarto Intento (Ej. 55).<br>• Demostración de Peterson 2 y N procesos (Ej. 57 y 62).<br>• Algoritmo de Dijkstra con cambio de guarda (Ej. 63) y Swap (Ej. 58).<br>• Tanda de 30 tests de exclusión en repasaYA. | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 61-77)<br>[Apuntes Tema 2-2](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/apuntes-teoria-scd.pdf) |
| **Lunes 26 Oct** | **09:30 - 13:30** *(Mañana)* | **Tema 2-1: Monitores Clásicos** | • Plantilla base de monitor C++ y diferencia crucial SU (`if`) vs SC (`while`) (Ej. 40).<br>• Resolver a mano el Puente de un solo carril (Ej. 43) y la Olla de Caníbales (Ej. 44). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 45-55) |
| | **16:00 - 20:00** *(Tarde)* | **Monitores Avanzados y Semáforos** | • Lectores-Escritores con prioridad a escritores (Ej. 42).<br>• Aseo compartido con semáforos POSIX (Ej. 39) y Filósofos (Ej. 48).<br>• Tanda de 40 preguntas tipo test de Monitores y Semáforos. | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 35-44)<br>[Tests SCD](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/test.json) |
| **Martes 27 Oct** | **09:30 - 13:30** *(Mañana)* | **Tema 1: Concurrencia y Bernstein** | • Ejercicio 1 (Bucles solapados con registros: máx 2k, mín 2).<br>• Condiciones de Bernstein y construcción de grafos de precedencias (Ej. 4 y 5). | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 4-15) |
| | **16:00 - 20:00** *(Tarde)* | **Tema 1: Lógica de Hoare y Owicki-Gries** | • Demostración de triples concurrentes con matriz de no interferencia (Ej. 14, 15 y 20).<br>• Tanda de 40 tests del Tema 1 en repasaYA analizando justificaciones. | [PDF Relaciones](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/public/scd/relaciones-problemas-scd.pdf) (Págs 16-34) |
| **Miércoles 28 Oct** | **09:30 - 13:30** *(Mañana)* | **Simulacro de Problemas a Contrarreloj** | • Resolver en papel en 55 minutos exactamente 2 problemas elegidos: un Monitor (Puente o Aseo) y un Ejercicio de Exclusión (Peterson o Hyman).<br>• Redactar invariantes formales y comprobar ausencia de deadlock. | Ejercicios 43 y 57 del PDF de Relaciones |
| | **16:00 - 19:30** *(Tarde)* | **Drill Masivo de Tipo Test** | • Simulacro global en repasaYA con penalización real (-0,5).<br>• Repaso de preguntas dudosas y aclaraciones de Capel.<br>• *Corte a las 20:00 h: Descanso y desconexión mental temprana.* | [Motor de Tests repasaYA](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/content/materials/informatica/sistemas-concurrentes-y-distribuidos/test.json) |
| **Jueves 29 Oct** *(Examen)* | **09:30 - 13:00** *(Mañana)* | **Sprint Visual y Fórmulas** | • Repasar las tablas de intercalación, cotas de Peterson ($N(N-1)/2$), Habermann y semánticas SU/SC.<br>• Almuerzo ligero, hidratación y llegada al aula con antelación. | Resumen Sección 6 |
| | **17:30 - 19:10** | **EL EXAMEN (100 MINUTOS)** | • Ejecutar la estrategia de los 100 minutos: descartar el problema feo, clavar el monitor y el de exclusión, y asegurar el test sin arriesgar a ciegas. | **¡A por el 3,5/3,5!** |

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
   * **Descarta de inmediato el que veas más largo o enrevesado** (por ejemplo, si uno pide una prueba formal exhaustiva con Owicki-Gries de muchas ramas algebraicas y otro es un monitor clásico de puente o caníbales, ve de cabeza a por el monitor).
   * Marca los dos problemas elegidos y no cambies de idea a mitad de examen salvo catástrofe.
2. **Minutos 5 a 35 — Bloque Test:**
   * Haz una primera pasada respondiendo **únicamente las que te sabes al 100%**.
   * En la segunda pasada, analiza aquellas donde dudes entre dos. Aplica la regla: si has descartado 3 opciones con solidez, marca la más fundamentada. Si dudas entre 3 o más, déjala en blanco.
3. **Minutos 35 a 90 — Los 2 Problemas Prácticos (25-30 min cada uno):**
   * *Estructura siempre la respuesta:*
     1. **Declaración de variables compartidas e inicialización.**
     2. **Invariante de seguridad formal** (ej. `0 ≤ dentro ≤ k` o `coches_norte × coches_sur == 0`).
     3. **Código claro en C++11 o pseudocódigo estructurado** con nombres descriptivos.
     4. **Justificación de progreso:** Explica brevemente por qué no hay interbloqueo (*deadlock*) ni inanición (*starvation*).
4. **Minutos 90 a 100 — Control de daños y repaso:**
   * Comprueba que no has marcado opciones dudosas por impulso en el test.
   * Verifica los nombres de variables y que todos los cerrojos/semáforos abiertos tienen su `post()` o `unlock()` correspondiente.

---

## 6. Resumen de Fórmulas y Conceptos Trampa Frecuentes

* **Habermann:** Semáforo como monitor con invariante `np = min(na, nv)`. Si `na < nv`, la cola de espera tiene `nv - na` procesos suspendidos.
* **Peterson N procesos:** Cota máxima de espera uniforme = **N(N - 1) / 2** adelantamientos.
* **Hoare vs. Mesa:** Señal desplazante (SU) ⟹ el señalador cede el monitor y el despertado entra sin competencia ⟹ `if`. Señal no desplazante (SC) ⟹ el señalador continúa y el despertado va a la cola de listos ⟹ `while`.
* **Desempate en Tickets:** Tupla lexicográfica `(n[i], i) < (n[j], j) ⟺ (n[i] < n[j]) ∨ (n[i] == n[j] ∧ i < j)`.
* **Instrucción Swap:** Garantiza exclusión mutua mediante conservación de llaves, pero **NO garantiza equidad ni orden FIFO**.
* **Bucles con registros locales:** Dos procesos concurrentes con $k$ iteraciones producen como máximo $2k$ y como mínimo **2** (por solapamiento en primera y última iteración).
* **Condiciones de Bernstein:** Para ejecutar $S_1$ y $S_2$ en paralelo deben cumplirse las 3 simultáneamente: $I(S_1) \cap O(S_2) = \emptyset$, $O(S_1) \cap I(S_2) = \emptyset$, y $O(S_1) \cap O(S_2) = \emptyset$.


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
     2. **Invariante de seguridad formal** (ej. `0 ≤ dentro ≤ k` o `coches_norte × coches_sur == 0`).
     3. **Código claro en C++11 o pseudocódigo estructurado** con nombres descriptivos.
     4. **Justificación de progreso:** Explica brevemente por qué no hay interbloqueo (*deadlock*) ni inanición (*starvation*).
4. **Minutos 90 a 100 — Control de daños y repaso:**
   * Comprueba que no has marcado opciones dudosas por impulso en el test.
   * Verifica los nombres de variables y que todos los cerrojos/semáforos abiertos tienen su `post()` o `unlock()` correspondiente.

---

## 6. Resumen de Fórmulas y Conceptos Trampa Frecuentes

* **Habermann:** Semáforo como monitor con invariante `np = min(na, nv)`. Si `na < nv`, la cola de espera tiene `nv - na` procesos suspendidos.
* **Peterson N procesos:** Cota máxima de espera uniforme = **N(N - 1) / 2** adelantamientos.
* **Hoare vs. Mesa:** Señal desplazante (SU) ⟹ el señalador cede el monitor y el despertado entra sin competencia ⟹ `if`. Señal no desplazante (SC) ⟹ el señalador continúa y el despertado va a la cola de listos ⟹ `while`.
* **Desempate en Tickets:** Tupla lexicográfica `(n[i], i) < (n[j], j) ⟺ (n[i] < n[j]) ∨ (n[i] == n[j] ∧ i < j)`.
* **Instrucción Swap:** Garantiza exclusión mutua mediante conservación de llaves, pero **NO garantiza equidad ni orden FIFO**.
