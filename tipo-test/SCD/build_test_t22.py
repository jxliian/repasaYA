"""Genera el banco de test del parcial T2.2 de SCD (algoritmos de exclusión mutua).

Cada pregunta se escribe con la opción correcta en primer lugar; el script baraja
las opciones con una semilla fija y calcula el índice correcto.
"""
import json
import random
import sys

A = "T2.2 · Propiedades y condiciones de Dijkstra"
B = "T2.2 · Refinamiento sucesivo y Dekker"
C = "T2.2 · Dijkstra y Knuth (N procesos)"
D = "T2.2 · Peterson (2 y N procesos)"
E = "T2.2 · Hyman, tickets, anillo y Lamport"
F = "T2.2 · Soporte hardware y cerrojos"
G = "T2.2 · Algoritmos distribuidos"

Q = []


def q(tema, texto, correcta, incorrectas, just):
    assert len(incorrectas) == 4, texto
    Q.append((tema, texto, correcta, incorrectas, just))


# ---------------------------------------------------------------- A
q(A, "La exclusión mutua es una propiedad de…",
  "Seguridad: nunca puede haber dos procesos a la vez en la sección crítica.",
  ["Vivacidad: algún proceso acabará entrando en la sección crítica.",
   "Equidad: todos los procesos entran el mismo número de veces.",
   "Rendimiento: reduce el tiempo de espera de los procesos.",
   "Alcanzabilidad: la sección crítica siempre se alcanza."],
  "Las propiedades de seguridad dicen que «nada malo ocurre» en ningún estado alcanzable. Que dos procesos coincidan en la SC es justo ese «algo malo», así que la EM es de seguridad y se demuestra con un invariante, sin hipótesis de planificación.")

q(A, "La ausencia de inanición es…",
  "Una propiedad de vivacidad: todo proceso que solicita la SC acaba entrando, y normalmente exige suponer planificación justa.",
  ["Una propiedad de seguridad que se demuestra con un invariante.",
   "Una consecuencia directa de garantizar exclusión mutua y ausencia de interbloqueo.",
   "Lo mismo que la espera acotada.",
   "Una propiedad que solo tiene sentido en sistemas distribuidos."],
  "Es de vivacidad («algo bueno acaba ocurriendo») y es individual: habla de cada proceso, no del sistema. Para demostrarla hay que suponer que el planificador no deja parado para siempre a un proceso listo (planificación débilmente justa).")

q(A, "Un algoritmo garantiza exclusión mutua y ausencia de interbloqueo. ¿Qué se puede afirmar de la inanición?",
  "Nada: el sistema progresa, pero un proceso concreto puede ser adelantado indefinidamente por los demás.",
  ["Queda garantizada su ausencia, porque si no hay interbloqueo todos entran.",
   "Queda garantizada su ausencia solo si hay dos procesos.",
   "Queda garantizada la espera acotada y, con ella, la ausencia de inanición.",
   "Queda garantizado un orden FIFO de entrada."],
  "Ausencia de interbloqueo es global (alguien entra); ausencia de inanición es individual (todos entran). El algoritmo de Dijkstra para N procesos es el ejemplo de clase: EM y alcanzabilidad, pero un proceso puede quedarse siempre en la primera barrera.")

q(A, "La propiedad de espera acotada (equidad) exige que…",
  "Exista una cota al número de veces que otros procesos entran en la SC antes que uno que ya la ha solicitado.",
  ["El tiempo que un proceso pasa dentro de la SC esté acotado.",
   "Cada proceso espere como máximo un tiempo fijo medido en segundos.",
   "Los procesos entren estrictamente en orden de llegada.",
   "Ningún proceso tenga que esperar nunca para entrar."],
  "La equidad se mide en «adelantamientos» o turnos, no en tiempo. FIFO es un caso particular (cota 0); Peterson para N procesos, por ejemplo, tiene cota n(n−1)/2 turnos.")

q(A, "¿Cuál de estas es una de las cuatro condiciones de Dijkstra?",
  "No hacer suposiciones sobre la velocidad de ejecución de los procesos, salvo que no es cero.",
  ["Todos los procesos deben ejecutarse a la misma velocidad.",
   "El multiprocesador debe disponer de una instrucción TestAndSet.",
   "Los procesos deben entrar en la SC en orden de llegada.",
   "El número de procesos debe ser 2."],
  "Las cuatro condiciones: (1) ninguna suposición sobre las instrucciones ni el número de procesos; (2) ninguna sobre la velocidad, salvo que no es cero (progreso finito); (3) un proceso fuera de la SC no puede impedir que otros entren; (4) la SC siempre es alcanzada por alguno de los que esperan.")

q(A, "Según la tercera condición de Dijkstra…",
  "Un proceso que ejecuta código fuera de la sección crítica no puede impedir que los demás entren en ella.",
  ["Un proceso dentro de la SC debe salir en un tiempo acotado.",
   "Los procesos no pueden usar instrucciones especiales del hardware.",
   "La SC debe ser alcanzada por todos los procesos que esperan.",
   "Un proceso no puede volver a entrar hasta que entren todos los demás."],
  "Es la condición que viola la primera etapa del refinamiento (alternancia estricta con turno): si P1 no quiere volver a entrar, P2 se queda esperando un turno que nunca le llega.")

q(A, "La cuarta condición de Dijkstra («la SC siempre será alcanzada por alguno de los procesos que esperan») corresponde a…",
  "La alcanzabilidad o ausencia de interbloqueo.",
  ["La exclusión mutua.",
   "La ausencia de inanición de cada proceso.",
   "La espera acotada.",
   "El orden FIFO de entrada."],
  "Dice que el conjunto de procesos progresa (alguno entra), no que entre cada uno de ellos. Por eso no implica ausencia de inanición.")

q(A, "En las condiciones de Dijkstra, «progreso finito» significa que…",
  "La velocidad de ejecución de cada proceso no es cero: ningún proceso se detiene para siempre.",
  ["Todo proceso entra en la SC en un número finito de pasos.",
   "El protocolo de entrada tiene un número finito de instrucciones.",
   "El número de procesos es finito.",
   "La sección crítica tarda un tiempo finito y conocido."],
  "Es la única suposición permitida sobre la velocidad (condición 2): los procesos pueden ir a cualquier ritmo, pero ninguno a velocidad cero.")

q(A, "¿Qué se puede afirmar de un algoritmo que solo satisface las cuatro condiciones de Dijkstra?",
  "Que es una solución parcialmente correcta: garantiza EM y alcanzabilidad, pero puede haber inanición.",
  ["Que es una solución totalmente correcta, sin inanición.",
   "Que garantiza el orden FIFO de entrada.",
   "Que solo garantiza la ausencia de inanición.",
   "Que no garantiza la exclusión mutua."],
  "Las diapositivas las presentan como condiciones «para obtener una solución parcialmente correcta». Lo que añaden Knuth, Peterson o Lamport es precisamente la equidad (ausencia de inanición con retraso acotado).")

q(A, "Según las diapositivas, ¿cuándo es aceptable resolver la EM con bucles de espera activa?",
  "Cuando el sistema o la aplicación no tiene muchos procesos.",
  ["Siempre, porque no consume CPU.",
   "Solo en sistemas distribuidos.",
   "Solo si se dispone de semáforos.",
   "Nunca: la espera activa no garantiza la exclusión mutua."],
  "Los procesos iteran en un bucle vacío hasta que entrar es seguro. Funciona, pero gasta CPU mientras espera, así que solo compensa con pocos procesos (típicamente en un multiprocesador).")

q(A, "¿Qué propuso Dijkstra en 1965 según la introducción histórica?",
  "Una solución segura y libre de interbloqueo, pero que puede producir inanición.",
  ["La primera solución sin inanición con retraso limitado.",
   "Una solución con orden FIFO para los procesos que esperan.",
   "La solución más simple para dos y n procesos.",
   "Un algoritmo de paso de testigo para multicomputadores."],
  "1962 Dekker plantea el problema; 1965 Dijkstra (seguro, sin interbloqueo, con inanición); 1966 Knuth (sin inanición, no FIFO); 1974 Lamport (FIFO); 1981 Peterson (equitativo y simple); 1983 algoritmos distribuidos.")

q(A, "¿Qué aportó Knuth en 1966?",
  "Una solución sin inanición que garantiza retraso limitado de los procesos, aunque no FIFO.",
  ["La primera solución segura y libre de interbloqueo, con inanición.",
   "Una solución FIFO que permite a los procesos detenerse en el protocolo.",
   "La solución más simple para multiprocesadores.",
   "El primer algoritmo distribuido basado en permisos."],
  "Knuth corrige el defecto de Dijkstra (la inanición) con un turno circular. El retraso queda acotado, pero el orden de entrada no es el de llegada.")

q(A, "¿Qué caracteriza a la solución de Lamport (1974) según las diapositivas?",
  "Permite que los procesos se detengan en el protocolo de adquisición, solapa lecturas con escrituras y da retraso FIFO a los que ya esperan.",
  ["Es la primera solución libre de interbloqueo.",
   "Garantiza retraso cuadrático y es la más simple.",
   "Solo funciona para dos procesos.",
   "Necesita una instrucción atómica de intercambio."],
  "Es el algoritmo de la panadería: cada proceso coge un número mayor que los que ve y se atiende por número (y por identificador si empatan), de ahí el orden FIFO.")

q(A, "Según la introducción histórica, la solución de Peterson (1981)…",
  "Es equitativa para 2 y n procesos, garantiza retraso cuadrático y es la más simple para multiprocesadores.",
  ["Puede producir inanición, igual que la de Dijkstra.",
   "Es la primera solución distribuida para multicomputadores.",
   "Solo funciona para dos procesos.",
   "Garantiza orden FIFO estricto."],
  "Para n procesos el retraso máximo es r(n) = n(n−1)/2 turnos: cuadrático en n.")

q(A, "La hipótesis de planificación débilmente justa se necesita para demostrar…",
  "Propiedades de vivacidad como la ausencia de inanición.",
  ["La exclusión mutua.",
   "Que las lecturas y escrituras son atómicas.",
   "Que el protocolo de salida es correcto.",
   "Que las variables compartidas tienen valores iniciales correctos."],
  "La seguridad se cumple con cualquier intercalación, así que no necesita hipótesis sobre el planificador. Las de vivacidad sí: si el planificador nunca ejecuta a un proceso, nada lo hará entrar.")

q(A, "¿En qué se diferencia un interbloqueo activo (livelock) de un interbloqueo?",
  "En el livelock los procesos siguen ejecutando instrucciones, pero ninguno consigue avanzar hacia la SC.",
  ["En el livelock los procesos quedan bloqueados en una cola del sistema operativo.",
   "El livelock solo puede ocurrir con semáforos.",
   "El livelock viola la exclusión mutua.",
   "No hay diferencia: son dos nombres para lo mismo."],
  "Es lo que pasa en la cuarta etapa del refinamiento: si los dos procesos van al mismo ritmo, ceden y reintentan a la vez una y otra vez. Ninguno está parado, pero ninguno entra.")

# ---------------------------------------------------------------- B
q(B, "En la primera etapa del refinamiento sucesivo (una variable turno que alterna entre P1 y P2)…",
  "Se garantiza la EM, pero no se cumple la tercera condición de Dijkstra.",
  ["No se garantiza la exclusión mutua.",
   "Se produce interbloqueo si ambos quieren entrar a la vez.",
   "Se cumplen todas las condiciones de Dijkstra.",
   "Se produce un livelock cuando los dos van al mismo ritmo."],
  "Es el esquema de «corrutinas»: los procesos entran alternándose. Si uno se queda fuera de la SC (o termina), el otro no puede volver a entrar porque el turno no le llega: un proceso fuera de la SC impide al otro entrar.")

q(B, "En la segunda etapa, cada proceso espera mientras la clave del otro valga 0 y después pone la suya a 0. ¿Qué falla?",
  "La seguridad: la salida de la espera y el cambio de clave no son atómicos, así que los dos pueden entrar a la vez.",
  ["La tercera condición de Dijkstra.",
   "La ausencia de interbloqueo: los dos se quedan esperando para siempre.",
   "La ausencia de inanición, pero la EM se cumple.",
   "Nada: es la solución correcta."],
  "Traza: P1 ve c2=1 y sale del bucle; antes de poner c1:=0, P2 ve c1=1 y sale también. Los dos asignan su clave a 0 y entran en la SC.")

q(B, "En la tercera etapa, cada proceso asigna su clave a 0 antes de comprobar la del otro. ¿Qué problema tiene?",
  "Es segura, pero si los dos asignan su clave a la vez se quedan esperando indefinidamente (interbloqueo).",
  ["No garantiza la exclusión mutua.",
   "Viola la tercera condición de Dijkstra por la alternancia estricta.",
   "Produce inanición solo si hay más de dos procesos.",
   "No tiene ningún problema."],
  "Adelantar la asignación da seguridad, pero «el proceso que modifica la clave no sabe si el otro hace lo mismo concurrentemente»: c1=0 y c2=0, y cada uno espera a que la clave del otro vuelva a 1.")

q(B, "En la cuarta etapa, un proceso que ve la clave del otro a 0 vuelve a poner la suya a 1, espera y lo reintenta. Esto…",
  "Mantiene la EM y evita el bloqueo permanente, pero si avanzan al mismo ritmo pueden ceder indefinidamente (livelock / inanición).",
  ["Pierde la exclusión mutua.",
   "Garantiza la ausencia de inanición.",
   "Es ya el algoritmo de Dekker.",
   "Provoca un interbloqueo permanente en cuanto los dos intentan entrar."],
  "Es la «cortesía»: cada uno cede al otro. Con velocidades distintas alguno entra, pero el planificador puede intercalarlos de forma que los dos cedan y reintenten a la vez sin fin.")

q(B, "¿Qué añade el algoritmo de Dekker (quinta etapa) respecto a la cuarta?",
  "Una variable turno que decide quién debe ceder cuando los dos quieren entrar a la vez.",
  ["Una instrucción atómica de intercambio.",
   "Un vector de números de ticket.",
   "Una segunda barrera que comprueba que nadie más está en la SC.",
   "Una cola FIFO de procesos en espera."],
  "Solo cede (pone su clave a 1 y espera) el proceso que no tiene el turno. El que lo tiene mantiene su clave a 0 y espera a que el otro ceda, así que se rompe la simetría del livelock.")

q(B, "En Dekker, un proceso Pi que encuentra la clave del otro a 0 y no tiene el turno…",
  "Pone su clave a 1, espera activamente mientras el turno sea del otro y luego vuelve a poner su clave a 0.",
  ["Entra directamente en la sección crítica.",
   "Se apropia del turno y entra.",
   "Espera con su clave a 0 hasta que el otro salga.",
   "Termina su ejecución."],
  "Así deja pasar al que tiene el turno. Cuando este sale y le cede el turno, Pi vuelve a manifestar su intención (clave a 0) y entra.")

q(B, "¿Qué hace un proceso al salir de la sección crítica en el algoritmo de Dekker?",
  "Cede el turno al otro proceso y pone su clave a 1.",
  ["Se queda con el turno y pone su clave a 1.",
   "Pone su clave a 0 y cede el turno.",
   "Solo pone su clave a 1, sin tocar el turno.",
   "Espera a que el otro proceso entre."],
  "turno := j; c[i] := 1. Ceder el turno a la salida es lo que impide que un mismo proceso adelante indefinidamente al otro.")

q(B, "¿Cómo se demuestra la exclusión mutua en el algoritmo de Dekker?",
  "Pi solo entra si ve c[j] = 1, y comprueba c[j] después de asignar c[i] = 0; así, al entrar se cumple c[j] = 1 ∧ c[i] = 0.",
  ["Con el valor de turno: solo entra el proceso que tiene el turno.",
   "Con la atomicidad de la instrucción swap.",
   "Contando los procesos que hay en cada etapa.",
   "Mediante el orden total de los números de secuencia."],
  "Si los dos estuvieran dentro, cada uno habría visto la clave del otro a 1 después de poner la suya a 0, lo que es imposible porque ninguno la vuelve a 1 hasta salir. El turno sirve para la alcanzabilidad, no para la EM.")

q(B, "El algoritmo de Dekker garantiza, para dos procesos…",
  "Exclusión mutua, ausencia de interbloqueo y ausencia de inanición.",
  ["Solo exclusión mutua.",
   "Exclusión mutua, pero puede haber livelock.",
   "Ausencia de inanición, pero no exclusión mutua.",
   "Exclusión mutua y orden FIFO para N procesos."],
  "Es la primera solución completamente correcta para dos procesos. No se generaliza directamente a N: para eso están Dijkstra, Knuth, Peterson y Lamport.")

q(B, "En Dekker, si P1 y P2 intentan entrar a la vez y turno = 1…",
  "P1 espera a que P2 ceda su clave y entra; P2 pone su clave a 1 y se queda en espera activa.",
  ["Entran los dos.",
   "No entra ninguno hasta que cambie el turno.",
   "Entra P2 porque fue el último en asignar su clave.",
   "P1 cede el turno a P2."],
  "Es el argumento de alcanzabilidad de las diapositivas: si encuentra la clave del otro a 1 entra; si no, decide el turno. Quien lo tiene espera; quien no lo tiene cede.")

q(B, "En el refinamiento sucesivo de las diapositivas, una clave ci = 0 indica que…",
  "El proceso i quiere entrar o está en la sección crítica.",
  ["El proceso i está fuera de la sección crítica.",
   "El proceso i tiene el turno.",
   "El proceso i ha terminado.",
   "El proceso i ha cedido el turno."],
  "Las claves se inicializan a 1 (fuera). Para indicar que intenta entrar, el proceso cambia su clave a 0, y al salir la devuelve a 1.")

# ---------------------------------------------------------------- C
q(C, "En el algoritmo de Dijkstra para N procesos, cada proceso tiene un estado c[i] que puede valer…",
  "pasivo, solicitando o en_SC.",
  ["libre u ocupado.",
   "un número de ticket.",
   "la etapa en la que se encuentra.",
   "verdadero o falso."],
  "Además hay una variable compartida turno. El número de ticket es de Lamport y la etapa, de Peterson para N procesos.")

q(C, "En el algoritmo de Dijkstra, la primera barrera (bucle mientras turno ≠ i)…",
  "Detiene a los procesos mientras el que posee el turno no esté pasivo; si lo está, el proceso se apropia del turno.",
  ["Asegura la exclusión mutua.",
   "Asigna a cada proceso un número de orden.",
   "Comprueba que ningún otro proceso está en_SC.",
   "Garantiza que no hay inanición."],
  "while turno ≠ i do if c[turno] = pasivo then turno := i. La comprobación y el cambio de turno no son atómicos, así que pueden pasar varios procesos: de la seguridad se encarga la segunda barrera.")

q(C, "En el algoritmo de Dijkstra, la segunda barrera…",
  "Asegura la seguridad: el proceso pone su estado a en_SC y solo entra si ningún otro está en_SC; si no, vuelve a empezar.",
  ["Reparte el turno de forma circular.",
   "Impide la inanición.",
   "Asigna el turno al proceso pasivo.",
   "Ordena los procesos por identificador."],
  "Es el mismo argumento que en Dekker: se marca en_SC antes de mirar a los demás, así que de dos procesos que se solapen al menos uno ve al otro y retrocede.")

q(C, "El algoritmo de Dijkstra para N procesos garantiza…",
  "Exclusión mutua y alcanzabilidad, pero no la ausencia de inanición.",
  ["Exclusión mutua, alcanzabilidad y ausencia de inanición.",
   "Solo la ausencia de inanición.",
   "Orden FIFO de entrada.",
   "Ausencia de inanición, pero no exclusión mutua."],
  "Las diapositivas lo dicen explícitamente: «satisface seguridad pero no evita el peligro de inanición». Corregirlo es lo que hace Knuth.")

q(C, "¿Por qué el algoritmo de Dijkstra garantiza la alcanzabilidad de la SC?",
  "Porque turno conserva el valor del último proceso que lo asignó: entre los que llegan a en_SC entra el que tiene el turno y los demás vuelven a la primera barrera.",
  ["Porque los procesos entran en orden de llegada.",
   "Porque cada proceso tiene un número de ticket distinto.",
   "Porque solo un proceso puede superar la primera barrera.",
   "Porque el proceso que sale cede el turno al siguiente."],
  "Como nadie puede quitarle el turno a un proceso que no está pasivo, el poseedor del turno termina pasando las dos barreras en tiempo finito.")

q(C, "En el algoritmo de Dijkstra, ¿pueden dos procesos superar la primera barrera a la vez?",
  "Sí, porque la comprobación del estado del que tiene el turno y el cambio de turno no se hacen atómicamente.",
  ["No, nunca: la primera barrera garantiza la exclusión mutua.",
   "Solo si hay exactamente dos procesos.",
   "Solo si el planificador es justo.",
   "No, porque turno es una variable atómica."],
  "La traza de la diapositiva lo muestra: P1 y P2 llegan a en_SC con turno = 3 (pasivo). Por eso hace falta la segunda barrera, que los hace volver a intentarlo.")

q(C, "Se cambia la guarda de la primera barrera de Dijkstra de «c[turno] = pasivo» a «c[turno] ≠ en_SC». Razonando sobre el protocolo completo, ¿qué ocurre?",
  "La EM se mantiene gracias a la segunda barrera, pero se pierde la alcanzabilidad: los procesos pueden arrebatarse el turno indefinidamente.",
  ["Se pierde la exclusión mutua.",
   "No cambia nada: las dos guardas son equivalentes.",
   "Mejora la equidad y desaparece la inanición.",
   "El algoritmo pasa a garantizar orden FIFO."],
  "Con la nueva guarda se puede quitar el turno a un proceso que está solicitando. Dos procesos pueden quitárselo uno a otro sin fin, así que se pierde el progreso. La segunda barrera sigue impidiendo que dos procesos estén en_SC a la vez. Ojo: en un banco de otros años la clave marcaba «pierde corrección (seguridad)»; si solo aparece esa opción como «pérdida de corrección», es la que se acerca.")

q(C, "¿Qué técnica introduce el algoritmo de Knuth para evitar la inanición?",
  "Un turno circular: el proceso que sale cede el turno a su predecesor en el anillo, y el que espera recorre los procesos desde el turno hacia atrás.",
  ["Un número de ticket por proceso.",
   "Una instrucción atómica TestAndSet.",
   "Un paso de mensajes con marcas de tiempo.",
   "Prioridades fijas por identificador."],
  "En la primera barrera, j empieza en turno y se decrementa módulo n mientras encuentra procesos pasivos; si encuentra uno activo, vuelve a j := turno. Al salir: turno := (i−1) mod n.")

q(C, "El algoritmo de Knuth para N procesos cumple…",
  "Exclusión mutua, alcanzabilidad y ausencia de inanición (retraso limitado), aunque no orden FIFO.",
  ["Solo exclusión mutua y alcanzabilidad, como Dijkstra.",
   "Orden FIFO estricto.",
   "Ausencia de inanición, pero no exclusión mutua.",
   "Exclusión mutua solo si hay planificación fuertemente justa."],
  "Mantiene la segunda barrera de Dijkstra (seguridad) y el turno circular garantiza que nadie es adelantado indefinidamente. La clave del examen de otros años lo resumía como «EM, alcanzabilidad, vivacidad y equidad».")

q(C, "La imposibilidad de inanición en el algoritmo de Knuth se demuestra suponiendo…",
  "Que existe un número finito de procesos.",
  ["Que la planificación es FIFO.",
   "Que la instrucción swap es atómica.",
   "Que solo hay dos procesos.",
   "Que los procesos tienen prioridades distintas."],
  "Con infinitos procesos, uno podría ser adelantado siempre por otros que van recibiendo el turno en el anillo (el escenario de inanición de la diapositiva). Con n finito, el turno circular acaba llegándole.")

q(C, "En el algoritmo de Knuth, ¿qué hace un proceso al entrar en la sección crítica y al salir de ella?",
  "Al entrar asigna turno := i, y al salir turno := (i−1) mod n antes de volver a pasivo.",
  ["Al entrar asigna turno := (i+1) mod n y al salir no toca el turno.",
   "No modifica el turno en ningún momento.",
   "Al salir asigna turno := i para volver a entrar el primero.",
   "Al salir asigna turno al proceso con menor identificador."],
  "Pasar el turno al predecesor hace que el turno recorra el anillo y que, con n finito, todo proceso que espera acabe teniéndolo.")

# ---------------------------------------------------------------- D
q(D, "En el algoritmo de Peterson para dos procesos tal como aparece en las diapositivas (solicitado[i] := true; turno := i; esperar mientras solicitado[j] y turno = i), si los dos compiten…",
  "Espera el último proceso que escribió turno; el otro entra.",
  ["Entra el último proceso que escribió turno.",
   "Entra siempre el proceso 0.",
   "Esperan los dos hasta que uno ceda.",
   "Entran los dos."],
  "turno solo puede tener un valor: el del último que lo escribió. Ese ve turno = i y espera; el otro ve turno ≠ j y entra. En la versión de la relación (turno := 1−i, el proceso cede el turno) la conclusión es la misma: espera el último que escribe.")

q(D, "En Peterson para dos procesos, si solo un proceso quiere entrar…",
  "Entra inmediatamente, porque el otro tiene su indicador a falso.",
  ["Tiene que esperar a que el otro entre antes.",
   "Solo entra si tiene el turno.",
   "Se produce interbloqueo.",
   "Entra después de un número fijo de iteraciones."],
  "La espera exige solicitado[j] = true. Por eso Peterson no tiene alternancia forzosa, a diferencia de la primera etapa del refinamiento.")

q(D, "¿Qué ocurre en Peterson para dos procesos si se intercambia el orden de las dos primeras asignaciones (primero turno, luego el indicador)?",
  "Se pierde la exclusión mutua.",
  ["No cambia nada.",
   "Se pierde solo la ausencia de inanición.",
   "Se produce interbloqueo.",
   "Mejora la equidad."],
  "Traza: P0 asigna turno; P1 asigna turno, pone su indicador y entra porque el de P0 sigue a falso; P0 pone su indicador y ve que el turno no le obliga a esperar: entra también.")

q(D, "El algoritmo de Peterson para dos procesos garantiza…",
  "Exclusión mutua, progreso, ausencia de inanición y espera acotada (a lo sumo una entrada del rival).",
  ["Solo exclusión mutua.",
   "Exclusión mutua y progreso, pero no ausencia de inanición.",
   "Ausencia de inanición, pero no exclusión mutua.",
   "Exclusión mutua solo si el planificador es FIFO."],
  "Si el rival sale y quiere volver a entrar, al escribir turno se convierte en el último y cede: no puede adelantar dos veces seguidas.")

q(D, "¿Por qué Peterson, correcto en un modelo secuencialmente consistente, puede fallar en un programa real con variables ordinarias?",
  "Porque el hardware y el compilador pueden reordenar escrituras y lecturas (memoria débil), y los dos procesos pueden leer el indicador del otro a falso.",
  ["Porque las variables booleanas no se pueden compartir.",
   "Porque necesita una instrucción swap.",
   "Porque solo funciona con un procesador.",
   "No puede fallar: la demostración vale para cualquier máquina."],
  "La demostración supone que cada proceso ve las operaciones en el orden escrito. Con buffers de escritura, la lectura de solicitado[j] puede adelantarse a la escritura de solicitado[i]. En C++ hay que usar std::atomic con orden secuencialmente consistente o barreras de memoria.")

q(D, "En Peterson para N procesos, ¿cuántas etapas tiene que recorrer un proceso antes de la sección crítica?",
  "n−1 etapas (de la 0 a la n−2); la n−1 es una etapa ficticia que indica que está en la SC.",
  ["2 etapas, como en Peterson para dos procesos.",
   "n etapas, una por proceso.",
   "log2(n) etapas, como un torneo.",
   "Una sola etapa con n turnos."],
  "c[i] va de −1 (fuera) a n−2; al terminar el bucle se ejecuta la metainstrucción c[i] := n−1 para indicar que ha llegado a la SC.")

q(D, "En Peterson para N procesos, turno[j] guarda…",
  "El último proceso que ha llegado a la etapa j, que es el que se queda esperando.",
  ["El primer proceso que ha llegado a la etapa j.",
   "El número de procesos que hay en la etapa j.",
   "El proceso que está en la sección crítica.",
   "La etapa en la que está el proceso j."],
  "Igual que en el caso de dos procesos, el último en llegar a una etapa es la «víctima» y espera mientras haya otro proceso en esa etapa o en una más avanzada.")

q(D, "En Peterson para N procesos, Pi espera en la etapa j mientras se cumple…",
  "(∃ k ≠ i : c[k] ≥ j) ∧ turno[j] = i",
  ["(∀ k ≠ i : c[k] < j) ∧ turno[j] = i",
   "(∃ k ≠ i : c[k] ≥ j) ∨ turno[j] = i",
   "turno[j] ≠ i",
   "(∃ k ≠ i : c[k] = n−1)"],
  "Deja de esperar si (a) va por delante de todos (nadie más está en su etapa o en una superior) o (b) ha llegado otro proceso después a su etapa, que pasa a ser el nuevo turno[j].")

q(D, "Según el lema 4 de Peterson para N procesos, el número máximo de procesos que puede haber en la etapa j es…",
  "n − j",
  ["j + 1", "n − 1", "2", "n / 2"],
  "Se demuestra con el lema 3. Consecuencia: en la etapa n−2 hay como máximo 2 procesos, y por el lema 2 solo uno de ellos puede pasar a la SC.")

q(D, "¿Cómo se demuestra la exclusión mutua en Peterson para N procesos?",
  "A la etapa n−2 llegan como máximo dos procesos y, por el lema 2, solo uno de ellos puede avanzar a la SC.",
  ["Por el orden total de los números de secuencia.",
   "Porque solo existe un testigo en el sistema.",
   "Porque la segunda barrera comprueba que ningún otro está en_SC.",
   "Porque turno[0] solo puede tener un valor."],
  "Un proceso que pasa de una etapa a la siguiente o precede a todos o no estaba solo en su etapa (lema 2). En la última etapa con dos procesos, el que llegó último es turno[n−2] y no puede avanzar mientras el otro esté en la SC.")

q(D, "Según las diapositivas, el número máximo de turnos que un proceso puede tener que esperar en Peterson para N procesos es…",
  "r(n) = n − 1 + r(n−1) = n(n−1)/2",
  ["n − 1", "2(n − 1)", "2ⁿ⁻¹ − 1", "log2 n"],
  "Es el «retraso cuadrático» de la introducción histórica. Ojo: en un banco de otros años aparece «N−1» como respuesta; según estas diapositivas la cota es n(n−1)/2.")

q(D, "En Peterson para N procesos, ¿pueden encontrarse dos procesos en la etapa n−2 y ninguno en la n−3?",
  "No: por el lema 3, si hay al menos dos procesos en una etapa, hay al menos uno en cada etapa anterior.",
  ["Sí, siempre que n sea par.",
   "Sí, si el turno de la etapa n−3 ha rotado.",
   "Sí, solo con planificación fuertemente justa.",
   "Depende del valor inicial de turno."],
  "El lema 3 se demuestra por inducción sobre la etapa: para que un segundo proceso alcance la etapa j, otro tuvo que «empujarlo» desde la j−1, y así hacia atrás.")

q(D, "En Peterson para N procesos, se dice que Pi precede a Pj cuando…",
  "c[i] > c[j]: Pi está en una etapa más avanzada.",
  ["i < j: tiene menor identificador.",
   "Pi llegó antes a su etapa actual.",
   "turno[c[i]] = j.",
   "Pi ha entrado más veces en la SC."],
  "Con esa definición, el lema 1 dice que un proceso que precede a todos los demás puede avanzar al menos una etapa.")

q(D, "La alcanzabilidad de la SC en Peterson para N procesos se demuestra…",
  "Por reducción al absurdo: si todos quedaran bloqueados, el más avanzado precedería a los demás (contradice el lema 1) o compartiría etapa (contradice el lema 2).",
  ["Por el orden total de las peticiones.",
   "Porque el turno es circular.",
   "Contando los mensajes de respuesta.",
   "Por inducción sobre el número de entradas en la SC."],
  "Se supone que ningún proceso avanza (hipótesis de incorrección) y se llega a contradicción con los lemas 1 y 2.")

# ---------------------------------------------------------------- E
q(E, "El algoritmo de Hyman (1966) para dos procesos es…",
  "Incorrecto: no garantiza la exclusión mutua.",
  ["Correcto.",
   "Correcto solo con planificación fuertemente justa.",
   "Correcto si las claves son booleanas.",
   "Correcto, pero con inanición."],
  "Se publicó como simplificación de Dekker y resultó erróneo: hay una intercalación que mete a los dos procesos en la SC.")

q(E, "¿Qué intercalación lleva a los dos procesos a la SC en el algoritmo de Hyman (c[0]=c[1]=1, turno=1)?",
  "P0 pone c[0]:=0, ve turno ≠ 0 y c[1]=1, y es interrumpido antes de turno:=0; P1 entra con turno=1; P0 asigna turno:=0 y entra también.",
  ["P0 y P1 ponen su clave a 0 a la vez y se quedan esperando.",
   "P1 sale de la SC sin restaurar su clave.",
   "Los dos leen turno = 1 y entran.",
   "No existe tal intercalación."],
  "El fallo está en que P0 se apropia del turno sin volver a comprobar si P1 ha entrado, y en que P1, como tiene el turno, entra sin mirar la clave de P0.")

q(E, "En el protocolo de tickets para dos procesos (n[i]:=1; n[i]:=n[j]+1; …), ¿para qué sirve la asignación n[i]:=1?",
  "Para avisar de que el proceso está calculando su ticket; sin ella se puede perder la exclusión mutua.",
  ["Es redundante: puede eliminarse sin efecto.",
   "Para dar prioridad al proceso 1.",
   "Para evitar el desbordamiento de los tickets.",
   "Para que el proceso entre sin esperar."],
  "Si se elimina, un proceso puede leer n[j]=0 mientras el otro está a medio calcular su ticket, entrar, y que el otro termine con un ticket menor o igual y entre también. Cumple el papel de «choosing» en la panadería de Lamport.")

q(E, "En el protocolo de tickets para dos procesos, el desempate por identificador cuando n[j] = n[i]…",
  "Rompe la simetría y evita que los dos esperen a la vez cuando calculan el mismo ticket.",
  ["Es innecesario porque los tickets nunca coinciden.",
   "Da prioridad permanente al proceso con mayor identificador.",
   "Provoca inanición del proceso con mayor identificador.",
   "Sirve para reiniciar los tickets."],
  "Los dos pueden leer n[j]=1 y quedarse con el mismo ticket. Con el orden lexicográfico (ticket, id) solo uno espera. El examen de otros años: la ausencia de inanición se apoya en «numeración creciente y orden lexicográfico (ticket, id)».")

q(E, "En el algoritmo de turnos circulares con el vector s[0..N−1] (problema 60), ¿qué ocurre si un proceso se queda indefinidamente en su sección no crítica?",
  "Los demás no pueden avanzar cuando les toca después de él: hay alternancia forzosa y se viola el progreso.",
  ["No afecta a nadie: los demás entran libremente.",
   "Se pierde la exclusión mutua.",
   "Se regenera automáticamente el testigo.",
   "Entran dos procesos a la vez."],
  "El vector implementa un testigo implícito que rota en orden 0, 1, …, N−1. La EM se cumple, pero si el que debe pasar el testigo no quiere entrar, el testigo se queda parado (viola la tercera condición de Dijkstra).")

q(E, "¿Cuál es la diferencia entre alternancia forzosa y equidad?",
  "La alternancia forzosa obliga a seguir un orden aunque el proceso no quiera entrar; la equidad solo acota los adelantamientos entre procesos que compiten.",
  ["Son lo mismo.",
   "La equidad obliga a un orden fijo de entrada.",
   "La alternancia forzosa garantiza el progreso.",
   "La equidad solo existe en algoritmos distribuidos."],
  "Un algoritmo equitativo deja entrar sin esperar a un proceso que compite solo. La alternancia forzosa no, y por eso viola la tercera condición de Dijkstra.")

q(E, "En el algoritmo de la panadería de Lamport…",
  "Cada proceso toma un número mayor que todos los que ve y se atiende por orden de número, desempatando por identificador.",
  ["Un testigo circula en anillo entre los procesos.",
   "Los procesos avanzan por etapas hasta la sección crítica.",
   "Se usa una instrucción TestAndSet sobre una variable compartida.",
   "El proceso con menor identificador entra siempre primero."],
  "Es lo que da el orden FIFO para los procesos que ya esperan. Sus números pueden crecer sin límite, y tolera que los procesos se detengan en el protocolo.")

# ---------------------------------------------------------------- F
q(F, "Un protocolo con swap atómico para N procesos (ocupado compartido, llave local) es:",
  "llave := true; repetir swap(ocupado, llave) hasta llave = false; SC; ocupado := false.",
  ["ocupado := true; swap(ocupado, llave); SC; llave := false.",
   "repetir llave := ocupado hasta llave = false; ocupado := true; SC; ocupado := false.",
   "swap(ocupado, llave); SC; swap(ocupado, llave).",
   "llave := false; repetir swap(ocupado, llave) hasta llave = true; SC."],
  "El que recibe false al intercambiar es el único que ha encontrado el cerrojo libre, y deja true en ocupado. La opción que lee y luego escribe en dos pasos separados es la segunda etapa del refinamiento: no es segura.")

q(F, "¿Basta la atomicidad de swap (o TestAndSet) para garantizar la equidad?",
  "No: garantiza la exclusión mutua, pero un proceso puede perder la carrera indefinidamente frente a otros.",
  ["Sí, porque la instrucción es atómica.",
   "Sí, si hay solo dos procesos.",
   "No, porque tampoco garantiza la exclusión mutua.",
   "Sí, porque el hardware atiende las peticiones en orden FIFO."],
  "Nada decide quién gana el siguiente swap cuando se libera el cerrojo. Para acotar la espera hay que añadir un orden (por ejemplo, tickets o pasar el cerrojo al siguiente que espera).")

q(F, "La instrucción TestAndSet(x)…",
  "Devuelve el valor anterior de x y lo pone a true, todo en una sola operación atómica.",
  ["Pone x a false y devuelve true.",
   "Compara x con un valor y lo cambia solo si coinciden.",
   "Intercambia el valor de dos variables locales.",
   "Bloquea al proceso hasta que x sea true."],
  "Con ella: while TestAndSet(cerrojo) do nothing; SC; cerrojo := false. La opción de comparar y cambiar describe CompareAndSwap.")

q(F, "Deshabilitar las interrupciones para proteger la sección crítica…",
  "Sirve en un monoprocesador, pero no garantiza la exclusión mutua en un multiprocesador.",
  ["Es la solución recomendada en multiprocesadores.",
   "Solo funciona en sistemas distribuidos.",
   "Garantiza la equidad entre procesos.",
   "No sirve ni siquiera en un monoprocesador."],
  "En un monoprocesador evita que el planificador cambie de proceso dentro de la SC. Con varios procesadores, otro núcleo puede ejecutar a la vez la SC sin que le afecten tus interrupciones.")

q(F, "Para limitar a k los procesos dentro de un recurso con un contador dentro y un cerrojo lock/unlock (problema 59), ¿por qué no se debe mantener el cerrojo mientras se espera a que haya sitio?",
  "Porque los procesos que quieren salir también necesitan el cerrojo para decrementar dentro: nadie liberaría plazas (interbloqueo).",
  ["Porque el cerrojo no es atómico.",
   "Porque se perdería el invariante 0 ≤ dentro ≤ k.",
   "Porque el cerrojo solo admite dos procesos.",
   "No hay ningún problema en mantenerlo."],
  "Patrón correcto: repetir { lock; si dentro < k entonces { dentro++; ok := true }; unlock } hasta ok. Comprobar y modificar dentro bajo el mismo cerrojo es lo que mantiene 0 ≤ dentro ≤ k.")

q(F, "El principal inconveniente de los cerrojos con espera activa (spinlocks) es…",
  "Que consumen CPU mientras esperan, iterando sin hacer trabajo útil.",
  ["Que no garantizan la exclusión mutua.",
   "Que no pueden usarse en multiprocesadores.",
   "Que provocan siempre interbloqueo.",
   "Que necesitan paso de mensajes."],
  "Por eso solo compensan con esperas cortas y pocos procesos. Los semáforos y monitores bloquean al proceso en lugar de hacerle girar.")

# ---------------------------------------------------------------- G
q(G, "En un sistema distribuido (multicomputador), los algoritmos de exclusión mutua…",
  "No pueden usar variables en memoria compartida y se sincronizan mediante paso de mensajes.",
  ["Usan las mismas variables compartidas que Peterson.",
   "Necesitan una instrucción TestAndSet en red.",
   "Solo funcionan con dos nodos.",
   "Necesitan un reloj físico global."],
  "No hay memoria común, así que no hay sincronización global por variables: todo se hace con operaciones atómicas de envío y recepción de mensajes.")

q(G, "¿Cuál de estas condiciones de la red NO se exige a los algoritmos distribuidos de exclusión mutua estudiados?",
  "Que los mensajes se entreguen en el mismo orden en que se enviaron.",
  ["Que la red esté completamente conectada.",
   "Que los mensajes se transmitan sin errores.",
   "Que el retraso de entrega sea variable pero acotado.",
   "Que cada nodo pueda enviar mensajes a cualquier otro."],
  "Las diapositivas piden red completamente conectada, transmisión sin errores y retraso variable acotado, y admiten expresamente posibles desordenamientos (desecuenciamientos) en la entrega.")

q(G, "¿Cuántos mensajes necesita el algoritmo de Ricart-Agrawala para que un proceso entre en la sección crítica?",
  "2(n−1): n−1 peticiones y n−1 respuestas.",
  ["n−1", "n", "2n", "Ninguno si ya tiene el testigo."],
  "Envía una petición a cada uno de los otros n−1 procesos y necesita una respuesta favorable de todos ellos.")

q(G, "En Ricart-Agrawala, ¿cuándo puede un proceso entrar en la sección crítica?",
  "Cuando ha recibido una respuesta favorable de todos los demás procesos.",
  ["Cuando recibe el testigo.",
   "Cuando ha recibido la mayoría de las respuestas.",
   "En cuanto envía su petición.",
   "Cuando su número de secuencia es el mayor."],
  "La hebra Rep cuenta las respuestas (num_repesperadas) y, al llegar a 0, hace signal(sinc) para que el proceso principal entre.")

q(G, "En Ricart-Agrawala, un proceso que recibe una petición (k, j) retrasa su respuesta si…",
  "Él también está solicitando la SC y su petición es prioritaria: su número es menor que k, o es igual y su identificador es menor que j.",
  ["Está fuera de la sección crítica.",
   "El número k es menor que el suyo.",
   "j tiene menor identificador.",
   "Ya ha respondido a otro proceso."],
  "prioridad := solicitaSC and (k > ns or (k = ns and i < j)). Si la tiene, marca repretrasadas[j] y contesta al salir de la SC; si no, contesta enseguida.")

q(G, "En Ricart-Agrawala, la instrucción mns := max(ns, k) al recibir una petición sirve para…",
  "Que las peticiones posteriores tengan números de secuencia mayores, como un reloj lógico de Lamport.",
  ["Elegir qué proceso tiene el testigo.",
   "Contar las respuestas recibidas.",
   "Detectar mensajes perdidos.",
   "Reiniciar los números de secuencia."],
  "La siguiente petición del proceso usará ns := mns + 1. Así se respeta el orden en que se hicieron las peticiones y, con el identificador como desempate, se obtiene un orden total.")

q(G, "¿En qué se apoya la alcanzabilidad de la SC en Ricart-Agrawala?",
  "En la ordenación total de las peticiones (número de secuencia e identificador): ninguna respuesta favorable se retrasa indefinidamente.",
  ["En que solo hay un testigo en el sistema.",
   "En el turno circular entre procesos.",
   "En que la red entrega los mensajes en orden.",
   "En un proceso coordinador central."],
  "Siempre hay una petición más prioritaria que todas las demás, y su dueño recibe todas las respuestas.")

q(G, "En Ricart-Agrawala, ¿qué hace un proceso al salir de la sección crítica?",
  "Pone solicitaSC a falso y envía la respuesta a todos los procesos cuya respuesta había retrasado.",
  ["Envía el testigo al siguiente proceso del anillo.",
   "Difunde una nueva petición a todos los procesos.",
   "Espera a recibir n−1 confirmaciones.",
   "Incrementa su número de secuencia y vuelve a entrar."],
  "Recorre repretrasadas[j] y contesta a cada proceso pendiente, que puede así completar sus n−1 respuestas.")

q(G, "¿Cuántos mensajes necesita el algoritmo de Suzuki-Kasami para una entrada en la SC si el proceso no tiene el testigo?",
  "n: n−1 peticiones difundidas y 1 mensaje con el testigo.",
  ["2(n−1)", "n−1", "2n", "1"],
  "Si el proceso ya tiene el testigo, entra sin enviar ningún mensaje.")

q(G, "La exclusión mutua en Suzuki-Kasami equivale a demostrar que…",
  "Globalmente hay exactamente un proceso con token_presente = true (o el testigo está en tránsito).",
  ["Cada proceso recibe n−1 respuestas.",
   "Los números de secuencia son distintos.",
   "La red entrega los mensajes en orden.",
   "Ningún proceso envía dos peticiones seguidas."],
  "Se cumple al principio y se conserva cada vez que se transmite el testigo, porque quien lo envía pone token_presente := false.")

q(G, "En Suzuki-Kasami, un proceso que tiene el testigo y no está en la SC se lo envía al proceso j cuando…",
  "peticion[j] > token[j]: j tiene una petición posterior a la última vez que se le atendió.",
  ["peticion[j] = 0.",
   "j tiene el menor identificador.",
   "token[j] > peticion[j].",
   "j ha enviado una respuesta favorable."],
  "peticion[] guarda el último número de petición recibido de cada proceso y token[] el de la última petición atendida de cada uno, que viaja con el testigo.")

q(G, "¿Cómo garantiza la equidad Suzuki-Kasami?",
  "El testigo se entrega en orden circular j+1, j+2, …, n, 1, …, j−1 al primero que lo tenga pedido.",
  ["Atendiendo siempre al proceso de menor identificador.",
   "Atendiendo al proceso con el número de secuencia más alto.",
   "Mediante un coordinador central.",
   "No garantiza equidad."],
  "Recorrer los procesos en orden circular desde el que lo tiene evita que uno sea saltado indefinidamente.")

q(G, "En Suzuki-Kasami, ¿qué pasa si se sustituye el vector de contadores de peticiones por booleanos?",
  "Se rompe la EM y/o la vivacidad, porque no se distinguen las peticiones nuevas de las ya atendidas.",
  ["Solo se pierde eficiencia.",
   "El algoritmo sigue siendo correcto.",
   "Solo se pierde la equidad.",
   "Solo funciona para n = 2."],
  "Con contadores, peticion[j] > token[j] identifica sin ambigüedad una petición pendiente. Con booleanos, una petición vieja o duplicada se confunde con una nueva.")

q(G, "El algoritmo de Misra resuelve…",
  "La regeneración del testigo cuando se pierde, usando dos testigos (ping y pong) que circulan por el anillo.",
  ["La exclusión mutua con variables compartidas.",
   "La asignación de números de ticket.",
   "El desempate en Ricart-Agrawala.",
   "La ordenación FIFO de los mensajes."],
  "Responde a la pregunta abierta de Suzuki-Kasami («¿qué pasa si se pierden mensajes?»): cada testigo vigila al otro y lo regenera si detecta que se ha perdido.")

q(G, "En el algoritmo de Misra, el invariante que se mantiene durante toda la ejecución es…",
  "num_ping + num_pong = 0",
  ["num_ping = num_pong", "num_ping · num_pong = 1", "num_ping + num_pong = n", "num_ping − num_pong = 0"],
  "Inicialmente num_ping = 1 y num_pong = −1. Cuando se encuentran se incrementa el contador de ping y pong pasa a valer su opuesto, así que el invariante se conserva.")

q(G, "En Misra, un proceso Pi detecta que se ha perdido el pong cuando…",
  "Recibe ping con un valor igual al que guardó en mi la última vez que pasó un testigo por él.",
  ["Pasa un tiempo sin recibir ningún mensaje.",
   "Recibe dos veces seguidas el pong.",
   "num_ping se hace negativo.",
   "Recibe un mensaje de error de la red."],
  "mi guarda el número del último testigo que pasó por Pi. Si el ping vuelve con el mismo número, el pong no ha pasado por Pi desde entonces y se ha perdido: Pi lo regenera.")

q(G, "En el estado inicial del algoritmo de Misra…",
  "Ambos testigos están en un mismo nodo, con num_ping = 1 y num_pong = −1.",
  ["Cada testigo está en un nodo distinto con valor 0.",
   "Solo existe el testigo ping.",
   "num_ping = num_pong = 1.",
   "Los testigos se crean al detectar la primera pérdida."],
  "A partir de ahí recorren el anillo. Cada vez que se encuentran, sus contadores (el número de colisiones) aumentan.")


def build():
    rng = random.Random(2226)
    items = []
    for tema, texto, correcta, incorrectas, just in Q:
        opts = [correcta] + list(incorrectas)
        rng.shuffle(opts)
        items.append({
            "tema": tema,
            "q": texto,
            "opts": opts,
            "correct": opts.index(correcta),
            "justification": just,
        })
    return items


if __name__ == "__main__":
    items = build()
    data = {
        "subject": "informatica/sistemas-concurrentes-y-distribuidos",
        "type": "test",
        "title": "Simulacro parcial T2.2: algoritmos de exclusión mutua",
        "description": f"{len(items)} preguntas nuevas del tema 2.2 (refinamiento sucesivo, Dekker, Dijkstra, Knuth, Peterson, Hyman, tickets, hardware, Ricart-Agrawala, Suzuki-Kasami y Misra) con justificación. Simulacro de 35 preguntas con la puntuación del examen: +0,15 por acierto y −0,075 por fallo.",
        "order": 0,
        "penalty": 0.5,
        "examSize": 35,
        "items": items,
    }
    out = sys.argv[1]
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    from collections import Counter
    print(len(items), Counter(i["tema"] for i in items))
    print(Counter(i["correct"] for i in items))
