# Rediseño "Claro + Carrusel Dual" — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Llevar repasaYA de su tema oscuro/lima a un tema **claro/pastel** con hero a
pantalla completa, navegación por **carrusel circular dual** y header con botones de
GitHub, manteniéndolo todo estático en Astro.

**Architecture:** Capa visual sobre tokens CSS globales en `Base.astro` (cambiar los
tokens recolorea casi todo el sitio), + un **componente nuevo** `SubjectCarousel.astro`
(canvas/DOM con motor `requestAnimationFrame`) que sustituye a la rejilla de tarjetas en
la landing. El resto de páginas se recolorean reemplazando valores oscuros/lima
hardcodeados.

**Tech Stack:** Astro 6 (static), CSS a mano con custom properties, JS vanilla en
`<script>`, fuentes self-hosted vía `@fontsource` (Unbounded nuevo; Space Grotesk y
JetBrains Mono ya instalados).

## Global Constraints

- **Sin llamadas externas de fuentes/JS** (coherencia con `/privacidad/`): fuentes solo
  self-hosted `@fontsource*`. Única llamada externa permitida: el badge de visitas de
  `hits.sh` (decisión del usuario).
- **Base path:** todas las URLs internas usan `import.meta.env.BASE_URL` (sitio servido
  en `/repasaYA`). No hardcodear `/`.
- **Acento lavanda** `#8a6bd8`. Tinta `#1b1b2e`. NADA de blanco puro como base (usar
  `#faf9fe`/pastel). NADA de texto blanco sobre lavanda claro (`--accent-soft`).
- **Contraste AA** obligatorio en botones y feedback de quiz.
- **`prefers-reduced-motion`**: desactiva rotación del carrusel, aurora y partículas
  (estados estáticos).
- **Verificación (no hay framework de tests):** cada tarea verifica con
  `npm run build` (Astro) **sin errores** + comprobación visual en `npm run dev`. La
  "prueba" de cada tarea es el build verde + el check visual descrito.
- **Commits frecuentes**, uno por tarea como mínimo. Mensajes en el estilo del repo
  (`feat(ui): …`, `fix(ui): …`).
- **Prototipos de referencia** (en disco, gitignored) en
  `.superpowers/brainstorm/18655-1782771731/content/`: `hero-direction.html`,
  `carousel-dual-v3.html`, `header.html`, `visits.html`. Son la **fuente visual de
  verdad**; portar de ahí.

---

### Task 1: Cimientos — tokens claros + fuente Unbounded

**Files:**
- Modify: `package.json` (dependencia `@fontsource/unbounded`)
- Modify: `src/layouts/Base.astro:1-92` (imports de fuente + bloque `:root` + grano)

**Interfaces:**
- Produces: el conjunto de tokens CSS globales que consumen TODAS las páginas:
  `--bg #faf9fe`, `--surface #ffffff`, `--surface2 #f5f1fd`, `--border rgba(20,20,40,.08)`,
  `--accent #8a6bd8`, `--accent-strong #7a5bcf`, `--accent-soft #ece6fb`,
  `--accent-line #d7ccf5`, `--on-accent #ffffff`, `--text #1b1b2e`, `--text-muted #6b6f86`,
  `--correct #1f9d57`, `--wrong #e5484d`, `--reveal #c98a00`,
  `--font-display 'Unbounded'`, `--font-body 'Space Grotesk Variable'`,
  `--font-mono 'JetBrains Mono Variable'`. (Se conserva `--header-bg` → `rgba(255,255,255,.78)`.)

- [ ] **Step 1: Instalar Unbounded**

```bash
npm install @fontsource/unbounded
```

- [ ] **Step 2: Importar Unbounded en `Base.astro`**

Tras las dos líneas de import de fuentes existentes (`src/layouts/Base.astro:3-4`) añade:

```astro
import '@fontsource/unbounded/500.css';
import '@fontsource/unbounded/700.css';
import '@fontsource/unbounded/800.css';
```

- [ ] **Step 3: Reescribir el bloque `:root`** (`src/layouts/Base.astro:45-70`) con los tokens claros

```css
:root {
  --bg:           #faf9fe;
  --surface:      #ffffff;
  --surface2:     #f5f1fd;
  --border:       rgba(20,20,40,0.08);
  --glass:        #ffffff;            /* compat */
  --glass-hi:     #f5f1fd;
  --glass-border: rgba(20,20,40,0.08);
  --accent:       #8a6bd8;            /* lavanda */
  --accent2:      #8a6bd8;            /* compat (ya no hay 2º color) */
  --accent-strong:#7a5bcf;
  --accent-hover: #7a5bcf;
  --accent-soft:  #ece6fb;
  --accent-line:  #d7ccf5;
  --on-accent:    #ffffff;
  --cyan:         #8a6bd8;            /* compat */
  --correct:      #1f9d57;
  --wrong:        #e5484d;
  --reveal:       #c98a00;
  --text:         #1b1b2e;
  --text-muted:   #6b6f86;
  --radius:       18px;
  --radius-lg:    26px;
  --header-bg:    rgba(255,255,255,0.78);
  --font-display: 'Unbounded', system-ui, -apple-system, sans-serif;
  --font-body:    'Space Grotesk Variable', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono Variable', ui-monospace, monospace;
}
```

- [ ] **Step 4: Cuerpo en fuente de cuerpo + grano más sutil** (`src/layouts/Base.astro:73-85`)

En `body { font-family: var(--font-display); ... }` cambia a `font-family: var(--font-body);`.
En `body::after` (grano) baja `opacity: 0.045` → `opacity: 0.02` y quita
`mix-blend-mode: overlay;` (sobre claro el overlay ensucia) → dejar sin blend.

- [ ] **Step 5: Build + check visual**

Run: `npm run build`
Expected: termina sin errores.
Visual (`npm run dev`): el sitio entero se ve en claro (fondos pálidos), aunque header,
hero y cards aún tengan estilos viejos. Los titulares que usen `--font-display` salen en
Unbounded.

- [ ] **Step 6: Commit**

```bash
git add package.json package-lock.json src/layouts/Base.astro
git commit -m "feat(ui): cimientos tema claro — tokens pastel + Unbounded (rediseño)"
```

---

### Task 2: Header / nav en claro + botones GitHub + fix móvil + visitas

**Files:**
- Modify: `src/pages/index.astro` — markup header `:594-626`, CSS header `:116-195`,
  CSS responsive `:540-577`.

**Interfaces:**
- Consumes: tokens de Task 1; constantes `ISSUE_URL`, `REPO_URL`, `PROFILE_URL` ya
  definidas en `:49-51`.
- Produces: `#search-input` (se conserva el id; lo consume el carrusel en Task 5).

- [ ] **Step 1: Markup del header** — reemplaza `.header-right` (`:612-625`) por:

```astro
<div class="header-right">
  <a class="hbtn b-ghost gh-only" href={PROFILE_URL} target="_blank" rel="noopener" aria-label="Seguir en GitHub">
    <svg class="gh" width="15" height="15" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 014 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
    <span>Seguir</span>
  </a>
  <a class="hbtn b-star gh-only" href={REPO_URL} target="_blank" rel="noopener" aria-label="Dar estrella en GitHub">★ <span>Star</span></a>
  <a class="hbtn b-accent" href={ISSUE_URL} target="_blank" rel="noopener" aria-label="Solicitar asignatura">
    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
    <span>Solicitar</span>
  </a>
  <div class="hits-pill gh-only" aria-label="Visitas">
    <span class="hits-lbl">👁 Visitas</span>
    <img class="hits-num" src="https://hits.sh/jxliian.github.io/repasaYA.svg?style=flat-square&label=&color=8a6bd8&labelColor=8a6bd8" alt="visitas" height="20" loading="lazy" />
  </div>
</div>
```

- [ ] **Step 2: CSS del header** — sustituye `.btn-neon`/`.hits-pill` (`:170-195`) y añade.
Portar estilos de `header.html` y `visits.html` (opción C segmentada). Valores clave:

```css
.site-header { background: var(--header-bg); border-bottom: 1px solid var(--border); backdrop-filter: blur(6px); }
.site-logo { color: var(--text); font-family: var(--font-display); }
.logo-dot { background: var(--accent); box-shadow: 0 0 8px rgba(138,107,216,.7); }
.search-wrap { background:#fff; border:1.5px solid var(--border); }
.search-wrap:focus-within { border-color: var(--accent); box-shadow:0 0 0 3px var(--accent-soft); }
.search-input { color: var(--text); } .search-input::placeholder { color:#9b9fb2; }
.search-icon { color:#9b9fb2; } .search-kbd { color:var(--text-muted); background:#f0f0f6; border:1px solid var(--border); }

.hbtn { display:inline-flex; align-items:center; gap:7px; border-radius:999px; padding:8px 14px;
  font-size:.82rem; font-weight:600; white-space:nowrap; border:1.5px solid transparent; transition:all .18s; }
.hbtn:hover { transform: translateY(-1px); }
.b-ghost { background:#fff; border-color:var(--border); color:var(--text); }
.b-star  { background:#fff8e8; border-color:#f0d699; color:#9a6b00; }
.b-accent{ background:var(--accent); color:var(--on-accent); box-shadow:0 6px 16px rgba(138,107,216,.32); }
.b-accent:hover { background:var(--accent-strong); }
.hits-pill { display:inline-flex; align-items:center; border-radius:8px; overflow:hidden; border:1.5px solid var(--border); }
.hits-lbl { font-family:var(--font-mono); font-size:.66rem; font-weight:700; letter-spacing:.04em;
  text-transform:uppercase; color:var(--text-muted); background:#efedf6; padding:6px 9px; }
.hits-num { display:block; background:var(--accent); }
```

- [ ] **Step 3: Fix responsive móvil** — en `@media (max-width:700px)` (`:552-577`) reemplaza
las reglas de `.btn-neon`/`.hits-pill` por:

```css
.gh-only { display: none; }              /* Seguir, Star y Visitas fuera en móvil */
.b-accent span { display: none; }        /* Solicitar solo icono */
.b-accent { padding: 8px 11px; }
```

Esto elimina el solapamiento (causa del bug): en móvil solo quedan logo + buscador +
Solicitar, sin elementos que se pisen.

- [ ] **Step 4: Build + check visual**

Run: `npm run build` → sin errores.
Visual: a ancho escritorio se ven **Seguir · ★ Star · ＋ Solicitar (lavanda) · Visitas**
(badge segmentado lavanda). Estrechando a <700px quedan solo logo + buscador + Solicitar
(icono), **sin solapes**. El número de visitas carga desde hits.sh.

- [ ] **Step 5: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat(ui): header claro con botones GitHub + visitas segmentadas + fix móvil"
```

---

### Task 3: Hero a pantalla completa (aurora + partículas recoloreadas + aviso scroll)

**Files:**
- Modify: `src/pages/index.astro` — bloque hero del bento `:663-710`, CSS del hero,
  bg-layer `:585-589`, script de partículas `:874-1019`, script constelación `:1025-1160`.

**Interfaces:**
- Consumes: tokens Task 1. `#particles-bg` canvas (ya existe en `.bg-layer`).
- Produces: sección `.hero` 100vh con `#particles-bg` recoloreado.

- [ ] **Step 1: Markup del hero** — reemplaza el `<article class="b-hero …>` (`:663-710`)
por una sección a pantalla completa (NO dentro del bento). Quita stats, wa-btn,
live-pill y el canvas `#hero-constellation`. Portar composición "Aurora centrada" de
`hero-direction.html` (opción A):

```astro
<section class="hero" aria-label="Bienvenida">
  <div class="hero-blob b1"></div><div class="hero-blob b2"></div><div class="hero-blob b3"></div>
  <div class="hero-inner">
    <h1 class="hero-h1">Estudia mejor,<br><span class="hero-grad">aprueba de verdad.</span></h1>
    <p class="hero-desc">Tests interactivos, V/F y flashcards para las asignaturas de la carrera. Gratis, sin registro, sin anuncios.</p>
  </div>
  <a class="hero-scroll" href="#carrusel" aria-label="Bajar a las asignaturas">baja<span class="chev" aria-hidden="true"></span></a>
</section>
```

- [ ] **Step 2: CSS del hero** — añadir (valores de `hero-direction.html`):

```css
.hero { position:relative; min-height:100vh; display:flex; flex-direction:column;
  align-items:center; justify-content:center; text-align:center; overflow:hidden; padding:24px; }
.hero-inner { position:relative; z-index:3; max-width:18ch; }
.hero-h1 { font-family:var(--font-display); font-weight:800; font-size:clamp(34px,6vw,72px);
  letter-spacing:-0.02em; line-height:1.02; color:var(--text); }
.hero-grad { color:var(--accent); }   /* fuera el gradiente morado-cyan */
.hero-desc { margin-top:18px; color:var(--text-muted); font-size:clamp(15px,2vw,18px); }
.hero-blob { position:absolute; border-radius:50%; filter:blur(60px); opacity:.55; z-index:1; }
.hero-blob.b1 { width:46%; height:60%; left:-6%; top:-10%; background:#dcd2ff; animation:drift1 14s ease-in-out infinite; }
.hero-blob.b2 { width:48%; height:64%; right:-8%; top:4%; background:#ffd9e4; animation:drift2 17s ease-in-out infinite; }
.hero-blob.b3 { width:42%; height:58%; left:24%; bottom:-22%; background:#cfeede; animation:drift3 20s ease-in-out infinite; }
@keyframes drift1 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(8%,6%) scale(1.12)} }
@keyframes drift2 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(-7%,8%) scale(1.1)} }
@keyframes drift3 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(5%,-7%) scale(1.14)} }
.hero-scroll { position:absolute; bottom:22px; left:50%; transform:translateX(-50%); z-index:4;
  display:flex; flex-direction:column; align-items:center; gap:4px; color:var(--text-muted);
  font-family:var(--font-mono); font-size:11px; letter-spacing:.22em; text-transform:uppercase; }
.hero-scroll .chev { width:18px; height:18px; border-right:2px solid var(--accent);
  border-bottom:2px solid var(--accent); transform:rotate(45deg); animation:bob 1.5s ease-in-out infinite; }
@keyframes bob { 0%,100%{transform:rotate(45deg) translate(0,0); opacity:.5} 50%{transform:rotate(45deg) translate(3px,3px); opacity:1} }
@media (prefers-reduced-motion: reduce){ .hero-blob,.chev{ animation:none } }
```

- [ ] **Step 3: Recolorear partículas** — en el script de partículas, cambia los colores
de lima a tinta translúcida:
  - `:947` `ctx!.fillStyle = 'rgba(198,241,53,0.55)';` → `'rgba(60,52,110,0.5)';`
  - `:960` `ctx!.strokeStyle = ` rgba(198,241,53,${alpha})` ;` → usar `rgba(70,60,120,${alpha})`
  - `:977` (líneas al cursor) idem → `rgba(110,95,200,${alpha})`

- [ ] **Step 4: Eliminar la constelación R** — borra el bloque `<script>` de
`initConstellation` (`:1025-1160`) entero (el hero ya no usa `#hero-constellation`).

- [ ] **Step 5: Build + check visual**

Run: `npm run build` → sin errores (verifica que no quede ninguna referencia a
`hero-constellation` ni a `initConstellation`).
Visual: el hero ocupa toda la pantalla; gradiente aurora derivando + partículas oscuras
sobre claro + titular Unbounded centrado + "baja ↓" abajo. Con reduced-motion, todo
estático.

- [ ] **Step 6: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat(ui): hero a pantalla completa — aurora + partículas claras + aviso scroll"
```

---

### Task 4: `subjects.ts` — campo `group`

**Files:**
- Modify: `src/data/subjects.ts:1-107`

**Interfaces:**
- Produces: `Subject.group: 'ade' | 'ing'` para todas las asignaturas. Lo consume Task 5.

- [ ] **Step 1: Ampliar la interface** (`:3-14`) añadiendo tras `type: QuizType;`:

```ts
  group: 'ade' | 'ing'; // carrusel: ADE/Economía vs Ingeniería
```

- [ ] **Step 2: Añadir `group` a cada asignatura** del array `subjects` (`:16-95`):
  - `economia-espanola` → `group: 'ade'`
  - `rrhh` → `group: 'ade'`
  - `organizacion-empresas` → `group: 'ade'`
  - `do1` → `group: 'ade'`
  - `sibw` → `group: 'ing'`
  - `dsd` → `group: 'ing'`
  - `mp` → `group: 'ing'`
  - `aef` → `group: 'ade'`
  (Resultado: ade=5, ing=3.) Actualiza también el comentario-plantilla `:96-106` para
  incluir `group`.

- [ ] **Step 3: Build**

Run: `npm run build`
Expected: sin errores de TypeScript (todas las entradas tienen `group`).

- [ ] **Step 4: Commit**

```bash
git add src/data/subjects.ts
git commit -m "feat(data): campo group (ade/ing) en subjects para el carrusel"
```

---

### Task 5: Componente `SubjectCarousel.astro` + integración en la landing

**Files:**
- Create: `src/components/SubjectCarousel.astro`
- Modify: `src/pages/index.astro` — sustituir filter-bar + secciones (`:738-778`) por
  `<SubjectCarousel/>`; eliminar el script de filtros viejo (`:807-866`); importar el
  componente; conservar Cmd/Ctrl+K (`:791-805`).

**Interfaces:**
- Consumes: `subjects` (con `group`) de `subjects.ts`; `#search-input` del header (Task 2).
- Produces: sección `#carrusel`.

- [ ] **Step 1: Crear `SubjectCarousel.astro`** portando `carousel-dual-v3.html` con estas
adaptaciones EXACTAS (no copiar el `DATA` inline del prototipo; renderizar desde
`subjects.ts`):

Frontmatter:
```astro
---
import { subjects } from '../data/subjects';
const base = import.meta.env.BASE_URL.replace(/\/?$/, '/');
const ade = subjects.filter(s => s.group === 'ade');
const ing = subjects.filter(s => s.group === 'ing');
const href = (s) => s.external ?? `${base}${s.slug}/`;
const hasFlash = (s) => s.chips.some(c => c.toLowerCase().includes('flashcard'));
---
```

Markup: la misma estructura `.cz-board` del prototipo (labels `#labA`/`#labI`, `#panel`
con filtros→buscador→contador, `#back`, `#toast`), pero las cards se renderizan en el
servidor desde `ade`/`ing`, cada una como:
```astro
<a class="ccard" data-group="ade" data-type={s.type} data-fc={hasFlash(s) ? '1':'0'}
   data-title={s.title.toLowerCase()} data-code={s.code.toLowerCase()}
   href={href(s)} {...(s.external ? {target:'_blank', rel:'noopener'} : {})}>
  <div class="cc-icon">{s.icon}</div>
  <div class="cc-title">{s.title}</div>
  <div class="cc-area">{s.code}</div>
  <div class="cc-extra">
    <div class="cc-desc">{s.description}</div>
    <div class="cc-chips">{s.chips.map(c => <span class="cc-chip">{c}</span>)}</div>
    <span class="cc-cta">Entrar →</span>
  </div>
</a>
```
(Para `ing`, `data-group="ing"`.)

CSS: portar tal cual el `<style>` del prototipo, pero **sustituir colores literales por
tokens** donde aplique (`#8a6bd8`→`var(--accent)`, tinta→`var(--text)`/`--text-muted`,
bordes→`var(--border)`). Mantener los tintes por grupo (ADE lavanda `#efe9ff`/`#7b6cf0`,
ING azul `#e7f1ff`/`#4f8fd1`) como reglas `.ccard[data-group="ade"]` /
`[data-group="ing"]` que fijan `--tint`/`--accent` de la card.

Script (`<script>` de Astro): portar el motor `requestAnimationFrame` del prototipo con
estos cambios respecto al `DATA` inline:
  - Construir `cards` leyendo los `<a class="ccard">` ya presentes en el DOM y sus
    `data-*` (group/type/fc/title/code) en vez de crearlos desde un array JS.
  - `pass(c)` usa `c.el.dataset.title`/`.dataset.code` para la query y
    `.dataset.type`/`.dataset.fc` para filtros.
  - **Sincronizar buscador del header:** además de `#cq` (panel), enganchar
    `#search-input` (header) al mismo `setQ`. En overview, la query filtra ambos grupos;
    en focus, solo el grupo enfocado (igual que el prototipo).
  - Clic en card: en overview → `focus(group)`; en focus → navegar (`window.location =
    el.href`) en vez del toast.
  - `prefers-reduced-motion`: no incrementar `spin` (anillo estático) — ya contemplado
    en el prototipo (`reduce`).
  - Reinicio en `astro:after-swap` (View Transitions): envolver el init en una función e
    invocarla en carga y en `astro:after-swap`, guardando estado en `window.__carousel`
    para cancelar el rAF anterior (mismo patrón que `initParticles`).

- [ ] **Step 2: Integrar en la landing** — en `index.astro`:
  - Añadir al frontmatter: `import SubjectCarousel from '../components/SubjectCarousel.astro';`
  - Reemplazar el bloque filter-bar + no-results + las dos `<section class="subject-section">`
    (`:738-778`) por: `<SubjectCarousel />`.
  - Eliminar el `<script>` de filtros viejo (`:807-866`: `applyFilters`, listeners de
    `data-degree`/`data-mtype`). Conservar el bloque Cmd/Ctrl+K (`:791-805`) pero quitar
    de él la llamada `applyFilters()` del Escape (sustituir por limpiar el input y dejar
    que el input event del carrusel reaccione).

- [ ] **Step 3: Build + check visual**

Run: `npm run build` → sin errores (ni referencias colgando a `applyFilters`,
`SubjectCard`, `filter-bar`, `subject-section` si ya no se usan; si `SubjectCard` se usa
en `mapa.astro` u hubs, NO borrarlo, solo dejar de usarlo aquí).
Visual: bajo el hero aparecen **dos carruseles** (ADE/Economía izq, Ingeniería der)
girando; clic en una mitad enfoca y superpone; panel derecho con filtros→buscador→
contador; flecha ← vuelve; buscar `fin` dentro de ADE deja 1 card grande; el buscador
del header filtra igual. Reduced-motion: anillos estáticos.

- [ ] **Step 4: Commit**

```bash
git add src/components/SubjectCarousel.astro src/pages/index.astro
git commit -m "feat(ui): carrusel circular dual de asignaturas (sustituye la rejilla)"
```

---

### Task 6: Novedades (timeline) + GitHub CTAs + footer en claro

**Files:**
- Modify: `src/pages/index.astro` — timeline `:641-661` + su CSS; bento GitHub CTAs
  `:712-734` (eliminar); footer `:782-786` + CSS footer `:520-532`; CSS del bento/stats.

**Interfaces:**
- Consumes: tokens Task 1.

- [ ] **Step 1: Mover y recolorear Novedades** — sacar el `<article class="b-timeline">`
(`:641-661`) fuera del bento, colocándolo **después** del `<SubjectCarousel/>` como
sección propia (`<section class="novedades">…`). Recolorear su CSS: fondo `var(--surface)`,
borde `var(--border)`, quitar cualquier `backdrop-filter`, badges/nodos a `var(--accent)`,
texto a `var(--text)`/`--text-muted`. El fallback "Sin historial" (`:659`) cambia el color
inline a `var(--text-muted)`.

- [ ] **Step 2: Eliminar las CTAs de GitHub del bento** (`:712-734`, `cta-gh` y `cta-star`)
y, si el `.bento` queda vacío, eliminar el contenedor `.bento` y su CSS asociado
(`:207-…`). Las stats del hero (`stat-chip`) ya se quitaron en Task 3; si quieres
conservarlas, móntalas como fila ligera dentro de `.novedades` con tokens claros (opcional).

- [ ] **Step 3: Footer en claro** (`CSS :520-532`):

```css
footer { border-top:1px solid var(--border); color:var(--text-muted); }
.footer-meta { color:#a8acbb; }
footer a { color: var(--accent); }
footer a:hover { color: var(--accent-strong); }
```

- [ ] **Step 4: Build + check visual**

Run: `npm run build` → sin errores.
Visual: bajo el carrusel, la sección **Novedades** en claro (timeline legible);
**no** quedan las tarjetas GitHub del bento (ahora están en la nav); footer claro con
enlaces lavanda.

- [ ] **Step 5: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat(ui): Novedades + footer en claro; CTAs GitHub fuera del bento"
```

---

### Task 7: SubjectCard + DegreeCard + QuizEngine en claro

**Files:**
- Modify: `src/components/SubjectCard.astro:61-181` (CSS) — quitar glass/lima.
- Modify: `src/components/DegreeCard.astro` (CSS) — recolorear a claro.
- Modify: `src/components/QuizEngine.astro` (CSS) — recolorear + feedback acierto/error.

**Interfaces:**
- Consumes: tokens Task 1.

- [ ] **Step 1: SubjectCard** — en su `<style>`:
  - `.scard`: `background:var(--surface)`; `border:1px solid var(--border)`;
    `box-shadow:0 10px 26px rgba(70,60,120,0.10)`; **quitar** `backdrop-filter` si lo
    hubiera (aquí ya es sólida).
  - hover (`:90-97`): `border-color:var(--accent-line)`; sombra lavanda suave
    `0 18px 40px rgba(70,60,120,0.18)`.
  - spotlight (`:100-108`): cambiar `rgba(198,241,53,0.14)` → `rgba(138,107,216,0.10)`.
  - línea superior (`:112-116`): `background:var(--accent)`.
  - icono/badge/chip/arrow: ya usan `var(--accent*)`; al cambiar tokens en Task 1 quedan
    lavanda. Verificar contraste de `.b-*` (texto lavanda sobre `--accent-soft` claro: OK).

- [ ] **Step 2: DegreeCard** — recolorear igual (fondo `--surface`, borde `--border`,
acento lavanda, sin glass). Revisar y reemplazar cualquier literal lima `#c6f135` /
`rgba(198,241,53,…)` por `var(--accent)`/`var(--accent-soft)`.

- [ ] **Step 3: QuizEngine** — recolorear superficies a claro y, CRÍTICO, el feedback:
  - Opciones/botones lima → `var(--accent)` con texto `var(--on-accent)`.
  - **Acierto** usa `var(--correct)` (#1f9d57, verde oscuro legible sobre claro);
    **error** `var(--wrong)` (#e5484d). Asegurar que el botón seleccionado correcto y el
    incorrecto se distinguen claramente sobre fondo blanco (texto blanco sobre verde/rojo
    sólidos; o texto del color sobre fondo `tint` claro, con contraste AA).
  - Reemplazar cualquier `#c6f135` / `rgba(198,241,53,…)` / morados `#7c6dfe` etc.
    hardcodeados por tokens.

- [ ] **Step 4: Build + check visual**

Run: `npm run build` → sin errores.
Visual: abre un hub (`/repasaYA/rrhh/`) y un quiz; las tarjetas y el motor de quiz se ven
en claro; al responder, **acierto verde** y **error rojo** claramente distintos, con
texto legible (AA).

- [ ] **Step 5: Commit**

```bash
git add src/components/SubjectCard.astro src/components/DegreeCard.astro src/components/QuizEngine.astro
git commit -m "feat(ui): SubjectCard/DegreeCard/QuizEngine en claro + feedback quiz AA"
```

---

### Task 8: Resto de páginas en claro (hubs, glosarios, mapa, privacidad, secreto)

**Files:**
- Modify: `src/pages/*/index.astro` (8 hubs), `src/pages/*/glosario.astro` (aef, rrhh,
  sibw, organizacion-empresas), `src/pages/mapa.astro`, `src/pages/privacidad.astro`,
  `src/pages/organizacion-empresas/secreto.astro`.

**Interfaces:**
- Consumes: tokens Task 1; componentes recoloreados Task 7.

- [ ] **Step 1: Barrido de literales oscuros/lima** — en cada archivo, localizar y
reemplazar por tokens:

```bash
grep -rnE "#c6f135|198,241,53|backdrop-filter|#050505|#060608|rgba\(255,255,255,0\.0|#7c6dfe|108,99,255|124,109,254|c4b5fd|a78bfa" src/pages
```
  - lima `#c6f135` / `rgba(198,241,53,…)` → `var(--accent)` / `var(--accent-soft)`.
  - fondos oscuros `#050505`/`#060608`/`#0d0d12` → `var(--bg)`/`var(--surface)`.
  - `backdrop-filter: blur(...)` → eliminar (superficies sólidas).
  - bordes `rgba(255,255,255,0.0x)` → `var(--border)`.
  - textos `rgba(255,255,255,.x)` → `var(--text)`/`var(--text-muted)`.
  - morados legados → `var(--accent)`.

- [ ] **Step 2: Revisión página a página** — abrir cada ruta en dev y ajustar contrastes
puntuales (la página `secreto` y `privacidad` suelen tener estilos propios). El header de
estas páginas usa el de su layout/markup; si replican el header viejo, alinear con Task 2.

- [ ] **Step 3: Build + check visual (recorrido completo)**

Run: `npm run build` → sin errores.
Run: `grep -rnE "#c6f135|198,241,53|backdrop-filter|#050505|#060608" src/` → **sin
resultados** (salvo comentarios). 
Visual: recorrer landing → hub → quiz → glosario → mapa → privacidad → secreto: todo en
claro, coherente, sin parches oscuros ni restos lima.

- [ ] **Step 4: Commit**

```bash
git add src/pages
git commit -m "feat(ui): resto de páginas (hubs, glosarios, mapa, privacidad, secreto) en claro"
```

---

## Self-Review (hecha)

- **Cobertura del spec:** §3.1 tokens→T1; §3.2 fuentes→T1; §3.3 partículas→T3; §3.4
  hero→T3; §3.5 carrusel→T4+T5; §3.6 header/visitas→T2; §3.7 Novedades→T6; §3.8
  footer→T6; §4 estructura landing→T3/T5/T6; §6 quiz/recolor→T7+T8; criterios de éxito
  cubiertos por los checks visuales y el grep final de T8.
- **Recencia "8 más recientes" (§3.5):** hoy ≤8 por grupo → se muestran todas; el campo
  `updatedAt`/orden queda como mejora futura no bloqueante (anotado en el spec). No
  requiere tarea para el estado actual.
- **Placeholders:** ninguno "TBD/TODO"; las piezas grandes referencian prototipos
  concretos y commiteables con adaptaciones explícitas.
- **Consistencia de nombres:** `#search-input` (header) se produce en T2 y se consume en
  T5; `Subject.group` se produce en T4 y se consume en T5; tokens de T1 consumidos por
  todas.
```
