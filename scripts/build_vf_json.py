import json
import os

materials_dir = "/home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/content/materials/ade/derecho-fiscal"
target_file = os.path.join(materials_dir, "vf.json")

vf_questions = [
    # Tema 1: Conceptos tributarios y LGT
    {
        "n": 1,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "Las tasas son tributos en los que no existe ninguna actividad administrativa dirigida individualmente al sujeto pasivo.",
        "answer": "F",
        "justification": "Falso: El hecho imponible de las tasas consiste precisamente en la utilización privativa del dominio público o en la prestación de servicios en régimen de derecho público dirigidos individualmente al obligado (art. 2.2.a LGT)."
    },
    {
        "n": 2,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El importe global recaudado por una tasa no puede superar el coste real o previsible del servicio público prestado.",
        "answer": "V",
        "justification": "Verdadero: Rige el principio de equivalencia (art. 7 Ley de Tasas y Precios Públicos), que limita el importe conjunto de las tasas al coste del servicio."
    },
    {
        "n": 3,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "En las contribuciones especiales, la base imponible puede alcanzar hasta el 100% del coste de las obras públicas ejecutadas por la entidad local.",
        "answer": "F",
        "justification": "Falso: El artículo 31 del TRLRHL fija un límite máximo del 90% del coste de la obra o establecimiento del servicio para la base imponible de las contribuciones especiales."
    },
    {
        "n": 4,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "Las sanciones tributarias pecuniarias forman parte de la deuda tributaria junto a los intereses de demora y recargos.",
        "answer": "F",
        "justification": "Falso: El artículo 58.3 de la LGT establece de forma terminante que 'las sanciones tributarias no formarán parte de la deuda tributaria en ningún caso'."
    },
    {
        "n": 5,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El plazo general de prescripción de las obligaciones tributarias en la LGT es de cuatro años.",
        "answer": "V",
        "justification": "Verdadero: El artículo 66 de la LGT fija con carácter general en 4 años la prescripción de los derechos de liquidar, recaudar y solicitar devoluciones."
    },
    {
        "n": 6,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El Impuesto sobre Construcciones, Instalaciones y Obras (ICIO) es un impuesto municipal directo y de obligatoria exacción por los ayuntamientos.",
        "answer": "F",
        "justification": "Falso: El ICIO es de carácter potestativo (voluntario mediante ordenanza fiscal) y es el único impuesto municipal de naturaleza indirecta (arts. 59 y 100 TRLRHL)."
    },
    {
        "n": 7,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El sustituto del contribuyente es un sujeto pasivo que por ley ocupa el lugar del contribuyente en el cumplimiento de la obligación tributaria principal y formal.",
        "answer": "V",
        "justification": "Verdadero: Conforme al artículo 36.3 de la LGT, el sustituto desplaza al contribuyente en la relación tributaria, teniendo derecho legal de reembolso frente a este."
    },
    {
        "n": 8,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El retenedor de IRPF tiene la consideración jurídica de sustituto del contribuyente según la LGT.",
        "answer": "F",
        "justification": "Falso: El retenedor es un obligado tributario específico de realizar pagos a cuenta (art. 35.2.f LGT), no es sustituto del contribuyente en la obligación principal."
    },
    {
        "n": 9,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "El devengo y la exigibilidad de la cuota tributaria coinciden obligatoriamente en el mismo instante temporal en todos los impuestos.",
        "answer": "F",
        "justification": "Falso: El devengo marca el nacimiento de la obligación tributaria, pero la exigibilidad puede diferirse por la ley a un momento posterior (por ejemplo, el plazo de presentación de la autoliquidación, art. 21 LGT)."
    },
    {
        "n": 10,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "Los tributos con fines no fiscales o extrafiscales tienen por objeto disuadir o incentivar conductas, como la protección del medio ambiente o la salud pública.",
        "answer": "V",
        "justification": "Verdadero: El artículo 2.1 de la LGT reconoce expresamente que los tributos, además de ser medios para obtener recursos públicos, pueden servir como instrumentos de política económica y responder a fines extrafiscales."
    },
    {
        "n": 11,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "Los tres impuestos municipales de exacción obligatoria son el IBI, el IAE y el IVTM, y los tres son de naturaleza directa.",
        "answer": "V",
        "justification": "Verdadero: El artículo 59.1 del TRLRHL establece que IBI, IAE e IVTM son los tres impuestos obligatorios para todos los consistorios y todos son directos."
    },
    {
        "n": 12,
        "tema": "Tema 1: Conceptos Tributarios y LGT",
        "q": "La Cuota Líquida de un tributo se obtiene restando las retenciones y pagos a cuenta a la Cuota Íntegra.",
        "answer": "F",
        "justification": "Falso: A la Cuota Íntegra se le restan las deducciones y bonificaciones para obtener la Cuota Líquida. Al restar los pagos a cuenta a la Cuota Líquida se obtiene la Cuota Diferencial (art. 56 LGT)."
    },

    # IRPF: Residencia, Hecho Imponible y Exenciones
    {
        "n": 13,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Un ciudadano español que pase 250 días en el extranjero sin obtener certificado de residencia fiscal de otro país se considera contribuyente del IRPF español.",
        "answer": "V",
        "justification": "Verdadero: Art. 9.1.a LIRPF: Los días de ausencia se computan como ausencias esporádicas salvo que se acredite residencia fiscal en otro país mediante certificado de la autoridad fiscal de dicho estado."
    },
    {
        "n": 14,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Si un contribuyente traslada su residencia a un paraíso fiscal, pierde automáticamente la condición de contribuyente del IRPF español desde el primer día.",
        "answer": "F",
        "justification": "Falso: El artículo 8.2 de la LIRPF establece la cuarentena fiscal: sigue siendo contribuyente español en el período del cambio y durante los cuatro períodos impositivos siguientes (total 5 años)."
    },
    {
        "n": 15,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "La indemnización por despido improcedente acordada en conciliación laboral está exenta en el IRPF con el límite de la cuantía fijada en el Estatuto de los Trabajadores y tope máximo absoluto de 180.000 €.",
        "answer": "V",
        "justification": "Verdadero: Art. 7.e LIRPF: Exención de la cuantía legal obligatoria del Estatuto de los Trabajadores (33 días/año, máx 24 mensualidades) con tope de 180.000 €."
    },
    {
        "n": 16,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Si un convenio colectivo pacta una indemnización por despido superior a la establecida en el Estatuto de los Trabajadores, el exceso también está exento de IRPF.",
        "answer": "F",
        "justification": "Falso: El artículo 7.e de la LIRPF delimita la exención exclusivamente a la cuantía fijada con carácter obligatorio en el Estatuto de los Trabajadores. Cualquier mejora por convenio o pacto tributa en el IRPF."
    },
    {
        "n": 17,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Las indemnizaciones por muerte o lesiones corporales fijadas por sentencia judicial están totalmente exentas en el IRPF para los herederos o perjudicados.",
        "answer": "V",
        "justification": "Verdadero: Art. 7.d LIRPF: Están exentas las indemnizaciones como consecuencia de responsabilidad civil por daños personales en la cuantía legal o judicialmente reconocida."
    },
    {
        "n": 18,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Una beca de 600 € percibida por un estudiante universitario para realizar un curso de verano no reglado de 30 horas está totalmente exenta de IRPF.",
        "answer": "F",
        "justification": "Falso: El artículo 2 del RIRPF exige que la beca sea para cursar estudios reglados del sistema educativo conducentes a títulos oficiales (Grado, Máster, Doctorado). Los cursos no reglados no están exentos y tributan como rendimiento del trabajo (art. 17.2.h LIRPF)."
    },
    {
        "n": 19,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "La prestación por desempleo percibida en la modalidad de pago único para iniciar una actividad como socio trabajador está 100% exenta en el IRPF si se mantiene la actividad 5 años.",
        "answer": "V",
        "justification": "Verdadero: Art. 7.n LIRPF: Las prestaciones por desempleo en modalidad de pago único están totalmente exentas con la condición de mantener la actividad durante cinco años."
    },
    {
        "n": 20,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Las anualidades por alimentos percibidas por los hijos de sus progenitores en virtud de sentencia judicial tributan como rendimientos de trabajo en el IRPF de los hijos.",
        "answer": "F",
        "justification": "Falso: El artículo 7.k de la LIRPF declara expresamente exentas las anualidades por alimentos percibidas de los padres en virtud de decisión judicial."
    },
    {
        "n": 21,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "La pensión compensatoria percibida por un cónyuge tras el divorcio está totalmente exenta en el IRPF de quien la cobra.",
        "answer": "F",
        "justification": "Falso: La pensión compensatoria del cónyuge NO está exenta; es un rendimiento del trabajo no sometido a retención para quien la percibe (art. 17.2.f LIRPF), y reduce la base imponible del pagador (art. 55 LIRPF)."
    },
    {
        "n": 22,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Los rendimientos del trabajo obtenidos en el matrimonio en régimen de gananciales se atribuyen al 50% a cada uno de los cónyuges.",
        "answer": "F",
        "justification": "Falso: Art. 11.2 LIRPF: Los rendimientos del trabajo se atribuirán exclusivamente a quien haya generado el derecho a su percepción, con independencia de las normas civiles sobre régimen económico matrimonial."
    },
    {
        "n": 23,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Las prestaciones de maternidad y paternidad abonadas por la Seguridad Social están exentas de tributación en el IRPF.",
        "answer": "V",
        "justification": "Verdadero: El artículo 7.h de la LIRPF recoge expresamente la exención plena de las prestaciones por maternidad y paternidad de la Seguridad Social."
    },
    {
        "n": 24,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "El devengo del IRPF se produce siempre el 31 de diciembre, sin ninguna excepción legal posible.",
        "answer": "F",
        "justification": "Falso: En caso de fallecimiento del contribuyente antes del 31 de diciembre, el período impositivo termina y el impuesto se devenga en la fecha del fallecimiento (art. 13.2 LIRPF)."
    },
    {
        "n": 25,
        "tema": "IRPF: Ámbito, Residencia y Exenciones",
        "q": "Los premios del Sorteo de Lotería de Navidad están exentos en el IRPF hasta un importe de 40.000 € por décimo premiado.",
        "answer": "V",
        "justification": "Verdadero: Disposición Adicional 33ª LIRPF: Los premios de loterías oficiales están exentos del gravamen especial hasta los primeros 40.000 € por décimo; solo tributa al 20% el exceso sobre 40.000 €."
    },

    # IRPF: Rendimientos del Trabajo (RNTP), Rentas en Especie y Dietas
    {
        "n": 26,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "La cuantía exenta por dietas de locomoción con vehículo particular fuera del centro de trabajo es de 0,26 € por kilómetro recorrido.",
        "answer": "V",
        "justification": "Verdadero: Art. 9.A.2.b RIRPF (tras Orden HFP/792/2023): El límite exento de locomoción por kilómetro recorrido en vehículo propio es de 0,26 €/km más gastos justificados de peaje y aparcamiento."
    },
    {
        "n": 27,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "En un viaje de trabajo de varios días con pernocta en España, el último día en que se regresa al municipio de residencia computa a 53,34 € de manutención exenta.",
        "answer": "F",
        "justification": "Falso: El día de regreso ya no se pernocta fuera del municipio habitual, por lo que su límite de manutención exenta es el de desplazamiento sin pernocta: 26,67 € (art. 9.A.3.a RIRPF)."
    },
    {
        "n": 28,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Para desplazamientos en el extranjero con pernocta, el importe exento diario por manutención es de 91,35 €.",
        "answer": "V",
        "justification": "Verdadero: Art. 9.A.3.a RIRPF: La dieta diaria exenta de manutención en el extranjero con pernocta es de 91,35 € (y 48,08 € sin pernocta)."
    },
    {
        "n": 29,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Las primas pagadas por la empresa para el seguro de salud del trabajador están exentas hasta un máximo de 500 € anuales por persona (1.500 € si tiene discapacidad).",
        "answer": "V",
        "justification": "Verdadero: Art. 42.3.c LIRPF: Límite de 500 € al año por asegurado (trabajador, cónyuge o descendientes), elevado a 1.500 € en caso de personas con discapacidad."
    },
    {
        "n": 30,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "La cesión de un vehículo de la empresa a un empleado para su uso exclusivamente particular se valora en el 10% de su valor catastral.",
        "answer": "F",
        "justification": "Falso: Art. 43.1.1ª.b LIRPF: La valoración en especie del uso de vehículos propiedad de la empresa es del 20% anual de su coste de adquisición (no del valor catastral, que solo aplica a inmuebles)."
    },
    {
        "n": 31,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Si la empresa asume el ingreso a cuenta de una retribución en especie y no se lo repercute al trabajador, el ingreso a cuenta se suma a la valoración para calcular el rendimiento íntegro.",
        "answer": "V",
        "justification": "Verdadero: Art. 43.2 LIRPF: Al valor resultante de la retribución en especie se le sumará el ingreso a cuenta no repercutido para obtener el rendimiento íntegro en especie computable."
    },
    {
        "n": 32,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Las cuotas pagadas a Colegios Oficiales son deducibles en el IRPF sin límite cuando la colegiación sea voluntaria.",
        "answer": "F",
        "justification": "Falso: Art. 19.2.d LIRPF y art. 10 RIRPF: Solo son deducibles las cuotas colegiales cuando la colegiación tenga carácter OBLIGATORIO para el desempeño del trabajo, y con un tope máximo de 500 € anuales."
    },
    {
        "n": 33,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Los gastos de defensa jurídica derivados de litigios laborales del trabajador con su empleador son deducibles hasta un máximo de 300 € anuales.",
        "answer": "V",
        "justification": "Verdadero: Art. 19.2.e LIRPF: Son deducibles los gastos de defensa jurídica derivados directamente de litigios suscitados en las relaciones entre el contribuyente y su pagador, con el límite de 300 € anuales."
    },
    {
        "n": 34,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Todos los trabajadores tienen derecho a deducir 2.000 € en concepto de 'otros gastos' del artículo 19.2.f de la LIRPF, con el límite del rendimiento íntegro previo.",
        "answer": "V",
        "justification": "Verdadero: Art. 19.2.f LIRPF: Se establece una deducción general de 2.000 € anuales en concepto de otros gastos distintos de las cotizaciones y cuotas colegiales/sindicales."
    },
    {
        "n": 35,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "La reducción del 30% por rendimientos irregulares del trabajo (art. 18.2 LIRPF) se aplica sin ningún límite cuantitativo máximo sobre el salario recibido.",
        "answer": "F",
        "justification": "Falso: Art. 18.2 LIRPF: La cuantía máxima del rendimiento íntegro sobre la que se aplicará la reducción del 30% no podrá exceder de 300.000 € anuales."
    },
    {
        "n": 36,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Las contribuciones realizadas por la empresa a un Plan de Pensiones a favor del trabajador son rendimientos del trabajo en especie que NO están sujetos a ingreso a cuenta.",
        "answer": "V",
        "justification": "Verdadero: Art. 17.2.a.5ª y art. 102.2 LIRPF: Las contribuciones empresariales imputadas al plan de pensiones son rentas en especie exentas de la obligación de practicar ingreso a cuenta."
    },
    {
        "n": 37,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Los cursos de formación y actualización profesional exigidos por el puesto de trabajo y pagados por el empleador constituyen retribución en especie sujeta a IRPF.",
        "answer": "F",
        "justification": "Falso: Art. 42.2.a LIRPF: Son supuestos de NO SUJECIÓN los gastos de estudio dispuestos por instituciones o empleadores para la actualización, capacitación o reciclaje del personal cuando vengan exigidos por el desarrollo de sus actividades."
    },
    {
        "n": 38,
        "tema": "IRPF: Rendimientos del Trabajo (RNTP)",
        "q": "Los vales restaurante o cheques comedor están exentos en el IRPF hasta un límite de 11 € diarios por día laborable.",
        "answer": "V",
        "justification": "Verdadero: Art. 45 RIRPF: La entrega de vales-comida está exenta con el límite máximo de 11 € diarios por cada día laborable en que se presten servicios."
    },

    # IRPF: Capital Inmobiliario e Imputación de Rentas
    {
        "n": 39,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Los gastos de reparación y de financiación (intereses) de un piso alquilado pueden provocar por sí solos un rendimiento neto de capital inmobiliario negativo en el año.",
        "answer": "F",
        "justification": "Falso: Art. 23.1.a LIRPF: Los intereses y gastos de reparación tienen como límite conjunto el importe de los rendimientos íntegros de ese inmueble (no pueden generar saldo negativo). El exceso se compensa en los 4 años siguientes."
    },
    {
        "n": 40,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "La amortización de un inmueble alquilado (3% anual) se calcula sobre el valor total de compra, incluido el valor del suelo.",
        "answer": "F",
        "justification": "Falso: Art. 23.1.b LIRPF y art. 14 RIRPF: El suelo no se desgasta por el uso y NO es amortizable; el 3% se aplica exclusivamente sobre el valor de la construcción (excluyendo el porcentaje del suelo)."
    },
    {
        "n": 41,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Los muebles y electrodomésticos cedidos conjuntamente en el arrendamiento de una vivienda se pueden amortizar al 10% anual sobre su coste de adquisición.",
        "answer": "V",
        "justification": "Verdadero: Art. 14.1 RIRPF: Los bienes muebles cedidos con el inmueble cumplen el requisito de depreciación efectiva cuando se amortizan al 10% anual sobre su coste."
    },
    {
        "n": 42,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "La reducción por arrendamiento de inmuebles destinados a vivienda habitual para contratos firmados a partir de 2024 (Ley 12/2023) es con carácter general del 50%.",
        "answer": "V",
        "justification": "Verdadero: Art. 23.2 LIRPF: La Ley de Vivienda estableció una reducción general del 50% para nuevos contratos de alquiler de vivienda habitual formalizados desde el 1 de enero de 2024."
    },
    {
        "n": 43,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Un alquiler por temporada para estudiantes durante los 9 meses del curso escolar tiene derecho a la reducción del 50% por arrendamiento de vivienda.",
        "answer": "F",
        "justification": "Falso: Art. 23.2 LIRPF: La reducción solo aplica a arrendamientos destinados a satisfacer la necesidad de vivienda permanente conforme a la LAU. Los contratos de temporada o curso escolar quedan excluidos."
    },
    {
        "n": 44,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Cuando se alquila un piso a un familiar hasta el tercer grado, el rendimiento neto computable no puede ser inferior al resultado de la imputación de rentas del art. 85.",
        "answer": "V",
        "justification": "Verdadero: Art. 24 LIRPF: En caso de parentesco hasta el 3.er grado, el rendimiento neto no podrá ser inferior al 2% o 1,1% del valor catastral del inmueble."
    },
    {
        "n": 45,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Si un padre cede gratuitamente un piso a su hijo sin cobrar ningún alquiler ni existir contrato, el padre debe declarar Imputación de Rentas Inmobiliarias del art. 85.",
        "answer": "V",
        "justification": "Verdadero: Solución oficial de clase (Práctica 7): Al ser cesión gratuita (no hay arrendamiento), no aplica el art. 24 sino el régimen de imputación de rentas del art. 85 (2% o 1,1% del VC)."
    },
    {
        "n": 46,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "Las fincas y parcelas rústicas improductivas a disposición de sus dueños generan una imputación de rentas inmobiliarias del 2% en el IRPF.",
        "answer": "F",
        "justification": "Falso: Art. 85.1 LIRPF (trampa clásica de examen): El régimen de imputación de rentas inmobiliarias solo alcanza a los inmuebles URBANOS. Las fincas rústicas nunca generan imputación de rentas."
    },
    {
        "n": 47,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "El porcentaje de imputación de rentas inmobiliarias es del 1,1% cuando el valor catastral del inmueble urbano ha sido revisado en los últimos 10 períodos impositivos.",
        "answer": "V",
        "justification": "Verdadero: Art. 85.1 LIRPF: Si el valor catastral ha sido revisado o valorado colectivamente en los últimos 10 años, el porcentaje de imputación baja del 2% al 1,1%."
    },
    {
        "n": 48,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "En el cálculo de la Imputación de Rentas Inmobiliarias (art. 85) se pueden deducir los recibos del IBI y los gastos de comunidad.",
        "answer": "F",
        "justification": "Falso: Art. 85 LIRPF: La imputación es una cuantía legal fija (2% o 1,1% del VC) y la ley no admite la deducción de ningún gasto real soportado."
    },
    {
        "n": 49,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "La vivienda habitual del contribuyente y hasta dos plazas de garaje adquiridas conjuntamente con ella están totalmente excluidas de la imputación de rentas del IRPF.",
        "answer": "V",
        "justification": "Verdadero: Art. 85.1 LIRPF: La vivienda habitual y sus anexos o plazas de garaje adquiridas conjuntamente (hasta un máximo de dos) no generan imputación de rentas."
    },
    {
        "n": 50,
        "tema": "IRPF: Rendimientos del Capital Inmobiliario e Imputación",
        "q": "El límite de obligación de declarar por rendimientos de trabajo con un solo pagador es de 22.000 € anuales.",
        "answer": "V",
        "justification": "Verdadero: Art. 96.2.a LIRPF: Los contribuyentes con rendimientos íntegros del trabajo de un único pagador no están obligados a declarar si no superan 22.000 € brutos anuales."
    }
]

vf_payload = {
    "subject": "ade/derecho-fiscal",
    "type": "vf",
    "title": "Verdadero o Falso: Trampas Oficiales de Examen",
    "description": "50 preguntas de V/F centradas en las trampas más habituales de la profesora sobre exenciones, imputaciones, dietas y límites legales con justificación completa.",
    "order": 4,
    "items": vf_questions
}

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(vf_payload, f, ensure_ascii=False, indent=2)

print(f"Created vf.json: {len(vf_questions)} questions.")
