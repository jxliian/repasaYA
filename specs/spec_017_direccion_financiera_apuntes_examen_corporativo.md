# Spec 017 — Dirección Financiera: apuntes de examen T1–T4 (rediseño corporativo)

## Cambios
- Nuevo PDF `public/ade/direccion-financiera/apuntes-primer-parcial.pdf` (17 págs., antes 24) generado desde
  `apuntes/direccion-financiera/apuntes_dfin.tex` (`./compilar.sh`).
- Estilo corporativo (azul marino/dorado), cajas por tipo (fórmula, examen, trampa, ejemplo), mapa del examen,
  procedimiento multietapa DDM/VAOC, checklist de proyecto, CAE (inflación y cambio tecnológico), demanda estacional,
  formulario de una página y 20 V/F.
- `apuntes.json`: título y descripción actualizados.

## Verificación
- Relación de problemas P1–P25 recalculada numéricamente: todos los resultados coinciden con las soluciones oficiales.
- Notas: P16 (exacto 38.244,36 → 38.245; oficial 38.243 por redondeo del factor), P25 (método de cátedra con capacidad
  anual → *d*), errata diapositiva 69 T2 (−7,27 → −7,57).
- `pdflatex`: 0 Overfull. `npm run build`: Complete! Métricas sin cambios (26 PDFs).
