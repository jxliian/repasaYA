# SPEC-016: Apuntes PDF en LaTeX de Casos Prácticos y Exámenes Oficiales Resueltos (Derecho Fiscal)

## 📌 1. Motivación y Alcance
A petición del usuario para la preparación intensiva del examen parcial del 9 de noviembre de Derecho Fiscal (5º ADE / DADE, UGR), se generan y publican dos documentos PDF de alta fidelidad compilados con LaTeX:
1. **Casos Prácticos Oficiales Resueltos (Prácticas 1 a 16)**: Enunciados íntegros verbatim y resolución paso a paso directa, limpia y sin palabrería, con los resultados numéricos oficiales de pizarra de Alicia (IRPF, dietas, rentas en especie, capital inmobiliario e imputación de rentas).
2. **Exámenes y Parciales Oficiales Resueltos**: 76 preguntas de examen oficial verbatim procedentes de los archivos PDF existentes (Parcial Wuolah Modelos A y B completos, Simulacro Oficial 9 Noviembre y Exámenes Ordinarios Oficiales 2019 y 2020 de la profesora de la UGR) con sus 4 opciones, plantilla oficial y justificaciones con los artículos exactos de la LGT y LIRPF.

---

## 🛠️ 2. Arquitectura de los Documentos LaTeX

### 2.1 Estilo Visual Compartido (`apuntes/derecho-fiscal/estilo_fiscal.tex`)
- Tipografía: Latin Modern Sans (`lmodern`) con `microtype` activado.
- Paleta cromática corporativa y jurídica:
  - `fiscalPrimary`: Azul marino institucional `#183C6C`.
  - `fiscalSecondary`: Azul medio `#296299`.
  - `fiscalAccent`: Ámbar/Ocre fiscal `#B45309`.
  - `fiscalLight`: Gris pizarra claro `#F8FAFC`.
  - `fiscalGreenLight` / `fiscalGreen`: Verde para resultados y respuestas correctas.
- Cajas de contenido con `tcolorbox` (`skins`, `breakable`):
  - `enunciadoBox`: Enunciados de los casos y supuestos.
  - `solucionBox`: Resoluciones y justificaciones jurídicas.
  - `resultadoBox`: Resumen numérico final para cotejar con calculadora en mano.
  - `trampaBox`: Alertas de examen y reglas de oro de la profesora.
- Encabezados y pies con `fancyhdr` y `truncate` para evitar colisiones y desbordamientos.

### 2.2 Documento 1: `casos-practicos-resueltos.pdf` (23 páginas)
- Ubicación fuente: `apuntes/derecho-fiscal/casos_practicos/main.tex`
- Ubicación pública: `public/derecho-fiscal/casos-practicos-resueltos.pdf`
- Enunciados oficiales: Extraídos 100% verbatim palabra por palabra del archivo oficial de ejercicios `Supuestos_Clase_IRPF_DERECHO_FISCAL_2026-27.pdf` sin omisiones ni resúmenes.
- Contenido:
  - Prácticas 1 a 7: Concepto de renta, hecho imponible, exenciones (Art. 7 LIRPF), indemnizaciones por despido (límite 180.000 € y 33/45 días/año), IPP/IPA, becas, anualidades por alimentos vs pensiones compensatorias, dividendos y seguros de vida.
  - Prácticas 8 a 12: Rendimientos del Trabajo Personal (RITP, dietas y asignaciones para gastos de viaje del Art. 9 RIRPF, vales de comida y guardería, vehículos y viviendas en especie con ingresos a cuenta repercutidos vs no repercutidos, reducción por irregularidad del Art. 18.2 LIRPF, reducción del Art. 20 LIRPF por bajos ingresos y gastos deducibles del Art. 19 LIRPF).
  - Prácticas 13 a 16: Capital Inmobiliario e Imputación de Rentas (arrendamiento de vivienda habitual, temporada, locales, fincas rústicas, amortizaciones del 3%, y reducción del 90% en zonas de mercado tensionado de la Ley 12/2023).

### 2.3 Documento 2: `examenes-oficiales-resueltos.pdf` (32 páginas)
- Ubicación fuente: `apuntes/derecho-fiscal/examenes_oficiales/main.tex` (generado vía `generar_examenes_tex.py`)
- Ubicación pública: `public/derecho-fiscal/examenes-oficiales-resueltos.pdf`
- Contenido:
  - **Bloque I: Parcial Oficial Wuolah (Modelos A y B)**: 23 preguntas de Tema 1 (LGT, tributos, tasas, contribuciones especiales, métodos de estimación objetiva vs directa, deuda tributaria y sucesores).
  - **Bloque II: Simulacro Oficial Parcial 9 Noviembre**: 10 teóricas + Caso Práctico Dña. Elena (5 preguntas de liquidación: RNT, dietas, coche en especie, alquiler con reducción 50% e imputación de segunda residencia).
  - **Bloque III: Examen Ordinario 2019 (Profesora UGR)**: Enunciado oficial íntegro del matrimonio Dña. María y D. Julio Gutiérrez + 18 preguntas resueltas.
  - **Bloque IV: Examen Ordinario Enero 2020 (Profesora UGR)**: Enunciado oficial íntegro del caso D. Jacobo y Dña. Dolores + 20 preguntas resueltas.

---

## 🌐 3. Integración en repasaYA

1. **Descriptores de Material en Astro**:
   - `src/content/materials/ade/derecho-fiscal/casos-practicos.json` (`type: "apuntes"`, `order: 6`, `pdf: "derecho-fiscal/casos-practicos-resueltos.pdf"`).
   - `src/content/materials/ade/derecho-fiscal/examenes-oficiales.json` (`type: "examen"`, `order: 7`, `pdf: "derecho-fiscal/examenes-oficiales-resueltos.pdf"`).
2. **Actualización de la Asignatura**:
   - `src/content/subjects/ade/derecho-fiscal.md`: Se añade `apuntes` y `examen` al array `materials: [guia, test, vf, flashcards, apuntes, examen]` y se actualiza la descripción informativa.

---

## ✅ 4. Verificación y Calidad

- **LaTeX Overfull**: 0 warnings de overfull hbox en ambos documentos (compilados 2 veces con `pdflatex`).
- **Astro Build**: Superado con éxito (`npm run build`, 105 páginas HTML estáticas generadas sin errores Zod).
- **Métricas (`npm run stats`)**:
  - Documentos PDF activos: **23** (+2 PDFs para Derecho Fiscal).
  - Bloques de material: **56** (+2 bloques).
  - Preguntas de test activas en la plataforma: **3.014**.
