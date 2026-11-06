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
        {\large\bfseries\color{fiscalDark}ENUNCIADOS ÍNTEGROS VERBATIM Y RESOLUCIÓN OFICIAL DE ALICIA}\\[0.3cm]
        \normalsize
        \begin{itemize}[leftmargin=1.5cm,itemsep=3pt]
            \item \textbf{Bloque 1: Contribuyentes y Residencia} (Práctica 1).
            \item \textbf{Bloque 2: Sujeción, No Sujeción y Exenciones} (Prácticas 2 a 7: despidos en ERE a 33 días vs. 20 días, accidentes, becas, desempleo en pago único, calificación global y cesión gratuita).
            \item \textbf{Bloque 3: Rendimientos del Trabajo Personal} (Prácticas 8 a 12: dietas, cursos, vales comida, planes de pensiones, especie de vehículo y vivienda, despidos improcedentes con fórmulas oficiales del Art.~20 y empleada de hogar).
            \item \textbf{Bloque 4: Capital Inmobiliario e Imputación de Rentas} (Prácticas 13 a 16: arrendamientos a familiares con Art.~24, locales con variante de traspaso al 30\%, alquileres vacacionales y reducción del 90\% en zonas tensionadas).
        \end{itemize}
        \vspace{0.2cm}
        \textbf{\color{fiscalAccent}Enunciados Verbatim 100\% $\cdot$ Notas de Pizarra de Alicia $\cdot$ Artículos LIRPF $\cdot$ Sin Palabrería}
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

\begin{solucionBox}[Resolución de Alicia paso a paso]
\begin{enumerate}[label=\alph*.]
    \item \textbf{D. José:} \textbf{SÍ es contribuyente del IRPF.}
    \begin{itemize}
        \item Los 290 días en Colombia son ausencias esporádicas y se suman a los días en España (Art.~9.1.a LIRPF). Para descontarlos necesitaría un certificado de residencia fiscal colombiano; los billetes, visados y contrato de alquiler solo prueban presencia física, no residencia fiscal.
        \item Además, su núcleo principal de intereses económicos está en España (Art.~9.1.b): trabaja para la sucursal española y tiene aquí su vivienda habitual.
        \item Tributa en España por obligación personal por su renta mundial (Art.~2 LIRPF), con posible deducción por doble imposición internacional (Art.~80) o exención del Art.~7.p si cumpliera requisitos.
    \end{itemize}
    
    \item \textbf{D. Antonio:} \textbf{NO es contribuyente del IRPF, si acredita su residencia fiscal en Alemania.}
    \begin{itemize}
        \item Como su cónyuge e hijos menores viven en España, entra en juego la presunción familiar (Art.~9.1 párr.~3º LIRPF). Es una presunción \textit{iuris tantum} que admite prueba en contrario.
        \item Puede destruirla probando que reside en Alemania $>183$ días y que allí están su trabajo y vivienda mediante el certificado de residencia fiscal alemán expedido por la autoridad tributaria alemana. En España solo tributaría por IRNR si obtuviera rentas aquí.
    \end{itemize}
    
    \item \textbf{Deportista profesional:} \textbf{SÍ es contribuyente del IRPF.}
    \begin{itemize}
        \item 100 días en España $+$ 265 días de ausencias esporádicas $= 365\text{ días} > 183\text{ días}$ (Art.~9.1.a). Viajar de torneo en torneo no genera residencia fiscal en ningún otro país.
        \item Que sus padres vivan en España \textbf{no activa la presunción familiar} (solo cuentan cónyuge e hijos menores dependientes). Su vivienda en España refuerza la conexión. Tributa por renta mundial.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Reglas de Examen de Alicia]
\textbf{a)} Estar fuera no basta: se exige certificado de residencia fiscal $\cdot$ \textbf{b)} La presunción familiar se rompe con prueba en contrario $\cdot$ \textbf{c)} Los padres nunca activan la presunción familiar.
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

\begin{solucionBox}[Resolución Corregida de Alicia (Corrige el Error de las Notas del Compañero)]
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{Caso Sr. López:}
    \begin{itemize}
        \item \textbf{Caso principal (ERE por causas económicas, Art.~51 ET):}
        \begin{itemize}
            \item \textit{¡Atención a la regla especial del Art.~7.e párr.~2º LIRPF!:} En despidos colectivos (ERE) y despidos por causas económicas (Art.~52.c ET), el importe exento no es el mínimo de 20 días del ET, sino \textbf{la cuantía establecida para el despido improcedente (33 días/año, máximo 24 mensualidades)}:
            $$\text{Límite exento} = 7\text{ años} \times 33\text{ días} \times 45\text{ \euro/día} = \mathbf{10.395,00\text{ \euro}}$$
            \textit{(No supera las 24 mensualidades $= 32.400\text{ \euro}$ ni el tope absoluto de $180.000\text{ \euro}$)}.
            \item \textit{Importe sujeto:} $19.000,00 - 10.395,00 = \mathbf{8.605,00\text{ \euro}}$ (Rendimiento del trabajo).
            \item \textit{Reducción del 30\% por irregularidad (Art.~18.2 LIRPF):} Generado en 7 años ($>2$ años) y cobrado en pago único:
            $$\text{Reducción 30\%} = 8.605,00 \times 0,30 = \mathbf{2.581,50\text{ \euro}}$$
            $$\mathbf{\text{Rendimiento Computable (BIG)}} = 8.605,00 - 2.581,50 = \mathbf{6.023,50\text{ \euro}}$$
        \end{itemize}
        \textit{\small(Aviso: las notas del compañero usaron erróneamente 20 días/año = 6.300 €; la solución oficial de clase aplica 33 días = 10.395 € exentos)}.
        
        \item \textbf{Variante (Modificación sustancial de condiciones, Art.~41.3 ET):}
        \begin{itemize}
            \item Cuantía legal obligatoria: 20 días de salario por año, máx. 9 mensualidades ($270\text{ días} = 12.150\text{ \euro}$):
            $$\text{Exento legal} = 7\text{ años} \times 20\text{ días} \times 45\text{ \euro/día} = \mathbf{6.300,00\text{ \euro}}$$
            \item Percibido por contrato (45 días/año): $7 \times 45 \times 45 = 14.175,00\text{ \euro}$.
            \item Importe sujeto: $14.175,00 - 6.300,00 = \mathbf{7.875,00\text{ \euro}}$.
            \item Rendimiento computable tras reducción del 30\%: $7.875 \times 0,70 = \mathbf{5.512,50\text{ \euro}}$.
        \end{itemize}
    \end{itemize}
    
    \item \textbf{Caso Sr. Gálvez:}
    \begin{itemize}
        \item \textbf{Indemnización por despido ($100.000\text{ \euro}$):} Reconocido como improcedente en el SMAC (cumple el requisito del Art.~7.e párr.~3º, no se considera pacto). Exenta en la cuantía obligatoria (33 días/año, máx. 24 meses o $180.000\text{ \euro}$). Si el límite legal cubriera los $100.000\text{ \euro}$, estaría totalmente exenta; cualquier exceso tributa como rendimiento del trabajo con reducción del 30\%.
        \item \textbf{Dos indemnizaciones de $2.000\text{ \euro}$ por derechos fundamentales:} \textbf{NO están exentas.} El Art.~7.d LIRPF exige fijación legal o judicial, y el SMAC es un órgano de conciliación administrativa, no un juzgado.
        \begin{itemize}
            \item Los $2.000\text{ \euro}$ pagados por la empresa $\implies$ \textbf{Rendimiento del Trabajo} (derivan de la relación laboral, Art.~17.1).
            \item Los $2.000\text{ \euro}$ pagados por su jefe $\implies$ \textbf{Ganancia Patrimonial no derivada de transmisión a la BIG} (no existe relación laboral con el jefe a título individual).
        \end{itemize}
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Cuadro Resumen de Alicia]
\textbf{ERE}: Exento = \textbf{10.395 \euro} $\cdot$ Computable = \textbf{6.023,50 \euro} $\cdot$ \textbf{Variante Art.~41}: Exento = \textbf{6.300 \euro} $\cdot$ Computable = \textbf{5.512,50 \euro} $\cdot$ \textbf{Gálvez}: 2.000 \euro{} empresa a RNT y 2.000 \euro{} jefe a Ganancia Patrimonial (BIG).
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 3: Accidente de Tráfico y Seguros de Vida Gananciales}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Como consecuencia de un accidente de automóvil en el que viajaban el Sr. Martínez y el Sr. López, el primero resultó muerto y el segundo con distintos daños físicos. En el juicio se condenó a la parte contraria a indemnizar a los herederos del Sr. Martínez con 150.000 \euro{} y al Sr. López con 75.000 \euro{}. Además, la viuda del Sr. Martínez recibe una prestación de 250.000 \euro{}, derivada de un contrato de seguro de vida con primas a cargo de la sociedad de gananciales.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso de Alicia]
\begin{enumerate}
    \item \textbf{Indemnización judicial por muerte a los herederos ($150.000\text{ \euro}$):}
    Exenta de IRPF (Art.~7.d LIRPF) por estar fijada judicialmente por daños corporales.
    
    \item \textbf{Indemnización judicial al Sr. López ($75.000\text{ \euro}$):}
    Exenta de IRPF (Art.~7.d LIRPF) por daños físicos fijados por sentencia judicial.
    
    \item \textbf{Seguro de vida de la viuda ($250.000\text{ \euro}$, primas gananciales):}
    Al pagarse las primas con fondos gananciales, el contrato se financió al 50\% por cada cónyuge:
    \begin{itemize}
        \item \textbf{50\% imputable al marido fallecido ($125.000\text{ \euro}$):} Tomador distinto de beneficiario (contratado por el marido a favor de la viuda). No sujeto al IRPF (Art.~6.4 LIRPF) $\implies$ \textbf{Tributa en el ISD} como adquisición por título sucesorio / seguro de vida.
        \item \textbf{50\% imputable a la viuda ($125.000\text{ \euro}$):} Coinciden tomador y beneficiaria. \textbf{Tributa en el IRPF} como Rendimiento del Capital Mobiliario (Art.~25.3.a LIRPF) en la Base Imponible del Ahorro.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Indemnizaciones de tráfico = \textbf{Exentas (0 \euro)} $\cdot$ Seguro de vida: \textbf{125.000 \euro{} al ISD} y \textbf{125.000 \euro{} a RCM (IRPF, Ahorro)}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 4: Tratamiento de Becas de Investigación y Estudio}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Sara García, licenciada en Medicina está escribiendo su tesis doctoral en el CSIC. Esta institución le ha concedido una beca para personal investigador por importe de 1.000 \euro{} al mes. Su hermana, María, es estudiante de 4º curso de Derecho. La Universidad Internacional de Andalucía le concede una beca de investigación para realizar un curso sobre «Tributación de las entidades sin fines lucrativos». La beca exime del pago de la matrícula y del alojamiento (600 euros en total). Dicho curso cubre 3 de créditos y 30 horas lectivas. ¿Cuál es el tratamiento en el IRPF de las beca recibida?
\end{enunciadoBox}

\begin{solucionBox}[Resolución de Alicia]
\begin{enumerate}
    \item \textbf{Sara García (Beca CSIC de 1.000 \euro/mes):} \textbf{Totalmente Exenta (Art.~7.j LIRPF).}
    Cumple todos los requisitos del RD 63/2006 (Estatuto del Personal Investigador en Formación): concedida por organismo público de investigación (CSIC) para la elaboración de la tesis doctoral.
    
    \item \textbf{María García (Beca curso UNIA de 600 \euro):} \textbf{Sujeta a IRPF como Rendimiento del Trabajo.}
    No está exenta porque no forma parte de estudios universitarios oficiales reglados ni programa de doctorado conducente al título oficial de doctor, sino de un curso de formación continua / extensión universitaria (3 créditos, 30 horas). Tributa como rendimiento íntegro del trabajo por \textbf{600,00 \euro}.
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Sara: \textbf{Exenta (0,00 \euro)} $\cdot$ María: \textbf{Rendimiento del Trabajo Sujeto = 600,00 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 5: Prestación por Desempleo en Pago Único vs. Cobro Periódico}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
El Sr. Sánchez, en situación legal de desempleo, ha constituido una sociedad laboral con un grupo de compañeros de trabajo en su misma situación legal, optando por recibir las prestaciones en la modalidad de pago único establecida en el Real Decreto 1044/1985, de 19 de junio, habiendo percibido en 2026, 30.000 \euro{} por tal concepto.

Piense cómo tributaria la prestación si no se cobrase en la modalidad de pago único.
\end{enunciadoBox}

\begin{solucionBox}[Resolución de Alicia]
\begin{enumerate}
    \item \textbf{Pago Único (Art.~7.n LIRPF):} \textbf{Totalmente Exenta sin límite de cuantía.}
    La prestación por desempleo capitalizada en pago único para incorporarse como socio trabajador a una cooperativa o sociedad laboral, o como autónomo, está 100\% exenta de IRPF. Condición: mantener la actividad/participación durante al menos 5 años.
    
    \item \textbf{Cobro Periódico Mensual:}
    Si se percibe mes a mes, es \textbf{Rendimiento del Trabajo Personal (RITP)} plenamente sujeto (Art.~17.1.b LIRPF) que tributa en la Base Imponible General.
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
Pago único en sociedad laboral = \textbf{Totalmente Exento (0 \euro)} $\cdot$ Cobro mensual = \textbf{RNT Sujeto}.
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

\begin{solucionBox}[Cuadro Oficial de Liquidación de Alicia]
\begin{center}
\small
\begin{tabularx}{\textwidth}{l p{5.5cm} c r}
\toprule
\textbf{Renta Obtenida} & \textbf{Tratamiento Jurídico} & \textbf{Base} & \textbf{Importe} \\
\midrule
Sueldo bufete ($13 \times 4.500$) & Rendimiento del trabajo (Art.~17.1) & General & $58.500,00\text{ \euro}$ \\
Ejercicio libre ($3.000 - 3.100$) & Actividades económicas (Art.~27) & General & $-100,00\text{ \euro}$ \\
Vivienda habitual & No hay imputación (Art.~85.1) & --- & $0,00\text{ \euro}$ \\
Dividendos exigibles en 2026 & Capital mobiliario (Art.~25.1; Art.~14.1.a) & Ahorro & $1.000,00\text{ \euro}$ \\
Venta terreno ($10.000 - 6.000$) & Ganancia patrimonial (Arts.~33--36) & Ahorro & $4.000,00\text{ \euro}$ \\
Acciones heredadas ($300.000$) & No sujeta al IRPF (Art.~6.4) $\to$ ISD & --- & $0,00\text{ \euro}$ \\
Lotería de Navidad ($20.000$) & Gravamen especial: exento $\le 40.000$ (DA 33ª) & --- & $0,00\text{ \euro}$ \\
Pensión alimentos de hijos & Exenta para hijos (Art.~7.k); no es de Francisca & --- & $0,00\text{ \euro}$ \\
\bottomrule
\end{tabularx}
\end{center}
\begin{itemize}[itemsep=2pt]
    \item \textbf{Base Imponible General:} $58.500 - 100 = \mathbf{58.400,00\text{ \euro}}$.
    \item \textbf{Base Imponible del Ahorro:} $1.000 + 4.000 = \mathbf{5.000,00\text{ \euro}}$.
    \item \textbf{Detalles clave de Alicia:} Los $1.000\text{ \euro}$ de dividendos exigibles en 2025 se imputan a 2025 por exigibilidad (Art.~14.1.a). En el terreno rústico no hay coeficientes de abatimiento (comprado en 2000, posterior al 31/12/1994).
    \item \textbf{Impuestos Directos Aplicables en 2026:}
    1) \textbf{IRPF} (trabajo, actividad, dividendos y ganancia).
    2) \textbf{ISD} (herencia de las acciones de su tía por $300.000\text{ \euro}$).
    3) \textbf{Impuesto sobre el Patrimonio} (se devenga a 31/12, si supera el mínimo exento).
    4) \textbf{IBI} (piso y terreno rústico, devengado el 1 de enero).
    \textit{¡No hay IIVTNU (Plusvalía municipal) porque el terreno es rústico y solo grava terrenos urbanos!}
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultados]
BIG = \textbf{58.400,00 \euro} $\cdot$ BIA = \textbf{5.000,00 \euro} $\cdot$ ISD = \textbf{300.000 \euro} $\cdot$ Sin IIVTNU por ser rústico.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 7: Cesión Gratuita de Vivienda entre Padre e Hijo (D. Braulio)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Braulio, de 29 años de edad, vive en un piso (valor catastral 50.000 \euro{}) cuyo propietario es su padre que no le cobra ningún tipo de alquiler, no existiendo tampoco ningún tipo de contratato entre ambos que ampare la cesión de la vivivienda. El alquiler de mercado de una vivienda de similares carácterísticas en la zona donde se encuentra la que ocupa D. Braulio es de 800 \euro{} mensuales.
\end{enunciadoBox}

\begin{solucionBox}[Resolución y Corrección de Alicia]
\begin{enumerate}
    \item \textbf{D. Braulio (Hijo):} \textbf{No tributa por nada (0,00 \euro).} Vivir gratis en el piso de sus padres no constituye renta computable.
    
    \item \textbf{El Padre (Propietario):} \textbf{Imputación de rentas inmobiliarias (Art.~85 LIRPF).}
    \begin{itemize}
        \item La ley presume que las cesiones son retribuidas (Art.~6.5 LIRPF), pero entre padre e hijo la gratuidad queda demostrada.
        \item Como la cesión es 100\% gratuita, el piso no genera rendimientos del capital inmobiliario. Al no ser su vivienda habitual ni estar arrendado, debe imputar renta por el Art.~85:
        $$\text{Imputación de rentas} = 1,1\% \times 50.000\text{ \euro} = \mathbf{550,00\text{ \euro}} \quad \text{(o } 2\% = \mathbf{1.000,00\text{ \euro}}\text{ si no está revisado)}$$
        \item \textbf{Alerta de Alicia sobre el error de las notas del compañero:} El Art.~24 LIRPF \textbf{no aplica aquí}. El Art.~24 es para cuando el piso se \textit{alquila} a un familiar por poco dinero. Aquí no hay alquiler alguno: es cesión gratuita $\implies$ Imputación pura del Art.~85.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Idea Clave de Alicia para el Examen]
Cesión gratuita a familiar = Imputación de rentas (Art.~85). Alquiler barato a familiar = Rendimiento con mínimo del Art.~85 (Art.~24).
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

\begin{solucionBox}[Desglose de Liquidación de Alicia]
\textbf{Paso 1: Calificación de las dietas (Art.~9 RIRPF):}
\begin{itemize}
    \item \textbf{Lucena (Marzo, 20 días sin pernocta):}
    \begin{itemize}
        \item Tren pagado directamente por la empresa a RENFE: Gasto de la empresa, no es renta para el trabajador ($0\text{ \euro}$).
        \item Manutención sin pernocta: Límite exento $= 20\text{ días} \times 26,67\text{ \euro/día} = \mathbf{533,40\text{ \euro}}$. Cobró $500\text{ \euro} \le 533,40\text{ \euro} \implies$ \textbf{100\% Exento}.
    \end{itemize}
    \item \textbf{Burgos (Septiembre, 7 días / 6 noches):}
    \begin{itemize}
        \item Locomoción coche propio: $900\text{ km} \times 0,26 = 234,00\text{ \euro}$. Cobró $234\text{ \euro} \implies$ \textbf{Exento}.
        \item Estancia justificada con factura de hotel: $350,00\text{ \euro} \implies$ \textbf{Exento}.
        \item Manutención (6 noches con pernocta $+$ 1 día sin pernocta):
        $$\text{Límite} = (6 \times 53,34) + (1 \times 26,67) = 320,04 + 26,67 = \mathbf{346,71\text{ \euro}}$$
        Total exento estancia $+$ manutención $= 350,00 + 346,71 = 696,71\text{ \euro}$.
        $$\text{Exceso sujeto (RITP)} = 1.000,00 - 696,71 = \mathbf{303,29\text{ \euro}}$$
    \end{itemize}
\end{itemize}

\textbf{Paso 2: Liquidación del Rendimiento Neto del Trabajo:}
\begin{align*}
    \text{Sueldo bruto} &= 20.000,00\text{ \euro} \\
    \text{Exceso de dietas gravadas} &= +303,29\text{ \euro} \\
    \mathbf{\text{Rendimiento Íntegro}} &= \mathbf{20.303,29\text{ \euro}} \\
    \text{Seguridad Social (Art.~19.2.a)} &= -1.240,00\text{ \euro} \\
    \mathbf{\text{Rendimiento Neto Previo}} &= \mathbf{19.063,29\text{ \euro}} \\
    \text{Reducción Art.~20: } 2.364,34 - 1,14 \times (19.063,29 - 17.673,52) &= -\mathbf{780,00\text{ \euro}} \\
    \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
    \mathbf{\text{RNTP Reducido}} &= \mathbf{16.283,29\text{ \euro}}
\end{align*}
\textit{\small(Las retenciones de 3.325,65 € no se restan aquí; van a la cuota diferencial)}.
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial]
Exceso de dietas = \textbf{303,29 \euro} $\cdot$ Reducción Art.~20 = \textbf{780,00 \euro} $\cdot$ RNTP Reducido = \textbf{16.283,29 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 9: Vales de Comida, Cursos de Empresa y Reducción Art.~20 (D. Alberto)}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
D. Alberto, joven de 22 años y residente en Granada, encuentra su primer trabajo en Motril como comercial de equipos de Golf y empieza a trabajar el 1 de febrero. Durante el ejercicio 2026, ha recibido una retribución bruta anual de 11.900 \euro{} más 2.000 por comisiones de ventas. Se le practica una retención del 7 \% (1.287 \euro{}) y la aportación del trabajador a la Seguridad Social es de 986 \euro{}.

Se sabe también que, durante el primer mes de trabajo recibe un curso de marketing pagado por la empresa valorado en 1000 \euro{} y otro de Golf, valorado en 2.000 \euro{}. Durante el año 2026, recibe también 5.000 \euro{} en concepto de dietas de desplazamiento, correspondientes a los 10.000 KM recorridos y los 35 viajes con 1 noche de pernocta cada uno (un día de ida y otro de vuelta) realizados a distintas provincias españolas. Los gastos de alojamiento en los correspondientes hoteles, a razón de 100 \euro{} la noche, fueron reservados y pagados directamente por la empresa a través de su agencia de viajes.

Además, recibiría 200 vales de comida/año por valor de 12 \euro{}/vale. En el ejercicio 2026 ha percibido la parte proporcional, 180 vales.

\textbf{Determinar el rendimiento del trabajo de D. Alberto.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Paso a Paso de Alicia]
\begin{enumerate}
    \item \textbf{Cursos de formación:}
    Ambos cursos (marketing y golf) son para actualización profesional exigida por su puesto de comercial de equipos de golf $\implies$ \textbf{No sujetos a IRPF} (Art.~42.2.a LIRPF y Art.~44 RIRPF). \textit{\small(Ojo de examen: si el de golf fuera ocio ajeno al puesto, serían 2.000 € en especie)}.
    
    \item \textbf{Dietas de viaje:} Límite legal exento:
    $$10.000\text{ km} \times 0,26 + 35 \times (53,34 + 26,67) = 2.600 + 2.800,35 = \mathbf{5.400,35\text{ \euro}}$$
    Como cobró $5.000\text{ \euro} \le 5.400,35\text{ \euro}$, están \textbf{100\% exentas}. Los hoteles pagados por la empresa son gastos de la empresa, no renta.
    
    \item \textbf{Vales de comida (Art.~42.3.a LIRPF y Art.~45 RIRPF):}
    Límite exento $= 11\text{ \euro/día}$. Exceso $= 180 \times (12 - 11) = 180,00\text{ \euro}$.
    A la valoración se le suma el ingreso a cuenta no repercutido al tipo del 7\% (Art.~43.2 LIRPF):
    $$\text{Ingreso a cuenta} = 7\% \times 180 = 12,60\text{ \euro} \implies \text{Renta en especie} = 180 + 12,60 = \mathbf{192,60\text{ \euro}}$$
    
    \item \textbf{Liquidación del RNTP:}
    \begin{align*}
        \text{Sueldo dinerario} &= 11.900 + 2.000 = 13.900,00\text{ \euro} \\
        \text{Especie vales de comida} &= +192,60\text{ \euro} \\
        \mathbf{\text{Rendimiento Íntegro}} &= \mathbf{14.092,60\text{ \euro}} \\
        \text{Seguridad Social} &= -986,00\text{ \euro} \\
        \mathbf{\text{Rendimiento Neto Previo}} &= \mathbf{13.106,60\text{ \euro}} \\
        \text{Reducción Art.~20 (base } \le 14.852\text{ \euro)} &= -\mathbf{7.302,00\text{ \euro}} \\
        \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
        \mathbf{\text{RNTP Reducido}} &= \mathbf{3.804,60\text{ \euro}}
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

\begin{solucionBox}[Resolución de Alicia]
\textbf{1. Liquidación de D. Antonio:}
\begin{itemize}
    \item \textit{Acciones de la empresa ($5.000\text{ \euro}$):} \textbf{Exentas} por el Art.~42.3.f LIRPF (valor $\le 12.000\text{ \euro}$, participación $<5\%$, oferta general por antigüedad igual para todos).
    \item \textit{Plan de pensiones empresa ($2.500\text{ \euro}$):} Renta en especie computable, pero \textbf{sin ingreso a cuenta} (Art.~102.2 RIRPF).
    \item \textit{Seguro médico ($450\text{ \euro}$):} \textbf{Exento} por no superar $500\text{ \euro/año}$ (Art.~42.3.c LIRPF).
    \item \textit{Vehículo Citroën ($35.000\text{ \euro}$):} Al ser exclusivo para desplazamientos comerciales sin uso privado $\implies$ \textbf{No genera retribución en especie}.
    \item \textit{Rendimiento Íntegro:} $25.000 + 2.500 = \mathbf{27.500,00\text{ \euro}}$.
    \item \textit{Gastos deducibles:} SS ($1.725\text{ \euro}$) $+$ Sindicato ($250\text{ \euro}$) $+$ Otros gastos ($2.000\text{ \euro}$) $= \mathbf{3.975,00\text{ \euro}}$.
    \item \textbf{RNTP D. Antonio:} $27.500,00 - 3.975,00 = \mathbf{23.525,00\text{ \euro}}$.
\end{itemize}

\textbf{2. Liquidación de Dña. Ana:}
\begin{itemize}
    \item \textit{Indemnización pactada ($18.000\text{ \euro}$):} Al ser voluntaria, \textbf{no está exenta} (Art.~7.e LIRPF solo ampara ceses obligatorios del ET).
    \item \textit{Reducción del 30\% por irregularidad (Art.~18.2 LIRPF):} Por generarse en 20 años ($>2$ años):
    $$18.000 \times (1 - 0,30) = 18.000 \times 0,70 = \mathbf{12.600,00\text{ \euro}}$$
    \item \textit{Rendimiento Íntegro:} $10.000 + 12.600 = \mathbf{22.600,00\text{ \euro}}$.
    \item \textit{Gastos deducibles:} SS ($600\text{ \euro}$) $+$ Otros gastos ($2.000\text{ \euro}$) $= \mathbf{2.600,00\text{ \euro}}$.
    \item \textbf{RNTP Dña. Ana:} $22.600,00 - 2.600,00 = \mathbf{20.000,00\text{ \euro}}$ \textit{(Reducción Art.~20 = 0 por superar $19.747,50\text{ \euro}$)}.
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultados Oficiales]
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

\begin{solucionBox}[Resolución Oficial Paso a Paso de Alicia]
\textbf{1. Indemnización por despido judicial improcedente (Art.~7.e):}
\begin{itemize}
    \item Salario diario $= 25.000 / 365 = 68,49\text{ \euro/día}$.
    \item Límite exento $= 33\text{ días} \times 3\text{ años} \times 68,49 = \mathbf{6.780,82\text{ \euro}}$.
    \item Exceso sujeto: $12.000,00 - 6.780,82 = 5.219,18\text{ \euro}$.
    \item Con reducción 30\% por irregularidad: $5.219,18 \times 0,70 = \mathbf{3.653,43\text{ \euro}}$.
    \item \textit{Salarios de tramitación ($1.000\text{ \euro}$):} No forman parte de la indemnización, son sueldo ordinario.
\end{itemize}

\textbf{2. Nuevo empleo VHF (6 meses, julio a diciembre):}
\begin{itemize}
    \item Sueldo dinerario: $14.000 \times (6/12) = 7.000,00\text{ \euro}$.
    \item Seguridad Social: $750 \times (6/12) = 375,00\text{ \euro}$ (Alicia prorratea los 750 € anuales a 6 meses).
    \item Seguro médico ($300\text{ \euro/persona}$): Exento al ser $\le 500\text{ \euro}$ por persona (Art.~42.3.c).
    \item Ford Focus uso personal (6 meses): $20\% \times 13.000 \times (6/12) = 1.300\text{ \euro}$.
    Con ingreso a cuenta del 12\% no repercutido: $1.300 + (12\% \times 1.300) = \mathbf{1.456,00\text{ \euro}}$.
\end{itemize}

\textbf{3. Liquidación del Rendimiento Neto:}
\begin{align*}
    \text{Salarios devengados} &= 2.083,00\text{ \euro} \\
    \text{Salarios de tramitación} &= 1.000,00\text{ \euro} \\
    \text{Exceso indemnización (tras 30\%)} &= 3.653,43\text{ \euro} \\
    \text{Prestación por desempleo} &= 2.000,00\text{ \euro} \\
    \text{Sueldo VHF (6 meses)} &= 7.000,00\text{ \euro} \\
    \text{Coche en especie (6 meses) + ingreso a cuenta} &= 1.456,00\text{ \euro} \\
    \mathbf{\text{Rendimiento Íntegro Total}} &= \mathbf{17.192,43\text{ \euro}} \\
    \text{Seguridad Social (142 + 375) + Colegio (300)} &= -\mathbf{817,00\text{ \euro}} \\
    \mathbf{\text{Rendimiento Neto Previo}} &= \mathbf{16.375,43\text{ \euro}} \\
    \text{Reducción Art.~20: } 7.302 - 1,75 \times (16.375,43 - 14.852) &= -\mathbf{4.636,00\text{ \euro}} \\
    \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
    \mathbf{\text{RNTP Reducido (cálculo base de Alicia)}} &= \mathbf{9.739,43\text{ \euro}}
\end{align*}
\textit{\small(\textbf{Alerta de Alicia sobre movilidad geográfica}: si el cambio a Málaga le obligó a trasladar su residencia habitual, el gasto deducible general de 2.000 € se incrementa en otros 2.000 € más por Art.~19.2.f, quedando el RNTP final en \textbf{7.739,43 \euro})}.
\end{solucionBox}

\begin{resultadoBox}[Resultados de Alicia]
RNTP Reducido = \textbf{9.739,43 \euro} $\cdot$ Con Movilidad Geográfica = \textbf{7.739,43 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 12: Empleada de Hogar y Obligación de Declarar}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
Una empleada de hogar, dada de alta en el régimen correspondiente de la Seguridad Social (siendo el importe de gasto en Seguridad Social de 1.100 \euro{}) gana 20.000 \euro{} anuales. Determinar su rendimiento neto del trabajo personal. Determinar si tendría que presentar la declaración del IRPF.
\end{enunciadoBox}

\begin{solucionBox}[Resolución Oficial de Alicia]
\begin{enumerate}
    \item \textbf{Liquidación del Rendimiento Neto del Trabajo Personal (RNTP):}
    \begin{align*}
        \text{Rendimiento Íntegro} &= \mathbf{20.000,00\text{ \euro}} \\
        \text{Seguridad Social} &= -\mathbf{1.100,00\text{ \euro}} \\
        \mathbf{\text{Rendimiento Neto Previo}} &= \mathbf{18.900,00\text{ \euro}} \\
        \text{Reducción Art.~20: } 2.364,34 - 1,14 \times (18.900 - 17.673,52) &= -\mathbf{966,15\text{ \euro}} \\
        \text{Otros gastos (Art.~19.2.f)} &= -\mathbf{2.000,00\text{ \euro}} \\
        \mathbf{\text{RNTP Reducido}} &= \mathbf{15.933,85\text{ \euro}}
    \end{align*}

    \item \textbf{Obligación formal de declarar (Art.~96 LIRPF):}
    \begin{itemize}
        \item Con un solo pagador el límite general para no declarar es $22.000\text{ \euro}$.
        \item Sin embargo, el límite baja a \textbf{15.876 \euro} cuando el pagador no está obligado a retener (Art.~96.3 LIRPF). Las familias que contratan a una empleada de hogar no son retenedores fiscales.
        \item Al percibir $20.000\text{ \euro} > 15.876\text{ \euro}$, \textbf{SÍ TIENE OBLIGACIÓN DE DECLARAR}.
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados de Alicia]
RNTP = \textbf{15.933,85 \euro} $\cdot$ ¿Tiene que declarar? = \textbf{SÍ} (límite reducido de 15.876 \euro).
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

\begin{solucionBox}[Resolución Paso a Paso de Alicia]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Piso en Granada (Imputación de rentas, Art.~85 LIRPF):}
    No está alquilado y no es su vivienda habitual $\implies$ Imputación de rentas sobre el valor catastral revisado:
    $$\mathbf{\text{IRI}} = 1,1\% \times 90.000\text{ \euro} = \mathbf{990,00\text{ \euro}}$$

    \item \textbf{Piso en Madrid (50\% de Juan, Arrendado al sobrino, Art.~24 LIRPF):}
    \begin{itemize}
        \item Ingresos de Juan ($50\%$): $500 \times 12 \times 50\% = 3.000,00\text{ \euro}$.
        \item Gastos de Juan ($50\%$): Comunidad ($1.050\text{ \euro}$) $+$ IBI ($300\text{ \euro}$) $+$ Amortización ($50\%$):
        $$\text{Amortización construcción} = 3\% \times 120.000 \times 50\% = 1.800,00\text{ \euro}$$
        $$\text{Total gastos} = 1.050 + 300 + 1.800 = 3.150,00\text{ \euro} \implies \text{Neto} = -150,00\text{ \euro}$$
        \item \textbf{Mínimo legal del Art.~24 LIRPF:} Por parentesco hasta el 3er grado (sobrino), el rendimiento neto no puede ser inferior a la imputación del Art.~85:
        $$\text{Mínimo Art.~24} = 1,1\% \times 200.000 \times 50\% = \mathbf{1.100,00\text{ \euro}} \implies \mathbf{\text{RNCI Computable}} = \mathbf{1.100,00\text{ \euro}}$$
    \end{itemize}

    \item \textbf{Local comercial (6 meses alquilado + 6 meses vacío):}
    \begin{itemize}
        \item \textit{Rendimiento del capital inmobiliario (Enero a junio, 181 días / 6 meses):}
        $$\text{Ingresos} = 1.200 \times 6 = 7.200,00\text{ \euro}$$
        Gastos jurídicos rescisión $= 100\text{ \euro}$. Amortización construcción ($300.000 \times \frac{100.000}{190.000} = 157.894,74\text{ \euro}$):
        $$\text{Amortización (181 días)} = 3\% \times 157.894,74 \times \frac{181}{365} = \mathbf{2.348,95\text{ \euro}} \quad \text{\small(o } 2.368,42\text{ \euro{} a 6/12)}$$
        $$\mathbf{\text{RNCI Local}} = 7.200,00 - 100,00 - 2.348,95 = \mathbf{4.751,05\text{ \euro}} \quad \text{\small(o } 4.731,58\text{ \euro{} a 6/12)}$$
        \item \textit{Imputación de rentas (Julio a diciembre, 184 días / 6 meses):}
        $$\mathbf{\text{IRI Local}} = 1,1\% \times 190.000 \times \frac{184}{365} = \mathbf{1.053,59\text{ \euro}} \quad \text{\small(o } 1.045,00\text{ \euro{} a 6/12)}$$
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resumen Global de D. Juan (Alicia)]
Granada: IRI = \textbf{990,00 \euro} $\cdot$ Madrid: RNCI = \textbf{1.100,00 \euro} $\cdot$ Local: RNCI = \textbf{4.751,05 \euro} e IRI = \textbf{1.053,59 \euro}. Total RNCI = \textbf{5.851,05 \euro} $\cdot$ Total IRI = \textbf{2.043,59 \euro}.
\end{resultadoBox}

\vspace{0.4cm}

\subsection{Práctica Nº 14: Arrendamiento de Local Comercial y Cesión de Traspaso}

\begin{enunciadoBox}[Enunciado Oficial de Clase (Verbatim)]
El Sr. Álvarez tiene un local de negocio arrendado (valor de adquisición 500.000 \euro{} y valor del suelo 200.000) desde el 1- Enero por el que cobra al mes la cantidad de 1.250 \euro{} más el correspondiente IVA. El 1-Agosto la arrendataria traspasa el derecho de arrendamiento a otra persona por 50.000 \euro{}, quien continúa pagando la mensualidad al Sr. Álvarez incrementada en un 15 por ciento. El IBI correspondiente al ejercicio es de 750 \euro{}.

\textbf{Calcular la incidencia de dicha operación en el IRPF.}
\end{enunciadoBox}

\begin{solucionBox}[Resolución Oficial de Alicia (Caso Principal y Variante de Pizarra)]
\textbf{1. Caso Principal (El propietario no participa del precio del traspaso):}
\begin{itemize}
    \item Los $50.000\text{ \euro}$ del traspaso son una ganancia patrimonial exclusiva de la arrendataria que traspasa (Art.~37.1.f LIRPF).
    \item El IVA repercutido no es ingreso en el IRPF (Art.~22.2 LIRPF).
    \item \textbf{Rendimiento de Capital Inmobiliario del Sr. Álvarez:}
    \begin{align*}
        \text{Enero a julio (7 meses): } 1.250 \times 7 &= 8.750,00\text{ \euro} \\
        \text{Agosto a diciembre (5 meses a +15\%): } 1.250 \times 1,15 \times 5 &= 7.187,50\text{ \euro} \\
        \mathbf{\text{Rendimiento Íntegro}} &= \mathbf{15.937,50\text{ \euro}} \\
        \text{IBI} &= -750,00\text{ \euro} \\
        \text{Amortización: } 3\% \times (500.000 - 200.000) &= -\mathbf{9.000,00\text{ \euro}} \\
        \mathbf{\text{RNCI Sr. Álvarez}} &= \mathbf{6.187,50\text{ \euro}}
    \end{align*}
\end{itemize}

\textbf{2. Variante de Pizarra (El propietario se queda el 30\% del traspaso = 15.000 \euro):}
\begin{itemize}
    \item Para el Sr. Álvarez, los $15.000\text{ \euro}$ son \textbf{Rendimiento del Capital Inmobiliario irregular} (Art.~15.a RIRPF), con reducción del 30\% (Art.~23.3 LIRPF) sobre la parte neta irregular:
    $$\text{Ingresos totales} = 15.937,50 + 15.000 = 30.937,50\text{ \euro}$$
    $$\text{Gastos totales} = 750 + 9.000 = 9.750\text{ \euro} \implies \text{Rendimiento neto total} = 21.187,50\text{ \euro}$$
    $$\text{Parte neta irregular} = 21.187,50 \times \frac{15.000}{30.937,50} = 10.272,73\text{ \euro}$$
    $$\text{Reducción 30\%} = 30\% \times 10.272,73 = 3.081,82\text{ \euro}$$
    $$\mathbf{\text{RNCI Reducido con Variante}} = 21.187,50 - 3.081,82 = \mathbf{18.105,68\text{ \euro}}$$
\end{itemize}
\end{solucionBox}

\begin{resultadoBox}[Resultados de Alicia]
Caso Principal: RNCI = \textbf{6.187,50 \euro} $\cdot$ Variante con 30\% del traspaso: RNCI Reducido = \textbf{18.105,68 \euro}.
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

\begin{solucionBox}[Resolución de Alicia]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Finca de pastos (RNCI en especie irregular):}
    \begin{itemize}
        \item Ingreso íntegro: $10\text{ vacas} \times 1.500\text{ \euro} = 15.000,00\text{ \euro}$.
        \item Período de generación de 5 años ($>2$ años) $\implies$ Reducción del 30\% (Art.~23.3 LIRPF):
        $$\mathbf{\text{RNCI Finca}} = 15.000,00 \times 0,70 = \mathbf{10.500,00\text{ \euro}}$$
    \end{itemize}

    \item \textbf{Apartamento de playa (2 meses alquilado, RNCI):}
    \begin{itemize}
        \item Ingresos íntegros: $3.000,00\text{ \euro}$.
        \item Comisión plataforma online (100\% deducible por estar afecta al alquiler): $60,00\text{ \euro}$.
        \item Amortización anual ($3\% \times 90.000 \times 70\%$ construcción): $1.890,00\text{ \euro}$.
        \item Gastos anuales prorrateados por meses a $2/12$ (julio y agosto):
        $$\text{Prorrateo } (2/12) = \frac{2}{12} \times [1.200 + 1.780 + 380 + 400 + 1.890] = \frac{2}{12} \times 5.650 = \mathbf{941,67\text{ \euro}}$$
        $$\text{Gastos deducibles totales} = 60,00 + 941,67 = \mathbf{1.001,67\text{ \euro}}$$
        $$\mathbf{\text{RNCI Apartamento}} = 3.000,00 - 1.001,67 = \mathbf{1.998,33\text{ \euro}}$$
        \textit{(Sin reducción por ser alquiler de temporada/vacacional)}.
    \end{itemize}

    \item \textbf{Apartamento de playa (10 meses de uso propio, Imputación Art.~85):}
    $$\mathbf{\text{IRI}} = 1,1\% \times 80.000 \times \frac{10}{12} = \mathbf{733,33\text{ \euro}}$$
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultados de Alicia]
Finca = \textbf{10.500,00 \euro} $\cdot$ Playa alquilado = \textbf{1.998,33 \euro} $\cdot$ Playa uso propio = \textbf{733,33 \euro}.
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

\begin{solucionBox}[Resolución Oficial de la Profesora según Notas de Alicia]
\begin{enumerate}[label=\alph*.]
    \item \textbf{Vivienda habitual:} \textbf{No tributa (0,00 \euro).} Excluida de la imputación de rentas (Art.~85.1 LIRPF); los gastos no son deducibles.
    
    \item \textbf{Apartamento alquilado (Ley 12/2023 por el Derecho a la Vivienda):}
    \begin{itemize}
        \item Ingresos íntegros $= (7.200 \times 6/12) + (6.800 \times 6/12) = 3.600 + 3.400 = \mathbf{7.000,00\text{ \euro}}$.
        \item Gastos deducibles: Comunidad ($700\text{ \euro}$) $+$ IBI ($370\text{ \euro}$) $+$ Amortización del mobiliario ($10\% \times 2.000 = 200\text{ \euro}$) $= \mathbf{1.270,00\text{ \euro}}$.
        \item \textbf{Rendimiento Neto previo (resultado oficial de la profesora):}
        $$\text{RNCI Previo} = 7.000,00 - 1.270,00 = \mathbf{5.730,00\text{ \euro}}$$
        \item \textbf{Comprobación de la reducción del 90\% (Art.~23.2.a LIRPF):}
        Al estar en zona tensionada y rebajar la renta:
        $$\text{Rebaja pactada} = 7.200 - 6.800 = 400,00\text{ \euro/año}$$
        $$\text{5\% de la renta anterior} = 5\% \times 7.200 = 360,00\text{ \euro/año}$$
        Como $400 > 360$, la rebaja supera el 5\% $\implies$ \textbf{Aplica la reducción del 90\%}:
        $$\mathbf{\text{RNCI Reducido (solución de la profesora)}} = 5.730,00 \times (1 - 0,90) = 5.730,00 \times 0,10 = \mathbf{573,00\text{ \euro}}$$
    \end{itemize}
\end{enumerate}
\end{solucionBox}

\begin{resultadoBox}[Resultado Oficial de la Profesora]
RNCI previo = \textbf{5.730,00 \euro} $\cdot$ Reducción 90\% = \textbf{573,00 \euro}.
\end{resultadoBox}

\end{document}
"""

with open('apuntes/derecho-fiscal/casos_practicos/main.tex', 'w', encoding='utf-8') as f:
    f.write(latex_doc)

print("Escrito main.tex con la resolución 100% fiel a los apuntes de Alicia.")
