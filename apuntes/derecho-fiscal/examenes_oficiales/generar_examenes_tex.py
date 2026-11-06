#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_examenes_tex.py
Genera el documento LaTeX 'main.tex' en apuntes/derecho-fiscal/examenes_oficiales/
con enunciados íntegros verbatim, opciones y resoluciones directas sin palabrería.
"""

import json
import re

def tex_escape(text):
    if not text:
        return ""
    # Global unicode replacements before splitting
    text = text.replace('✅', '')
    text = text.replace('❌', '')
    text = text.replace('⚠️', '')
    text = text.replace('🔹', '')
    text = text.replace('📌', '')
    text = text.replace('📝', '')
    text = text.replace('🗓️', '').replace('📅', '')
    text = text.replace('≈', r'$\approx$ ')
    text = text.replace('≤', r'$\le$ ')
    text = text.replace('≥', r'$\ge$ ')
    text = text.replace('×', r'$\times$ ')
    text = text.replace('≠', r'$\ne$ ')
    text = text.replace('→', r'$\to$ ')
    text = text.replace('•', r'$\bullet$ ')
    text = text.replace('…', r'\dots{}')
    text = text.replace('“', "``").replace('”', "''")
    text = text.replace('‘', "`").replace('’', "'")
    
    # Split text by math delimiters if any ($ ... $)
    parts = text.split('$')
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            # Inside math mode: preserve math commands, but replace € and % safely
            p = p.replace('€', r'\text{ \euro}')
            p = p.replace('%', r'\%')
            out.append('$' + p + '$')
        else:
            # Outside math mode
            p = p.replace('\\', r'\textbackslash{}')
            p = p.replace('&', r'\&')
            p = p.replace('%', r'\%')
            p = p.replace('_', r'\_')
            p = p.replace('#', r'\#')
            p = p.replace('€', r'\euro{}')
            # Quotes
            p = re.sub(r'«([^»]*)»', r"``\1''", p)
            p = re.sub(r'"([^"]*)"', r"``\1''", p)
            out.append(p)
    return ''.join(out)

def format_question_latex(q_num, q_text, opts, correct_idx, just, prefix=""):
    letters = ['a', 'b', 'c', 'd', 'e']
    correct_letter = letters[correct_idx] if 0 <= correct_idx < len(letters) else 'a'
    
    # Clean up q_text if it already starts with a number
    q_clean = re.sub(r'^\d+\.\s*', '', q_text.strip())
    
    tex = []
    label_num = f"{prefix}{q_num}" if prefix else f"{q_num}"
    tex.append(f"\\noindent\\textbf{{\\sffamily Pregunta {label_num}:}} {tex_escape(q_clean)}\\\\[0.15cm]")
    
    if opts and len(opts) > 1:
        tex.append(r"\begin{enumerate}[label=\textbf{\alph*)},leftmargin=1.8em,itemsep=1.5pt,topsep=2pt,partopsep=0pt,parsep=0pt]")
        for opt in opts:
            # Clean letter prefix if in opt
            opt_clean = re.sub(r'^[a-e]\)\s*', '', opt.strip())
            tex.append(f"    \\item {tex_escape(opt_clean)}")
        tex.append(r"\end{enumerate}")
    elif opts and len(opts) == 1:
        # Single option (Modelo B partial)
        tex.append(f"\\noindent\\textbf{{Opción Oficial:}} \\textbf{{{correct_letter})}} {tex_escape(opts[0])}\\\\[0.15cm]")
        
    tex.append(f"\\begin{{solucionBox}}[Respuesta Oficial: Opción {correct_letter.upper()}]")
    tex.append(f"\\textbf{{Justificación Oficial / Fundamentación:}}\\\\[0.1cm]")
    tex.append(f"{tex_escape(just.strip())}")
    tex.append(r"\end{solucionBox}")
    tex.append(r"\vspace{0.35cm}")
    tex.append("")
    return "\n".join(tex)

def main():
    # Load JSON supuestos
    with open('src/content/materials/ade/derecho-fiscal/supuestos-examen.json', 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    
    # Load Guia Maestra for Wuolah Parcial 1
    with open('/home/jxlig0d/Escritorio/QUINTO/FIS/GUIA_MAESTRA_EXAMEN_9_NOV.md', 'r', encoding='utf-8') as f:
        guia_text = f.read()

    doc = []
    
    # PREAMBLE
    doc.append(r"""\documentclass[11pt,a4paper,openany]{article}
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
    {\Large\textbf{\textsf{\color{fiscalAccent}COMPILACIÓN OFICIAL DE EXÁMENES RESUELTOS}}\par}
    \vspace{0.5cm}
    {\large\textsf{Facultad de Ciencias Económicas y Empresariales --- Universidad de Granada}\par}
    \vspace{0.25cm}
    {\normalsize\textsf{Grado en ADE $\cdot$ Doble Grado DADE / FICO}\par}
    
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
        {\large\bfseries\color{fiscalDark}EXÁMENES Y PARCIALES OFICIALES ÍNTEGROS VERBATIM}\\[0.3cm]
        \normalsize
        \begin{itemize}[leftmargin=1.5cm,itemsep=3pt]
            \item \textbf{Bloque I: Parcial Oficial Wuolah (Modelos A y B)} --- 23 preguntas de Tema 1 (LGT, tributos, liquidación, deudas y sucesores).
            \item \textbf{Bloque II: Simulacro Oficial Parcial 9 Noviembre} --- 10 preguntas teóricas LGT/IRPF + Caso Práctico Dña. Elena (5 preguntas de liquidación).
            \item \textbf{Bloque III: Examen Ordinario 2019 (Profesora Titular)} --- Enunciado oficial íntegro del matrimonio Dña. María y D. Julio + 18 preguntas resueltas.
            \item \textbf{Bloque IV: Examen Ordinario Enero 2020 (Profesora Titular)} --- Enunciado oficial íntegro del caso D. Jacobo y Dña. Dolores + 20 preguntas resueltas.
        \end{itemize}
        \vspace{0.2cm}
        \textbf{\color{fiscalAccent}76 Preguntas Verbatim $\cdot$ Soluciones de Pizarra $\cdot$ Artículos LGT/LIRPF $\cdot$ Sin Palabrería}
        \vspace{0.2cm}
    \end{tcolorbox}
    
    \vfill
    {\footnotesize\textsf{\color{gray}repasaYA $\cdot$ Material docente de máxima fidelidad para examen $\cdot$ Noviembre 2026}\par}
\end{titlepage}

\newpage
\tableofcontents
\newpage
""")

    # --------------------------------------------------------------------------
    # BLOQUE I: PARCIAL WUOLAH MODELOS A Y B
    # --------------------------------------------------------------------------
    doc.append(r"""\section{Bloque I: Parcial Oficial de Nociones Tributarias y LGT (Wuolah)}
\label{sec:wuolah}

\begin{enunciadoBox}[Contexto del Parcial Oficial de Nociones Tributarias]
Examen parcial oficial correspondiente al Bloque Temático I (Concepto de tributo, hechos imponibles, exención/no sujeción, sujetos pasivos, métodos de estimación de bases, extinción de la deuda tributaria y sucesión mortis causa). Incluye los dos modelos oficiales (A y B) con sus plantillas corregidas y la cita exacta de los preceptos de la Ley 58/2003 General Tributaria (LGT).
\end{enunciadoBox}

\vspace{0.4cm}
\subsection{Modelo A: 15 Preguntas Oficiales Verbatim}
""")

    # Parse Wuolah Modelo A
    model_a_match = re.search(r'#### 🔹 MODELO A.*?\n(1\..*?)(?=#### 🔹 MODELO B)', guia_text, re.DOTALL)
    content_a = model_a_match.group(1)
    q_blocks = re.split(r'\n(?=\d+\.\s+\*\*)', content_a.strip())

    for i, q in enumerate(q_blocks):
        lines = q.strip().split('\n')
        header = lines[0]
        q_text = re.sub(r'^\d+\.\s+\*\*(.*?)\*\*.*', r'\1', header)
        options = []
        correct_idx = 0
        justification = ""
        letters_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        for line in lines[1:]:
            line = line.strip()
            m_opt = re.match(r'^\*\s+(\*\*[✅❌]\s*)?([a-d]\))\s*(.*)', line)
            if m_opt:
                is_correct = bool(m_opt.group(1))
                opt_letter = m_opt.group(2)[0]
                opt_text = m_opt.group(3)
                m_just = re.search(r'\*\((.*?)\)\*', opt_text)
                if is_correct:
                    correct_idx = letters_map.get(opt_letter, 0)
                    if m_just:
                        justification = m_just.group(1)
                        opt_text = opt_text[:m_just.start()].strip()
                elif m_just:
                    opt_text = opt_text[:m_just.start()].strip()
                opt_text = opt_text.replace('**', '').strip()
                options.append(opt_text)
        
        doc.append(format_question_latex(i+1, q_text, options, correct_idx, justification, prefix="A."))

    doc.append(r"""\newpage
\subsection{Modelo B: Preguntas Específicas del Modelo B}
\begin{enunciadoBox}[Preguntas Diferenciales del Modelo B]
Preguntas incorporadas en la variante B del examen oficial que evalúan la deuda tributaria, tributos estatales vs autonómicos y locales, tasas y contribuciones especiales.
\end{enunciadoBox}
\vspace{0.4cm}
""")

    # Parse Wuolah Modelo B
    model_b_match = re.search(r'#### 🔹 MODELO B.*?\n(\* \*\*Preg\..*?)(?=---|\n## )', guia_text, re.DOTALL)
    content_b = model_b_match.group(1)
    qb_blocks = re.split(r'\n(?=\* \*\*Preg\.)', content_b.strip())

    for i, q in enumerate(qb_blocks):
        lines = q.strip().split('\n')
        header = lines[0]
        m_head = re.match(r'^\*\s+\*\*Preg\.\s+(\d+)\s+\(Modelo B\):\s*(.*?)\*\*.*', header)
        if m_head:
            orig_num = m_head.group(1)
            q_text = m_head.group(2)
        else:
            orig_num = str(i+1)
            q_text = header
        
        options = []
        correct_idx = 0
        justification = ""
        letters_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        for line in lines[1:]:
            line = line.strip()
            m_opt = re.match(r'^\*\s+(\*\*[✅❌]\s*)?([a-d]\))\s*(.*)', line)
            if m_opt:
                is_correct = bool(m_opt.group(1))
                opt_letter = m_opt.group(2)[0]
                opt_text = m_opt.group(3)
                m_just = re.search(r'\*\((.*?)\)\*', opt_text)
                if is_correct:
                    correct_idx = letters_map.get(opt_letter, 0)
                    if m_just:
                        justification = m_just.group(1)
                        opt_text = opt_text[:m_just.start()].strip()
                elif m_just:
                    opt_text = opt_text[:m_just.start()].strip()
                opt_text = opt_text.replace('**', '').strip()
                options.append(opt_text)
            else:
                m_single = re.match(r'^\*\s+\*\*✅\s+([a-d])\)\s+(.*?)\*\*\s*(?:\*\((.*?)\)\*)?', line)
                if m_single:
                    opt_letter = m_single.group(1)
                    correct_idx = letters_map.get(opt_letter, 0)
                    opt_text = m_single.group(2)
                    justification = m_single.group(3) or ""
                    options.append(opt_text)
        
        doc.append(format_question_latex(orig_num, q_text, options, correct_idx, justification, prefix="B."))

    # --------------------------------------------------------------------------
    # BLOQUE II: SIMULACRO PARCIAL 9 NOV
    # --------------------------------------------------------------------------
    doc.append(r"""\newpage
\section{Bloque II: Simulacro Oficial Parcial 9 Noviembre}
\label{sec:simulacro}

\begin{enunciadoBox}[Estructura y Reglas del Parcial Oficial de Aula]
\textbf{Convocatoria:} Parcial de Aula D16 (1,5 puntos sobre nota final, eliminatorio a partir de 0,75 puntos).\\
\textbf{Estructura:} 15 preguntas tipo test de 4 opciones (10 teóricas de LGT e IRPF $+$ 5 prácticas de liquidación).\\
\textbf{Criterio de corrección:} Cada 3 errores restan 1 acierto ($-0,33$ por fallo).
\end{enunciadoBox}

\vspace{0.3cm}
\subsection{Parte 1: 10 Preguntas Teóricas Clave}
""")

    sim_items = [it for it in data_json['items'] if it['caseId'] == 'simulacro-9nov']
    for i, it in enumerate(sim_items[:10]):
        doc.append(format_question_latex(i+1, it['q'], it['opts'], it['correct'], it['justification'], prefix="S."))

    doc.append(r"""\newpage
\subsection{Parte 2: Caso Práctico de Liquidación --- Dña. Elena}

\begin{enunciadoBox}[Enunciado Oficial del Caso Práctico]
Dña. Elena (42 años), residente en Granada, presenta los siguientes datos fiscales en el ejercicio:
\begin{enumerate}[label=\textbf{\arabic*)}]
    \item Trabaja como directiva en una empresa desde hace 6 años con un sueldo bruto anual de $44.000\text{ \euro}$, habiendo cotizado a la Seguridad Social $2.650\text{ \euro}$ y pagado $580\text{ \euro}$ al Colegio Oficial de Economistas (colegiación obligatoria para su puesto) y $200\text{ \euro}$ a un sindicato.
    \item En mayo se desplazó en su vehículo particular de Granada a Sevilla ($500\text{ km}$ ida y vuelta en total) durante 3 días (pernoctando 2 noches en hotel y regresando el 3.er día). La empresa le abonó: $0,36\text{ \euro/km}$ ($180\text{ \euro}$), peajes y parking justificados ($40\text{ \euro}$), factura de hotel de las 2 noches ($210\text{ \euro}$) y $220\text{ \euro}$ en concepto de dieta de manutención por los 3 días.
    \item Además, la empresa le cedió para uso exclusivamente particular un vehículo propiedad de la empresa cuyo coste de adquisición fue de $28.000\text{ \euro}$ (sin distintivo de eficiencia energética). El ingreso a cuenta ($20\%$) fue REPERCUTIDO a la trabajadora.
    \item Es propietaria de un piso en Granada (Coste de adquisición satisfecho $= 180.000\text{ \euro}$; Valor Catastral $= 90.000\text{ \euro}$, correspondiendo el $20\%$ al suelo y el $80\%$ a la construcción), alquilado todo el año como vivienda habitual a un matrimonio por $750\text{ \euro/mes}$ ($9.000\text{ \euro/año}$) mediante contrato firmado en 2024 (reducción general del $50\%$). Gastos anuales soportados: intereses de hipoteca $5.500\text{ \euro}$, reparación de caldera y pintura $4.000\text{ \euro}$, IBI $450\text{ \euro}$ y comunidad $650\text{ \euro}$.
    \item Posee un apartamento de vacaciones en Salobreña (Valor Catastral revisado hace 4 años $= 80.000\text{ \euro}$) que ha permanecido a su disposición todo el año (vacío).
\end{enumerate}
\end{enunciadoBox}

\vspace{0.3cm}
""")

    for i, it in enumerate(sim_items[10:]):
        doc.append(format_question_latex(i+11, it['q'], it['opts'], it['correct'], it['justification'], prefix="S."))

    # --------------------------------------------------------------------------
    # BLOQUE III: EXAMEN ORDINARIO 2019
    # --------------------------------------------------------------------------
    doc.append(r"""\newpage
\section{Bloque III: Examen Oficial Convocatoria Ordinaria 2019}
\label{sec:examen2019}

\begin{enunciadoBox}[Enunciado Oficial de la Profesora: Matrimonio Casares --- Gutiérrez]
Doña María Casares y D. Julio Gutiérrez, ambos de 50 años, son un matrimonio casado en régimen de gananciales desde el año 2000 y residentes en Granada. Tienen dos hijos solteros de 19 y 17 años, que están estudiando, sin rentas y que conviven con ellos. También reside con el matrimonio la madre de Doña María de 76 años, sin rentas y con un grado de minusvalía reconocido del $40\%$.

\textbf{Actividad económica de Doña María:} Tiene una escuela de patronaje y corte y confección (IAE 933.9) que montó en 2016, por la que está en el régimen de módulos en el IRPF. No ha contratado a nadie hasta 2018 que ha tenido una persona asalariada a jornada completa desde el 1 de Febrero (1650 horas). La actividad se desarrolla en un local de $40\text{ m}^2$, adquirido en 2017 por $90.000\text{ \euro}$ (de los que $45.000\text{ \euro}$ corresponden al suelo) y se sabe que, en 2017, se compraron máquinas de coser por $2.000\text{ \euro}$ (valor por máquina de $300\text{ \euro}$) y un ordenador de $2.000\text{ \euro}$. En el ejercicio 2018, se han comprado más máquinas de coser por $1.000\text{ \euro}$, por $260\text{ \euro}$ cada una, y dos máquinas remalladoras profesionales de segunda mano, cada una de las cuales ha supuesto una inversión de $700\text{ \euro}$. En el 2017, se obtuvieron ingresos por $20.000\text{ \euro}$ y en 2018, por $50.000\text{ \euro}$. Se viene amortizando a coeficientes máximos y los pagos fraccionados han sido de $456\text{ \euro}$.

\textbf{Rendimientos del trabajo de D. Julio:} D. Julio es ingeniero y trabaja para una empresa tecnológica. Su salario íntegro en 2018 ha sido de $62.000\text{ \euro}$ (tipo de retención $25\%$, retenciones $15.500\text{ \euro}$, y Seguridad Social $2.900\text{ \euro}$). En mayo de 2018 asistió a un Congreso de Barcelona, durante 3 días (dos noches) del que D. Julio conserva factura del hotel donde se quedó por importe de $300\text{ \euro}$ y un billete de avión por $90\text{ \euro}$. Por la asistencia al congreso, la empresa le paga $400\text{ \euro}$.
Se sabe que en 2018, D. Julio recibió un premio por sus 10 años al servicio de la empresa por $5.000\text{ \euro}$ (de los que $875\text{ \euro}$ corresponden a retención), que la empresa le paga una prima anual por un seguro de enfermedad de $600\text{ \euro}$ y que se han realizado aportaciones a un plan de pensiones por $6.000\text{ \euro}$, de los que $3.000\text{ \euro}$ corresponden a la empresa. Los derechos consolidados en el Plan de Pensiones ascienden a $40.000\text{ \euro}$.

\textbf{Patrimonio e información patrimonial adicional en 2018:}
\begin{itemize}[itemsep=1.5pt]
    \item Residen en una vivienda adquirida en 2001 por $180.000\text{ \euro}$, cuyo valor catastral es de $200.000\text{ \euro}$ ($50\%$ suelo). IBI: $312\text{ \euro}$.
    \item El 1 de abril de 2018, Doña María vendió una finca rústica, heredada de su padre en 2013, por $30.000\text{ \euro}$. Valor en Sucesiones: $35.000\text{ \euro}$, valor catastral revisado $23.000\text{ \euro}$ ($20\%$ suelo). La finca ha estado improductiva todo este tiempo.
    \item En 2010 adquirieron un apartamento en la playa, alquilado en 2018 todo el año por $400\text{ \euro/mes}$. Valor adquisición: $130.000\text{ \euro}$, VC revisado $90.000\text{ \euro}$ ($25\%$ suelo). IBI asumido: $130\text{ \euro}$.
    \item En enero de 2018, por fallecimiento de un primo lejano de sus padres, D. Julio heredó 300 acciones cotizadas en bolsa (valor en ISD $= 21.000\text{ \euro}$, es decir $70\text{ \euro/acción}$). Dividendos líquidos: $2.430\text{ \euro}$ (retención $570\text{ \euro}$), gastos administración $5\text{ \euro}$.
    \item De las 300 acciones, vendió 50 en noviembre a $100\text{ \euro/acción}$. Cotización a 31 de diciembre: $101\text{ \euro}$.
    \item Cuenta corriente conjunta con saldo medio último trimestre de $62.000\text{ \euro}$ y saldo a 31 dic de $75.000\text{ \euro}$.
    \item Doña María tiene bonos a largo plazo heredados de su padre con intereses de $500\text{ \euro}$ en 2018 (cotización último trimestre: $12.000\text{ \euro}$).
    \item Donativos de D. Julio a Cruz Roja: $300\text{ \euro}$.
\end{itemize}
\end{enunciadoBox}

\vspace{0.4cm}
""")

    ex2019_items = [it for it in data_json['items'] if it['caseId'] == 'examen-2019']
    for i, it in enumerate(ex2019_items):
        doc.append(format_question_latex(i+1, it['q'], it['opts'], it['correct'], it['justification'], prefix="2019."))

    # --------------------------------------------------------------------------
    # BLOQUE IV: EXAMEN ORDINARIO ENERO 2020
    # --------------------------------------------------------------------------
    doc.append(r"""\newpage
\section{Bloque IV: Examen Oficial Convocatoria Ordinaria Enero 2020}
\label{sec:examen2020}

\begin{enunciadoBox}[Enunciado Oficial de la Profesora: Matrimonio Jacobo J. --- Dolores H.]
D. Jacobo J., de 56 años, está casado en régimen de gananciales con Dña. Dolores H. de 57, desde 1997. Ambos residen en Granada y tienen dos hijos solteros de 20 y 18 años, sin rentas, que conviven con ellos. También reside con el matrimonio la madre de Dña. Dolores de 80 años. Dña. Dolores tiene un hijo de un matrimonio anterior de 26 años, estudiando un máster en Madrid y que reside solo, asumiendo tanto su madre como su padre sus gastos en la capital.

\textbf{Rendimientos del trabajo de D. Jacobo:} Investigador del Centro de Investigación Genética (CIG) con sueldo íntegro en 2019 de $42.000\text{ \euro}$ (retención $22\% = 9.240\text{ \euro}$, Seguridad Social $2.400\text{ \euro}$). En marzo de 2019 asistió a un congreso en Madrid durante 3 días (dos noches); conserva facturas de hotel por $200\text{ \euro}$, tren ida y vuelta $100\text{ \euro}$ y restaurantes por $150\text{ \euro}$. La empresa le abona $430\text{ \euro}$ por el congreso.
En 2019 la empresa otorgó a D. Jacobo un premio por 20 años de servicio de $2.000\text{ \euro}$ (retención $308\text{ \euro}$); aportaciones a planes de pensiones por $8.000\text{ \euro}$ ($50\%$ pagado por la empresa $= 4.000\text{ \euro}$); y la empresa le paga un bono transporte anual de $1.200\text{ \euro}$.

\textbf{Actividad económica de Dña. Dolores:} Pequeño restaurante (IAE 671.4) montado en 2012. En 2019 ha trabajado su hijo de 18 años por las tardes (sin alta en SS, 700 horas) y un empleado contratado en 2014 (1.800 horas). Local alquilado de $70\text{ m}^2$ por $700\text{ \euro/mes}$ (VC $90.000\text{ \euro}$, suelo $40\%$). Potencia eléctrica: $10\text{ kW}$. Mesas: 8 (4 de 4 plazas y 4 de 2 plazas). En 2019 adquirió sillas nuevas por $700\text{ \euro}$ ($50\text{ \euro/silla}$) y en 2018 un ordenador por $1.500\text{ \euro}$. Amortización a coeficientes máximos. Pagos fraccionados: $2.234\text{ \euro}$. Ingresos 2019: $10.000\text{ \euro}$, compras: $14.000\text{ \euro}$ (en 2018: ingresos $90.000\text{ \euro}$, compras $12.000\text{ \euro}$).

\textbf{Bienes patrimoniales del matrimonio:}
\begin{itemize}[itemsep=1.5pt]
    \item Vivienda habitual adquirida en 2001 por $350.000\text{ \euro}$ (VC revisado $170.000\text{ \euro}$, $25\%$ suelo).
    \item Apartamento en la playa, adquirido por D. Jacobo en 1991 (antes del matrimonio en 1997, por tanto \textbf{100\% privativo}), alquilado durante el curso escolar (9 meses) por $500\text{ \euro/mes}$. Valor adquisición: $65.000\text{ \euro}$, IBI asumido: $120\text{ \euro}$. Luz y agua a cargo del inquilino.
    \item 300 acciones cotizadas adquiridas en 2010 a $60\text{ \euro/acción}$. En noviembre de 2019 vendió 50 a $55\text{ \euro/acción}$. Cotización a 31 de diciembre: $58\text{ \euro/acción}$.
    \item Cuenta corriente común con saldo medio último trimestre de $50.000\text{ \euro}$.
    \item 50 bonos a largo plazo heredados por Dña. Dolores en 2012 que generan $1.000\text{ \euro}$ anuales de intereses (cotización último trimestre: $50.000\text{ \euro}$).
    \item Finca rústica heredada por Dña. Dolores en febrero de 2019 (valor ISD $300.000\text{ \euro}$, VC $170.000\text{ \euro}$). Improductiva.
    \item Premio de la ONCE del hijo mayor de 26 años: $2.300\text{ \euro}$.
\end{itemize}
\end{enunciadoBox}

\vspace{0.4cm}
""")

    ex2020_items = [it for it in data_json['items'] if it['caseId'] == 'examen-2020']
    for i, it in enumerate(ex2020_items):
        doc.append(format_question_latex(i+1, it['q'], it['opts'], it['correct'], it['justification'], prefix="2020."))

    doc.append(r"\end{document}")

    # Write output
    out_path = 'apuntes/derecho-fiscal/examenes_oficiales/main.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(doc))
    print(f"Successfully generated {out_path} with {len(doc)} sections.")

if __name__ == '__main__':
    main()
