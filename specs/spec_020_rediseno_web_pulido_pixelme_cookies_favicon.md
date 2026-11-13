# Spec 020 — Pulido del rediseño: sin emojis, desplegables propios, aviso de cookies, PixelMe y favicon

## Cambios
- Fuera todos los emojis del sitio: motor de tests (iconos de modo pasan a SVG de línea en granate; papelera de
  estadísticas en SVG), flashcards, guías (SCD, Derecho Fiscal, Organización de Empresas), mapa web, buscador
  global y cabeceras de catálogo. Radios de píldora (99px, 12–20px) pasan a `var(--radius)` y los morados
  heredados del tema antiguo, a granate.
- Buscador de la portada: los `<select>` nativos se sustituyen por desplegables propios (listbox con teclado:
  flechas, Intro, Esc) con el estilo de la web.
- Pestañas «Ambos grados / ADE / Informática»: quitada la barra de desplazamiento vertical que aparecía.
- Aviso de cookies abajo en la primera visita (`CookieNotice.astro`): informa de que no hay cookies, qué se
  guarda y enlaza a Privacidad. Se recuerda con `ry-aviso` (añadida a la tabla de Privacidad). Zero sube mientras
  el aviso está abierto.
- Pie: «Hecho con ganas por» pasa a «Developed by Julián Carrión, juliancarrion.dev».
- `PixelMe.astro`: Julián en vóxeles (three.js, render a baja resolución pixelado) estudiando en su escritorio con
  portátil, taza, libros y planta, a la derecha de la banda. Animación de cabeza, manos tecleando, vapor y vaivén
  de cámara; solo anima en pantalla, un fotograma con `prefers-reduced-motion`, oculto en < 960 px.
- Favicon e iconos (`favicon.svg/.ico`, PNG 32/48/192/512, `apple-touch-icon`) rehechos: «r.» blanca en Source
  Serif sobre granate con el punto dorado. `theme-color` granate.
- Controles de formulario heredan la tipografía de la web.

## Verificación
- `npm run build`: 112 páginas, sin errores. Consola del navegador sin errores en portada y test.
- Capturas revisadas de la portada (escena 3D con WebGL) y del motor de tests.
