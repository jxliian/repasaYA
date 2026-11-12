# Spec 018 — Dirección Financiera: relación de problemas P1–P25 (rediseño corporativo)

## Cambios
- Nuevo PDF `public/ade/direccion-financiera/relacion-problemas-resueltos.pdf` (30 págs., antes 37) generado desde
  `apuntes/direccion-financiera/relacion_dfin.tex`. `compilar.sh` compila ahora apuntes y relación.
- Mismo estilo que los apuntes (spec 017): plantilla de soluciones, método común de proyectos, enunciado oficial
  literal en caja azul, resultado en verde, notas en rojo.
- Gráficos rehechos en TikZ: Fisher P1 (baja de r), P2 (r_e > r_p) y P3 (numérico, sin etiquetas solapadas);
  VAN(X) del punto muerto P16; líneas temporales de flujos (P11, P13, P19–P22); barras de CAE (P24) y de VA de
  costes (P25).
- `relacion-problemas.json`: título y descripción actualizados.
- Apuntes: corregidos avisos de `\headheight` y anclas de hyperref duplicadas (sin cambios de contenido).

## Verificación
- Enunciados cotejados con `RELACION_PROBLEMAS_DF_25-26` y soluciones oficiales P1–P3, P18–P22.
- Cifras recalculadas: P5 285,04 (285,01 sin redondear), P8 169,86, P9 693,25, P10 115,83, P11 48,64, P13 732.841,04,
  P16 38.244,36 (oficial 38.243), P17 2.317,57, P18 −104,32, P19 112.587,82, P20 10.388,30, P21 6.346.457,61,
  P22 ΔVAN 0, P24 8.596,99 / 8.996,19, P25 ahorro 500.000.
- Notas añadidas: P21 (transporte activado sin amortizar en la solución oficial), P22 (local "amortizado" con VNC
  500.000 en balance), P25 (sin solución oficial; con capacidad por estación saldría b).
- `pdflatex`: 0 Overfull, 0 avisos.
