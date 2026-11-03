import json
import os

materials_dir = "/home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/content/materials/ade/derecho-fiscal"
os.makedirs(materials_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 1. SUPUESTOS-EXAMEN.JSON
# ─────────────────────────────────────────────────────────────────────────────

# Load existing 15 questions of simulacro-9nov if present
existing_supuestos_path = os.path.join(materials_dir, "supuestos-examen.json")
simulacro_items = []
if os.path.exists(existing_supuestos_path):
    with open(existing_supuestos_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
        simulacro_items = [q for q in existing_data.get('items', []) if q.get('caseId') == 'simulacro-9nov']

statement_2019 = """EXAMEN OFICIAL CONVOCATORIA ORDINARIA — DERECHO FISCAL (FACULTAD CC.EE. Y EMPRESARIALES UGR)

DATOS DEL CASO PRÁCTICO (MATRIMONIO EN GANANCIALES RESIDENTE EN GRANADA):
Doña María Casares y D. Julio Gutiérrez (ambos de 50 años) están casados en régimen de gananciales desde el año 2000 y residen en Granada con sus dos hijos solteros (19 y 17 años, estudiantes sin rentas) y la madre de Doña María (76 años, sin rentas, con minusvalía del 40%).

1) D. Julio trabaja como ingeniero para una empresa tecnológica:
• Salario íntegro anual: 62.000 € (retenciones practicadas: 15.500 €; Seguridad Social: 2.900 €).
• En mayo asistió a un Congreso en Barcelona durante 3 días (2 noches de hotel). Aporta factura de hotel (300 €) y billete de avión (90 €). La empresa le abonó una asignación global para gastos de manutención de 400 €.
• Recibió un premio por sus 10 años de servicio en la empresa por importe de 5.000 € (retención practicada: 875 €).
• La empresa le paga una prima anual por seguro de enfermedad de 600 € (cobertura exclusiva para D. Julio).
• Se realizaron aportaciones a planes de pensiones por 6.000 € (de las cuales 3.000 € fueron aportadas por la empresa y 3.000 € por el trabajador).

2) Inmuebles del matrimonio:
• Residen en vivienda habitual adquirida en 2001 por 180.000 € (Valor Catastral = 200.000 €, 50% suelo y 50% construcción; IBI satisfecho = 312 €).
• Apartamento en la playa adquirido en 2010 por 130.000 € (Valor Catastral revisado = 90.000 €, 25% suelo y 75% construcción). Alquilado todo el año por 400 €/mes (4.800 €/año). Único gasto asumido por los propietarios: IBI de 130 €.
• Finca rústica privativa de Doña María heredada de su padre en 2013 por valor a efectos del ISD de 35.000 € (Valor Catastral = 23.000 €). La finca ha estado improductiva todo el tiempo hasta su venta el 1 de abril de 2018 por 30.000 €.

3) Patrimonio mobiliario:
• En enero de 2018 D. Julio heredó de un pariente 300 acciones cotizadas (valor a efectos de ISD = 21.000 €, a 70 €/acción). Generaron dividendos líquidos de 2.430 € (retención de 570 €; gastos de administración 5 €). En noviembre vendió 50 acciones a 100 € cada una (cotización en dicho momento)."""

questions_2019 = [
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "1. Respecto a las 300 acciones cotizadas heredadas por D. Julio a principios de año, señale su calificación tributaria exacta:",
        "opts": [
            "Suponen una ganancia de patrimonio en el IRPF de D. Julio y a la vez tributan en el Impuesto sobre Sucesiones.",
            "No están sujetas al IRPF de D. Julio por su adquisición lucrativa 'mortis causa' (tributan exclusivamente en el ISD).",
            "No generan ningún tipo de renta ni tributación en el ejercicio al tratarse de una herencia familiar directa.",
            "Están exentas en el ISD y tributan como rendimiento del capital mobiliario en el IRPF."
        ],
        "correct": 1,
        "justification": "Art. 6.4 LIRPF: No está sujeta al IRPF la renta que se encuentre sujeta al Impuesto sobre Sucesiones y Donaciones (ISD). La adquisición gratuita de las acciones por herencia tributa en el ISD, no en el IRPF."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "2. De los 400 € que la empresa abonó a D. Julio para manutención por su asistencia al Congreso en Barcelona (3 días y 2 noches), ¿cuánto debe tributar en su IRPF?",
        "opts": [
            "Están totalmente exentos al estar justificada la asistencia al congreso con factura de hotel.",
            "Tributan 266,65 € como rendimiento del trabajo personal dinerario (exentos 133,35 €).",
            "Tributan íntegramente los 400 € al no haber aportado facturas individuales de cada restaurante.",
            "Tributan 10 € en concepto de retribución en especie."
        ],
        "correct": 1,
        "justification": "Art. 9.A.3.a RIRPF: Para desplazamientos en territorio nacional con pernocta, la dieta de manutención exenta es de 53,34 €/día en días con pernocta (2 días × 53,34 € = 106,68 €) y de 26,67 € el día de regreso sin pernocta (1 día × 26,67 € = 26,67 €). Total exento = 133,35 €. Como la empresa le dio 400 €, el exceso (400 € - 133,35 € = 266,65 €) tributa como rendimiento del trabajo dinerario."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "3. En relación con la prima anual de 600 € satisfecha por la empresa para el seguro de enfermedad de D. Julio:",
        "opts": [
            "Está totalmente exenta de tributación por el art. 42.3.c de la LIRPF.",
            "Tributa íntegramente como retribución en especie por importe de 600 €.",
            "Está exenta hasta el límite legal de 500 € anuales, tributando únicamente como retribución en especie los 100 € restantes.",
            "Está no sujeta al IRPF al tratarse de un gasto obligatorio de prevención de riesgos laborales."
        ],
        "correct": 2,
        "justification": "Art. 42.3.c LIRPF: Están exentas las primas satisfechas a entidades aseguradoras para la cobertura de enfermedad del trabajador, su cónyuge y descendientes hasta el límite de 500 € anuales por cada uno de ellos (1.500 € si tienen discapacidad). Por tanto, 500 € están exentos y el exceso de 100 € tributa como rendimiento del trabajo en especie."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "4. Por las aportaciones al Plan de Pensiones realizadas en el ejercicio (6.000 € en total, 3.000 € por la empresa y 3.000 € por D. Julio), ¿qué cantidad debe integrar D. Julio como rendimiento íntegro de trabajo?",
        "opts": [
            "0 €, porque las aportaciones a planes de pensiones están totalmente exentas de computarse como rentas del trabajo.",
            "6.000 €, computando tanto la aportación propia como la empresarial.",
            "3.000 €, correspondientes a la contribución empresarial imputada (retribución en especie no sujeta a ingreso a cuenta).",
            "3.000 € más un ingreso a cuenta obligatorio del 20%."
        ],
        "correct": 2,
        "justification": "Art. 17.2.a.5ª LIRPF: Las contribuciones satisfechas por los promotores de planes de pensiones se consideran rendimientos del trabajo en especie imputados al trabajador. Además, según el art. 102.2 LIRPF, no existe obligación de efectuar ingreso a cuenta sobre estas contribuciones imputadas."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "5. ¿Cómo debe tributar el premio de 5.000 € concedido a D. Julio por sus 10 años de servicio en la empresa?",
        "opts": [
            "Tributa íntegramente por 5.000 € sin reducción al ser una retribución dineraria ordinaria.",
            "Disfruta de la reducción del 30% por rendimientos irregulares generados en más de 2 años (art. 18.2 LIRPF), computándose por 3.500 €.",
            "Está totalmente exento por constituir una recompensa honorífica laboral.",
            "Tributa como una ganancia patrimonial derivada de transmisión lucrativa."
        ],
        "correct": 1,
        "justification": "Art. 18.2 LIRPF y art. 12 RIRPF: Los premios por antigüedad o vinculación laboral con período de generación superior a 2 años tienen la consideración de rendimientos del trabajo obtenidos de forma notoriamente irregular en el tiempo, aplicándose la reducción del 30% sobre el importe íntegro (5.000 € - 30% = 3.500 €)."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "6. Respecto a la finca rústica improductiva heredada por Doña María, ¿qué renta determina en el IRPF durante el tiempo que estuvo en su patrimonio?",
        "opts": [
            "Genera una imputación de rentas inmobiliarias del 2% sobre su valor catastral.",
            "Genera una imputación de rentas inmobiliarias del 1,1% proporcional a los 3 meses hasta la venta.",
            "No genera ningún tipo de renta inmobiliaria en el IRPF hasta el momento de su venta (las fincas rústicas no generan imputación de rentas).",
            "Tributa como rendimiento del capital inmobiliario presunto según precios de mercado."
        ],
        "correct": 2,
        "justification": "Art. 85 LIRPF (clave de examen): El régimen de imputación de rentas inmobiliarias se aplica ÚNICAMENTE a los bienes inmuebles URBANOS (no afectos ni arrendados). Las fincas y terrenos rústicos NO generan en ningún caso imputación de rentas en el IRPF."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "7. Por el apartamento en la playa alquilado todo el año por 400 €/mes (4.800 € anuales), ¿cuál es el rendimiento neto de capital inmobiliario para cada cónyuge?",
        "opts": [
            "872,50 € para cada uno de los cónyuges.",
            "1.745 € para D. Julio y 0 € para Doña María.",
            "2.335 € para cada uno de los cónyuges.",
            "436,25 € para cada uno tras aplicar una reducción del 50%."
        ],
        "correct": 0,
        "justification": "Art. 22 y 23 LIRPF: Ingresos íntegros = 4.800 €. Gastos deducibles: IBI = 130 €. Amortización construcción (art. 23.1.b): mayor entre coste (130.000 € × 75% = 97.500 €) o VC construcción (90.000 € × 75% = 67.500 €). Amortización = 3% de 97.500 € = 2.925 €. Rendimiento neto = 4.800 € - 130 € - 2.925 € = 1.745 €. Al ser bien ganancial, corresponde el 50% a cada uno: 872,50 €."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "8. Los dividendos íntegros generados por las acciones heredadas por D. Julio ascienden a 3.000 € (2.430 € netos + 570 € de retención) y soportaron 5 € de gastos de custodia. ¿Cuál es el rendimiento neto de capital mobiliario computable para D. Julio?",
        "opts": [
            "2.995 € a integrar en la base imponible del ahorro.",
            "3.000 € a integrar en la base imponible general.",
            "2.430 € a integrar en la base imponible del ahorro.",
            "1.500 € al atribuirse la mitad a su cónyuge por régimen de gananciales."
        ],
        "correct": 0,
        "justification": "Art. 25.1.a y art. 26.1.a LIRPF: Los dividendos de acciones son rendimientos del capital mobiliario por participación en fondos propios. Son deducibles exclusivamente los gastos de administración y depósito de valores negociables (3.000 € - 5 € = 2.995 €). Al ser acciones privativas heredadas por D. Julio (art. 11.3 LIRPF), el rendimiento corresponde al 100% a D. Julio y se integra en la Base Imponible del Ahorro."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "9. Por la venta de 50 acciones en noviembre a 100 € cada una (cuyo valor de adquisición en la herencia fue de 70 € por acción), ¿qué renta obtiene D. Julio?",
        "opts": [
            "Una ganancia de patrimonio de 1.500 € para D. Julio (en la Base Imponible del Ahorro).",
            "Un rendimiento del capital mobiliario de 1.500 € repartido entre el matrimonio.",
            "Una ganancia patrimonial de 1.500 € para la sociedad de gananciales.",
            "Una ganancia de patrimonio exenta por reinversión en acciones."
        ],
        "correct": 0,
        "justification": "Arts. 33 a 35 LIRPF: Valor de transmisión = 50 × 100 € = 5.000 €. Valor de adquisición = 50 × 70 € = 3.500 €. Ganancia de patrimonio = 5.000 € - 3.500 € = 1.500 €. Al tratarse de un bien privativo recibido por herencia, la alteración patrimonial corresponde íntegramente a D. Julio (art. 11.5 LIRPF) y tributa en la Base Imponible del Ahorro."
    },
    {
        "tema": "Examen Ordinario 2019",
        "caseId": "examen-2019",
        "caseTitle": "Examen Ordinario 2019: Caso Dña. María y D. Julio",
        "caseStatement": statement_2019,
        "q": "10. Respecto a la vivienda habitual del matrimonio (Valor Catastral 200.000 €), ¿qué repercusión tributaria tiene en su IRPF del ejercicio?",
        "opts": [
            "Genera una imputación de rentas del 1,1% sobre el valor catastral.",
            "No genera ninguna renta ni imputación en el IRPF (está excluida del régimen de imputación de rentas inmobiliarias).",
            "Permite deducir el importe pagado por el IBI (312 €) de los rendimientos del trabajo.",
            "Genera una ganancia patrimonial tácita sujeta al tipo del ahorro."
        ],
        "correct": 1,
        "justification": "Art. 85.1 LIRPF: La vivienda habitual de los contribuyentes está expresamente excluida del régimen de imputación de rentas inmobiliarias. Por tanto, no genera ningún tipo de rendimiento en la base imponible del IRPF."
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# Caso 3: Examen Ordinario Enero 2020
# ─────────────────────────────────────────────────────────────────────────────

statement_2020 = """EXAMEN OFICIAL CONVOCATORIA ENERO 2020 — DERECHO FISCAL (FACULTAD CC.EE. Y EMPRESARIALES UGR)

DATOS DEL CASO PRÁCTICO (MATRIMONIO EN GANANCIALES RESIDENTE EN GRANADA):
D. Jacobo J. (56 años) y Dña. Dolores H. (57 años), casados en gananciales desde 1997, residen en Granada con sus dos hijos solteros (20 y 18 años, sin rentas) y la madre de Dña. Dolores (80 años).

1) Rendimientos de D. Jacobo como investigador en el Centro de Investigación Genética (CIG):
• Sueldo íntegro anual: 42.000 € (retenciones practicadas: 9.240 €; cuotas a la Seguridad Social: 2.400 €).
• Asistió a un congreso en Madrid durante 3 días (2 noches). Factura de hotel aportada: 200 €; billete de tren (ida y vuelta): 100 €; facturas de restaurantes: 150 €. La empresa le abonó una asignación para dietas de manutención de 430 €.
• Recibió un premio de 2.000 € por sus 20 años de dedicación a la investigación en la empresa (retención: 308 €).
• La empresa aportó 4.000 € a un plan de pensiones a favor de D. Jacobo (D. Jacobo aportó otros 4.000 € propios).
• La empresa le pagó un bono transporte anual para sus desplazamientos en transporte público por 1.200 €.

2) Inmuebles e inversiones del matrimonio:
• Vivienda habitual adquirida en 2001 por 350.000 € (Valor Catastral revisado = 170.000 €, 25% suelo y 75% construcción).
• Apartamento en la playa, adquirido por D. Jacobo en 1991 por 65.000 €, arrendado durante el curso escolar por 500 €/mes (9 meses de alquiler). El IBI satisfecho por D. Jacobo asciende a 120 €.
• Finca rústica improductiva heredada por Dña. Dolores en 2019 (Valor a efectos del ISD = 300.000 €; Valor Catastral = 170.000 €).
• Un hijo de Dña. Dolores obtuvo un premio del cupón de la ONCE por 2.300 €."""

questions_2020 = [
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "1. ¿Cómo debe tributar el bono de transporte público anual de 1.200 € pagado por la empresa a D. Jacobo?",
        "opts": [
            "Tributa íntegramente como retribución dineraria ordinaria con ingreso a cuenta.",
            "Tributa como retribución en especie por el exceso sobre 500 € anuales.",
            "Está totalmente EXENTO del IRPF al tratarse de entregas para desplazamiento en transporte público de viajeros hasta el límite de 1.500 € anuales.",
            "Es una renta no sujeta que solo tributa en el Impuesto sobre el Patrimonio."
        ],
        "correct": 2,
        "justification": "Art. 42.3.h LIRPF y art. 46 bis RIRPF: Las entregas a trabajadores de títulos de transporte colectivo o bonos para desplazamiento al centro de trabajo están EXENTAS hasta un límite de 1.500 € anuales para cada trabajador. Los 1.200 € están 100% exentos."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "2. De los 430 € percibidos por D. Jacobo en concepto de dietas de manutención por el congreso de 3 días (2 noches) en Madrid, ¿cuál es el importe exento y cuánto debe tributar?",
        "opts": [
            "Están totalmente exentos los 430 € al haber justificado los restaurantes con factura.",
            "Están exentos 133,35 € (2 días × 53,34 € + 1 día × 26,67 €) y tributan 296,65 € como rendimiento del trabajo dinerario.",
            "Están exentos 160,02 € (3 días × 53,34 €) y tributan 269,98 €.",
            "Tributan los 430 € íntegros como retribución en especie con ingreso a cuenta."
        ],
        "correct": 1,
        "justification": "Art. 9.A.3.a RIRPF (regla de oro): En desplazamientos en España con pernocta, el importe exento de manutención es de 53,34 €/día en días con pernocta (2 noches = 2 días a 53,34 € = 106,68 €) y de 26,67 € en el día de regreso (sin pernocta). Total exento = 133,35 €. El exceso sobre el límite (430 € - 133,35 € = 296,65 €) tributa obligatoriamente como salario."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "3. En relación con el premio de 2.000 € por 20 años dedicados a la investigación, señale el cómputo correcto en los rendimientos íntegros de D. Jacobo:",
        "opts": [
            "Se computa al 100% (2.000 €) sin reducciones.",
            "Se aplica la reducción del 30% por irregularidad temporal (art. 18.2 LIRPF) al generarse en más de 2 años, computándose por 1.400 €.",
            "Está totalmente exento al ser un premio de investigación reconocido por la Administración.",
            "Se califica como ganancia patrimonial derivada de juego lícito."
        ],
        "correct": 1,
        "justification": "Art. 18.2 LIRPF: Rendimientos íntegros del trabajo con período de generación superior a dos años que no se obtengan de forma periódica o recurrente tienen una reducción del 30% con límite de 300.000 €. Por tanto, 2.000 € × 70% = 1.400 € a integrar."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "4. Respecto a los 4.000 € que la empresa aportó al Plan de Pensiones de D. Jacobo, ¿cómo se califica y cómo opera en la declaración?",
        "opts": [
            "Se imputa como rendimiento del trabajo en especie (art. 17.2.a.5ª) sin ingreso a cuenta, y posteriormente D. Jacobo podrá reducirlo en su base imponible general.",
            "Es una renta no sujeta que no aparece en la declaración de IRPF.",
            "Tributa como retribución dineraria con retención obligatoria del 22%.",
            "Genera una deducción directa en la cuota íntegra estatal del 40%."
        ],
        "correct": 0,
        "justification": "Art. 17.2.a.5ª LIRPF y art. 51 LIRPF: La contribución empresarial se suma a los rendimientos íntegros del trabajo como retribución en especie exenta de ingreso a cuenta (art. 102.2 LIRPF). A su vez, en la fase de base liquidable, el contribuyente puede reducirla de la Base Imponible General junto con sus aportaciones directas dentro de los límites legales."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "5. ¿Qué efectos tributarios en el IRPF produce la finca rústica improductiva heredada por Dña. Dolores en febrero de 2019?",
        "opts": [
            "Determina una imputación de rentas inmobiliarias proporcional a los 11 meses de titularidad.",
            "No genera ningún tipo de rendimiento ni renta en el IRPF (art. 85 LIRPF: las fincas rústicas no generan imputación de rentas).",
            "Supone una ganancia de patrimonio en el IRPF por la diferencia con su valor catastral.",
            "Tributa al tipo fijo del ahorro del 19% sobre el valor del ISD."
        ],
        "correct": 1,
        "justification": "Art. 85.1 LIRPF: Solo generan imputación de rentas inmobiliarias los inmuebles URBANOS no afectos a actividades económicas ni productores de rendimientos de capital. Las fincas rústicas están totalmente excluidas."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "6. El apartamento en la playa estuvo alquilado durante el curso escolar (9 meses a 500 €/mes = 4.500 €) y los 3 meses de verano estuvo vacío a disposición del propietario. ¿Procede aplicar la reducción por alquiler de vivienda habitual?",
        "opts": [
            "Sí, procede la reducción general por arrendamiento de vivienda sobre el rendimiento neto de los 9 meses.",
            "NO procede aplicar la reducción por arrendamiento de vivienda porque un alquiler por temporada escolar no satisface la necesidad permanente de vivienda habitual del inquilino (art. 23.2 LIRPF).",
            "Procede una reducción incrementada del 90% al ser zona turística.",
            "No procede tributar por el alquiler al haber estado desocupado en verano."
        ],
        "correct": 1,
        "justification": "Art. 23.2 LIRPF (criterio reiterado de la AEAT y DGT): La reducción por arrendamiento de vivienda solo es aplicable cuando el contrato tiene por destino satisfacer la necesidad permanente de vivienda habitual del arrendatario (conforme al art. 2 de la Ley de Arrendamientos Urbanos). Los contratos por curso escolar, temporada vacacional o fines de semana carecen de dicha reducción."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "7. En relación con el apartamento en la playa durante los 3 meses en que estuvo desocupado a disposición del propietario, ¿cómo debe tributar?",
        "opts": [
            "Debe declarar imputación de rentas inmobiliarias (art. 85 LIRPF) proporcional a los 3 meses (92/365 o 3/12 del cálculo anual).",
            "No tributa porque ya produjo rentas en los 9 meses anteriores.",
            "Tributa como rendimiento del capital mobiliario.",
            "Se deducen los gastos de IBI y suministros de los 3 meses de verano."
        ],
        "correct": 0,
        "justification": "Art. 85 LIRPF: Cuando un inmueble urbano alternativamente se alquila y está a disposición de su propietario en el mismo ejercicio, por el período arrendado genera Rendimientos de Capital Inmobiliario y por los días restantes genera Imputación de Rentas Inmobiliarias (2% o 1,1% del VC prorrateado por días)."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "8. ¿Cómo tributa en el IRPF el premio de 2.300 € obtenido por el hijo de 26 años en el cupón de la ONCE?",
        "opts": [
            "Tributa como rendimiento del trabajo en la base imponible general.",
            "Tributa como ganancia patrimonial al tipo fijo del ahorro del 19%.",
            "Está totalmente EXENTO de tributación en el Gravamen Especial sobre Premios de Loterías al ser su cuantía inferior a 40.000 €.",
            "Tributa con una retención a cuenta no recuperable del 20%."
        ],
        "correct": 2,
        "justification": "Disposición Adicional 33ª LIRPF y art. 7.ñ LIRPF: Los premios de loterías y apuestas organizadas por la SELAE y por la ONCE están exentos del Gravamen Especial de Loterías hasta una cuantía de 40.000 € por cupón o décimo premiado. Al ser de 2.300 €, la tributación es cero."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "9. Respecto a la vivienda habitual de la familia (adquirida en 2001 por 350.000 €, VC 170.000 €), ¿cuál es su estatus tributario en el IRPF e Impuesto sobre el Patrimonio?",
        "opts": [
            "Genera imputación de rentas en el IRPF y está exenta en el Impuesto sobre el Patrimonio.",
            "Está exenta de imputación de rentas en el IRPF y exenta en el Impuesto sobre el Patrimonio hasta un límite de 300.000 € por contribuyente.",
            "Tributa en el IRPF al 1,1% y está sujeta en el IP por 50.000 €.",
            "Tributa en ambos tributos por el 50% de su valor de mercado."
        ],
        "correct": 1,
        "justification": "Art. 85.1 LIRPF y art. 4.Nueve Ley 19/1991 del IP: En IRPF la vivienda habitual no genera imputación de rentas (exenta). En el IP, la vivienda habitual está exenta hasta un importe máximo de 300.000 € por cada cotitular contribuyente (por lo que el matrimonio dispone de hasta 600.000 € de exención conjunta)."
    },
    {
        "tema": "Examen Enero 2020",
        "caseId": "examen-2020",
        "caseTitle": "Examen Ordinario Enero 2020: Caso D. Jacobo y Dña. Dolores",
        "caseStatement": statement_2020,
        "q": "10. La transmisión gratuita de una empresa o negocio individual por fallecimiento del titular (mortis causa) a favor de sus hijos:",
        "opts": [
            "Genera una ganancia patrimonial obligatoria en el IRPF del causante.",
            "No está sujeta al IRPF del fallecido (plusvalía del muerto, art. 33.3.b LIRPF) y tributa en el Impuesto sobre Sucesiones de los herederos (pudiendo disfrutar de reducción del 95%).",
            "Constituye una pérdida patrimonial computable para el causante.",
            "Tributa simultáneamente en el IRPF y en el ISD al tipo marginal del 45%."
        ],
        "correct": 1,
        "justification": "Art. 33.3.b LIRPF y art. 20.2.c LISD: No existe ganancia o pérdida patrimonial en el IRPF con ocasión de transmisiones lucrativas por causa de muerte del contribuyente (la llamada 'plusvalía del muerto'). Los causahabientes tributan en el ISD, donde además suele aplicar la reducción del 95% para empresas familiares."
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# Caso 4: Casos Prácticos Oficiales 1 a 16 de Clase (Seminario IRPF)
# ─────────────────────────────────────────────────────────────────────────────

statement_clase = """SUPUESTOS PRÁCTICOS OFICIALES DE CLASE (PRÁCTICAS 1 A 16) — PRIMER PARCIAL DERECHO FISCAL

RECOPILACIÓN DE LOS 16 CASOS PRÁCTICOS OFICIALES EXPLICADOS Y RESUELTOS EN CLASE POR LA PROFESORA (CURSO 2026-2027):

• PRÁCTICA 1: Residencia fiscal y contribuyentes (D. José 290 días en Colombia; D. Antonio en Alemania con familia en Granada; Deportista profesional 100 días en España).
• PRÁCTICA 2: Indemnizaciones por despido (Sr. López ERE 45 €/día y 7 años; despido improcedente vs vulneración derechos fundamentales del Sr. Gálvez).
• PRÁCTICA 3: Indemnización por accidente de tráfico (Herederos Sr. Martínez 150.000 €; Daños físicos Sr. López 75.000 €; Seguro de vida viuda 250.000 € gananciales).
• PRÁCTICA 4: Becas de investigación y estudio (Sara en CSIC 1.000 €/mes; María en UNIA curso 3 créditos 600 €).
• PRÁCTICA 5: Prestación por desempleo en pago único (30.000 €) vs pago mensual periódico.
• PRÁCTICA 6: Calificación global de rentas de Dña. Francisca Guzmán (abogada cuenta ajena, actividad económica, vivienda habitual, dividendos, venta terreno rústico, acciones heredadas, lotería y pensión alimentos hijos).
• PRÁCTICA 7: D. Braulio (29 años) vive gratis en piso de su padre (sin alquiler ni contrato).
• PRÁCTICA 8: D. Álvaro Molina (dietas Lucena 20 días sin pernocta y Burgos 7 días / 6 noches + locomoción 900 km a 0,26 €/km; reducción art. 20 LIRPF).
• PRÁCTICA 9: D. Alberto en Motril (sueldo 11.900 €, comisiones 2.000 €, curso marketing vs curso golf 2.000 €, dietas de desplazamiento y reducción art. 20).
• PRÁCTICA 10: Dietas por desplazamiento con o sin justificantes de estancia y locomoción.
• PRÁCTICA 11: Despido improcedente con indemnización de 12.000 € (límite legal 33 días/año y reducción 30% del exceso), retribución en especie de vehículo de empresa con repercusión de ingreso a cuenta y seguro de enfermedad.
• PRÁCTICA 12: Vivienda propiedad de la empresa cedida a directivo: valoración en especie del 5% vs 10% del Valor Catastral con tope del 10% de las demás retribuciones.
• PRÁCTICA 13: Arrendamiento de vivienda habitual a matrimonio: ingresos íntegros, gastos de financiación y conservación con tope art. 23.1.a, amortización del 3% y reducción general del 50% de la Ley 12/2023.
• PRÁCTICA 14: Arrendamiento y gastos de mejora (las obras que amplían o mejoran el inmueble no son gasto del año sino mayor valor de adquisición).
• PRÁCTICA 15: Arrendamiento a familiar hasta tercer grado (art. 24 LIRPF: rendimiento neto mínimo del 2% o 1,1% del Valor Catastral).
• PRÁCTICA 16: Imputación de rentas inmobiliarias (art. 85 LIRPF: inmuebles desocupados, segundas residencias vacías y plazas de garaje independientes)."""

questions_clase = [
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "1. [Práctica 1.a] D. José (español) pasa 290 días en Colombia trabajando para la sucursal de una empresa colombiana en España, aportando contrato de alquiler en Bogotá y billetes de avión, pero SIN certificado de residencia fiscal de Colombia. ¿Es contribuyente del IRPF en España?",
        "opts": [
            "NO es contribuyente, porque ha permanecido más de 183 días fuera del territorio nacional español.",
            "SÍ es contribuyente del IRPF: los 290 días se computan como ausencias esporádicas al no acreditar residencia fiscal mediante certificado de la autoridad fiscal de Colombia (art. 9.1.a LIRPF).",
            "Tributa únicamente por obligación real en el Impuesto sobre la Renta de No Residentes (IRNR).",
            "Depende de si su contrato de trabajo se formalizó en España o en Colombia."
        ],
        "correct": 1,
        "justification": "Art. 9.1.a LIRPF (solución oficial de clase): Para computar el período de permanencia en el extranjero y no considerar los días como ausencias esporádicas, la ley exige taxativamente que el contribuyente acredite su residencia fiscal en otro país mediante certificado expedido por las autoridades fiscales de dicho país. Los visados, billetes y contratos de alquiler NO son prueba suficiente."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "2. [Práctica 1.b] D. Antonio trabaja y reside en Alemania desde hace 2 años con contrato de trabajo y vivienda allí, pero su mujer e hijos siguen viviendo en Granada en la vivienda familiar. Según el art. 9.1.b LIRPF:",
        "opts": [
            "Se presume 'iuris tantum' que es contribuyente en España por radicar en España el núcleo familiar (cónyuge no separado legalmente e hijos menores).",
            "Es contribuyente exclusivo en Alemania por residir allí más de 183 días.",
            "Tributa el 50% de su sueldo en España y el 50% en Alemania.",
            "Deja de ser contribuyente español de forma automática e irrevocable."
        ],
        "correct": 0,
        "justification": "Art. 9.1.b LIRPF (Práctica 1.b de clase): Se presume, salvo prueba en contrario, que el contribuyente tiene su residencia habitual en territorio español cuando, con arreglo a los criterios anteriores, resida habitualmente en España el cónyuge no separado legalmente y los hijos menores de edad que dependan de él."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "3. [Práctica 2.1] El Sr. López es despedido por ERE tras 7 años de servicio cobrando 45 €/día y percibe 19.000 € de indemnización. Sabiendo que la indemnización legal obligatoria por despido colectivo/objetivo es de 20 días por año de servicio (límite 12 mensualidades):",
        "opts": [
            "Los 19.000 € están totalmente exentos en el IRPF.",
            "Está exento el importe legal obligatorio: 20 días × 7 años × 45 € = 6.300 €. El exceso (12.700 €) tributa como rendimiento del trabajo personal.",
            "Tributa íntegramente por 19.000 € al tratarse de un cese por causas económicas.",
            "Está exento hasta 180.000 € con independencia de los años de servicio."
        ],
        "correct": 1,
        "justification": "Art. 7.e LIRPF (Práctica 2 de clase): La exención alcanza únicamente a la cuantía fijada con carácter obligatorio en el Estatuto de los Trabajadores (para despido objetivo/ERE: 20 días de salario por año de servicio, prorrateándose por meses los períodos inferiores a un año, con máximo de 12 mensualidades: 20 × 7 × 45 € = 6.300 €). Cualquier cantidad pactada por encima tributa en el IRPF."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "4. [Práctica 3] Por sentencia judicial en un juicio de accidente de tráfico, se indemniza a los herederos del Sr. Martínez con 150.000 € y al Sr. López (lesionado) con 75.000 €. ¿Cómo tributan en el IRPF?",
        "opts": [
            "Ambas indemnizaciones están TOTALMENTE EXENTAS en virtud del artículo 7.d de la LIRPF.",
            "La del Sr. López está exenta, pero la de los herederos del Sr. Martínez tributa en el IRPF como ganancia patrimonial.",
            "La de los herederos tributa en el Impuesto sobre Sucesiones y la del Sr. López en el IRPF.",
            "Ambas tributan como rendimientos del trabajo al 19%."
        ],
        "correct": 0,
        "justification": "Art. 7.d LIRPF (Práctica 3 de clase, nota de Alicia): Las indemnizaciones fijadas judicialmente por daños personales o muerte están EXENTAS en el IRPF. Los herederos perciben la indemnización por derecho propio ('iure proprio') como perjudicados por el daño moral del fallecimiento, por lo que NO forma parte del caudal hereditario ni tributa en el ISD, sino que está exenta en el IRPF por el art. 7.d."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "5. [Práctica 4] Sara percibe del CSIC 1.000 €/mes por beca de tesis doctoral. Su hermana María percibe de la UNIA una beca de 600 € para realizar un curso de 30 horas / 3 créditos sobre entidades no lucrativas. ¿Cuál es su régimen fiscal en el IRPF?",
        "opts": [
            "Ambas becas están totalmente exentas del IRPF.",
            "La beca de Sara está EXENTA (art. 7.j LIRPF), pero la de María NO ESTÁ EXENTA y tributa como rendimiento del trabajo (art. 17.2.h LIRPF).",
            "Ninguna beca está exenta al superar los 500 € mensuales.",
            "La beca de María está exenta por ser universitaria y la de Sara tributa como rendimiento de actividades económicas."
        ],
        "correct": 1,
        "justification": "Art. 7.j LIRPF y art. 2.1 RIRPF (Práctica 4 de clase): La beca predoctoral de formación investigadora de Sara cumple los requisitos de la Ley de la Ciencia y está exenta. La beca de María para un curso de 30 h y 3 créditos no es una enseñanza reglada conducente a la obtención de un título oficial universitario (Grado, Máster o Doctorado), por lo que no cumple el art. 2 RIRPF y tributa como rendimiento del trabajo."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "6. [Práctica 5] El Sr. Sánchez percibe la prestación por desempleo en la modalidad de pago único (30.000 €) para constituir una sociedad laboral con sus compañeros. ¿Cómo tributa?",
        "opts": [
            "Tributa como rendimiento del trabajo personal con una retención del 15%.",
            "Está totalmente EXENTA de tributación en el IRPF (art. 7.n LIRPF) condicionada al mantenimiento de la actividad durante 5 años.",
            "Tributa como ganancia patrimonial no derivada de transmisión.",
            "Está exenta hasta el límite de 15.000 €, tributando el exceso."
        ],
        "correct": 1,
        "justification": "Art. 7.n LIRPF (Práctica 5 de clase): Las prestaciones por desempleo percibidas en la modalidad de pago único están totalmente exentas en el IRPF, con el requisito de que se mantenga la acción o participación y la actividad durante al menos 5 años."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "7. [Práctica 6] Dña. Francisca Guzmán recibe 6.500 € anuales de pensión por alimentos de sus hijos satisfecha por su exmarido por sentencia de divorcio. ¿Cómo tributa en el IRPF de Dña. Francisca?",
        "opts": [
            "Tributa como rendimiento del trabajo en la base general de Dña. Francisca.",
            "Está totalmente EXENTA de tributación en el IRPF (art. 7.k LIRPF) tanto para la madre como para los hijos.",
            "Tributa como rendimiento del capital mobiliario.",
            "Tributa en el Impuesto sobre Donaciones."
        ],
        "correct": 1,
        "justification": "Art. 7.k LIRPF (Práctica 6 de clase): Las anualidades por alimentos percibidas de los padres en virtud de decisión judicial están totalmente EXENTAS en el IRPF."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "8. [Práctica 7] D. Braulio (29 años) reside gratuitamente en un piso (VC = 50.000 € no revisado) propiedad de su padre, sin mediar contrato ni pago alguno. ¿Qué rendimiento debe declarar el padre en su IRPF?",
        "opts": [
            "Debe declarar un rendimiento de capital inmobiliario igual al valor de mercado (800 €/mes = 9.600 €) por el art. 24.",
            "Debe declarar IMPUTACIÓN DE RENTAS INMOBILIARIAS (art. 85 LIRPF) por el 2% del Valor Catastral: 2% × 50.000 € = 1.000 €.",
            "No debe declarar nada porque entre padres e hijos no hay hecho imponible.",
            "Debe declarar una ganancia de patrimonio de 9.600 €."
        ],
        "correct": 1,
        "justification": "Art. 85 LIRPF (solución oficial de clase, corrección de Alicia): Al ser una cesión totalmente gratuita (no hay arrendamiento), NO aplica el art. 24 (que exige la existencia de un arrendamiento a un familiar). Por tanto, para el propietario se considera un inmueble urbano a su disposición y tributa por Imputación de Rentas del art. 85: 2% × 50.000 € = 1.000 €."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "9. [Práctica 8] D. Álvaro Molina se desplaza en septiembre a Burgos durante 7 días (6 noches) en su vehículo particular (900 km ida y vuelta). Percibe 1.000 € de dietas de manutención y 234 € de locomoción. Justifica factura de hotel por 350 €. ¿Cuánto tributa por dietas?",
        "opts": [
            "Tributan 653,29 € por exceso de manutención (exento: 6 × 53,34 € + 1 × 26,67 € = 346,71 €) y 0 € por locomoción (exento 900 km × 0,26 € = 234 €).",
            "Tributan los 1.234 € íntegros.",
            "Está todo exento por haber pernoctado en hotel.",
            "Tributan 500 € en concepto de retribución en especie."
        ],
        "correct": 0,
        "justification": "Art. 9 RIRPF (Práctica 8 de clase): Manutención exenta: 6 días con pernocta × 53,34 € (320,04 €) + 1 día sin pernocta (vuelta) × 26,67 € = 346,71 €. De los 1.000 € abonados, el exceso tributable es 1.000 € - 346,71 € = 653,29 €. Locomoción: 900 km × 0,26 €/km = 234 € justificados -> 100% exentos."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "10. [Práctica 9] D. Alberto (22 años) recibe un curso de marketing pagado por su empresa (1.000 €) y otro curso de Golf (2.000 €). ¿Cómo computan en su IRPF?",
        "opts": [
            "Ambos cursos son retribuciones en especie sujetas a ingreso a cuenta.",
            "El curso de marketing es un supuesto NO SUJETO por formación profesional requerida por el puesto (art. 42.2.a LIRPF), y el curso de golf tributa íntegramente como retribución en especie.",
            "Ambos cursos están exentos por el art. 42.3.",
            "El curso de marketing tributa como retribución dineraria y el de golf no computa."
        ],
        "correct": 1,
        "justification": "Art. 42.2.a LIRPF (Práctica 9 de clase): No tienen la consideración de rendimientos de trabajo en especie los gastos de estudio y formación dispuestos por el empleador exigidos por el desarrollo de sus actividades o las características de los puestos de trabajo. El curso de golf es para fines particulares del trabajador, por lo que constituye retribución en especie."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "11. [Práctica 11] Un trabajador con salario de 25.000 €/año (68,49 €/día) y 3 años de antigüedad es despedido de forma improcedente percibiendo 12.000 € de indemnización acordada en el SMAC. ¿Cuánto tributa?",
        "opts": [
            "Tributan 12.000 € íntegros como rendimiento del trabajo ordinario.",
            "Exento el límite legal (33 días × 3 años × 68,49 € = 6.780,51 €). El exceso (5.219,49 €) tributa con reducción del 30% por irregularidad (art. 18.2), computándose por 3.653,64 €.",
            "Los 12.000 € están totalmente exentos al no superar 180.000 €.",
            "Tributa únicamente una cuota fija de retención del 2%."
        ],
        "correct": 1,
        "justification": "Art. 7.e LIRPF y art. 18.2 LIRPF (solución oficial de clase, aviso de Alicia frente al error de Ismael): Límite legal obligatorio ET: 33 días × 3 años × (25.000/365) = 6.780,51 € exentos. Exceso sobre el límite legal: 12.000 € - 6.780,51 € = 5.219,49 €. Al cobrarse en un único pago derivado de extinción laboral con período de generación superior a 2 años, se le aplica la reducción del 30% del art. 18.2 LIRPF: 5.219,49 € × 70% = 3.653,64 € de rendimiento computable."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "12. [Práctica 12] Una empresa cede gratuitamente a un directivo para su uso particular una vivienda propiedad de la empresa cuyo Valor Catastral es de 120.000 € (revisado en los últimos 10 años). Las demás retribuciones íntegras del directivo ascienden a 70.000 €. ¿Cuál es la valoración de la renta en especie?",
        "opts": [
            "6.000 € (5% del Valor Catastral revisado), al no superar el límite del 10% de las demás contraprestaciones de trabajo (7.000 €).",
            "12.000 € (10% del Valor Catastral).",
            "7.000 € por aplicación del tope máximo.",
            "El valor de mercado del alquiler en la zona."
        ],
        "correct": 0,
        "justification": "Art. 43.1.1ª.a LIRPF (Práctica 12 de clase): La utilización o disfrute de vivienda propiedad del pagador se valora en el 10% del valor catastral, o en el 5% si el valor catastral ha sido revisado en los últimos 10 períodos impositivos (5% de 120.000 € = 6.000 €). Dicha valoración no puede superar el límite del 10% de las restantes contraprestaciones del trabajo (10% de 70.000 € = 7.000 €). Como 6.000 € ≤ 7.000 €, la valoración es de 6.000 €."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "13. [Práctica 13] Un propietario alquila una vivienda habitual por 800 €/mes (9.600 €/año). Soporta intereses de hipoteca de 6.000 € y gastos de reparación de caldera de 5.000 €. Sabiendo que los gastos del art. 23.1.a tienen como tope los rendimientos íntegros:",
        "opts": [
            "Deduce los 11.000 € íntegros, generando un rendimiento neto negativo de -1.400 €.",
            "Deduce por intereses y reparación como máximo 9.600 € (dejando el saldo previo en 0 €) y el exceso de 1.400 € puede compensarlo en los 4 años siguientes.",
            "Solo puede deducir los intereses de hipoteca, pero no la reparación de la caldera.",
            "Pierde el derecho a deducir el exceso de 1.400 € definitivamente."
        ],
        "correct": 1,
        "justification": "Art. 23.1.a LIRPF (regla de oro de capital inmobiliario): Los gastos de financiación (intereses) y los gastos de reparación y conservación tienen un límite conjunto: no pueden exceder de la cuantía de los rendimientos íntegros obtenidos de cada inmueble. El exceso no deducido en el año (1.400 €) se puede deducir en los 4 años inmediatos siguientes."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "14. [Práctica 14] En un piso alquilado, el arrendador realiza obras de instalación de aire acondicionado centralizado y cerramiento de terraza por importe de 8.000 €. ¿Cómo se computan estos gastos en el IRPF?",
        "opts": [
            "Son gastos de conservación y reparación deducibles al 100% en el ejercicio.",
            "Son gastos de MEJORA: no son deducibles directamente en el ejercicio, sino que se incorporan al valor de adquisición del inmueble para amortizarse al 3% anual.",
            "Son gastos no deducibles que no producen ningún efecto fiscal.",
            "Dan derecho a una deducción directa en cuota del 20%."
        ],
        "correct": 1,
        "justification": "Art. 23.1.a y 23.1.b LIRPF: Las obras de mejora o ampliación aumentan la capacidad o habitabilidad del inmueble y no son gastos de conservación del año; se consideran mayor valor de adquisición del inmueble y se recuperan vía amortización anual del 3% (o del 10% si se trata de instalaciones muebles independientes)."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "15. [Práctica 15] D. Carlos alquila un piso a su hermana (parentesco hasta tercer grado) por un precio simbólico de 100 €/mes (1.200 €/año). El Valor Catastral es de 80.000 € (revisado). Tras deducir gastos reales, el rendimiento neto resulta ser de 300 €. Según el artículo 24 de la LIRPF:",
        "opts": [
            "El rendimiento neto computable será de 300 € al haberse justificado los gastos.",
            "El rendimiento neto computable no podrá ser inferior al 1,1% del Valor Catastral: 1,1% × 80.000 € = 880 €.",
            "Debe tributar por el valor de mercado del alquiler en esa zona (600 €/mes = 7.200 €).",
            "El contrato se considera nulo a efectos tributarios."
        ],
        "correct": 1,
        "justification": "Art. 24 LIRPF (regla especial de parentesco hasta 3.er grado): Cuando el adquirente, cesionario o arrendatario sea el cónyuge o un pariente hasta el tercer grado inclusive, el rendimiento neto total no podrá ser inferior al que resulte de las reglas del artículo 85 (Imputación de rentas: 2% o 1,1% del VC). Como 880 € > 300 €, el rendimiento a computar es 880 €."
    },
    {
        "tema": "Casos Prácticos 1-16",
        "caseId": "casos-clase-irpf",
        "caseTitle": "Casos Prácticos 1 a 16: Seminario Oficial de Clase",
        "caseStatement": statement_clase,
        "q": "16. [Práctica 16] Un contribuyente es propietario de una segunda residencia en la playa (Valor Catastral revisado hace 3 años = 90.000 €) y de una plaza de garaje en otra calle comprada independientemente (Valor Catastral no revisado = 15.000 €), ambos vacíos todo el año. ¿Qué importe debe declarar por imputación de rentas (art. 85 LIRPF)?",
        "opts": [
            "0 €, porque los inmuebles desocupados no producen rendimientos.",
            "1.290 € en total: 990 € por la vivienda (1,1% de 90.000 €) y 300 € por el garaje (2% de 15.000 €).",
            "2.100 € aplicando el 2% a ambos bienes.",
            "1.290 € menos los recibos del IBI pagados durante el año."
        ],
        "correct": 1,
        "justification": "Art. 85 LIRPF (Práctica 16 de clase): La imputación de rentas inmobiliarias se calcula: para la vivienda con VC revisado en los últimos 10 años, al 1,1% (1,1% × 90.000 € = 990 €); para el garaje no afecto con VC no revisado, al 2% (2% × 15.000 € = 300 €). Suma total = 1.290 €. En la imputación de rentas NO se admite la deducción de ningún tipo de gasto."
    }
]

all_supuestos_items = simulacro_items + questions_2019 + questions_2020 + questions_clase

supuestos_payload = {
    "subject": "ade/derecho-fiscal",
    "type": "test",
    "title": "Examen Online por Supuestos (Enunciados + Test)",
    "description": "Simulador de examen online oficial: enunciado del caso en grande arriba y preguntas tipo test debajo (Simulacro 9 Nov, Exámenes Oficiales 2019/2020 y Prácticas 1 a 16).",
    "order": 2,
    "items": all_supuestos_items
}

with open(existing_supuestos_path, 'w', encoding='utf-8') as f:
    json.dump(supuestos_payload, f, ensure_ascii=False, indent=2)

print(f"Updated supuestos-examen.json: {len(all_supuestos_items)} questions total across 4 exam cases.")
