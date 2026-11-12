# Spec 019 — Rediseño corporativo de la web (granate y oro)

## Cambios
- Sistema visual nuevo en `src/styles/tokens.css` y `base.css`: un único tema claro, granate `#7a1f2b` y oro
  `#d9a13a`, titulares en Source Serif 4 (la misma familia que los PDF), texto en Source Sans 3 y marca en
  IBM Plex Sans Condensed (fuentes autoalojadas con Fontsource). Los nombres de token antiguos siguen existiendo
  como alias, así el motor de tests y las guías adoptan la paleta sin reescribirse.
- Fuera: tema oscuro y su selector, partículas, nebulosa, cristal, brillos, grano, cursor de estrella y logo 3D
  (`Hero`, `HeroLogo3D`, `ParticleField`, `ThemeToggle`).
- Portada: banda granate con patrón nazarí y buscador (asignatura, grado, curso); «Seguir donde lo dejaste»
  (clave `ry-recent`, la escribe la página de asignatura); plan de estudios curso × cuatrimestre con los dos
  grados juntos y cifras reales por asignatura; novedades desde git; opiniones en rejilla.
- Cabecera corporativa con navegación (segunda fila desplazable en móvil) y pie granate con columnas, contador
  de visitas (una sola petición a hits.sh por build: `fetchHitsOnce`) y firma.
- «Sobre mí»: QR regenerado en SVG (`src/assets/qr-repasaYA.svg`) bajo la presentación; caja de mensaje con
  altura fija (antes se podía estirar sin límite) y contador.
- RepasaBot pasa a **Zero**: busca en `search-index.json` entendiendo grado, curso y tipo de material, y mantiene
  las dudas frecuentes. Conserva el archivo `RepasaBot.astro` y el id `#repasa-bot-root`.
- Ficha de asignatura con materiales en filas y lateral; páginas de grado, curso y cuatrimestre con listas en vez
  de tarjetas con emojis; filtros como botones rectos; migas y cabeceras con el punto dorado.
- Privacidad: sustituida la clave `theme` por `ry-recent`.

## Verificación
- `npm run build`: 112 páginas, sin errores.
- Capturas revisadas: portada (escritorio y móvil), Dirección Financiera, ADE, test, flashcards, privacidad,
  mapa web y guía de Organización de Empresas.
- `npm run stats`: sin cambios de contenido (26 PDF, 64 asignaturas, 62 bloques).

## Pendiente
- `QuizEngine.astro` conserva emojis y píldoras propias; su botón de tema se oculta y el de GitHub pasa a la
  izquierda desde `base.css`.
