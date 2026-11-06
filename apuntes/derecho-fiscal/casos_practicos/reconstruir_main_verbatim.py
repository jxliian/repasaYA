import os

latex_doc = r"""\documentclass[11pt,a4paper,openany]{article}
\input{../estilo_fiscal.tex}

\begin{document}

% ------------------------------------------------------------------------------
% PORTADA INSTITUCIONAL
% ------------------------------------------------------------------------------
\begin{titlepage}
    \centering
    \vspace*{1.2cm}
    
    {\Huge\textbf{\textsf{\color{fiscalPrimary}DERECHO FISCAL}}\par}
    \vspace{0.35cm}
    {\Large\textbf{\textsf{\color{fiscalAccent}CASOS PRÁCTICOS OFICIALES RESUELTOS (1 A 16)}}\par}
    \vspace{0.5cm}
    {\large\textsf{Facultad de Ciencias Económicas y Empresariales --- Universidad de Granada}\par}
    \vspace{0.25cm}
    {\normalsize\textsf{Grado en ADE $\cdot$ Doble Grado DADE / FICO $\cdot$ Curso 2026--2027}\par}
    
    \vspace{1.2cm}
    
    \begin{tcolorbox}[
        enhanced,
        colback=fiscalLight,
        colframe=fiscalPrimary,
        arc=4pt,
        boxrule=1.5pt,
        width=0.96\textwidth,
        halign=center
    ]
        \vspace{0.2cm}
        {\large\bfseries\color{fiscalDark}ENUNCIADOS ÍNTEGROS VERBATIM Y RESOLUCIÓN OFICIAL}\\[0.3cm]
        \normalsize
        \begin{itemize}[leftmargin=1.5cm,itemsep=3pt]
            \item \textbf{Bloque 1: Contribuyentes y Residencia} (Práctica 1).
            \item \textbf{Bloque 2: Sujeción, No Sujeción y Exenciones} (Prácticas 2 a 7: despidos, accidentes, becas, desempleo en pago único, calificación global y cesión gratuita).
            \item \textbf{Bloque 3: Rendimientos del Trabajo Personal} (Prácticas 8 a 12: dietas, cursos, vales comida, planes de pensiones, especie de vehículo y vivienda, despidos improcedentes y empleada de hogar).
            \item \textbf{Bloque 4: Capital Inmobiliario e Imputación de Rentas} (Prácticas 13 a 16: arrendamientos a familiares, locales, cesión de traspaso, alquileres vacacionales y reducción del 90\% en zonas tensionadas).
        \end{itemize}
        \vspace{0.2cm}
        \textbf{\color{fiscalAccent}Enunciados Verbatim 100\% $\cdot$ Resoluciones de Pizarra $\cdot$ Artículos LIRPF $\cdot$ Sin Palabrería}
        \vspace{0.2cm}
    \end{tcolorbox}
    
    \vfill
    {\footnotesize\textsf{\color{gray}repasaYA $\cdot$ Material docente de máxima fidelidad para examen $\cdot$ Noviembre 2026}\par}
\end{titlepage}

\newpage
\tableofcontents
\newpage

% ==============================================================================
% BLOQUE 1: CONTRIBUYENTES
% ==============================================================================
\section{Bloque 1: Contribuyentes y Residencia Habitual (Práctica 1)}

\subsection{Práctica Nº 1: Condición de Contribuyente en el IRPF y Residencia Habitual}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Determinar la condición o no de contribuyentes en el IRPF de las siguientes personas, según cada una de sus situaciones personales:
\begin{enumerate}[label=\textbf{\alph*.}]
    \item D. José, español, soltero, con vivienda habitual en Madrid, trabaja para una sucursal de una empresa colombiana en España. Durante el ejercicio 2026 ha realizado varios viajes a Colombia, por un total de 290 días. Dispone de copias de los billetes de avión, visados en el pasaporte y contrato de alquiler de una vivienda en Bogotá, donde residió durante sus estancias en Colombia.
    \item D. Antonio, natural de Granada, trabaja y reside habitualmente en Alemania desde hace 2 años. Su mujer e hijos siguen viviendo en Granada. D. Antonio aporta como prueba su contrato de trabajo con la empresa alemana y un contrato de arrendamiento de una vivienda en ese país.
    \item Un deportista profesional español pasa un total de 100 días en España. El resto viaja y entrena según los diferentes torneos en los que participa. Se sabe que sus padres residen habitualmente en España y que tiene una vivienda en nuestro país.
\end{enumerate}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}[label=\alph*.]
    \item \textbf{D. José:}
    \begin{itemize}
        \item \textit{Criterio temporal (Art.~9.1.a LIRPF):} Permaneció 290 días en Colombia, por lo que residió en España únicamente $365 - 290 = 75\text{ días} < 183\text{ días}$. No cumple el criterio de permanencia continuada.
        \item \textit{Criterio del núcleo económico (Art.~9.1.b LIRPF):} Trabaja para la sucursal en España y mantiene su vivienda habitual en Madrid. Salvo que acredite residencia fiscal en Colombia mediante un certificado de residencia fiscal emitido por la autoridad tributaria colombiana (DIAN) al amparo del Convenio de Doble Imposición (CDI España-Colombia), la Administración tributaria española presumirá su residencia en España por centro de intereses económicos.
    \end{itemize}
    
    \item \textbf{D. Antonio:}
    \begin{itemize}
        \item \textit{Presunción por núcleo familiar (Art.~9.1 párr.~3º LIRPF):} Aunque resida y trabaje en Alemania, al residir legalmente en Granada su cónyuge no separado legalmente y sus hijos menores de edad dependientes, opera la presunción legal de que D. Antonio mantiene su residencia habitual en España.
        \item \textit{Prueba en contrario:} Se trata de una presunción \textit{iuris tantum}. Al aportar contrato de trabajo indefinido y vivienda habitual en Alemania por más de 2 años, puede destruir la presunción y tributar en Alemania, salvo que no acredite certificado de residencia fiscal de la Hacienda alemana.
    \end{itemize}
    
    \item \textbf{Deportista profesional:}
    \begin{itemize}
        \item Permanece en España 100 días ($< 183\text{ días}$). Los padres no generan presunción legal (el Art.~9.1 solo incluye cónyuge e hijos menores).
        \item Sin embargo, según el Art.~9.1.a, para computar el período de permanencia se consideran ausencias esporádicas las salidas al extranjero que no acrediten residencia fiscal en otro país. Si el deportista no demuestra que tiene residencia fiscal en un tercer país, las estancias en torneos se computan como ausencias temporales y computa como residente en territorio español.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Conclusiones Directas]
\textbf{a)} No residente si acredita certificado fiscal en Colombia; si no, residente por centro económico $\cdot$ \textbf{b)} Residente por presunción de cónyuge e hijos, salvo certificado fiscal alemán $\cdot$ \textbf{c)} Residente por ausencias esporádicas.
\end{resultadoBox}

\vspace{0.4cm}

% ==============================================================================
% BLOQUE 2: SUJECIÓN, NO SUJECIÓN Y EXENCIONES
% ==============================================================================
\section{Bloque 2: Sujeción, No Sujeción y Exenciones (Prácticas 2 a 7)}

\subsection{Práctica Nº 2: Sujeción, No Sujeción y Exenciones en Indemnizaciones Laborales}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item El Sr. López ve extinguida su relacion laboral como consecuencia de su cese por causas económicas y en virtud de un expediente de regulación de empleo autorizado el día 15 de mayo de 2026. Su salario en la empresa hasta esa fecha era de 45\euro{}/día y ha trabajado en ella durante 7 años. Recibe una indemnización de 19.000 \euro{}.
    
    Qué ocurriría si el Sr. López, en virtud de su contrato recibe, 45 días de salario por año de servicio en virtud de su contrato, siendo la causa del cese de la relación laboral una modificación sustancial de su horario de trabajo que redunda en su perjuicio.
    
    \item En mayo de 2026, el Sr. Gálvez recibió una indemnización por despido, reconocido como improcedente ante el Servicio de Mediación y Arbitraje y Conciliación (SMAC) por importe de 100.000 \euro{}, igualmente percibió dos indemnizaciones de 2.000 \euro{}, respectivamente, por vulneración de derechos fundamentales que fueron satisfechas por la empresa en la que trabajaba y por su jefe. Dichas indemnizaciones constan en el acta de conciliación del Área de Mediación, Arbitraje y Conciliación perteneciente a la Dirección General de Trabajo de la Comunidad de Madrid.
\end{enumerate}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{Caso Sr. López:}
    \begin{itemize}
        \item \textit{Despido colectivo por causas económicas (ERE / Art.~51 ET):} El límite obligatorio por ley (Estatuto de los Trabajadores) es de 20 días de salario por año de servicio, con un máximo de 12 mensualidades:
        $$\text{Límite legal exento} = 20\text{ días} \times 7\text{ años} \times 45\text{ \euro/día} = \mathbf{6.300,00\text{ \euro}}$$
        $$\text{Tope 12 mensualidades} = 12 \times 30 \times 45 = 16.200\text{ \euro} \implies 6.300,00 \le 16.200\text{ \euro}$$
        $$\text{Importe sujeto} = 19.000,00 - 6.300,00 = \mathbf{12.700,00\text{ \euro}}$$
        Al haberse generado en 7 años ($>2$ años), aplica reducción del 30\% por irregularidad (Art.~18.2 LIRPF):
        $$\text{Rendimiento Neto Sujeto} = 12.700,00 \times 0,70 = \mathbf{8.890,00\text{ \euro}}$$
        
        \item \textit{Variante: Modificación sustancial de condiciones (Art.~41 ET):}
        El Estatuto fija 20 días/año con máximo de 9 mensualidades ($9 \times 30 \times 45 = 12.150\text{ \euro}$). Los 45 días pactados por contrato por encima del límite legal están sujetos al IRPF.
    \end{itemize}
    
    \item \textbf{Caso Sr. Gálvez:}
    \begin{itemize}
        \item \textit{Despido improcedente en conciliación (SMAC):} Al formalizarse en sede del SMAC, cumple el requisito del Art.~7.e LIRPF. Límite exento: 33 días por año trabajado, con tope absoluto de $180.000\text{ \euro}$. Como $100.000\text{ \euro} \le 180.000\text{ \euro}$ y dentro de la escala legal, está \textbf{totalmente exenta}.
        \item \textit{Indemnizaciones por vulneración de derechos fundamentales ($2 \times 2.000\text{ \euro} = 4.000\text{ \euro}$):} Están exentas (Art.~7.d LIRPF) por acordarse en acto de conciliación administrativa ante la autoridad laboral competente.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Sr. López: Exento = \textbf{6.300,00 \euro} $\cdot$ Rendimiento sujeto = \textbf{8.890,00 \euro} $\cdot$ Sr. Gálvez: \textbf{100\% Exento}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 3: Accidente de Tráfico y Seguros de Vida Gananciales}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Como consecuencia de un accidente de automóvil en el que viajaban el Sr. Martínez y el Sr. López, el primero resultó muerto y el segundo con distintos daños físicos. En el juicio se condenó a la parte contraria a indemnizar a los herederos del Sr. Martínez con 150.000 \euro{} y al Sr. López con 75.000 \euro{}. Además, la viuda del Sr. Martínez recibe una prestación de 250.000 \euro{}, derivada de un contrato de seguro de vida con primas a cargo de la sociedad de gananciales.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Indemnización a herederos del Sr. Martínez ($150.000\text{ \euro}$):}
    Fijada judicialmente por daños personales. \textbf{Totalmente exenta} en el IRPF (Art.~7.d LIRPF).
    
    \item \textbf{Indemnización al Sr. López ($75.000\text{ \euro}$):}
    Fijada judicialmente por daños corporales sufridos en accidente. \textbf{Totalmente exenta} en el IRPF (Art.~7.d LIRPF).
    
    \item \textbf{Seguro de vida de la viuda ($250.000\text{ \euro}$, primas gananciales):}
    \begin{itemize}
        \item \textit{50\% correspondiente al causante ($125.000\text{ \euro}$):} Contratante distinto de beneficiario (contratante el marido con fondos de la sociedad de gananciales, beneficiaria la viuda). Tributa en el \textbf{Impuesto sobre Sucesiones y Donaciones (ISD)}, no en el IRPF (Art.~6.4 LIRPF).
        \item \textit{50\% pagado con fondos propios de la viuda ($125.000\text{ \euro}$):} Coincide tomador y beneficiario. Tributa en el \textbf{IRPF} como Rendimiento del Capital Mobiliario (RCM / Art.~25.3 LIRPF) en la base imponible del ahorro.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Indemnizaciones judiciales = \textbf{Exentas (0,00 \euro)} $\cdot$ Seguro: \textbf{125.000 \euro{} al ISD} y \textbf{125.000 \euro{} a RCM (IRPF)}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 4: Tratamiento de Becas de Investigación y Estudio}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Sara García, licenciada en Medicina está escribiendo su tesis doctoral en el CSIC. Esta institución le ha concedido una beca para personal investigador por importe de 1.000 \euro{} al mes. Su hermana, María, es estudiante de 4º curso de Derecho. La Universidad Internacional de Andalucía le concede una beca de investigación para realizar un curso sobre «Tributación de las entidades sin fines lucrativos». La beca exime del pago de la matrícula y del alojamiento (600 euros en total). Dicho curso cubre 3 de créditos y 30 horas lectivas. ¿Cuál es el tratamiento en el IRPF de las beca recibida?
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Sara García (Beca CSIC de 1.000 \euro/mes):}
    Conforme al Art.~7.j LIRPF y Real Decreto 63/2006 (Estatuto del Personal Investigador en Formación), las becas públicas concedidas por entidades sin fines lucrativos o del sector público para investigación y elaboración de tesis doctoral están \textbf{totalmente exentas} en el IRPF.
    
    \item \textbf{María García (Beca curso UNIA de 600 \euro):}
    No se trata de una titulación universitaria oficial reglada ni de un programa de doctorado conducente al grado de doctor, sino de un curso de formación continua / extensión universitaria (3 créditos, 30 horas). Por tanto, no reúne los requisitos del Art.~7.j LIRPF y tributa como \textbf{Rendimiento del Trabajo Personal} por importe de \textbf{600,00 \euro}.
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Sara: \textbf{Totalmente Exenta (0,00 \euro)} $\cdot$ María: \textbf{Sujeta a IRPF (600,00 \euro) como RNT}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 5: Prestación por Desempleo en Pago Único vs. Cobro Periódico}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
El Sr. Sánchez, en situación legal de desempleo, ha constituido una sociedad laboral con un grupo de compañeros de trabajo en su misma situación legal, optando por recibir las prestaciones en la modalidad de pago único establecida en el Real Decreto 1044/1985, de 19 de junio, habiendo percibido en 2026, 30.000 \euro{} por tal concepto.

Piense cómo tributaria la prestación si no se cobrase en la modalidad de pago único.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Modalidad de Pago Único (Art.~7.n LIRPF):}
    Las prestaciones por desempleo percibidas en la modalidad de pago único para incorporarse como socio trabajador a cooperativas o sociedades laborales, o como autónomo, están \textbf{100\% exentas de IRPF sin límite de importe}.
    Requisito de permanencia: el beneficiario debe mantener la actividad o la condición de socio trabajador durante al menos 5 años; si se incumple dicho plazo, deberá reintegrar la exención.
    
    \item \textbf{Cobro Periódico Mensual:}
    Si la prestación se percibe de forma fraccionada mes a mes, se califica como \textbf{Rendimiento Íntegro del Trabajo Personal (RITP)} sujeto y no exento (Art.~17.1.b LIRPF).
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Pago único constituido en sociedad laboral = \textbf{Totalmente Exento (0,00 \euro)}. Cobro mensual = \textbf{Sujeto a IRPF}.
\end{resultadoBox}

\newpage

\subsection{Práctica Nº 6: Calificación e Integración Global de Rentas (Dña. Francisca Guzmán)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Dña. Francisca Guzmán, abogada de profesión, está empleada por el Bufete “HH, S.L” como abogada, percibiendo 4.500 \euro{} mensuales, más una paga extraordinaria. En el año 2025, decidió dedicarse al ejercicio libre de su profesión, haciéndose autónoma y llevando algunos temas. Este año 2026, sólo ha percibido unos ingresos de 3.000 \euro{}. Sus gastos han sido de 3.100 \euro{}.

Es propietaria de un piso que constituye su vivienda habitual, con un valor catastral de 59.000 \euro{} y cuyo coste de adquisión fue de 85.000 \euro{}.

Tiene acciones por los que recibió dividendos por 2.000 \euro{}, de los que 1.000 \euro{} se corresponden a dividendos exigibles o devengados en 2025 pero abonados en 2026.

En diciembre de 2026, vendió por 10.000 \euro{} un terreno rústico, heredado de sus padres en el año 2000 y valorado en el Impuesto sobre Sucesiones y Donaciones por 6.000 \euro{}.

En mayo, recibe unas acciones en herencia de una tía sin hijos. Las acciones cotizan en Bolsa y tienen un valor de mercado de 300.000 \euro{}.

Por último, se sabe también que resultó premiada en el Sorteo de Loteria de Navidad con 20.000 \euro{}.

Dña. Francisca está divorciada y tiene dos hijos de un matrimonio anterior, de los que tiene la guardia y custodia, por los que recibe una pensión por alimentos de 6.500 \euro{} anuales.

\textbf{Se pide:} Determinar los distintos componentes de la renta obtenida por Dña. Francisca en 2026 y precisar que impuestos directos podrían gravar a Dña. Francisca en ese mismo ejercicio 2026.
\end{enunciadoBox}

\begin{solucionBox}[Desglose de Liquidación y Bases Imponibles]
\textbf{1. Componentes de la Renta en el IRPF (2026):}
\begin{enumerate}[label=\alph*.]
    \item \textbf{Rendimientos del Trabajo:} $13 \text{ pagas} \times 4.500 = \mathbf{58.500,00\text{ \euro}}$ (Base Imponible General).
    \item \textbf{Actividad Económica:} $3.000 - 3.100 = \mathbf{-100,00\text{ \euro}}$ (Rendimiento neto negativo compensable en BIG).
    \item \textbf{Vivienda habitual:} Exenta de imputación de rentas inmobiliarias (Art.~85.1 LIRPF: $\mathbf{0,00\text{ \euro}}$).
    \item \textbf{Rendimientos del Capital Mobiliario:} De los $2.000\text{ \euro}$, solo $1.000\text{ \euro}$ son devengados en 2026 y se integran en la Base Imponible del Ahorro. Los otros $1.000\text{ \euro}$ devengados en 2025 debieron declararse en 2025: $\mathbf{1.000,00\text{ \euro}}$ (BIA).
    \item \textbf{Ganancia patrimonial terreno rústico:} $10.000 - 6.000 = \mathbf{4.000,00\text{ \euro}}$ (Base Imponible del Ahorro).
    \item \textbf{Acciones heredadas en mayo ($300.000\text{ \euro}$):} No sujeta al IRPF (Art.~6.4 LIRPF).
    \item \textbf{Lotería de Navidad ($20.000\text{ \euro}$):} Exenta del Gravamen Especial de Loterías (límite exento $40.000\text{ \euro}$, Disposición Adicional 33ª LIRPF).
    \item \textbf{Pensión por alimentos para hijos ($6.500\text{ \euro}$):} Exenta en el IRPF de los hijos (Art.~7.k LIRPF) y no computable como ingreso de Dña. Francisca.
\end{enumerate}

\textbf{2. Impuestos Directos que gravan a Dña. Francisca en 2026:}
\begin{itemize}
    \item \textbf{IRPF:} Por rendimientos del trabajo, actividad económica, capital mobiliario y ganancia patrimonial.
    \item \textbf{Impuesto sobre Sucesiones y Donaciones (ISD):} Por la herencia mortis causa de las acciones de su tía ($300.000\text{ \euro}$, Grupo III de colaterales).
    \item \textbf{Impuesto sobre el Patrimonio (IP):} Se devenga a 31 de diciembre si el patrimonio neto global supera el mínimo exento.
    \item \textit{Nota:} El IIVTNU no grava el terreno rústico por ser exclusivo de terrenos de naturaleza urbana.
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultados Clave]
BIG = $58.500 - 100 = \mathbf{58.400,00\text{ \euro}}$ $\cdot$ BIA = $1.000 + 4.000 = \mathbf{5.000,00\text{ \euro}}$ $\cdot$ ISD = \textbf{300.000 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 7: Cesión Gratuita de Vivienda entre Padre e Hijo (D. Braulio)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Braulio, de 29 años de edad, vive en un piso (valor catastral 50.000 \euro{}) cuyo propietario es su padre que no le cobra ningún tipo de alquiler, no existiendo tampoco ningún tipo de contratato entre ambos que ampare la cesión de la vivivienda. El alquiler de mercado de una vivienda de similares carácterísticas en la zona donde se encuentra la que ocupa D. Braulio es de 800 \euro{} mensuales.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Situación de D. Braulio (Hijo ocupante):}
    No obtiene ningún rendimiento computable en el IRPF. Al no pagar renta ni existir relación laboral o de parentesco con empresa, no tiene retribución en especie ni ganancia patrimonial.
    
    \item \textbf{Situación del Padre (Propietario):}
    \begin{itemize}
        \item \textit{Rendimiento presunto vs. Cesión gratuita:} El Art.~6.5 LIRPF presume retribuidas las prestaciones de bienes y servicios. Sin embargo, al mediar parentesco en línea recta y cesión de vivienda para uso exclusivo sin precio, la jurisprudencia del Tribunal Supremo y el criterio administrativo aplican el régimen de \textbf{Imputación de Rentas Inmobiliarias (Art.~85 LIRPF)}.
        \item \textit{Cálculo de la Imputación (Art.~85 LIRPF):}
        $$\text{Imputación de Rentas} = 1,1\% \times 50.000\text{ \euro} = \mathbf{550,00\text{ \euro}}$$
        \textit{(o $2\%$ si el valor catastral no estuviera revisado en los últimos 10 años $= 1.000,00\text{ \euro}$)}.
        \item El padre \textbf{no puede computar ningún gasto deducible} contra la imputación de rentas.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Hijo (Braulio): \textbf{0,00 \euro} $\cdot$ Padre: Imputación de Rentas Inmobiliarias = \textbf{550,00 \euro} (al 1,1\%).
\end{resultadoBox}

\newpage

% ==============================================================================
% BLOQUE 3: RENDIMIENTOS DEL TRABAJO PERSONAL
% ==============================================================================
\section{Bloque 3: Rendimientos del Trabajo Personal (Prácticas 8 a 12)}

\subsection{Práctica Nº 8: Liquidación de Dietas Complejas y Reducción del Art.~20 (D. Álvaro Molina)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Álvaro Molina, con domicilio en Andújar (Jaén) y soltero, trabaja en una empresa dedicada a la construcción domiciliada en Andujar donde radica el centro de trabajo. La empresa le satisface un sueldo bruto de 20.000 \euro{} (retenciones por 3.325,65 \euro{}) y 1.734 \euro{} por dietas. Las aportaciones a la Seguridad Social han sido de 1.240 \euro{}.

Las dietas por desplazamiento se refieren al traslado del centro de trabajo a otras obras fuera de su municipio. Durante el mes de Marzo (20 días sin pernocta) fue a trabajar a Lucena (Córdoba), por lo que cobró en concepto de dietas la cantidad de 500 \euro{}. El transporte fue abonado directamente por la empresa a RENFE y no tiene justificantes del resto de gastos que el viaje le supuso.

En el mes de septiembre, durante siete días (seis noches) se le envía a efectuar una serie de trabajos a Burgos, habiendo percibido en concepto de dietas la cantidad de 1.000 \euro{}. Justifica debidamente gastos de estancia por importe de 350 \euro{}. La empresa le abona por gastos de locomoción para este traslado 234 \euro{} (distancia Andújar - Burgos 900 Kilómetros) habiendo efectuado el desplazamiento en su vehículo particular.
\end{enunciadoBox}

\begin{solucionBox}[Desglose de Liquidación]
\textbf{1. Viaje de Marzo a Lucena (20 días sin pernocta):}
\begin{itemize}
    \item Transporte: Pagado directamente por la empresa a RENFE $\implies$ \textbf{100\% Exento}.
    \item Manutención sin pernocta: Límite legal $= 20\text{ días} \times 26,67\text{ \euro/día} = \mathbf{533,40\text{ \euro}}$.
    \item Como cobró $500\text{ \euro} \le 533,40\text{ \euro}$, las dietas están \textbf{totalmente exentas (0,00 \euro{})}.
\end{itemize}

\textbf{2. Viaje de Septiembre a Burgos (7 días, 6 noches de pernocta):}
\begin{itemize}
    \item Locomoción en vehículo particular ($900\text{ km}$): Límite legal $= 900 \times 0,26 = \mathbf{234,00\text{ \euro}}$. Percibió $234\text{ \euro} \implies$ \textbf{100\% Exento}.
    \item Estancia con justificante: Factura de hotel por $350\text{ \euro} \implies$ \textbf{Exento}.
    \item Manutención con pernocta (6 noches con pernocta $+$ 1 día sin pernocta):
    $$\text{Límite legal} = (6 \times 53,34) + (1 \times 26,67) = 320,04 + 26,67 = \mathbf{346,71\text{ \euro}}$$
    \item Total exento estancia $+$ manutención $= 350,00 + 346,71 = \mathbf{696,71\text{ \euro}}$.
    \item Como cobró $1.000\text{ \euro}$, el exceso gravado es:
    $$\text{Dietas gravadas} = 1.000,00 - 696,71 = \mathbf{303,29\text{ \euro}}$$
\end{itemize}

\textbf{3. Liquidación del Rendimiento Neto del Trabajo Personal (RNTP):}
\begin{align*}
    \text{RITP (Ingresos)} &= 20.000,00 + 303,29\text{ (dietas)} = \mathbf{20.303,29\text{ \euro}} \\
    \text{Gastos SS (Art.~19.2.a)} &= -\mathbf{1.240,00\text{ \euro}} \\
    \text{Rendimiento Neto Previo} &= 20.303,29 - 1.240,00 = \mathbf{19.063,29\text{ \euro}}
\end{align*}
\begin{itemize}
    \item \textit{Reducción del Art.~20 LIRPF (solución oficial de clase):} Al situarse el rendimiento neto previo por debajo de $19.747,50\text{ \euro}$, le corresponde la reducción legal por obtención de rendimientos del trabajo calculada en clase en \textbf{780,00 \euro}.
    \item \textit{Otros gastos generales a tanto alzado (Art.~19.2.f):} $-\mathbf{2.000,00\text{ \euro}}$.
\end{itemize}
$$\text{Rendimiento Neto Reducido} = 19.063,29 - 780,00 - 2.000,00 = \mathbf{16.283,29\text{ \euro}}$$
\end{solucionBox}

\begin{resultadoBox}[Resultados Clave para el Test]
Dietas gravadas = \textbf{303,29 \euro} $\cdot$ RNT previo = \textbf{19.063,29 \euro} $\cdot$ RNT reducido = \textbf{16.283,29 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 9: Vales de Comida, Cursos de Empresa y Reducción Art.~20 (D. Alberto)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Alberto, joven de 22 años y residente en Granada, encuentra su primer trabajo en Motril como comercial de equipos de Golf y empieza a trabajar el 1 de febrero. Durante el ejercicio 2026, ha recibido una retribución bruta anual de 11.900 \euro{} más 2.000 por comisiones de ventas. Se le practica una retención del 7 \% (1.287 \euro{}) y la aportación del trabajador a la Seguridad Social es de 986 \euro{}.

Se sabe también que, durante el primer mes de trabajo recibe un curso de marketing pagado por la empresa valorado en 1000 \euro{} y otro de Golf, valorado en 2.000 \euro{}. Durante el año 2026, recibe también 5.000 \euro{} en concepto de dietas de desplazamiento, correspondientes a los 10.000 KM recorridos y los 35 viajes con 1 noche de pernocta cada uno (un día de ida y otro de vuelta) realizados a distintas provincias españolas. Los gastos de alojamiento en los correspondientes hoteles, a razón de 100 \euro{} la noche, fueron reservados y pagados directamente por la empresa a través de su agencia de viajes.

Además, recibiría 200 vales de comida/año por valor de 12 \euro{}/vale. En el ejercicio 2026 ha percibido la parte proporcional, 180 vales.

\textbf{Determinar el rendimiento del trabajo de D. Alberto.}
\end{enunciadoBox}

\begin{solucionBox}[Desglose de Liquidación]
\begin{enumerate}
    \item \textbf{Cursos de formación:} El curso de marketing está no sujeto (Art.~42.2.a LIRPF: actualización profesional requerida por el puesto). El curso de golf tributa como retribución en especie si no se considera formación laboral.
    \item \textbf{Dietas de viaje:} Límite exento $= 10.000 \times 0,26 + 35 \times (53,34 + 26,67) = 2.600 + 2.800,35 = \mathbf{5.400,35\text{ \euro}}$. Como cobró $5.000\text{ \euro} \le 5.400,35\text{ \euro}$, están \textbf{100\% exentas}.
    \item \textbf{Vales de comida:} Límite exento $= 11\text{ \euro/día}$. Exceso sujeto $= 180 \times (12 - 11) = 180\text{ \euro}$. Añadiendo el ingreso a cuenta del $7\%$ no repercutido: $180 + (7\% \times 180) = 180 + 12,60 = \mathbf{192,60\text{ \euro}}$.
    \item \textbf{Cálculo del Rendimiento Neto Reducido (solución oficial de clase):}
    \begin{align*}
        \text{RITP} &= 11.900 + 2.000 + 192,60 = \mathbf{14.092,60\text{ \euro}} \\
        \text{RN Previo} &= 14.092,60 - 986\text{ (SS)} = \mathbf{13.106,60\text{ \euro}} \\
        \text{Reducción Art.~20} &= -\mathbf{7.302,00\text{ \euro}} \quad \text{\small(Tope por base $\le 14.852$)} \\
        \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
        \text{RNTP Reducido} &= 13.106,60 - 7.302,00 - 2.000,00 = \mathbf{3.804,60\text{ \euro}}
    \end{align*}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial]
Rendimiento Neto del Trabajo Reducido = \textbf{3.804,60 \euro}.
\end{resultadoBox}

\newpage

\subsection{Práctica Nº 10: Planes de Pensiones de Empresa y Bajas Voluntarias}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Antonio, de 66 años, casado con Dña. Ana de 60, en régimen de gananciales, trabaja como Director Comercial de una fábrica de pinturas situada en Granada, recibe una retribución bruta de 25.000 \euro{} anuales, de las que se le retraen 3.750 \euro{} en concepto de retenciones (15\%) y 1.725 \euro{} por aportación obligatoria a la SS.

En 2025, como premio de antigüedad de 25 años en la empresa, le son entregadas acciones de la sociedad para la que trabaja, que ascienden al 0.5\% del capital social, y que están valoradas en 5.000 \euro{} en el momento de la entrega. Asimismo, la empresa realiza una aportación a su plan de pensiones de 2.500 \euro{} y contrata un seguro médico por 450 \euro{} anuales.

La empresa pone a su disposición para sus desplazamientos comerciales un vehículo Citroën valorado en 35.000 \euro{}. Por su parte, el D. Antonio realiza una aportación de 250 \euro{} al sindicato de trabajadores al que pertenece desde hace 20 años.

Dña. Ana ha trabajado 20 años en una empresa de tejidos y decide solicitar voluntariamente la rescisión de su contrato laboral por razones de salud, llegando a un acuerdo con la empresa por el que se le pagan 18.000 \euro{}. Hasta la fecha había recibido unas retribuciones íntegras por 10.000 \euro{} ( Seguridad Social 600 y retenciones por 1.500 \euro{}).

\textbf{Determinar el rendimiento del trabajo.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución de Clase]
\textbf{1. Rendimientos de D. Antonio:}
\begin{itemize}[leftmargin=*]
    \item \textit{Sueldo íntegro dinerario:} $25.000,00\text{ \euro}$.
    \item \textit{Entrega de acciones de la propia empresa ($5.000\text{ \euro}$):} Cumple los requisitos del Art.~42.3.f LIRPF (participación $<5\%$, entrega a trabajadores en activo, valor $\le 12.000\text{ \euro}$). Está \textbf{totalmente exenta}.
    \item \textit{Plan de pensiones empresa ($2.500\text{ \euro}$):} Se integra como rendimiento del trabajo en especie pero \textbf{sin ingreso a cuenta} (Art.~102.2 RIRPF).
    \item \textit{Seguro médico ($450\text{ \euro}$):} Exento al no superar $500\text{ \euro/año}$ (Art.~42.3.c LIRPF).
    \item \textit{Vehículo Citroën ($35.000\text{ \euro}$):} Al estar puesto a su disposición para desplazamientos comerciales sin uso privado, está afecto 100\% a la actividad laboral $\implies$ \textbf{No genera retribución en especie}.
    \item \textit{RITP Total Antonio:} $25.000 + 2.500 = \mathbf{27.500,00\text{ \euro}}$.
    \item \textit{Gastos deducibles:} SS ($1.725\text{ \euro}$) $+$ Cuota sindical ($250\text{ \euro}$, Art.~19.2.d) $+$ Otros gastos ($2.000\text{ \euro}$) $= \mathbf{3.975,00\text{ \euro}}$.
    \item \textbf{RNTP Antonio:} $27.500,00 - 3.975,00 = \mathbf{23.525,00\text{ \euro}}$.
\end{itemize}

\textbf{2. Rendimientos de Dña. Ana:}
\begin{itemize}[leftmargin=*]
    \item \textit{Indemnización por baja voluntaria ($18.000\text{ \euro}$):} Al ser rescisión voluntaria, \textbf{no está exenta} por el Art.~7.e LIRPF (solo despidos forzosos u obligatorios por el ET).
    \item \textit{Reducción del 30\% por irregularidad (Art.~18.2 LIRPF):} Al haberse generado en un período superior a dos años (20 años trabajados), aplica la reducción del 30\%:
    $$\text{Importe computable} = 18.000 \times (1 - 0,30) = 18.000 \times 0,70 = \mathbf{12.600,00\text{ \euro}}$$
    \item \textit{Retribuciones previas:} $10.000,00\text{ \euro}$.
    \item \textit{RITP Total Ana:} $10.000 + 12.600 = \mathbf{22.600,00\text{ \euro}}$.
    \item \textit{Gastos deducibles:} SS ($600\text{ \euro}$) $+$ Otros gastos ($2.000\text{ \euro}$) $= \mathbf{2.600,00\text{ \euro}}$.
    \item \textbf{RNTP Ana:} $22.600,00 - 2.600,00 = \mathbf{20.000,00\text{ \euro}}$.
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
RNTP D. Antonio = \textbf{23.525,00 \euro} $\cdot$ RNTP Dña. Ana = \textbf{20.000,00 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 11: Despido, Especie de Vehículo y Movilidad Geográfica}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
El Sr. A estaba contratado en Granada como arquitecto técnico en una tienda de diseño de interiores con un sueldo bruto de 25.000 \euro{} anuales. El 31/01/2026, tras tres años de trabajo, es despedido de la empresa en la que trabajaba, siendo calificado el despido como despido improcedente por resolución judicial. Se le abonan los siguientes conceptos: 2.083 \euro{} en concepto de salarios devengado hasta la fecha del despido; 1.000 \euro{} por salarios de tramitación; y 12.000 \euro{} de indemnización. Ha satisfecho una cuota anual de colegiación (obligatoria) de 300 \euro{}.

Las aportaciones a la SS ascienden a 142 \euro{} y su retención del 15\%.

Durante los meses de mayo a julio recibe 2.000 \euro{} de la prestación por desempleo. El 01/07/2026 es contratado en Málaga por la empresa VHF en las siguientes condiciones: 14.000 \euro{} anuales; 750 \euro{}, alta SS; seguro médico para él y su cónyuge de 300 \euro{} anuales cada uno y un vehículo Ford Focus para su uso personal con un precio de adquisición de 13.000 \euro{}. En 2026 recibe la parte proporcional al tiempo trabajado y se le practica una retención del 12\%.

\textbf{Determinar el rendimiento del trabajo.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Extinción del primer empleo en Granada (despido improcedente judicial):}
    \begin{itemize}
        \item Salarios devengados: $2.083,00\text{ \euro}$.
        \item Salarios de tramitación: $1.000,00\text{ \euro}$ (plenamente sujetos a IRPF).
        \item Límite exento de indemnización (33 días/año):
        $$\text{Salario diario} = \frac{25.000}{365} = 68,49\text{ \euro/día} \implies 33 \times 3 \times 68,49 = \mathbf{6.780,82\text{ \euro}}$$
        \item Exceso sujeto con reducción del 30\% por irregularidad ($>2$ años):
        $$(12.000,00 - 6.780,82) \times 0,70 = 5.219,18 \times 0,70 = \mathbf{3.653,43\text{ \euro}}$$
    \end{itemize}

    \item \textbf{Prestación por desempleo (mayo a julio):} $2.000,00\text{ \euro}$ (RITP ordinario).

    \item \textbf{Segundo empleo en Málaga (VHF, 6 meses):}
    \begin{itemize}
        \item Sueldo dinerario (6 meses): $14.000 / 2 = 7.000,00\text{ \euro}$.
        \item Seguro médico ($300 + 300 = 600\text{ \euro/año} \implies 300\text{ \euro}$ en 6 meses): \textbf{Exento} por ser $\le 500\text{ \euro}$ por persona (Art.~42.3.c LIRPF).
        \item Vehículo Ford Focus uso personal (6 meses):
        $$\text{Valoración en especie} = 20\% \times 13.000 \times \frac{6}{12} = \mathbf{1.300,00\text{ \euro}}$$
        Ingreso a cuenta ($12\%$ no repercutido): $1.300 + (12\% \times 1.300) = 1.300 + 156 = \mathbf{1.456,00\text{ \euro}}$.
    \end{itemize}

    \item \textbf{RITP Total:} $2.083 + 1.000 + 3.653,43 + 2.000 + 7.000 + 1.456 = \mathbf{17.192,43\text{ \euro}}$.

    \item \textbf{Gastos deducibles:}
    \begin{itemize}
        \item Seguridad Social: $142 + 750 = 892,00\text{ \euro}$.
        \item Cuota colegio profesional obligatorio: $300,00\text{ \euro}$ (límite $500\text{ \euro}$, Art.~19.2.d).
        \item Gastos generales a tanto alzado: $2.000,00\text{ \euro}$.
        \item \textbf{Gasto adicional por movilidad geográfica (Art.~19.2.f):} $+2.000,00\text{ \euro}$ por aceptar empleo en un nuevo municipio (Málaga) estando desempleado.
        \item Total gastos deducibles $= 892 + 300 + 2.000 + 2.000 = \mathbf{5.192,00\text{ \euro}}$.
    \end{itemize}
    $$\mathbf{\text{RNTP}} = 17.192,43 - 5.192,00 = \mathbf{12.000,43\text{ \euro}}$$
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial]
Rendimiento Neto del Trabajo Personal = \textbf{12.000,43 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 12: Empleada de Hogar y Obligación de Declarar}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Una empleada de hogar, dada de alta en el régimen correspondiente de la Seguridad Social (siendo el importe de gasto en Seguridad Social de 1.100 \euro{}) gana 20.000 \euro{} anuales. Determinar su rendimiento neto del trabajo personal. Determinar si tendría que presentar la declaración del IRPF.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}
    \item \textbf{Liquidación del Rendimiento Neto del Trabajo Personal (RNTP):}
    \begin{align*}
        \text{RITP (Salario bruto)} &= \mathbf{20.000,00\text{ \euro}} \\
        \text{Gastos deducibles SS} &= -\mathbf{1.100,00\text{ \euro}} \\
        \text{Rendimiento Neto Previo} &= 20.000,00 - 1.100,00 = \mathbf{18.900,00\text{ \euro}} \\
        \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
        \text{Reducción Art.~20 (bajos ingresos)} &= -\mathbf{1.047,38\text{ \euro}} \\
        \text{RNTP Reducido} &= 18.900,00 - 2.000,00 - 1.047,38 = \mathbf{15.852,62\text{ \euro}}
    \end{align*}

    \item \textbf{Obligación formal de declarar (Art.~96 LIRPF):}
    \begin{itemize}
        \item En el Régimen Especial de Empleados de Hogar, el empleador es una persona física que no actúa como retenedor fiscal (no existe retención a cuenta del IRPF).
        \item Cuando el pagador no está obligado a retener, el límite legal para no declarar baja de $22.000\text{ \euro}$ al límite reducido de \textbf{15.876 \euro} (o $15.000\text{ \euro}$ según ejercicio).
        \item Como la trabajadora percibe $20.000\text{ \euro} > 15.876\text{ \euro}$, \textbf{SÍ TIENE OBLIGACIÓN FORMAL DE PRESENTAR DECLARACIÓN DEL IRPF}.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
RNTP = \textbf{15.852,62 \euro} $\cdot$ Obligación de declarar: \textbf{SÍ ESTÁ OBLIGADA} (pagador no obligado a retener).
\end{resultadoBox}

\newpage

% ==============================================================================
% BLOQUE 4: CAPITAL INMOBILIARIO E IMPUTACIÓN DE RENTAS
% ==============================================================================
\section{Bloque 4: Capital Inmobiliario e Imputación de Rentas (Prácticas 13 a 16)}

\subsection{Práctica Nº 13: Arrendamiento a Sobrino (Art.~24) y Local 6 Meses Alquilado}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Juan, residente en Barcelona, posee tres inmuebles:
\begin{enumerate}[label=\textbf{\alph*.}]
    \item Un piso en Granada, adquirido en 1993 por 70.000 \euro{} y un valor catastral revisado de 90.000 \euro{} (valor del suelo 40.000).
    \item Un piso en Madrid, heredado de sus padres, y cuya propiedad comparte con su hermana al 50\%. Su adquisición fue valorada en 150.000 \euro{} y su valor catastral revisado es de 200.000 \euro{} (valor del suelo 80.000 \euro{}). Está arrendado al hijo (39 años) de su hermana por 500 \euro{} mensuales. Los gastos de comunidad son 2100 \euro{} anuales y el IBI 600 \euro{}, que pagan los propietarios.
    \item Un local comercial alquilado a una Compañía de Seguros por 1200 \euro{}/mes. Los gastos de comunidad son 25 \euro{}/mes y el IBI 800 \euro{} anuales, ambos a cargo del inquilino. El valor de adquisición fue de 300.000 \euro{} en el año 2000 y su valor catastral revisado de 190.000 \euro{} (valor del suelo 90.000 \euro{}). Por acuerdo de arrendador y arrendatario, se rescinde el contrato el 30 de junio de 2026, siendo los gastos jurídicos de la rescisión del contrato de 100 \euro{}. D. Juan no encuentra nuevo arrendatario hasta el febrero de 2027, cobrándose 1.300 \euro{} al mes desde el día 1 de dicho mes.
\end{enumerate}
\textbf{Calcular estos rendimientos a efectos del IRPF.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Piso en Granada (Imputación de Rentas Inmobiliarias, Art.~85):}
    Inmueble urbano vacío todo el año a disposición de su propietario:
    $$\text{IRI} = 1,1\% \times 90.000,00 = \mathbf{990,00\text{ \euro}}$$

    \item \textbf{Piso en Madrid (50\% titularidad de Juan, Arrendado a familiar, Art.~24):}
    \begin{itemize}
        \item Ingresos computables a Juan ($50\%$): $500 \times 12 \times 50\% = 3.000,00\text{ \euro}$.
        \item Gastos de Juan ($50\%$): Comunidad ($1.050\text{ \euro}$) $+$ IBI ($300\text{ \euro}$) $+$ Amortización ($50\%$):
        $$\text{Amortización construcción} = 3\% \times \frac{120.000}{200.000} \times 200.000 \times 50\% = 3\% \times 60.000 = 1.800,00\text{ \euro}$$
        $$\text{Gastos totales} = 1.050 + 300 + 1.800 = 3.150,00\text{ \euro}$$
        $$\text{Rendimiento Real Calculado} = 3.000,00 - 3.150,00 = -150,00\text{ \euro}$$
        \item \textbf{Regla del Rendimiento Mínimo en Caso de Parentesco (Art.~24 LIRPF):} Al ser el arrendatario pariente hasta el tercer grado (sobrino), el rendimiento neto total no puede ser inferior a la imputación de rentas del Art.~85:
        $$\text{Mínimo legal} = 1,1\% \times 200.000 \times 50\% = \mathbf{1.100,00\text{ \euro}}$$
        $$\mathbf{\text{RNCI Computable}} = \max(-150, 1.100) = \mathbf{1.100,00\text{ \euro}}$$
    \end{itemize}

    \item \textbf{Local comercial (6 meses arrendado + 6 meses vacío):}
    \begin{itemize}
        \item \textit{Rendimiento de Capital Inmobiliario (6 meses alquilado):}
        $$\text{Ingresos} = 1.200 \times 6 = 7.200,00\text{ \euro}$$
        Gastos asumidos por Juan: rescisión ($100\text{ \euro}$) $+$ amortización de 6 meses:
        $$\text{Amortización} = 3\% \times \left(300.000 \times \frac{100.000}{190.000}\right) \times \frac{6}{12} = 3\% \times 157.894,74 \times \frac{6}{12} = 2.368,42\text{ \euro}$$
        $$\text{Gastos deducibles} = 100,00 + 2.368,42 = 2.468,42\text{ \euro}$$
        $$\mathbf{\text{RNCI Local (6 meses)}} = 7.200,00 - 2.468,42 = \mathbf{4.731,58\text{ \euro}}$$
        \item \textit{Imputación de Rentas Inmobiliarias (6 meses a disposición, Art.~85):}
        $$\mathbf{\text{IRI Local (6 meses)}} = 1,1\% \times 190.000 \times \frac{6}{12} = \mathbf{1.045,00\text{ \euro}}$$
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Granada: IRI = \textbf{990,00 \euro} $\cdot$ Madrid: RNCI = \textbf{1.100,00 \euro} $\cdot$ Local: RNCI = \textbf{4.731,58 \euro} e IRI = \textbf{1.045,00 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 14: Arrendamiento de Local Comercial y Cesión de Traspaso}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
El Sr. Álvarez tiene un local de negocio arrendado (valor de adquisición 500.000 \euro{} y valor del suelo 200.000) desde el 1- Enero por el que cobra al mes la cantidad de 1.250 \euro{} más el correspondiente IVA. El 1-Agosto la arrendataria traspasa el derecho de arrendamiento a otra persona por 50.000 \euro{}, quien continúa pagando la mensualidad al Sr. Álvarez incrementada en un 15 por ciento. El IBI correspondiente al ejercicio es de 750 \euro{}.

\textbf{Calcular la incidencia de dicha operación en el IRPF.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución]
\begin{itemize}[leftmargin=*]
    \item \textbf{Tributación del Traspaso:}
    El precio del traspaso ($50.000,00\text{ \euro}$) es una ganancia patrimonial exclusiva de la \textbf{antigua arrendataria} (Art.~33.1 LIRPF). El Sr. Álvarez no percibe participación en el traspaso, por lo que no tributa por esos $50.000\text{ \euro}$.
    
    \item \textbf{Rendimientos de Capital Inmobiliario del Sr. Álvarez:}
    \begin{itemize}
        \item Enero a julio (7 meses): $7 \times 1.250 = 8.750,00\text{ \euro}$.
        \item Agosto a diciembre (5 meses a $+15\%$): $1.250 \times 1,15 = 1.437,50\text{ \euro/mes} \implies 5 \times 1.437,50 = 7.187,50\text{ \euro}$.
        \item Ingresos íntegros anuales $= 8.750,00 + 7.187,50 = \mathbf{15.937,50\text{ \euro}}$.
        \item Gastos deducibles: IBI ($750\text{ \euro}$) $+$ Amortización de la construcción ($300.000\text{ \euro}$):
        $$\text{Amortización} = 3\% \times (500.000 - 200.000) = 3\% \times 300.000 = \mathbf{9.000,00\text{ \euro}}$$
        $$\text{Total gastos deducibles} = 750,00 + 9.000,00 = \mathbf{9.750,00\text{ \euro}}$$
        $$\mathbf{\text{RNCI}} = 15.937,50 - 9.750,00 = \mathbf{6.187,50\text{ \euro}}$$
    \end{itemize}
    \item Al ser arrendamiento de local de negocio, \textbf{no aplica ninguna reducción} por vivienda habitual.
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial]
Rendimiento Neto del Capital Inmobiliario = \textbf{6.187,50 \euro} (Traspaso tributa en la inquilina).
\end{resultadoBox}

\newpage

\subsection{Práctica Nº 15: Finca Rústica en Especie y Apartamento de Verano}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
La Sra. D posee:
\begin{itemize}[leftmargin=1.5em]
    \item una finca de pastos que arrienda en 2022 a un ganadero durante cinco años. Se establece que como precio que se entregarán diez vacas adultas al fin del contrato. En 2026, se entregan las vacas, valoradas en 1.500 \euro{} cada una.
    \item un apartamento en la playa (Valor catastral revisado 80.000 \euro{}, correspondiendo al suelo un 30\%; valor de adquisición 90.000 \euro{}) que ha arrendado los meses de julio y agosto, por lo que ha obtenido 3.000 euros, disfrutando del apartamento el resto del año. De esta forma obtienen recursos para hacer frente a los gastos que consisten en 1200 euros de intereses por un préstamo solicitado para su compra, el recibo del IBI anual de 380 euros, el seguro por 400 euros y los gastos de mantenimiento que ese año han sido de 1.780 euros, ya que han tenido que pintarlo. Además, y para evitar los problemas de gestión en la búsqueda de inquilino se ha servido de la ayuda de una plataforma online que le ha cobrado 60 \euro{}.
\end{itemize}
\end{enunciadoBox}

\begin{solucionBox}[Resolución]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Finca de pastos (RNCI):}
    \begin{itemize}
        \item Ingreso íntegro $= 10 \times 1.500\text{ \euro} = 15.000,00\text{ \euro}$.
        \item Al haberse generado en un período superior a dos años (arrendamiento de 5 años cobrado al final), resulta aplicable la \textbf{reducción del 30\% por irregularidad} (Art.~23.3 LIRPF):
        $$\mathbf{\text{RNCI Finca}} = 15.000,00 \times (1 - 0,30) = 15.000 \times 0,70 = \mathbf{10.500,00\text{ \euro}}$$
    \end{itemize}

    \item \textbf{Apartamento en la playa alquilado (2 meses, RNCI):}
    \begin{itemize}
        \item Ingresos íntegros $= 3.000,00\text{ \euro}$.
        \item Gastos de la plataforma online: afectos al 100\% al arrendamiento $= 60,00\text{ \euro}$.
        \item Amortización anual (mayor entre coste $90.000$ y VC $80.000$, con $70\%$ construcción):
        $$\text{Amortización anual} = 3\% \times (90.000 \times 0,70) = 3\% \times 63.000 = 1.890,00\text{ \euro}$$
        \item Prorrateo de gastos anuales a $2/12$ (julio y agosto):
        $$\text{Gastos prorrateados} = \frac{2}{12} \times [1.200 + 1.780 + 380 + 400 + 1.890] = \frac{2}{12} \times 5.650 = 941,67\text{ \euro}$$
        $$\text{Total gastos deducibles} = 60,00 + 941,67 = \mathbf{1.001,67\text{ \euro}}$$
        $$\mathbf{\text{RNCI}} = 3.000,00 - 1.001,67 = \mathbf{1.998,33\text{ \euro}}$$
        \textit{(Sin reducción: el alquiler de temporada/vacaciones no tiene reducción por vivienda habitual)}.
    \end{itemize}

    \item \textbf{Apartamento en la playa vacío (10 meses, Imputación de Rentas Art.~85):}
    $$\mathbf{\text{IRI}} = 1,1\% \times 80.000 \times \frac{10}{12} = \mathbf{733,33\text{ \euro}}$$
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Finca = \textbf{10.500,00 \euro} $\cdot$ Playa alquilado = \textbf{1.998,33 \euro} $\cdot$ Playa vacío = \textbf{733,33 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 16: Usufructo y Arrendamiento en Zona Tensionada (Reducción 90\%)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
La Sra. Gómez adquirió el usufructo vitalicio, por la herencia de su marido, de dos viviendas:
\begin{enumerate}[label=\textbf{\alph*)}]
    \item Una vivienda cuyo valor de adquisición es de 60.000 \euro{} (VC 120.000 \euro{}, valor suelo 30.000 \euro{}) destinada a su vivienda habitual. Ha pagado las siguientes cantidades en relación a la vivienda:
    \begin{itemize}
        \item Gastos de Comunidad: 900 \euro{}.
        \item IBI: 470 \euro{}.
        \item Pintura de la vivienda: 625 \euro{}.
    \end{itemize}
    \item Un apartamento amueblado en una zona céntrica de la capital calificada como situada en zona de mercado residencial tensionado que tiene alquilado y por el que cobra una renta anual de 7.200 \euro{} (VC 120.000 \euro{}, valor suelo 30.000 \euro{}). Al vencimiento del contrato, el 30 de junio de 2025, renegocia las condiciones con el inquilino, pasando a cobrarle una renta de 6.800 \euro{}. La renta percibida hasta el vencimiento del contrato fue la proporcional al contrato anterior. Ha pagado las siguientes cantidades en relación a la vivienda:
    \begin{itemize}
        \item Gastos de Comunidad: 700 \euro{}.
        \item IBI: 370 \euro{}.
        \item Mobiliario: 2.000 \euro{}.
    \end{itemize}
\end{enumerate}
\textbf{Liquidar dichos rendimientos en el IRPF.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Vivienda habitual:} No genera rentas ni imputación inmobiliaria (Art.~85.1 LIRPF: $\mathbf{0,00\text{ \euro}}$). Los gastos no son deducibles.
    
    \item \textbf{Apartamento alquilado (Ley 12/2023 de Vivienda):}
    \begin{itemize}
        \item Ingresos íntegros $= (600 \times 6) + (566,67 \times 6) = 3.600 + 3.400 = \mathbf{7.000,00\text{ \euro}}$.
        \item Gastos deducibles $= 700\text{ (comunidad)} + 370\text{ (IBI)} + 10\% \times 2.000\text{ (amortización muebles)} = \mathbf{1.270,00\text{ \euro}}$.
        \item Rendimiento neto previo $= 7.000,00 - 1.270,00 = \mathbf{5.730,00\text{ \euro}}$.
        \item \textbf{Aplicación de la reducción del 90\% (Art.~23.2.a LIRPF):} Al estar ubicado en zona de mercado residencial tensionado y pactarse una rebaja superior al 5\% sobre la renta del contrato anterior ($400\text{ \euro/año} > 5\% \times 7.200 = 360\text{ \euro}$), aplica la reducción máxima del 90\%:
        $$\mathbf{\text{RNCI Reducido}} = 5.730,00 \times (1 - 0,90) = 5.730,00 \times 0,10 = \mathbf{573,00\text{ \euro}}$$
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial]
Rendimiento Neto del Capital Inmobiliario Reducido = \textbf{573,00 \euro}.
\end{resultadoBox}

\end{document}
"""

with open('apuntes/derecho-fiscal/casos_practicos/main.tex', 'w', encoding='utf-8') as f:
    f.write(latex_doc)

print("Escrito main.tex con enunciados 100% verbatim.")
