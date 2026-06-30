# Tema oscuro + Hero logo 3D — Design Spec

**Fecha:** 2026-06-30
**Estado:** aprobado por el usuario ("así tal cual, todo de un tono").

Sobre la landing "Claro + Carrusel Dual" ya implementada, añadimos: (1) tema oscuro
conmutable con toggle sol/luna, (2) sustituir el contenido del hero por un wordmark
**"repasaYA" 3D glossy en WebGL** que se distorsiona al pasar el ratón (estilo
haoqi.design), (3) arreglar la transición hero→carrusel (corte duro), (4) reubicar la
frase de valor.

## Constraints globales

- **Sin llamadas externas de JS/fuentes** (regla de privacidad): Three.js y todo asset
  van empaquetados/self-hosted vía npm; cero red en runtime salvo el badge hits.sh.
- **Base path** `import.meta.env.BASE_URL` para URLs internas.
- **`prefers-reduced-motion`**: hero 3D en fotograma estático (sin flotación/giro);
  toggle de tema no anima.
- **Contraste AA** en ambos temas.
- **Verificación:** `npm run build` verde + check visual en `npm run dev` (no hay tests).
- **Commits frecuentes**, estilo del repo (`feat(ui): …`).

---

## Parte 1 · Tema oscuro + toggle sol/luna

**Tokens (Base.astro `:root`)**
- El `:root` actual queda como tema **claro** (default).
- Nuevo bloque `:root[data-theme="dark"]` sobre-escribe los mismos nombres de token:
  - `--bg #0e0e15`, `--surface #181826`, `--surface2 #21212f`
  - `--border rgba(255,255,255,0.10)`, `--glass-border rgba(255,255,255,0.10)`,
    `--glass #181826`, `--glass-hi #21212f`
  - `--accent #a78bea` (lavanda un punto más claro para legibilidad sobre oscuro),
    `--accent-strong #b89bf0`, `--accent-hover #b89bf0`,
    `--accent-soft rgba(167,139,234,0.16)`, `--accent-line rgba(167,139,234,0.34)`,
    `--accent2 #a78bea`, `--cyan #a78bea`
  - `--on-accent #15101f` (texto sobre lavanda claro en dark, para AA)
  - `--text #f3f2fa`, `--text-muted #a3a0b5`
  - `--correct #2fbf6c`, `--wrong #f0595e`, `--reveal #e0a93a`
  - `--header-bg rgba(18,18,30,0.78)`
- Nuevo token compartido `--particle` (lo consume el script de partículas):
  claro `60,52,110`; dark `167,139,234`. (Se define como **RGB sin alpha** para
  componer `rgba(var(--particle), x)` en JS leyendo `getComputedStyle`.)

**Init sin FOUC**
- Script **inline bloqueante** en `<head>` de `Base.astro`, antes del `<slot/>`:
  lee `localStorage.getItem('theme')`; si no existe, usa
  `matchMedia('(prefers-color-scheme: dark)')`; fija `document.documentElement.dataset.theme`.
- Persistencia en `localStorage('theme')` con valores `'light'|'dark'`.

**Toggle**
- Botón `<button data-theme-toggle aria-label="Cambiar tema">` con dos iconos SVG
  (sol/luna); CSS muestra el icono según `data-theme`.
- Ubicación: header de `index.astro` (en `.header-right`, antes de "Solicitar"),
  y en los `page-hdr` de `mapa.astro` y `privacidad.astro`, y en el `header` de
  `QuizEngine.astro`. Estilo: reutiliza `.hbtn`/icon-button redondo, neutro.
- Listener **global** en el script inline de Base (delegación en `document` →
  sobrevive a View Transitions): al click alterna `data-theme`, persiste, y emite
  `window.dispatchEvent(new Event('themechange'))`.

**Recolor por tema (lo que no va por token)**
- **Partículas** (`index.astro` script): leer color de `--particle` vía
  `getComputedStyle(document.documentElement)`; recalcular en `themechange`
  (re-init o actualizar variable interna). Líneas y nodos usan ese color.
- **Orbs** (`index.astro`, `mapa`, `privacidad`): ya lavanda translúcido; en dark
  subir un pelín la opacidad vía `[data-theme="dark"] .orb-*` (glow). Opcional menor.
- **Board del carrusel** (`SubjectCarousel.astro`): el gradiente claro
  `linear-gradient(135deg,#fcfbff,#f4eefe,#fbeef4)` → en dark
  `[data-theme="dark"] .cz-board { background: linear-gradient(135deg,#171622,#1c1830,#241a2b) }`.
  Blobs `.cz-blob` bajar opacidad en dark. `.cz-back`/`.cz-panel` usan
  `rgba(255,255,255,.85)` → en dark `rgba(30,28,44,.85)`.
- **Tarjetas carrusel**: tints por grupo (`--tint`/`--accent` de card) en dark se
  oscurecen levemente vía `[data-theme="dark"] .ccard[data-group=...]`.
- **Toast** `#2a2440` ya es oscuro: en dark cambiar a `--surface2` con borde.

---

## Parte 2 · Hero = wordmark "repasaYA" 3D (WebGL)

**Componente nuevo:** `src/components/HeroLogo3D.astro` (canvas + `<script>` con Three.js).
Sustituye el contenido textual actual del `.hero` en `index.astro`; el `.hero` sigue
siendo 100vh con los blobs aurora de fondo y la flecha "baja".

**Dependencia:** `three` (npm). Importar solo lo necesario (core + addons
`FontLoader`, `TextGeometry`, `RoomEnvironment`, y para hover `EffectComposer`/
`RenderPass`/`ShaderPass` con un shader RGB-shift propio). Todo bundled por Astro/Vite.

**Tipografía → geometría**
- Se necesita un `*.typeface.json` (formato facetype) para `TextGeometry`. Se genera
  **una vez** desde una fuente bold redondeada y se commitea en `src/assets/fonts/`
  (asset self-hosted). Candidata: Unbounded 700/800 (coherente con la marca) o, si la
  conversión da problemas, una redondeada equivalente. Render del texto **"repasaYA"**
  en **un solo tono** (decisión del usuario).
- Geometría inflada: `TextGeometry` con `bevelEnabled`, `bevelThickness`/`bevelSize`
  altos y `curveSegments` altos → cantos redondeados tipo globo. Centrar geometría
  (boundingBox) en el origen.

**Material y luz**
- `MeshPhysicalMaterial`: color lavanda (token-driven o fijo `#8a6bd8`), `roughness`
  baja, `clearcoat` alto, `clearcoatRoughness` baja, `envMap` desde
  `RoomEnvironment` (PMREM) → reflejos glossy. Fondo del canvas **transparente**
  (`alpha:true`) para que se vea la aurora/página.
- Luz suave de relleno + key light.

**Interacción**
- Idle: flotación/rotación muy sutil (seno del tiempo).
- Hover: el puntero sobre el canvas controla (a) parallax/tilt del mesh hacia el
  cursor, (b) intensidad de una **distorsión** (desplazamiento de vértices vía
  `onBeforeCompile` o un uniform de "wobble" que crece cerca del cursor) y (c)
  **aberración cromática** (ShaderPass RGB-shift) que sube en hover y decae al salir.
- `prefers-reduced-motion`: sin idle ni wobble; un render estático. (El composer puede
  desactivarse y hacer `renderer.render` simple.)

**Rendimiento / responsive / fallback**
- Carga **diferida**: inicializar tras `window load` (o `requestIdleCallback`), import
  dinámico de Three para no bloquear el first paint.
- `devicePixelRatio` cap a 2. Pausar el rAF cuando el hero no está en viewport
  (IntersectionObserver) y en `visibilitychange` oculto.
- **Móvil (<700px o coarse pointer):** sin postprocesado (sin aberración), wobble
  reducido o desactivado; si el dispositivo no soporta WebGL → **fallback CSS**.
- **Fallback CSS** (no WebGL): wordmark "repasaYA" en `var(--font-display)` grande,
  centrado, con sombra/gradiente lavanda. Markup presente siempre; el canvas se
  superpone y se oculta el fallback solo si WebGL arranca.
- Reinicio/cleanup en `astro:after-swap` (patrón `window.__heroLogo`: cancelar rAF,
  `renderer.dispose()`, quitar listeners) — igual que `__particles`/`__carousel`.

**Layout / centrado**
- El canvas ocupa el `.hero-inner` centrado (flex center ya existente). Al eliminar el
  titular de texto, el problema de "no centrado" desaparece. Verificar centrado real
  del canvas en el viewport.

---

## Parte 3 · Transición hero→carrusel

- Causa: borde duro a `min-height:100vh` con blobs aurora cortados en seco.
- Fix: `.hero::after` overlay no interactivo con
  `background: linear-gradient(to bottom, transparent 60%, var(--bg))` (alto ~30% del
  hero, `pointer-events:none`, `z-index` por encima de blobs y por debajo del canvas/
  contenido) → la aurora se disuelve hacia el fondo de la página. Funciona en claro y
  dark porque usa `var(--bg)`.
- Asegurar que la sección del carrusel arranca sobre `var(--bg)` continuo (sin caja con
  fondo distinto que reintroduzca un corte).

---

## Parte 4 · Frase de valor reubicada

- La descripción *"Tests interactivos, V/F y flashcards para las asignaturas de la
  carrera. Gratis, sin registro, sin anuncios."* sale del hero y pasa a una
  **tagline fina centrada justo encima del `<SubjectCarousel/>`** (un `<p>` con
  `--text-muted`, tamaño medio), para no perder el mensaje.

---

## Componentes / interfaces

- **`Base.astro`**: produce tokens (claro + `[data-theme="dark"]`), `--particle`, el
  script inline de tema (init + toggle global + evento `themechange`). Consumido por
  todo.
- **`HeroLogo3D.astro`** (nuevo): consume `three` y el `.typeface.json`; produce el
  canvas del hero + fallback. Autónomo (un propósito: render del wordmark 3D).
- **`index.astro`**: consume `HeroLogo3D`; el script de partículas pasa a leer
  `--particle` y a reaccionar a `themechange`; añade `.hero::after` y la tagline.
- **`SubjectCarousel.astro`**, **`QuizEngine.astro`**, **`mapa.astro`**,
  **`privacidad.astro`**: añaden overrides `[data-theme="dark"]` y (donde aplique) el
  botón de toggle.

## Criterios de éxito

1. Toggle sol/luna cambia todo el sitio claro↔oscuro, sin FOUC, persistente, en todas
   las páginas; coherente tras navegación (View Transitions).
2. Hero muestra "repasaYA" 3D glossy que se distorsiona/refracta al pasar el ratón;
   degrada a fallback CSS sin WebGL; estático con reduced-motion; no bloquea el load.
3. La transición hero→carrusel se ve fundida, sin corte, en ambos temas.
4. La frase de valor sigue presente (encima del carrusel).
5. `npm run build` verde; contraste AA en ambos temas.

## Riesgos / decisiones abiertas

- **Conversión de fuente a `typeface.json`**: principal riesgo. Si Unbounded no
  convierte limpio, usar una fuente bold redondeada equivalente (documentar cuál).
- **Fidelidad**: wordmark extruido glossy que *evoca* haoqi, no un globo modelado.
- **Peso**: Three.js ~150–200 KB solo en landing, diferido.
