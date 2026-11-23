#!/usr/bin/env python3
"""Genera el material del Tema 4 (Scrum) de MDA para repasaYA.

Fuente: diapositivas «Unidad 1 - Desarrollo Ágil de Software. Tema 4 – SCRUM» (104) y
«Tema 4 – Elevator Pitch» (11), LSI-UGR. Las referencias «diap. N» son de la primera.

Uso: python3 tipo-test/MDA/build_tema4.py   (escribe en src/content/materials/...)
"""
import json
import random
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / 'src/content/materials/informatica/metodologias-de-desarrollo-agil'
SUBJECT = 'informatica/metodologias-de-desarrollo-agil'
rng = random.Random(2711)

# ----------------------------------------------------------------------------- TEST
T1 = '1. Origen, definición, pilares y valores'
T2 = '2. Roles: Product Owner, Scrum Master, equipo y stakeholders'
T3 = '3. Artefactos: Product Backlog, Sprint Backlog y Burndown'
T4 = '4. El Sprint y el Sprint Planning'
T5 = '5. Daily, Review, Retrospectiva y grooming'
T6 = '6. Sprint 0, visión del producto y elevator pitch'

TEST = []


def q(tema, texto, correcta, incorrectas, just):
    assert len(incorrectas) == 3
    opts = [correcta] + incorrectas
    rng.shuffle(opts)
    TEST.append({'tema': tema, 'q': texto, 'opts': opts, 'correct': opts.index(correcta), 'justification': just})


q(T1, '¿Qué imagen usan Takeuchi y Nonaka (1986) para describir la nueva forma de desarrollar productos que dio nombre a Scrum?',
  'Un equipo de rugby que avanza como una unidad pasándose el balón adelante y atrás.',
  ['Una carrera de relevos en la que cada fase pasa el testigo a la siguiente.',
   'Una cadena de montaje en la que cada puesto se especializa en una tarea.',
   'Una orquesta dirigida por un director que marca el ritmo a cada músico.'],
  'Diap. 2: frente al enfoque de «carrera de relevos», proponen un enfoque «rugby» en el que el equipo va a la distancia como una unidad. Un scrum es la melé del rugby. La carrera de relevos es justo lo que critican.')
q(T1, '¿Quién formalizó Scrum en el artículo «Scrum Development Process» presentado en OOPSLA en 1996?',
  'Ken Schwaber.', ['Jeff Sutherland.', 'Mike Cohn.', 'Hirotaka Takeuchi.'],
  'Diap. 4: Ken Schwaber lo formalizó en OOPSLA (1996). Sutherland fue el primero en aplicarlo (Easel Corp., 1993), Cohn cofundó la Scrum Alliance (2002) y Takeuchi acuñó el término en 1986 con Nonaka.')
q(T1, '¿Dónde y cuándo trabajó por primera vez un equipo con Scrum?',
  'En Easel Corp., con Jeff Sutherland, en 1993.',
  ['En Toyota, con Takeuchi y Nonaka, en 1986.', 'En la Scrum Alliance, con Schwaber y Cohn, en 2002.',
   'En IBM, con Schwaber y Beedle, en 2001.'],
  'Diap. 3: «El primer equipo que trabajó con SCRUM fue el compuesto por J. Sutherland en Easel Corp. 1993». 1986 es el artículo de Takeuchi y Nonaka; 2001, el libro de Schwaber y Beedle; 2002, la fundación de la Scrum Alliance.')
q(T1, 'Según las diapositivas, Scrum es…',
  'Un marco de trabajo iterativo e incremental que se basa en la adaptación continua, no en seguir un plan.',
  ['Una metodología secuencial basada en un plan detallado que se sigue de principio a fin.',
   'Un conjunto de prácticas de programación como la programación por parejas y el TDD.',
   'Una herramienta de gestión de proyectos para diagramas de Gantt.'],
  'Diap. 8: «Scrum es un marco de trabajo iterativo e incremental… no se basa en el seguimiento de un plan, sino en la adaptación continua a las circunstancias de la evolución del proyecto».')
q(T1, '¿Cuáles son los tres pilares empíricos de Scrum?',
  'Transparencia, inspección y adaptación.',
  ['Compromiso, coraje y foco.', 'Planificación, ejecución y control.', 'Visión, backlog y entrega.'],
  'Diap. 9. Compromiso, coraje y foco son valores, no pilares; planificación-ejecución-control es el ciclo de gestión tradicional.')
q(T1, 'Un equipo revisa cada día en el Daily cómo va respecto al objetivo y, si se desvía, reorganiza el trabajo. ¿Qué pilares empíricos está aplicando?',
  'Inspección y adaptación.', ['Solo transparencia.', 'Compromiso y respeto.', 'Ninguno: el Daily no tiene relación con el empirismo.'],
  'Revisar el avance es inspección; reorganizar el trabajo cuando hay desviación es adaptación (diap. 9). La transparencia es la condición previa: que todos vean el estado real.')
q(T1, '¿Cuál de estos NO aparece entre los valores de Scrum de la diapositiva 10?',
  'Jerarquía.', ['Time-boxing.', 'Coraje.', 'Respeto.'],
  'Diap. 10: mejora continua, calidad, time-boxing, responsabilidad, multidisciplinar, flexibilidad, ritmo, compromiso, simplicidad, respeto, coraje, foco, predictibilidad y personas. La jerarquía va contra la auto-organización.')
q(T1, '¿Cuál de estas afirmaciones forma parte de «la esencia de Scrum»?',
  'El equipo entrega con regularidad las funciones más valiosas y reflexiona sobre su forma de trabajar para mejorar.',
  ['El equipo recibe las tareas ya asignadas por la gerencia y las ejecuta.',
   'El progreso del equipo solo lo conoce el Scrum Master.',
   'El equipo entrega todo el producto al final, en una única entrega.'],
  'Diap. 11-12: objetivos claros, auto-organización, entregas regulares de lo más valioso, retroalimentación externa, reflexión para mejorar, visibilidad para toda la organización y comunicación honesta con la gerencia.')
q(T1, 'Según las diapositivas, ¿en qué tipo de software se ha usado Scrum?',
  'En casi cualquiera: videojuegos, sistemas críticos de soporte vital, software certificado ISO 9001, sistemas 7x24…',
  ['Solo en aplicaciones web pequeñas.', 'Solo en proyectos internos sin contrato con cliente.',
   'Nunca en sistemas críticos ni en proyectos de precio cerrado.'],
  'Diap. 7: la lista incluye desarrollo de videojuegos, sistemas críticos, proyectos fixed-price, aplicaciones certificadas ISO 9001, sistemas embebidos y sistemas 7x24 con 99,999 % de disponibilidad.')

q(T2, 'Según las diapositivas, los roles en Scrum representan…',
  'Una responsabilidad en el proceso, no la posición dentro de la organización.',
  ['El puesto que cada persona tiene en el organigrama.', 'El nivel de experiencia de cada miembro.',
   'Un cargo fijo que no puede cambiar entre proyectos.'], 'Diap. 15, textualmente.')
q(T2, '¿Qué roles son los «roles cerdo» en Scrum?',
  'Product Owner, Scrum Master y equipo de desarrollo.',
  ['Usuario, cliente y dirección.', 'Product Owner, cliente y dirección.', 'Solo el equipo de desarrollo.'],
  'Diap. 16 (3 + 3 Scrum Roles): los cerdos son el equipo Scrum, comprometidos con el resultado; las gallinas son los stakeholders (user, customer, management), interesados pero no comprometidos.')
q(T2, '¿Cuáles son las dos responsabilidades de los stakeholders según las diapositivas?',
  'Ser fuente de requisitos y validar el trabajo dando su feedback.',
  ['Estimar las historias y descomponerlas en tareas.', 'Eliminar impedimentos y facilitar las reuniones.',
   'Priorizar el Product Backlog y aceptar el incremento.'],
  'Diap. 17. Estimar y descomponer es del equipo; eliminar impedimentos, del SM; priorizar y aceptar, del PO.')
q(T2, '¿Quién es el responsable de crear, administrar y priorizar el Product Backlog?',
  'El Product Owner.', ['El Scrum Master.', 'El equipo de desarrollo.', 'Los stakeholders, por votación.'],
  'Diap. 21 y 36. El equipo colabora y estima, pero prioriza el PO.')
q(T2, '¿Cuál de estas NO es una responsabilidad del Product Owner?',
  'Eliminar los impedimentos que encuentra el equipo.',
  ['Aceptar o rechazar el software al final de cada iteración.', 'Maximizar el retorno de la inversión (ROI).',
   'Administrar el plan de entregas.'],
  'Eliminar impedimentos es del Scrum Master (diap. 23). Las otras tres están en la diap. 21.')
q(T2, 'En una implementación «proxy» del Product Owner…',
  'Alguien de la organización (por ejemplo, un product manager) representa a uno o varios clientes ante el equipo.',
  ['El propio cliente hace de Product Owner.', 'El Scrum Master asume también el papel de Product Owner.',
   'No hay Product Owner y el equipo habla directamente con todos los clientes.'],
  'Diap. 19: en la implementación directa el PO es el propio cliente; en la proxy, un intermediario (product manager) representa a varios clientes.')
q(T2, '¿Cuál es la mejor descripción del Scrum Master según las diapositivas?',
  'Un facilitador, coach y mentor que garantiza el proceso y mejora la productividad del equipo.',
  ['El jefe del equipo, que asigna tareas y controla horarios.', 'El representante del cliente ante el equipo.',
   'El miembro más técnico, que toma las decisiones de arquitectura.'],
  'Diap. 22: «¡El Scrum Master es un facilitador, coach y mentor!». Aunque la diapositiva lo traduzca como «director de proyecto», no es un jefe tradicional; el representante del cliente es el PO.')
q(T2, 'Un directivo interrumpe al equipo a mitad de Sprint con peticiones urgentes. ¿Qué rol debe actuar como «escudo»?',
  'El Scrum Master.', ['El Product Owner.', 'El stakeholder que más aporta.', 'El miembro más veterano del equipo.'],
  'Diap. 23: entre las responsabilidades del SM está ser «escudo del equipo ante interferencias externas». La petición debería llegar al PO para que la priorice en el Product Backlog.')
q(T2, '¿Cuál de estos NO es un atributo del Scrum Master en las diapositivas?',
  'Autoritario.', ['Humilde.', 'Influyente.', 'Colaborador.'],
  'Diap. 24: responsable, humilde, colaborador, comprometido, influyente y entendido.')
q(T2, '¿Cuál es el tamaño típico del equipo de desarrollo según las diapositivas?',
  'De 5 a 9 personas.', ['De 1 a 3 personas.', 'De 10 a 15 personas.', 'No hay límite: cuantas más, mejor.'],
  'Diap. 31: lo bastante pequeño para seguir siendo ágil y lo bastante grande para completar un trabajo significativo; típicamente de 5 a 9.')
q(T2, '¿Qué afirmación sobre el equipo de desarrollo es correcta?',
  'Es auto-organizado y multifuncional, y Scrum no reconoce sub-equipos dentro de él.',
  ['Tiene un jefe técnico que reparte las tareas.', 'Se divide en sub-equipos de análisis, desarrollo y pruebas.',
   'Sus miembros trabajan a tiempo parcial en varios proyectos.'],
  'Diap. 30: auto-organizado (no jerarquizado), multidisciplinar, multifuncional, comprometido, sin sub-equipos, a tiempo completo y de forma fija.')
q(T2, '¿Quién estima el tamaño de los ítems del Product Backlog?',
  'El equipo de desarrollo.', ['El Product Owner.', 'El Scrum Master.', 'El cliente.'],
  'Diap. 32: la estimación del tamaño de los ítems es responsabilidad del equipo de desarrollo, como un todo.')

q(T3, '¿Cuáles son los tres artefactos de Scrum según las diapositivas?',
  'Product Backlog, Sprint Backlog y Burndown Chart.',
  ['Product Backlog, plan de proyecto y diagrama de Gantt.', 'Historias de usuario, casos de uso y diagrama de clases.',
   'Sprint Backlog, Daily Meeting y Sprint Review.'],
  'Diap. 13 y 34. El Daily y la Review son reuniones, no artefactos.')
q(T3, '¿Cómo se define el Product Backlog?',
  'Una lista ordenada y priorizada de todo lo que podría ser necesario en el producto.',
  ['La lista de tareas técnicas que el equipo hará en el Sprint actual.', 'Un documento de requisitos cerrado que se firma con el cliente.',
   'La gráfica del trabajo pendiente del Sprint.'],
  'Diap. 36. La lista de tareas del Sprint es el Sprint Backlog; la gráfica, el Burndown.')
q(T3, '¿Qué significa que el Product Backlog sea una lista DEEP?',
  'Detallada, Emergente, Estimada y Priorizada.',
  ['Definida, Estable, Exhaustiva y Pública.', 'Documentada, Entregable, Escalable y Probada.',
   'Detallada, Estática, Estimada y Pequeña.'],
  'Diap. 38. Emergente porque en cualquier momento pueden aparecer historias nuevas; por eso nunca es estática.')
q(T3, 'Que el Product Backlog sea «emergente» significa que…',
  'En cualquier momento pueden aparecer nuevas historias de usuario.',
  ['Solo contiene los requisitos urgentes.', 'Se cierra al terminar el Sprint 0.', 'Lo escriben únicamente los stakeholders.'],
  'Diap. 38. El backlog describe los requisitos conocidos en un momento dado y evoluciona (diap. 37).')
q(T3, '¿Qué tipo de requisitos contiene el Product Backlog?',
  'Funcionales y no funcionales, descritos en lenguaje de negocio.',
  ['Solo funcionales, en lenguaje técnico.', 'Solo las tareas de programación.', 'Solo los requisitos no funcionales.'],
  'Diap. 36-37: lista de requisitos en lenguaje de negocio, que contiene requisitos funcionales y no funcionales.')
q(T3, '¿Cuál de estas NO aparece entre las técnicas de priorización de la diapositiva 39?',
  'Planning por diagrama de Gantt.', ['MoSCoW.', 'Modelo de Kano.', 'Peso relativo.'],
  'Diap. 39: priority poker, MoSCoW, modelo de Kano, criba de temas y peso relativo.')
q(T3, '¿De quién es propiedad el Sprint Backlog?',
  'Del equipo de desarrollo.', ['Del Product Owner.', 'Del Scrum Master.', 'De los stakeholders.'],
  'Diap. 40: «Es propiedad del Equipo de desarrollo». El Product Backlog es responsabilidad del PO.')
q(T3, '¿En qué estados puede estar una historia o tarea del Sprint Backlog?',
  'Pendiente, en curso, terminada o impedida.', ['Nueva, aprobada o rechazada.', 'Must, Should, Could o Won\'t.',
                                               'Detallada, emergente, estimada o priorizada.'],
  'Diap. 58: dimensiones del Sprint Backlog: prioridad, detalle y estado (pendiente de iniciar, en curso, terminada, impedida). MoSCoW es una técnica de priorización y DEEP describe el Product Backlog.')
q(T3, 'A mitad de Sprint, la línea real del Burndown va claramente por encima de la ideal. ¿Qué indica y qué conviene hacer?',
  'El ritmo es bajo; puede convenir reducir el alcance del Sprint.',
  ['El ritmo es alto; se pueden añadir historias.', 'Todo va según lo previsto.', 'Hay que bajar los objetivos de calidad para recuperar.'],
  'Diap. 44. Bajar la calidad no es una opción: «los objetivos de calidad no disminuyen» (diap. 49).')
q(T3, '¿Quién es el responsable de la lista de impedimentos (Impediments Backlog)?',
  'El Scrum Master.', ['El Product Owner.', 'El miembro del equipo que encontró el impedimento.', 'El cliente.'],
  'Diap. 66: la lista de impedimentos sale del Daily y su responsable es el Scrum Master; cada impedimento tiene además un responsable de resolverlo (diap. 67).')

q(T4, '¿Cuánto dura un Sprint según las diapositivas?',
  'Un bloque de tiempo fijo de 1 a 4 semanas.', ['Lo que tarde el equipo en terminar todas las historias.',
                                                 'Siempre exactamente 2 meses.', 'De 1 a 4 días.'],
  'Diap. 47 y 49: time-box de 1 a 4 semanas y de longitud fija, para tener mejor ritmo.')
q(T4, '¿Qué se obtiene al final de cada Sprint?',
  'Un incremento de producto «terminado», utilizable y potencialmente desplegable.',
  ['Un documento de diseño para el siguiente Sprint.', 'Un prototipo desechable.', 'Solo el informe del Burndown.'],
  'Diap. 47.')
q(T4, '¿Qué NO se puede hacer durante un Sprint?',
  'Hacer cambios que afecten al objetivo del Sprint.',
  ['Clarificar el alcance entre el PO y el equipo.', 'Renegociar el alcance a medida que se aprende.',
   'Actualizar el Burndown cada día.'],
  'Diap. 49: no se realizan cambios que puedan afectar al objetivo del Sprint y los objetivos de calidad no disminuyen; el alcance sí puede clarificarse y renegociarse.')
q(T4, 'En un Sprint de 4 semanas, ¿cuánto duran como máximo el Sprint Planning, la Sprint Review y la Retrospectiva?',
  '8 horas, 4 horas y 3 horas.', ['4 horas, 8 horas y 3 horas.', '1 hora, 1 hora y 1 hora.', '8 horas, 8 horas y 8 horas.'],
  'Diap. 50 (gráfico «Sprint de 4 semanas»).')
q(T4, '¿Cuáles son las dos fases del Sprint Planning?',
  'Planificación (qué historias entran) y planificación detallada (cómo: dividirlas en tareas).',
  ['Estimación y priorización del Product Backlog.', 'Demostración y retrospectiva.', 'Análisis y diseño.'],
  'Diap. 53: en la primera se seleccionan, siguiendo la prioridad, los ítems que pueden hacerse; en la segunda el equipo los traduce al lenguaje de desarrollo y los subdivide en tareas.')
q(T4, 'En la primera fase del Sprint Planning, ¿cuándo se deja de seleccionar historias?',
  'Cuando la suma de puntos de historia alcanza (o supera ligeramente) la velocidad media del equipo.',
  ['Cuando el PO decide que ya hay suficientes, sin tener en cuenta la velocidad.', 'Cuando se acaban las historias del Product Backlog.',
   'Cuando el Scrum Master asigna una historia a cada miembro.'],
  'Diap. 56, paso 5.')
q(T4, 'En la selección de historias del Sprint Planning, ¿en qué orden pasan al Sprint Backlog?',
  'Manteniendo el orden de prioridad del Product Backlog.', ['De menor a mayor tamaño.', 'Por orden alfabético.',
                                                             'En el orden que prefiera el equipo.'],
  'Diap. 56: el PO lee la historia de mayor prioridad, la explica con sus criterios de aceptación, el equipo la estima y pasa al Sprint Backlog manteniendo el orden de prioridad.')
q(T4, '¿Qué papel tiene el Scrum Master en el Sprint Planning?',
  'Facilita la reunión para que se mantenga el foco y sea eficiente.',
  ['Decide qué historias entran en el Sprint.', 'Estima las historias en lugar del equipo.', 'No asiste.'],
  'Diap. 59: el PO explica prioridades y negocia; el equipo descompone y estima; el SM facilita.')
q(T4, 'El objetivo del Sprint es…',
  'Una descripción corta y clara de lo que el equipo se propone lograr, que guía su trabajo.',
  ['La lista completa de tareas técnicas.', 'El número de horas que trabajará el equipo.', 'La velocidad media del equipo.'],
  'Diap. 55.')

q(T5, '¿Qué tres cosas comenta cada miembro en el Daily?',
  'Qué ha hecho, qué va a hacer a continuación y qué impedimentos ha encontrado.',
  ['Cuántas horas ha trabajado, cuánto cobra y cuándo tiene vacaciones.', 'Qué historias quiere el cliente, cuánto cuestan y cuándo se entregan.',
   'Qué ha ido bien, qué ha ido mal y qué cambiaría del proceso.'],
  'Diap. 64. La última opción es más bien de una retrospectiva.')
q(T5, '¿Quién participa en el Daily?',
  'El equipo de desarrollo y el Scrum Master; el Product Owner puede asistir.',
  ['Solo el Product Owner y los stakeholders.', 'Todo el equipo Scrum y los stakeholders, obligatoriamente.', 'Solo el Scrum Master.'],
  'Diap. 63 y 68. El PO puede asistir, pero no es un participante activo.')
q(T5, 'Durante el Daily, dos programadores empiezan a discutir cómo solucionar un fallo de la base de datos. ¿Qué debería pasar?',
  'Anotar el impedimento y tratar la solución después de la reunión, con quien haga falta.',
  ['Resolverlo en ese momento con todo el equipo presente.', 'Cancelar el Daily ese día.', 'Pedir al PO que decida la solución.'],
  'Diap. 65: no hay que discutir las soluciones ni divagar sobre el origen del impedimento, solo cómo resolverlo y quién.')
q(T5, 'Respecto al Daily, el Scrum Master…',
  'Lo facilita para que se cumpla el tiempo y el propósito, pero no debería dirigirlo.',
  ['Lo dirige preguntando a cada uno y asignándole tareas.', 'No puede asistir.', 'Es el único que habla.'],
  'Diap. 68.')
q(T5, '¿Qué artefactos se generan o actualizan en el Daily?',
  'La lista de impedimentos y el Burndown Chart.', ['El Product Backlog y el plan de entregas.', 'La visión del producto.',
                                                    'Las técnicas de retrospectiva.'],
  'Diap. 66. El Product Backlog adaptado y el plan de entregas los genera la Sprint Review.')
q(T5, '¿Cuándo tiene lugar la Sprint Review?',
  'El último día del Sprint.', ['El primer día del Sprint.', 'Cada día, al empezar la jornada.', 'Justo antes de cada Sprint Planning, sustituyendo al grooming.'],
  'Diap. 71.')
q(T5, '¿Cuál es el objetivo de la Sprint Review?',
  'Recoger feedback sobre el estado del producto y la aceptación de lo comprometido en el Sprint.',
  ['Mejorar la forma de trabajar del equipo.', 'Repartir las tareas del siguiente Sprint.', 'Decidir la duración del siguiente Sprint.'],
  'Diap. 71 y 73. Mejorar la forma de trabajar es la Retrospectiva.')
q(T5, '¿Qué se obtiene de la Sprint Review?',
  'El Product Backlog adaptado a las nuevas necesidades y un plan de entregas actualizado con la nueva velocidad.',
  ['Una lista de acciones de mejora del proceso.', 'La lista de impedimentos.', 'El Sprint Backlog del siguiente Sprint.'],
  'Diap. 77.')
q(T5, '¿En qué reunión participan los stakeholders?',
  'En la Sprint Review.', ['En la Retrospectiva.', 'En el Daily.', 'En la segunda fase del Sprint Planning.'],
  'Diap. 79: los stakeholders (clientes, inversores, otros departamentos) dan su feedback en la Review.')
q(T5, '¿Qué analiza la Sprint Retrospective?',
  '«El cómo»: la forma de trabajar del equipo, para mejorarla.', ['«El qué»: el producto construido.',
                                                                    'El presupuesto del proyecto.', 'Las prioridades del Product Backlog.'],
  'Diap. 80-82. La Review mira el producto; la Retrospectiva, el proceso.')
q(T5, 'En la retrospectiva del Barco, ¿qué representa el ancla?',
  'Los impedimentos que nos frenan.', ['Los riesgos.', 'Lo que nos impulsa.', 'El objetivo.'],
  'Diap. 86-87: viento (nos impulsa), ancla (impedimentos), iceberg (riesgos), sol (lo que nos facilita) e isla o tesoro (el objetivo).')
q(T5, 'En la retrospectiva de la Estrella de mar, ¿dónde van las prácticas que no aportan valor y se pueden desechar?',
  'En «Stop doing».', ['En «Do less».', 'En «Continue to do».', 'En «Start doing».'],
  'Diap. 89: Do less es para lo que aporta poco en comparación con otras acciones; Stop doing, para lo que no aporta valor.')
q(T5, 'Las 4 L de la retrospectiva son…',
  'Liked, Lacked, Learned y Longed for.', ['Look, Learn, Let go y Lead.', 'Liked, Loved, Lost y Left.', 'Listen, Learn, Lean y Launch.'],
  'Diap. 90-91.')
q(T5, '¿Qué afirmación sobre el backlog grooming es correcta?',
  'No está formalmente incluido entre las reuniones de Scrum y se hace inmediatamente antes de cada planificación.',
  ['Es la quinta reunión obligatoria de Scrum y se hace al final del Sprint.', 'Lo dirige el Scrum Master y el PO no participa.',
   'Sirve para revisar la forma de trabajar del equipo.'],
  'Diap. 60-62: lo dirige el PO, el equipo aporta detalle técnico y estimación, y el SM facilita.')

q(T6, '¿Qué es el Sprint 0?',
  'La etapa en la que se define la misión del trabajo, las herramientas y el equipo; de duración variable pero no indefinida.',
  ['El primer Sprint de desarrollo, en el que ya se entrega código.', 'Una reunión de una hora para presentar el equipo.',
   'El Sprint final de cierre del proyecto.'],
  'Diap. 93.')
q(T6, '¿Qué dos cosas deben quedar claras al acabar el Sprint 0?',
  'La viabilidad del proyecto y el contrato (recursos, equipo, alcance y fechas acordados).',
  ['El diseño completo del sistema y el código de la primera versión.', 'El Burndown del proyecto y la lista de impedimentos.',
   'La retrospectiva y la review.'],
  'Diap. 94.')
q(T6, '¿Qué actividad corresponde al «¿cuándo hacerlo?» del Sprint 0?',
  'Desarrollar un plan de entregas.', ['Desarrollar la visión del producto.', 'Hacer una prueba de concepto.',
                                       'Definir la duración de los Sprints.'],
  'Diap. 95: qué (visión y Product Backlog inicial), cómo (organización del equipo, duración de los Sprints, arquitectura inicial, prueba de concepto) y cuándo (plan de entregas).')
q(T6, '¿Quién define la visión del producto?',
  'El Product Owner, y debe ser conocida, comprendida y compartida por todo el equipo.',
  ['El Scrum Master.', 'Cada miembro del equipo por separado.', 'Los stakeholders, sin el equipo.'],
  'Diap. 96.')
q(T6, '¿Por qué se dice que la visión es «el origen y el final» del proceso?',
  'Porque es lo primero que se hace para empezar a trabajar y también el punto al que se quiere llegar.',
  ['Porque se escribe al principio y no se vuelve a mirar.', 'Porque se redacta al final como resumen del proyecto.',
   'Porque la escribe el primer y el último miembro que entra en el equipo.'],
  'Diap. 97.')
q(T6, '¿Cuál de estas NO es una característica de la visión del producto?',
  'Detallada al nivel de tareas técnicas.', ['Sencilla, clara, concisa y sin ambigüedades.',
                                             'Fácilmente comunicable a todo el mundo.', 'Instrumento vital para conseguir presupuesto.'],
  'Diap. 98: es información de alto nivel y propósito general; el detalle técnico está en el Sprint Backlog.')
q(T6, '«¿Cómo se va a generar beneficio?» y «¿cuáles son los costes del producto?» son preguntas de…',
  'El modelo de negocio de la visión.', ['El concepto de la visión.', 'La retrospectiva.', 'El Daily.'],
  'Diap. 99-100: el concepto define cómo se benefician los usuarios (problema, solución, usuarios, necesidad, competencia); el modelo de negocio, cómo se benefician los creadores (presupuesto, tiempo, beneficio, distribución, costes).')
q(T6, '¿Qué dice el test del ascensor de Geoffrey Moore?',
  'Que la visión debería poder explicarse en el tiempo que se tarda en subir o bajar varios pisos en ascensor.',
  ['Que el Daily debe durar lo que un viaje en ascensor.', 'Que el equipo no debe tener más miembros de los que caben en un ascensor.',
   'Que el Product Backlog debe caber en una hoja.'],
  'Diap. 101.')

# ----------------------------------------------------------------------------- FLASHCARDS
FC = [
    ('Origen', 'Takeuchi y Nonaka (1986)', '«The New New Product Development Game» (HBR): proponen el enfoque «rugby» (el equipo avanza unido) frente a la «carrera de relevos». Primeros en usar el término.'),
    ('Origen', 'Hitos de Scrum', '1993 Sutherland en Easel Corp. (primer equipo) · 1996 Schwaber en OOPSLA (formalización) · 2001 libro de Schwaber y Beedle · 2002 Scrum Alliance (Schwaber y Cohn).'),
    ('Origen', '¿Qué es Scrum?', 'Un marco de trabajo iterativo e incremental que no sigue un plan, sino que se adapta continuamente a la evolución del proyecto.'),
    ('Origen', 'Pilares empíricos', 'Transparencia, inspección y adaptación.'),
    ('Origen', 'Valores de Scrum (diap. 10)', 'Mejora continua, calidad, time-boxing, responsabilidad, multidisciplinar, flexibilidad, ritmo, compromiso, simplicidad, respeto, coraje, foco, predictibilidad y personas.'),
    ('Origen', 'Factores clave', 'Delegación al equipo (auto-organización), respeto entre personas, responsabilidad y autodisciplina, compromiso, y transparencia y visibilidad.'),
    ('Origen', 'Elementos de Scrum (3-4-3)', '3 artefactos (Product Backlog, Sprint Backlog, Burndown), 4 reuniones (Planning, Daily, Review, Retrospective), 3 roles (PO, SM, equipo) + reglas de trabajo.'),
    ('Roles', 'Rol en Scrum', 'Una responsabilidad en el proceso, no la posición en la organización.'),
    ('Roles', 'Roles cerdo y gallina', 'Cerdos: PO, SM y equipo (comprometidos). Gallinas: stakeholders (user, customer, management), interesados pero no comprometidos.'),
    ('Roles', 'Stakeholders', 'Personas u organizaciones con interés en el trabajo. Son fuente de requisitos y validan el trabajo dando feedback.'),
    ('Roles', 'Product Owner', 'Representante del cliente e intermediario con el equipo. Visión, requisitos, Product Backlog priorizado, aceptar o rechazar el incremento, resolver dudas, plan de entregas y ROI.'),
    ('Roles', 'PO directo y proxy', 'Directo: el propio cliente es el PO. Proxy: un intermediario (p. ej. product manager) representa a varios clientes.'),
    ('Roles', 'Necesidades del PO', 'Conocer a fondo el negocio, tener atribuciones para decidir, conocer Scrum y recibir retroinformación continua.'),
    ('Roles', 'Scrum Master', 'Facilitador, coach y mentor. Garantiza el proceso, elimina impedimentos, protege al equipo (escudo) y mejora su productividad. No asigna tareas.'),
    ('Roles', 'Atributos del SM', 'Responsable, humilde, colaborador, comprometido, influyente y entendido.'),
    ('Roles', 'Servicios del SM', 'Al PO (gestionar y ordenar el backlog), al equipo (auto-organización, impedimentos, facilitar eventos) y a la organización (adopción de Scrum).'),
    ('Roles', 'Equipo de desarrollo', 'Entrega cada Sprint un incremento «terminado» y desplegable. Auto-organizado, multidisciplinar, multifuncional, sin sub-equipos, a tiempo completo, de 5 a 9 personas.'),
    ('Roles', 'Responsabilidades del equipo', 'Estimar los ítems del backlog, comprometerse a entregar con calidad de producción y seguir su propio plan de avance.'),
    ('Artefactos', 'Product Backlog', 'Lista ordenada y priorizada de todo lo que podría necesitar el producto. Lenguaje de negocio, flexible y dinámica; responsable: el PO. Requisitos funcionales y no funcionales.'),
    ('Artefactos', 'Lista DEEP', 'Detallada (entendible y estimable), Emergente (aparecen historias nuevas), Estimada y Priorizada.'),
    ('Artefactos', 'Técnicas de priorización', 'Priority poker, MoSCoW (Must, Should, Could, Won\'t), modelo de Kano, criba de temas y peso relativo.'),
    ('Artefactos', 'Sprint Backlog', 'Historias del Product Backlog negociadas para el Sprint, descompuestas en tareas técnicas. Propiedad del equipo.'),
    ('Artefactos', 'Dimensiones del Sprint Backlog', 'Prioridad, detalle (historia dividida en tareas) y estado: pendiente, en curso, terminada o impedida.'),
    ('Artefactos', 'Burndown Chart', 'Gráfica del trabajo pendiente, del Sprint o del proyecto. Real por encima de la ideal: ritmo bajo, reducir alcance. Por debajo: ritmo alto, se pueden añadir historias.'),
    ('Artefactos', 'Lista de impedimentos', 'Sale del Daily: todo lo que impide alcanzar los objetivos. Responsable: el SM. Cada impedimento se describe, se busca solución y se le asigna responsable.'),
    ('Sprint y reuniones', 'Sprint', 'Time-box fijo de 1 a 4 semanas que produce un incremento terminado y desplegable. No se cambia su objetivo ni bajan los objetivos de calidad; el alcance se puede renegociar.'),
    ('Sprint y reuniones', 'Duraciones (Sprint de 4 semanas)', 'Planning 8 h, Review 4 h, Retrospectiva 3 h. Daily: 15 min (Guía de Scrum; no viene en la diapositiva).'),
    ('Sprint y reuniones', 'Fases del Sprint Planning', '1) Planificación: qué historias entran, por prioridad y hasta la velocidad media. 2) Planificación detallada: el equipo las divide en tareas.'),
    ('Sprint y reuniones', 'Selección de historias (5 pasos)', 'El PO lee la más prioritaria; la explica con sus criterios de aceptación; el equipo la estima; pasa al Sprint Backlog en orden; se para al alcanzar la velocidad media.'),
    ('Sprint y reuniones', 'Backlog grooming', 'Refinar el Product Backlog (depurar, añadir, eliminar, dividir épicas, repriorizar). No es formal en Scrum; justo antes de cada Planning; lo dirige el PO.'),
    ('Sprint y reuniones', 'Daily Meeting', 'Diaria; equipo y SM (el PO puede asistir). Qué hice, qué haré, qué impedimentos tengo. Breve, sin discutir soluciones; el SM facilita sin dirigir.'),
    ('Sprint y reuniones', 'Sprint Review', 'Último día del Sprint; equipo, SM, PO y stakeholders. Demo de lo terminado y feedback. Genera el Product Backlog adaptado y el plan de entregas actualizado.'),
    ('Sprint y reuniones', 'Guion de la Review (8 pasos)', 'Normas · objetivos del Sprint · el PO dice qué se terminó · métricas del equipo · demostración · el PO repasa backlog y plan de entregas · comentarios de los stakeholders · recogida de comentarios.'),
    ('Sprint y reuniones', 'Sprint Retrospective', 'Después de la Review; equipo y SM (PO opcional). Mejorar «el cómo»: qué hacemos bien, qué mejorar y qué haremos en la siguiente iteración. Revisa personas, relaciones, procesos y herramientas.'),
    ('Sprint y reuniones', 'Retrospectiva del Barco', 'Viento: nos impulsa. Ancla: impedimentos. Iceberg: riesgos. Sol: lo que nos facilita. Isla o tesoro: objetivo.'),
    ('Sprint y reuniones', 'Estrella de mar', 'Start doing, Do more, Continue to do, Do less, Stop doing.'),
    ('Sprint y reuniones', 'Las 4 L', 'Liked, Lacked, Learned y Longed for.'),
    ('Sprint 0 y visión', 'Sprint 0', 'Define la misión, las herramientas y el equipo. Duración variable pero no indefinida. Al final: viabilidad y contrato.'),
    ('Sprint 0 y visión', 'Actividades del Sprint 0', 'Qué: visión y Product Backlog inicial. Cómo: organizar el equipo (incluida la duración de los Sprints), arquitectura inicial y prueba de concepto. Cuándo: plan de entregas.'),
    ('Sprint 0 y visión', 'Visión del producto', 'Dónde se quiere estar. La define el PO; conocida, comprendida y compartida por todos. Origen y final del proceso.'),
    ('Sprint 0 y visión', 'Elementos de la visión', 'Concepto (cómo se benefician los usuarios: problema, solución, usuarios, necesidad, competencia) y modelo de negocio (cómo se benefician los creadores: presupuesto, tiempo, beneficio, distribución, costes).'),
    ('Sprint 0 y visión', 'Test del ascensor', 'G. Moore: la visión debe poder explicarse en lo que dura un viaje de varios pisos en ascensor. Plantilla: Para [cliente] que [necesidad], [producto] es un [categoría] que [beneficio]. A diferencia de [competencia], [diferencia].'),
]

# ----------------------------------------------------------------------------- V/F
VF = [
    ('Roles', 'El Scrum Master asigna las tareas del Sprint a cada miembro del equipo.', 'F', 'El equipo es auto-organizado (diap. 30) y descompone y reparte el trabajo. El SM es facilitador, coach y mentor (diap. 22).'),
    ('Roles', 'Los roles de Scrum representan una responsabilidad en el proceso, no un puesto en la organización.', 'V', 'Diap. 15, textualmente.'),
    ('Roles', 'Los stakeholders son «roles cerdo» porque están comprometidos con el resultado.', 'F', 'Son roles gallina: interesados, no comprometidos. Los cerdos son PO, SM y equipo (diap. 16).'),
    ('Roles', 'El Product Owner es quien acepta o rechaza el software al final de cada iteración.', 'V', 'Diap. 21.'),
    ('Roles', 'Scrum recomienda dividir el equipo en sub-equipos de desarrollo y de pruebas.', 'F', 'Scrum no reconoce sub-equipos; el equipo es multifuncional (diap. 30).'),
    ('Roles', 'El tamaño típico del equipo de desarrollo es de 5 a 9 personas.', 'V', 'Diap. 31.'),
    ('Roles', 'Eliminar impedimentos es responsabilidad del Product Owner.', 'F', 'Es del Scrum Master (diap. 23 y 26).'),
    ('Roles', 'En una implementación proxy, un product manager puede actuar como Product Owner en representación de varios clientes.', 'V', 'Diap. 19.'),
    ('Artefactos', 'El Product Backlog se cierra al acabar el Sprint 0 y ya no cambia.', 'F', 'Es emergente y dinámico: pueden aparecer historias nuevas en cualquier momento (diap. 36-38).'),
    ('Artefactos', 'El Product Backlog solo contiene requisitos funcionales.', 'F', 'Contiene requisitos funcionales y no funcionales (diap. 37).'),
    ('Artefactos', 'El Sprint Backlog es propiedad del equipo de desarrollo.', 'V', 'Diap. 40.'),
    ('Artefactos', 'Si en el Burndown la línea real va por debajo de la ideal, el equipo va más rápido de lo previsto y puede plantearse añadir historias.', 'V', 'Diap. 44.'),
    ('Artefactos', 'El responsable de la lista de impedimentos es el Scrum Master.', 'V', 'Diap. 66.'),
    ('Artefactos', 'MoSCoW, Kano y priority poker son técnicas de estimación del tamaño de las historias.', 'F', 'Son técnicas de priorización (diap. 39).'),
    ('Sprint', 'La duración de cada Sprint se ajusta a la cantidad de trabajo pendiente.', 'F', 'La longitud es fija, de 1 a 4 semanas (diap. 47 y 49).'),
    ('Sprint', 'Si el Sprint va retrasado, se pueden relajar los objetivos de calidad para cumplir la fecha.', 'F', '«Los objetivos de calidad no disminuyen» (diap. 49); en su lugar se renegocia el alcance.'),
    ('Sprint', 'Durante el Sprint, el PO y el equipo pueden clarificar y renegociar el alcance a medida que aprenden.', 'V', 'Diap. 49. Lo que no se cambia es el objetivo del Sprint.'),
    ('Sprint', 'En un Sprint de 4 semanas, el Sprint Planning dura como máximo 8 horas.', 'V', 'Diap. 50.'),
    ('Sprint', 'En la primera fase del Sprint Planning el equipo divide las historias en tareas técnicas.', 'F', 'Eso es la segunda fase (planificación detallada). En la primera se seleccionan historias por prioridad hasta la velocidad media (diap. 53-57).'),
    ('Sprint', 'El backlog grooming es una de las cuatro reuniones formales de Scrum.', 'F', 'No está formalmente incluido; se hace justo antes de cada planificación (diap. 61).'),
    ('Reuniones', 'En el Daily se discuten las soluciones técnicas a los problemas que surgen.', 'F', 'No se discuten soluciones ni el origen del impedimento: solo cómo resolverlo y quién (diap. 65).'),
    ('Reuniones', 'El Product Owner puede asistir al Daily, pero no es un participante activo.', 'V', 'Diap. 68.'),
    ('Reuniones', 'El Scrum Master dirige el Daily preguntando a cada miembro.', 'F', 'Lo facilita para que cumpla tiempo y propósito, pero no debería dirigirlo (diap. 68).'),
    ('Reuniones', 'La Sprint Review se celebra el último día del Sprint.', 'V', 'Diap. 71.'),
    ('Reuniones', 'Los stakeholders participan en la Sprint Retrospective para dar su feedback del producto.', 'F', 'El feedback del producto lo dan en la Review (diap. 79). La Retrospectiva es del equipo y el SM; el PO es opcional (diap. 85).'),
    ('Reuniones', 'La Retrospectiva analiza «el cómo» trabaja el equipo para mejorar continuamente.', 'V', 'Diap. 80.'),
    ('Reuniones', 'En la retrospectiva del Barco, el iceberg representa los riesgos.', 'V', 'Diap. 87.'),
    ('Sprint 0 y visión', 'El Sprint 0 puede durar indefinidamente hasta que el producto esté perfectamente definido.', 'F', 'Su duración es variable pero no indefinida (diap. 93).'),
    ('Sprint 0 y visión', 'La visión del producto debe ser información de alto nivel, sencilla y sin ambigüedades.', 'V', 'Diap. 98.'),
    ('Sprint 0 y visión', 'Según el test del ascensor, la visión debe poder explicarse en lo que dura un viaje de varios pisos en ascensor.', 'V', 'Diap. 101 (G. Moore).'),
]

# ----------------------------------------------------------------------------- PREGUNTAS CORTAS Y EJERCICIOS
RC = 'Preguntas cortas de teoría'
RE = 'Ejercicios de examen'
REVEAL = [
    (RC, '¿Qué es Scrum y de dónde viene su nombre?', 'Un marco de trabajo iterativo e incremental que no sigue un plan fijo, sino que se adapta continuamente a la evolución del proyecto (diap. 8). El nombre viene del rugby: Takeuchi y Nonaka (1986) comparan el desarrollo en fases («carrera de relevos») con un equipo que avanza unido pasándose el balón (la melé o scrum).'),
    (RC, 'Enumera los elementos de Scrum.', '3 artefactos: Product Backlog, Sprint Backlog y Burndown Chart. 4 reuniones: Sprint Planning, Daily Meeting, Sprint Review y Sprint Retrospective. 3 roles: Product Owner, Scrum Master y equipo de desarrollo. Más las reglas de trabajo (diap. 13).'),
    (RC, 'Explica los pilares empíricos con un ejemplo de cada uno.', 'Transparencia: el Burndown y el panel muestran a todos el estado real. Inspección: en el Daily y en la Review se revisan el avance y el producto. Adaptación: si el Burndown va por encima de la ideal, se renegocia el alcance; tras la Retrospectiva se cambia la forma de trabajar.'),
    (RC, 'Diferencia entre roles cerdo y gallina.', 'Cerdos: el equipo Scrum (PO, SM y equipo), comprometidos con el resultado. Gallinas: los stakeholders (usuarios, clientes, dirección), interesados pero no comprometidos; son fuente de requisitos y validan el trabajo (diap. 16-17).'),
    (RC, 'Responsabilidades del Product Owner.', 'Obtener una visión compartida, recoger requisitos, crear, administrar y priorizar el Product Backlog, aceptar o rechazar el software al final de cada iteración, resolver dudas del equipo, administrar el plan de entregas y maximizar el ROI (diap. 21).'),
    (RC, '¿Por qué se dice que el Scrum Master no es un jefe de proyecto?', 'Porque es un facilitador, coach y mentor (diap. 22): garantiza el proceso, elimina impedimentos y protege al equipo de interferencias, pero no asigna tareas (el equipo se auto-organiza) ni decide qué se construye (eso es del PO).'),
    (RC, 'Características del equipo de desarrollo.', 'Auto-organizado y no jerarquizado, multidisciplinar, multifuncional, con elevado compromiso, sin sub-equipos, a tiempo completo y fijo, típicamente de 5 a 9 personas. Estima los ítems y se compromete a entregar incrementos con calidad de producción (diap. 30-32).'),
    (RC, 'Define el Product Backlog y explica DEEP.', 'Lista ordenada y priorizada de todo lo que podría necesitar el producto, en lenguaje de negocio, responsabilidad del PO, con requisitos funcionales y no funcionales. DEEP: Detallada (entendible y estimable), Emergente (aparecen historias nuevas), Estimada y Priorizada (diap. 36-38).'),
    (RC, 'Diferencias entre Product Backlog y Sprint Backlog.', 'Product Backlog: todo lo que podría necesitar el producto; lenguaje de negocio; del PO; dura todo el proyecto. Sprint Backlog: las historias seleccionadas para un Sprint, descompuestas en tareas técnicas; del equipo; se rehace cada Sprint; cada tarea está pendiente, en curso, terminada o impedida.'),
    (RC, 'Describe las dos fases del Sprint Planning.', '1) Planificación: el PO presenta las historias por prioridad con sus criterios de aceptación, el equipo las estima y se seleccionan hasta alcanzar la velocidad media; se define el objetivo del Sprint. 2) Planificación detallada: el equipo traduce las historias al lenguaje de desarrollo y las divide en tareas (diap. 53-57).'),
    (RC, '¿Cómo es el Daily Meeting?', 'Reunión diaria y breve del equipo con el SM (el PO puede asistir). Cada uno dice qué ha hecho, qué va a hacer y qué impedimentos tiene. No se discuten soluciones. Genera la lista de impedimentos (del SM) y actualiza el Burndown. El SM la facilita sin dirigirla (diap. 63-70).'),
    (RC, 'Diferencia entre Sprint Review y Sprint Retrospective.', 'Review: último día del Sprint, con stakeholders; inspecciona el producto («qué»), con una demo; genera el Product Backlog adaptado y el plan de entregas actualizado. Retrospective: después de la Review, el equipo y el SM; inspecciona el proceso («cómo»); genera acciones de mejora.'),
    (RC, 'Explica dos técnicas de retrospectiva.', 'Barco: viento (impulsa), ancla (impedimentos), iceberg (riesgos), sol (facilita) e isla (objetivo). Estrella de mar: start doing, do more, continue to do, do less y stop doing. (También las 4 L: liked, lacked, learned y longed for.)'),
    (RC, '¿Qué es el Sprint 0 y qué actividades incluye?', 'Etapa de duración variable pero no indefinida para definir la misión, las herramientas y el equipo. Qué: visión y Product Backlog inicial. Cómo: organización del equipo y forma de trabajar (duración de los Sprints, herramientas, reglas), arquitectura inicial y prueba de concepto. Cuándo: plan de entregas. Al final: viabilidad y contrato (diap. 93-95).'),
    (RC, 'Características y elementos de la visión del producto.', 'La define el PO y la comparte todo el equipo. Características: alto nivel, sencilla, clara, concisa y sin ambigüedades, con la esencia del producto, fácil de comunicar, sirve para conseguir presupuesto y para el lanzamiento. Elementos: concepto (beneficio para los usuarios) y modelo de negocio (beneficio para los creadores). Test del ascensor de Moore.'),
    (RE, 'Ejercicio 1 (Visión): redacta la visión y el elevator pitch de una app para reservar las pistas deportivas de la UGR.', 'Concepto. Problema: las reservas se hacen en persona o por teléfono y las pistas quedan vacías. Solución: app con disponibilidad en tiempo real y reserva con el correo de la UGR. Usuarios: estudiantes y personal. Necesidad: reservar rápido y sin desplazarse. Competencia: la web actual y apps genéricas como Playtomic, que no están integradas con la UGR.\nModelo de negocio. Financiación del Centro de Actividades Deportivas; 4 meses; cobro de la reserva con una pequeña comisión; difusión en la web y las redes de la UGR; costes de desarrollo y servidores.\nElevator pitch: «Para los estudiantes y el personal de la UGR que pierden tiempo reservando pistas, ReservaUGR es una app que permite reservar en segundos con la cuenta de la universidad. A diferencia de la web actual y de Playtomic, muestra la disponibilidad en tiempo real y libera automáticamente las reservas no confirmadas».'),
    (RE, 'Ejercicio 2 (Sprint 0): planifica el Sprint 0 del proyecto anterior.', 'Qué: visión (ejercicio 1) y Product Backlog inicial (registro, ver disponibilidad, reservar, cancelar, pagar, avisos). Cómo: equipo de 6 multifuncional + SM; PO del Centro de Deportes; Sprints de 2 semanas; Trello y Slack; estándares y Definition of Done; arquitectura inicial (app + API + base de datos); prueba de concepto del login con la cuenta de la UGR. Cuándo: plan de entregas (reservas básicas en el Sprint 3, pagos en el 5). Al final: viabilidad y contrato con alcance, fechas y recursos.'),
    (RE, 'Ejercicio 3 (Sprint Planning): velocidad media de 15 puntos; backlog priorizado: H1 (5), H2 (8), H3 (3), H4 (5), H5 (2). ¿Qué entra en el Sprint?', 'Se recorren las historias en orden de prioridad: H1 → 5; H2 → 13; H3 → 16, que supera ligeramente los 15, así que es aceptable según la diap. 56. Entran H1, H2 y H3, en ese orden. H4 y H5 quedan para el siguiente Sprint. Después, en la planificación detallada, el equipo divide cada historia en tareas.'),
    (RE, 'Ejercicio 4 (Burndown): Sprint de 10 días y 100 horas. El día 6 quedan 70 horas. Interpreta y decide.', 'La línea ideal el día 6 está en 40 horas. Con 70 horas la real va por encima: el ritmo es bajo. Acciones: revisar los impedimentos en el Daily; el SM trabaja en eliminarlos; si no se recupera, el equipo y el PO renegocian el alcance (sacar la historia menos prioritaria) sin bajar la calidad ni cambiar el objetivo del Sprint.'),
    (RE, 'Ejercicio 5 (Roles): ¿quién hace cada cosa? (a) Decidir que el pago con Bizum va antes que las notificaciones. (b) Estimar la historia de reservas en 8 puntos. (c) Conseguir que el servicio de informática dé acceso al servidor. (d) Decidir quién programa la pantalla de login.', '(a) El Product Owner, que prioriza el Product Backlog. (b) El equipo de desarrollo, que estima. (c) El Scrum Master, porque es un impedimento y se apunta en su lista. (d) El equipo, que se auto-organiza; no lo decide el SM.'),
    (RE, 'Ejercicio 6 (¿Qué está mal?): «El SM abre el Daily, pregunta a cada uno qué ha hecho y le dice qué hacer hoy. Cuando aparece un error de la base de datos, el equipo se queda 40 minutos resolviéndolo».', 'Dos errores. (1) El SM dirige y asigna tareas: debe facilitar sin dirigir, y el equipo se auto-organiza. (2) Se discute la solución en el Daily: hay que anotarlo como impedimento, decir quién lo resolverá y tratarlo después. El Daily es breve y solo responde a qué hice, qué haré y qué impedimentos tengo.'),
    (RE, 'Ejercicio 7 (Review): organiza la Sprint Review del primer incremento de la app de reservas.', 'Preparación: entorno de demo con datos, guion y comprobar que funciona. Guion: 1) normas para los nuevos asistentes; 2) objetivos del Sprint; 3) el PO dice qué se terminó (registro y ver disponibilidad) y qué no (reservar); 4) el equipo presenta métricas y problemas; 5) demo de lo terminado; 6) el PO repasa el backlog y el plan de entregas; 7) comentarios de los stakeholders (Centro de Deportes, estudiantes); 8) recoger comentarios. Resultado: Product Backlog adaptado y plan de entregas con la nueva velocidad.'),
    (RE, 'Ejercicio 8 (Retrospectiva): el equipo ha tenido problemas con despliegues manuales y con un PO poco disponible, pero las pruebas automáticas funcionan bien. Haz la retrospectiva con el Barco.', 'Viento (nos impulsa): las pruebas automáticas. Sol (nos facilita): buen ambiente y panel actualizado. Ancla (impedimentos): despliegues manuales y PO poco disponible. Iceberg (riesgos): no llegar a la entrega de pagos; dependencia del servicio de informática. Isla (objetivo): MVP de reservas en el Sprint 3. Acciones: automatizar el despliegue (responsable: un miembro del equipo) y fijar 30 minutos semanales con el PO (el SM lo gestiona).'),
    (RE, 'Ejercicio 9 (Product Backlog): escribe 5 historias para la app de reservas y priorízalas con MoSCoW.', '1. Como estudiante, quiero iniciar sesión con mi cuenta de la UGR para reservar a mi nombre (Must). 2. Como estudiante, quiero ver las pistas libres por día y hora para elegir (Must). 3. Como estudiante, quiero reservar una pista para asegurarme de jugar (Must). 4. Como estudiante, quiero cancelar mi reserva para liberar la pista (Should). 5. Como estudiante, quiero recibir un aviso una hora antes para no olvidarme (Could). Pagar con Bizum: Won\'t en esta entrega. Es DEEP: detallado arriba, emergente, estimado por el equipo y priorizado por el PO.'),
    (RE, 'Ejercicio 10 (Sprint Backlog): descompón «Como estudiante, quiero reservar una pista» en tareas e indica quién lo hace y en qué estados pueden estar.', 'Tareas: diseñar la pantalla de reserva; servicio de reserva en la API con control de solapes; tabla de reservas en la base de datos; correo de confirmación; pruebas de aceptación (no se puede reservar una pista ocupada; máximo 2 reservas por persona); pruebas en móvil. Lo hace el equipo en la planificación detallada del Sprint Planning. Estados: pendiente, en curso, terminada e impedida.'),
]


def dump(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('escrito', name)


dump('test-t4-scrum.json', {
    'subject': SUBJECT, 'type': 'test', 'order': -9,
    'title': 'Test Tema 4: Scrum',
    'description': f'{len(TEST)} preguntas tipo test del Tema 4 (origen, pilares, roles, artefactos, Sprint, reuniones, retrospectivas, Sprint 0 y visión) con justificación y la diapositiva de la que sale cada una.',
    'items': TEST,
})
dump('flashcards-t4-scrum.json', {
    'subject': SUBJECT, 'type': 'flashcards', 'order': -8,
    'title': 'Flashcards Tema 4: Scrum',
    'description': f'{len(FC)} tarjetas con todo el Tema 4: elementos 3-4-3, roles, DEEP, duraciones de las reuniones, técnicas de retrospectiva, Sprint 0 y visión.',
    'items': [{'tema': t, 'term': a, 'def': b} for t, a, b in FC],
})
dump('vf-t4-scrum.json', {
    'subject': SUBJECT, 'type': 'vf', 'order': -7,
    'title': 'Verdadero o falso: Tema 4 Scrum (trampas de examen)',
    'description': f'{len(VF)} afirmaciones con las confusiones típicas: quién prioriza y quién estima, qué reunión es cuál, qué no se cambia en un Sprint.',
    'items': [{'n': k + 1, 'tema': t, 'q': a, 'answer': r, 'justification': j} for k, (t, a, r, j) in enumerate(VF)],
})
dump('preguntas-cortas-t4-scrum.json', {
    'subject': SUBJECT, 'type': 'reveal', 'order': -6,
    'title': 'Preguntas cortas y ejercicios: Tema 4 Scrum',
    'description': f'{sum(1 for x in REVEAL if x[0] == RC)} preguntas cortas y {sum(1 for x in REVEAL if x[0] == RE)} ejercicios resueltos del tipo de la prueba (visión y elevator pitch, Sprint 0, Sprint Planning con velocidad, Burndown, roles, Review y retrospectiva).',
    'items': [{'tema': t, 'q': a, 'answer': b} for t, a, b in REVEAL],
})
