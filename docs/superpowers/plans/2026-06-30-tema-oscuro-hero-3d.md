# Tema oscuro + Hero logo 3D — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Añadir tema oscuro conmutable (toggle sol/luna, sin FOUC) y sustituir el hero por un wordmark "repasaYA" 3D glossy en WebGL que se distorsiona al pasar el ratón, arreglando además la transición hero→carrusel.

**Architecture:** Tema por tokens CSS en `Base.astro` (`:root` claro + `:root[data-theme="dark"]`), conmutados por un script inline anti-FOUC y un `ThemeToggle.astro` compartido. El hero pasa a un componente `HeroLogo3D.astro` (Three.js empaquetado local, carga diferida, fallback CSS). El resto se recolorea con overrides `[data-theme="dark"]`.

**Tech Stack:** Astro 6 (static), CSS custom properties, JS vanilla, **Three.js** (npm, self-hosted) con addons `FontLoader`/`TextGeometry`/`RoomEnvironment`/`EffectComposer`/`RGBShiftShader`.

## Global Constraints

- **Sin llamadas externas de JS/fuentes:** Three.js y la fuente (typeface json del propio paquete `three`) van empaquetados por Vite. Única red en runtime: badge hits.sh.
- **Base path:** URLs internas con `import.meta.env.BASE_URL`.
- **`prefers-reduced-motion`:** hero 3D en fotograma estático; nada de auto-giro/flotación/wobble.
- **Contraste AA** en claro y oscuro.
- **Verificación (no hay framework de tests):** cada tarea = `npm run build` sin errores + check visual en `npm run dev`. Esa es la "prueba".
- **Commits frecuentes**, uno por tarea mínimo, estilo `feat(ui): …` / `feat(theme): …`.
- **Acento lavanda** claro `#8a6bd8`, dark `#a78bea`. Tinta clara `#1b1b2e`; texto dark `#f3f2fa`.
- **Spec de referencia:** `docs/superpowers/specs/2026-06-30-tema-oscuro-hero-3d-design.md`.

---

### Task 1: Tokens de tema oscuro + token `--particle` + init anti-FOUC + toggle global

**Files:**
- Modify: `src/layouts/Base.astro` (bloque `:root`, head `is:inline` script, script módulo del toggle)

**Interfaces:**
- Produces: atributo `document.documentElement.dataset.theme` (`'light'|'dark'`); token CSS `--particle` (RGB sin alpha); evento global `window` `'themechange'`; persistencia `localStorage('theme')`. Lo consumen Tasks 3, 5 y el resto de páginas.

- [ ] **Step 1: Añadir token `--particle` al `:root` claro**

En `src/layouts/Base.astro`, dentro de `:root { … }`, tras `--text-muted: #6b6f86;` añade:

```css
      --particle:     60,52,110;   /* RGB (sin alpha) para el canvas de fondo */
```

- [ ] **Step 2: Añadir el bloque de tema oscuro**

Justo **después** del cierre del `:root { … }` (antes de `*, *::before, *::after`), añade:

```css
    :root[data-theme="dark"] {
      --bg:           #0e0e15;
      --surface:      #181826;
      --surface2:     #21212f;
      --border:       rgba(255,255,255,0.10);
      --glass:        #181826;
      --glass-hi:     #21212f;
      --glass-border: rgba(255,255,255,0.10);
      --accent:       #a78bea;
      --accent2:      #a78bea;
      --accent-strong:#b89bf0;
      --accent-hover: #b89bf0;
      --accent-soft:  rgba(167,139,234,0.16);
      --accent-line:  rgba(167,139,234,0.34);
      --on-accent:    #15101f;
      --cyan:         #a78bea;
      --correct:      #2fbf6c;
      --wrong:        #f0595e;
      --reveal:       #e0a93a;
      --text:         #f3f2fa;
      --text-muted:   #a3a0b5;
      --header-bg:    rgba(18,18,30,0.78);
      --particle:     167,139,234;
    }
    color-scheme: light dark;
```

(Quita la línea `color-scheme: light dark;` si tu linter la marca fuera de regla; es opcional.)

- [ ] **Step 3: Script anti-FOUC en el `<head>`**

En `src/layouts/Base.astro`, **antes** de `</head>` (después del `<ClientRouter />` o del `<style>`), añade un script inline bloqueante:

```astro
  <script is:inline>
    (function () {
      try {
        var t = localStorage.getItem('theme');
        if (!t) t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        document.documentElement.dataset.theme = t;
      } catch (e) { document.documentElement.dataset.theme = 'light'; }
    })();
  </script>
```

- [ ] **Step 4: Listener global del toggle (sobrevive a View Transitions)**

Antes de `</body>` (tras el `<slot />`), añade un `<script>` (módulo Astro):

```astro
<script>
  // Delegación en document: un solo listener que sobrevive a navegación.
  function applyTheme(t: string) {
    document.documentElement.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch (e) {}
    window.dispatchEvent(new Event('themechange'));
  }
  if (!(window as any).__themeBound) {
    (window as any).__themeBound = true;
    document.addEventListener('click', (e) => {
      const btn = (e.target as HTMLElement)?.closest('[data-theme-toggle]');
      if (!btn) return;
      const cur = document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light';
      applyTheme(cur === 'dark' ? 'light' : 'dark');
    });
  }
</script>
```

- [ ] **Step 5: Build + check visual**

Run: `npm run build` → sin errores.
Visual (`npm run dev`): por defecto se ve igual (claro) salvo que tu SO pida dark.
En la consola del navegador, `document.documentElement.dataset.theme = 'dark'` debe oscurecer fondo/superficies/texto de toda la página al instante (tokens). Recarga → mantiene el último valor si lo guardaste con `localStorage`.

- [ ] **Step 6: Commit**

```bash
git add src/layouts/Base.astro
git commit -m "feat(theme): tokens tema oscuro + init anti-FOUC + toggle global"
```

---

### Task 2: Componente `ThemeToggle.astro` + insertarlo en todos los headers

**Files:**
- Create: `src/components/ThemeToggle.astro`
- Modify: `src/pages/index.astro` (header `.header-right`), `src/pages/mapa.astro` (`.page-hdr`), `src/pages/privacidad.astro` (`.page-hdr`), `src/components/QuizEngine.astro` (`header`)

**Interfaces:**
- Consumes: el listener global de Task 1 (busca `[data-theme-toggle]`).
- Produces: botón reutilizable `<ThemeToggle />`.

- [ ] **Step 1: Crear `src/components/ThemeToggle.astro`**

```astro
---
// Botón sol/luna. El listener vive en Base.astro (delegación global).
---
<button type="button" class="theme-toggle" data-theme-toggle aria-label="Cambiar tema claro/oscuro" title="Cambiar tema">
  <svg class="ic-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
    <circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/>
  </svg>
  <svg class="ic-moon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>
  </svg>
</button>

<style>
  .theme-toggle {
    display: inline-flex; align-items: center; justify-content: center;
    width: 38px; height: 38px; flex-shrink: 0;
    border-radius: 999px; cursor: pointer;
    background: var(--surface); border: 1.5px solid var(--border);
    color: var(--text); transition: all .18s;
  }
  .theme-toggle:hover { border-color: var(--accent); color: var(--accent); transform: translateY(-1px); }
  /* Mostrar sol en claro, luna en oscuro */
  .theme-toggle .ic-moon { display: none; }
  :global(html[data-theme="dark"]) .theme-toggle .ic-sun  { display: none; }
  :global(html[data-theme="dark"]) .theme-toggle .ic-moon { display: inline; }
</style>
```

- [ ] **Step 2: Insertar en el header de `index.astro`**

Importar en el frontmatter (junto a los otros imports):

```astro
import ThemeToggle from '../components/ThemeToggle.astro';
```

En el markup, dentro de `<div class="header-right">`, **antes** del `<a class="hbtn b-accent" …>Solicitar</a>`, añade:

```astro
    <ThemeToggle />
```

- [ ] **Step 3: Insertar en `mapa.astro` y `privacidad.astro`**

En cada uno, importar en frontmatter:

```astro
import ThemeToggle from '../components/ThemeToggle.astro';
```

En el `<header class="page-hdr">`, **antes** de `<a class="back-link" …>`, añade:

```astro
  <ThemeToggle />
```

(Si `back-link` usa `margin-left:auto`, queda el toggle a la izquierda del enlace; añade `style="margin-left:auto"` al `<ThemeToggle />` envuelto, o mueve el `margin-left:auto` al toggle. Implementación: en ambas páginas cambia `.back-link { … margin-left: auto; }` para que el `margin-left:auto` lo lleve el primer elemento del grupo derecho — pon el toggle con `style="margin-left:auto"` y quita `margin-left:auto` de `.back-link`.)

- [ ] **Step 4: Insertar en el header de `QuizEngine.astro`**

En el `<header>` (línea ~134), dentro del segundo bloque (el de stats a la derecha), o como elemento previo a `#hdr-stats`. Sustituye:

```astro
  <div style="font-size:.78rem;color:var(--text-muted)" id="hdr-stats">
```

por (añadiendo el toggle antes):

```astro
  <div style="display:flex;align-items:center;gap:12px">
    <button type="button" class="theme-toggle" data-theme-toggle aria-label="Cambiar tema" title="Cambiar tema" style="width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:var(--surface2);border:1px solid var(--border);color:var(--text);cursor:pointer">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
    </button>
    <span style="font-size:.78rem;color:var(--text-muted)" id="hdr-stats">
```

y cierra: cambia el `</div>` que cerraba el `#hdr-stats` por `</span>\n  </div>` (el `#hdr-stats` pasa a `<span>`; mantén su contenido `{hasVF && …}` igual).

(QuizEngine no usa `<Base>` con el toggle global → el listener global de Base SÍ aplica porque QuizEngine se renderiza dentro de páginas que usan `<Base>`. Verificar que las páginas de quiz envuelven con `<Base>`; si alguna no, el toggle no responderá: en ese caso, omitir el toggle del QuizEngine. **Comprobar antes**: `grep -L "layouts/Base" src/pages/*/quiz.astro`.)

- [ ] **Step 5: Build + check visual**

Run: `npm run build` → sin errores.
Visual: en cada página (index, mapa, privacidad, un quiz) aparece el botón sol/luna; al pulsarlo todo conmuta claro↔oscuro y persiste al recargar y al navegar entre páginas.

- [ ] **Step 6: Commit**

```bash
git add src/components/ThemeToggle.astro src/pages/index.astro src/pages/mapa.astro src/pages/privacidad.astro src/components/QuizEngine.astro
git commit -m "feat(theme): toggle sol/luna en todos los headers"
```

---

### Task 3: Recolor por tema de lo no-tokenizado (partículas, carrusel, orbs, toast)

**Files:**
- Modify: `src/pages/index.astro` (script de partículas + overrides `[data-theme="dark"]` de orbs)
- Modify: `src/components/SubjectCarousel.astro` (overrides dark del board/blobs/back/panel/tints/toast)

**Interfaces:**
- Consumes: token `--particle` y evento `themechange` (Task 1).

- [ ] **Step 1: Partículas leen `--particle` y reaccionan a `themechange`**

En `src/pages/index.astro`, dentro de `initParticles()`, tras `const reduce = …`, añade una variable de color viva:

```ts
    let pRGB = getComputedStyle(document.documentElement).getPropertyValue('--particle').trim() || '60,52,110';
    const onTheme = () => { pRGB = getComputedStyle(document.documentElement).getPropertyValue('--particle').trim() || pRGB; };
    window.addEventListener('themechange', onTheme);
```

Sustituye los 3 colores hardcodeados del dibujo:
- `ctx!.fillStyle = 'rgba(60,52,110,0.5)';` → `ctx!.fillStyle = ` + "`rgba(${pRGB},0.5)`" + `;`
- línea entre partículas `` `rgba(70,60,120,${alpha})` `` → `` `rgba(${pRGB},${alpha})` ``
- línea al cursor `` `rgba(110,95,200,${alpha})` `` → `` `rgba(${pRGB},${Math.min(alpha*1.6,0.6)})` ``

En el `cleanup()` del `state`, añade `window.removeEventListener('themechange', onTheme);`.

- [ ] **Step 2: Orbs más visibles en dark (index.astro `<style>`)**

Tras las reglas `.orb-tl`/`.orb-br`, añade:

```css
:root[data-theme="dark"] .orb-tl,
:root[data-theme="dark"] .orb-br { filter: blur(100px); opacity: 1.4; }
```

- [ ] **Step 3: Overrides dark del carrusel (`SubjectCarousel.astro` `<style>`)**

Al final del `<style>` del componente añade:

```css
  :global(html[data-theme="dark"]) .cz-board {
    background: linear-gradient(135deg, #171622 0%, #1c1830 55%, #241a2b 100%);
  }
  :global(html[data-theme="dark"]) .cz-blob { opacity: .34; }
  :global(html[data-theme="dark"]) .cz-blob.x1 { background: #4b3a86; }
  :global(html[data-theme="dark"]) .cz-blob.x2 { background: #2f5a47; }
  :global(html[data-theme="dark"]) .cz-back,
  :global(html[data-theme="dark"]) .cz-panel { background: rgba(28,26,42,0.86); }
  :global(html[data-theme="dark"]) .ccard[data-group="ade"] { --tint: #241d3a; --accent: #a78bea; }
  :global(html[data-theme="dark"]) .ccard[data-group="ing"] { --tint: #18283c; --accent: #6ea6dd; }
  :global(html[data-theme="dark"]) .cc-cta { color: #15101f; }
  :global(html[data-theme="dark"]) .cz-toast { background: var(--surface2); border: 1px solid var(--border); }
```

- [ ] **Step 4: Build + check visual**

Run: `npm run build` → sin errores.
Visual: en dark, el fondo de partículas se ve en lavanda claro (no tinta oscura invisible); el board del carrusel y su panel se ven oscuros y legibles; las tarjetas mantienen contraste (texto claro, CTA legible). En claro, todo idéntico a antes.

- [ ] **Step 5: Commit**

```bash
git add src/pages/index.astro src/components/SubjectCarousel.astro
git commit -m "feat(theme): partículas, carrusel y orbs adaptados a tema oscuro"
```

---

### Task 4: `HeroLogo3D.astro` — wordmark 3D glossy (render estático) + fallback + carga diferida

**Files:**
- Modify: `package.json` (dep `three`)
- Create: `src/components/HeroLogo3D.astro`

**Interfaces:**
- Consumes: `three` y `three/examples/fonts/helvetiker_bold.typeface.json`.
- Produces: `<div class="hero3d">` con `<canvas id="hero3d-canvas">` + fallback `.hero3d-fallback`. Lo consume Task 6.

- [ ] **Step 1: Instalar Three.js**

```bash
npm install three
```

- [ ] **Step 2: Crear `src/components/HeroLogo3D.astro`** (render estático glossy)

```astro
---
// Wordmark "repasaYA" en 3D glossy. Three.js diferido; fallback CSS si no hay WebGL.
---
<div class="hero3d" id="hero3d">
  <canvas id="hero3d-canvas" aria-hidden="true"></canvas>
  <div class="hero3d-fallback" aria-label="repasaYA">repasaYA</div>
</div>

<style>
  .hero3d { position: relative; width: 100%; max-width: 880px; height: clamp(180px, 34vh, 360px); }
  #hero3d-canvas { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
  .hero3d-fallback {
    position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-family: var(--font-display); font-weight: 800; letter-spacing: -.02em;
    font-size: clamp(38px, 8vw, 92px); color: var(--accent);
    text-shadow: 0 6px 30px rgba(138,107,216,.35);
  }
  .hero3d.gl-on .hero3d-fallback { display: none; }
</style>

<script>
  function initHeroLogo() {
    const wrap = document.getElementById('hero3d');
    const canvas = document.getElementById('hero3d-canvas') as HTMLCanvasElement | null;
    if (!wrap || !canvas) return;

    // Cancela instancia previa (View Transitions)
    const prev = (window as any).__heroLogo;
    if (prev) { try { cancelAnimationFrame(prev.raf); prev.dispose(); } catch (e) {} }

    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

    import('three').then(async (THREE) => {
      const { FontLoader } = await import('three/addons/loaders/FontLoader.js');
      const { TextGeometry } = await import('three/addons/geometries/TextGeometry.js');
      const { RoomEnvironment } = await import('three/addons/environments/RoomEnvironment.js');
      const fontJson = (await import('three/examples/fonts/helvetiker_bold.typeface.json')).default;

      const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
      if (!renderer.getContext()) return;           // sin WebGL → deja el fallback
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
      camera.position.set(0, 0, 9);

      // Entorno glossy
      const pmrem = new THREE.PMREMGenerator(renderer);
      scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

      // Luces de apoyo
      scene.add(new THREE.AmbientLight(0xffffff, 0.4));
      const key = new THREE.DirectionalLight(0xffffff, 1.1); key.position.set(3, 5, 6); scene.add(key);

      // Geometría inflada
      const font = new (FontLoader as any)().parse(fontJson);
      const geo = new (TextGeometry as any)('repasaYA', {
        font, size: 1, depth: 0.5, curveSegments: 14,
        bevelEnabled: true, bevelThickness: 0.34, bevelSize: 0.22, bevelSegments: 10,
      });
      geo.center();

      const mat = new THREE.MeshPhysicalMaterial({
        color: 0x8a6bd8, metalness: 0, roughness: 0.16,
        clearcoat: 1, clearcoatRoughness: 0.12, envMapIntensity: 1.1,
      });
      const mesh = new THREE.Mesh(geo, mat);
      const group = new THREE.Group(); group.add(mesh); scene.add(group);

      // Escala/posición de cámara para encajar el ancho del wordmark
      geo.computeBoundingBox();
      const bb = geo.boundingBox!;
      const wordW = bb.max.x - bb.min.x;

      function resize() {
        const r = wrap!.getBoundingClientRect();
        renderer.setSize(r.width, r.height, false);
        camera.aspect = r.width / r.height;
        // Encaja el ancho del texto al ~78% del viewport del canvas
        const fitW = wordW / 0.78;
        const dist = (fitW / 2) / Math.tan((camera.fov * Math.PI / 180) / 2) / camera.aspect;
        camera.position.z = Math.max(6, dist);
        camera.updateProjectionMatrix();
      }
      resize();
      window.addEventListener('resize', resize);

      const state: any = {
        raf: 0,
        dispose() {
          window.removeEventListener('resize', resize);
          geo.dispose(); mat.dispose(); renderer.dispose(); pmrem.dispose();
        },
      };
      (window as any).__heroLogo = state;
      wrap!.classList.add('gl-on');

      function frame() {
        renderer.render(scene, camera);
        state.raf = requestAnimationFrame(frame);
      }
      if (reduce) { renderer.render(scene, camera); }   // estático
      else frame();
    }).catch(() => { /* sin WebGL/Three → fallback CSS visible */ });
  }

  // Carga diferida para no bloquear el first paint
  function deferHeroLogo() {
    if (document.readyState === 'complete') (window as any).requestIdleCallback?.(initHeroLogo) ?? setTimeout(initHeroLogo, 200);
    else window.addEventListener('load', () => setTimeout(initHeroLogo, 150), { once: true });
  }
  deferHeroLogo();
  document.addEventListener('astro:after-swap', deferHeroLogo);
</script>
```

- [ ] **Step 3: Build + check visual**

Run: `npm run build` → sin errores (Three se empaqueta; el build puede tardar algo más).
Visual: incluye temporalmente `<HeroLogo3D />` en una página de prueba o espera a Task 6. Si lo pruebas aislado, debe verse "repasaYA" en 3D lavanda glossy con reflejos; sin WebGL, el texto fallback CSS. (Si TextGeometry da error por `depth`, prueba `height` en vez de `depth`.)

- [ ] **Step 4: Commit**

```bash
git add package.json package-lock.json src/components/HeroLogo3D.astro
git commit -m "feat(ui): HeroLogo3D — wordmark repasaYA 3D glossy (WebGL) + fallback"
```

---

### Task 5: Interacción del hero 3D (hover: tilt + wobble + aberración cromática) + idle + móvil

**Files:**
- Modify: `src/components/HeroLogo3D.astro` (script)

**Interfaces:**
- Consumes: el render estático de Task 4.
- Produces: hero interactivo. Lo consume Task 6 (sin cambios de interfaz).

- [ ] **Step 1: Añadir wobble al material (vertex displacement)**

En `HeroLogo3D.astro`, justo después de crear `mat` y antes de `new THREE.Mesh`, engancha un uniform de hover y un wobble en el shader:

```ts
      const uniforms = { uTime: { value: 0 }, uHover: { value: 0 } };
      mat.onBeforeCompile = (shader) => {
        shader.uniforms.uTime = uniforms.uTime;
        shader.uniforms.uHover = uniforms.uHover;
        shader.vertexShader = 'uniform float uTime;uniform float uHover;\n' + shader.vertexShader;
        shader.vertexShader = shader.vertexShader.replace(
          '#include <begin_vertex>',
          '#include <begin_vertex>\n' +
          'float w = sin(position.x*2.2 + uTime*2.0)*cos(position.y*2.6 + uTime*1.6);\n' +
          'transformed += normal * w * 0.10 * uHover;'
        );
      };
```

- [ ] **Step 2: Postprocesado de aberración cromática (solo desktop)**

Sustituye el bloque de imports `import('three').then(async (THREE) => { … })` para añadir, tras crear `renderer`, la detección de móvil y el composer:

Añade los imports dentro del `then` (junto a los demás `await import`):

```ts
      const coarse = matchMedia('(pointer: coarse)').matches || Math.min(window.innerWidth, window.innerHeight) < 700;
      const { EffectComposer } = await import('three/addons/postprocessing/EffectComposer.js');
      const { RenderPass } = await import('three/addons/postprocessing/RenderPass.js');
      const { ShaderPass } = await import('three/addons/postprocessing/ShaderPass.js');
      const { RGBShiftShader } = await import('three/addons/shaders/RGBShiftShader.js');
```

Después de `resize()` (y de definir `renderer`/`scene`/`camera`), crea el composer **solo si no es coarse**:

```ts
      let composer: any = null, rgb: any = null;
      if (!coarse && !reduce) {
        composer = new (EffectComposer as any)(renderer);
        composer.addPass(new (RenderPass as any)(scene, camera));
        rgb = new (ShaderPass as any)(RGBShiftShader);
        rgb.uniforms.amount.value = 0.0;
        composer.addPass(rgb);
      }
```

En `resize()`, tras `renderer.setSize(...)`, añade: `composer && composer.setSize(r.width, r.height);`

- [ ] **Step 3: Puntero + idle + bucle de animación**

Sustituye el bloque `function frame() { … }` y el arranque por:

```ts
      const pointer = { x: 0, y: 0, inside: false };
      function onMove(e: PointerEvent) {
        const r = canvas!.getBoundingClientRect();
        pointer.x = ((e.clientX - r.left) / r.width) * 2 - 1;
        pointer.y = ((e.clientY - r.top) / r.height) * 2 - 1;
        pointer.inside = true;
      }
      function onLeave() { pointer.inside = false; }
      wrap!.addEventListener('pointermove', onMove);
      wrap!.addEventListener('pointerleave', onLeave);
      state.dispose = (function (base) { return function () {
        wrap!.removeEventListener('pointermove', onMove);
        wrap!.removeEventListener('pointerleave', onLeave);
        composer && composer.dispose && composer.dispose();
        base();
      }; })(state.dispose);

      const clock = new THREE.Clock();
      function frame() {
        const t = clock.getElapsedTime();
        uniforms.uTime.value = t;
        const targetHover = pointer.inside ? 1 : 0;
        uniforms.uHover.value += (targetHover - uniforms.uHover.value) * 0.08;
        // idle float + tilt hacia el puntero
        const tiltX = (pointer.inside ? -pointer.y * 0.5 : Math.sin(t * 0.6) * 0.06);
        const tiltY = (pointer.inside ?  pointer.x * 0.6 : Math.sin(t * 0.5) * 0.10);
        group.rotation.x += (tiltX - group.rotation.x) * 0.06;
        group.rotation.y += (tiltY - group.rotation.y) * 0.06;
        if (rgb) rgb.uniforms.amount.value = uniforms.uHover.value * 0.0026;
        if (composer) composer.render(); else renderer.render(scene, camera);
        state.raf = requestAnimationFrame(frame);
      }
      if (reduce) { renderer.render(scene, camera); }
      else frame();
```

- [ ] **Step 4: Pausar fuera de viewport (rendimiento)**

Tras `(window as any).__heroLogo = state;`, añade:

```ts
      const io = new IntersectionObserver((ents) => {
        ents.forEach((en) => {
          if (en.isIntersecting && !reduce && !state.raf) frame();
          else if (!en.isIntersecting && state.raf) { cancelAnimationFrame(state.raf); state.raf = 0; }
        });
      });
      io.observe(wrap!);
      state.dispose = (function (base) { return function () { io.disconnect(); base(); }; })(state.dispose);
```

- [ ] **Step 5: Build + check visual**

Run: `npm run build` → sin errores.
Visual (desktop): el wordmark flota sutil; al pasar el ratón se inclina siguiéndolo, se ondula (wobble) y aparece aberración cromática que decae al salir. En móvil (DevTools responsive): sin aberración, wobble leve o nulo, sigue legible. Con reduced-motion: estático. Al hacer scroll fuera del hero, el rAF se pausa (CPU baja).

- [ ] **Step 6: Commit**

```bash
git add src/components/HeroLogo3D.astro
git commit -m "feat(ui): hero 3D interactivo — tilt, wobble y aberración cromática al hover"
```

---

### Task 6: Integrar el hero 3D en la landing + fundido de transición + tagline

**Files:**
- Modify: `src/pages/index.astro` (markup del `.hero`, `.hero::after`, import, tagline antes del carrusel)

**Interfaces:**
- Consumes: `HeroLogo3D` (Task 4/5).

- [ ] **Step 1: Importar el componente**

En el frontmatter de `index.astro`, junto a los imports:

```astro
import HeroLogo3D from '../components/HeroLogo3D.astro';
```

- [ ] **Step 2: Sustituir el contenido textual del hero**

Reemplaza el bloque actual:

```astro
  <div class="hero-inner">
    <h1 class="hero-h1">Estudia mejor,<br><span class="hero-grad">aprueba de verdad.</span></h1>
    <p class="hero-desc">Tests interactivos, V/F y flashcards para las asignaturas de la carrera. Gratis, sin registro, sin anuncios.</p>
  </div>
```

por:

```astro
  <div class="hero-inner">
    <HeroLogo3D />
  </div>
```

- [ ] **Step 3: Fundido de transición (`.hero::after`)**

En el `<style>` de `index.astro`, dentro del bloque del hero, añade:

```css
.hero::after {
  content: ''; position: absolute; left: 0; right: 0; bottom: 0;
  height: 28%; z-index: 2; pointer-events: none;
  background: linear-gradient(to bottom, transparent, var(--bg));
}
```

Y asegúrate de que `.hero-inner { z-index: 3; }` (ya lo es) queda por encima del fundido.

- [ ] **Step 4: Tagline encima del carrusel**

En `index.astro`, **antes** de `<SubjectCarousel />`, añade:

```astro
  <p class="lead-tagline">Tests interactivos, V/F y flashcards para las asignaturas de la carrera. <strong>Gratis, sin registro, sin anuncios.</strong></p>
```

Y su CSS en el `<style>`:

```css
.lead-tagline {
  text-align: center; max-width: 60ch; margin: 0 auto;
  color: var(--text-muted); font-size: clamp(15px,1.6vw,18px); line-height: 1.6;
}
.lead-tagline strong { color: var(--text); font-weight: 700; }
```

- [ ] **Step 5: Build + check visual (recorrido)**

Run: `npm run build` → sin errores.
Visual: el hero muestra el wordmark 3D centrado (sin titular de texto); la aurora se funde suavemente hacia el carrusel (sin corte); justo encima del carrusel aparece la tagline; en claro y en oscuro todo coherente. Probar toggle de tema en caliente: el hero 3D sigue visible (su color no depende del tema, pero el fondo sí cambia).

- [ ] **Step 6: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat(ui): hero 3D integrado + fundido hero→carrusel + tagline"
```

---

## Self-Review (hecha)

- **Cobertura del spec:** Parte 1 (tokens dark + FOUC + toggle) → T1; toggle en headers → T2; recolor no-token (partículas/carrusel/orbs/toast) → T3; Parte 2 (hero 3D WebGL, material glossy, font, lazy, fallback, lifecycle) → T4; interacción hover + idle + reduced-motion + móvil + pausa viewport → T5; Parte 3 (fundido transición) → T6 Step 3; Parte 4 (tagline reubicada) → T6 Step 4. Criterios de éxito cubiertos por los checks visuales.
- **Placeholders:** ninguno; todo el código del componente WebGL está completo. Riesgos anotados con alternativa concreta (font `depth`/`height`; composer solo desktop; fallback CSS).
- **Consistencia de nombres:** `data-theme`, `--particle`, evento `themechange`, `[data-theme-toggle]`, `window.__heroLogo`, `.gl-on`, `#hero3d`/`#hero3d-canvas` usados igual en todas las tareas.
- **Riesgo principal (typeface):** se usa la fuente del paquete `three` (`helvetiker_bold.typeface.json`) para evitar pipeline de conversión; swap a Unbounded convertido = mejora futura.
