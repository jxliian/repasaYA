# Spec 015: Extracción Fidedigna e Integración del Banco de Test Oficial de Derecho Fiscal (Temas 2 y 3: IRPF)

- **Fecha**: 2026-11-06
- **Estado**: Implementado
- **Ámbito**: Contenido Docente / ADE 5º Curso / Derecho Fiscal (UGR)
- **Documento Fuente**: `tipo-test/FIS/wuolah-app-2026-11-06-13-23-43.pdf` (`PREGUNTAS-DERECHO-T-2-3.pdf`)

---

## 1. Contexto y Objetivos

1. **Petición del Usuario**:
   - Extraer al 100% de fidelidad e identidad los tests de examen contenidos en el PDF `wuolah-app-2026-11-06-13-23-43.pdf` ubicado en la carpeta `tipo-test/FIS/` (correspondiente a Derecho Fiscal de la Facultad de CC. Económicas y Empresariales de la UGR).
   - Incorporar las preguntas de forma canónica a la asignatura **Derecho Fiscal** (`ade/derecho-fiscal`).
   - Tras la verificación técnica y de build, realizar la subida a Git/GitHub conforme al protocolo operativo y la directiva expresa del usuario.

2. **Criterios Pedagógicos y Técnicos**:
   - Mantener con total exactitud la formulación de los enunciados, datos numéricos de casos reales de IRPF (dietas, retribuciones en especie de vivienda y vehículos, aportaciones a planes de pensiones, exenciones del artículo 7 y 42 de la LIRPF, gastos deducibles por discapacidad del art. 19 LIRPF y reducciones por obtención de rendimientos del trabajo del art. 20 LIRPF).
   - Validar exhaustivamente los índices de opción correcta en base 0 (`correct: 0..3`).
   - Conservar y ampliar con rigor las justificaciones jurídicas paso a paso artículo por artículo para cada uno de los 42 ítems del documento.

---

## 2. Inventario de Preguntas Extraídas (42 Ítems Oficiales)

Las preguntas abarcan los bloques esenciales del IRPF (Temas 2 y 3 del programa docente de la UGR):

1. **IRPF: Naturaleza, Ámbito, Sujetos y Familia (Temas 2 y 3)**:
   - Pensiones compensatorias y desequilibrio económico vs. anualidades por alimentos (art. 17.2.f y 84 LIRPF).
   - Caracteres del IRPF: impuesto personal, progresivo, subjetivo y cedido parcialmente (50%) a las Comunidades Autónomas.
   - Diferencias normativas autonómicas: escala de tipos autonómica, tramos, deducciones y mínimo personal/familiar.
   - Régimen de unidad familiar: requisitos de convivencia y minoría de edad en hijos de matrimonios anteriores (art. 82 LIRPF).
   - Exenciones específicas: pensiones de orfandad (art. 7.h LIRPF).
   - Residencia fiscal: estatuto de diplomáticos y funcionarios españoles en el extranjero (colegio español en Marruecos, art. 10 LIRPF).
   - Imputación temporal en caso de fallecimiento y opciones de declaración individual o conjunta (art. 14 y 84 LIRPF).

2. **IRPF: Rendimientos del Trabajo, Dietas, Retribuciones en Especie y Reducciones (Tema 3)**:
   - Régimen tributario de las dietas de locomoción (0,19 €/km según escala del examen más peajes/parkings, art. 9 RIRPF).
   - Liquidación de dietas complejas con pernocta y sin pernocta en territorio nacional y extranjero (Granada, Madrid, Londres).
   - Retribuciones en especie:
     - Entrega de vehículos en propiedad: coste de adquisición más ingreso a cuenta no repercutido (art. 43.1.1ª.b LIRPF).
     - Cesión de uso de vehículos: 20% anual más ingreso a cuenta (art. 43.1.1ª.b LIRPF).
     - Utilización de vivienda de la empresa: porcentaje legal sobre valor catastral revisado / no revisado más ingreso a cuenta (art. 43.1.1ª.a LIRPF).
     - Primas de seguro de enfermedad a favor del trabajador y familia: límite exento de 500 € anuales por persona (art. 42.2.c LIRPF).
     - Entrega de acciones a trabajadores: límite de 12.000 € anuales exentos y tributación del exceso con ingreso a cuenta (art. 42.2.f LIRPF).
     - Préstamos a tipo cero para empleados bancarios: calificación como rendimiento en especie por diferencia con el interés legal (art. 43.1.1ª.c LIRPF).
     - Vales de comida / tarjetas restaurante: límite legal de 11 €/día exento e integración del exceso con ingreso a cuenta (art. 45 RIRPF).
     - Prestaciones de servicios propios de la empresa (viajes ofertados por agencias): valoración por valor de mercado público más ingreso a cuenta.
   - Gastos deducibles del art. 19 LIRPF: cotizaciones a la Seguridad Social, cuotas sindicales, 2.000 € de gastos generales e incrementos por discapacidad de trabajadores activos (3.500 € para 33%-64% y 7.750 € para $\ge 65\%$).
   - Planes de pensiones: aportaciones del promotor como rendimiento en especie no sujeto a ingreso a cuenta (art. 102.2 LIRPF); tributación íntegra de rescates por viudedad sin reducción del 30% por irregularidad (art. 18.2 LIRPF).
   - Prestaciones por desempleo y capitalización en pago único (art. 7.n LIRPF) e indemnizaciones por despido (art. 7.e LIRPF).
   - Imputación temporal por sentencias judiciales firmes de premios de antigüedad (art. 14.2.a LIRPF).

---

## 3. Impacto en Métricas y Catálogo

- **Banco de Test de Derecho Fiscal (`src/content/materials/ade/derecho-fiscal/test.json`)**:
  - Antes: 60 preguntas.
  - Incremento: +42 preguntas oficiales del examen.
  - Total: **102 preguntas tipo test interactivas**.
- **Total Preguntas de Derecho Fiscal**:
  - 102 Tipo Test + 51 Test de Supuestos de Examen + 50 V/F = **203 preguntas activas**.
- **Métricas Globales de repasaYA**:
  - Total preguntas activas: supera por primera vez los tres millares alcanzando **3.014 preguntas**.
  - Total tipo test: **2.284**.

---

## 4. Validación Técnica

- Esquema Zod de contenido validado con éxito.
- Compilación estática `npm run build` ejecutada sin advertencias ni errores:
  - 103 páginas generadas en `dist/`.
  - Rutas dinámicas `/ade/5/c1/derecho-fiscal/test/` y `/ade/5/c1/derecho-fiscal/` operativas.
