# Rediseño "Editorial Bold" — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rehacer la capa visual de todo el sitio repasaYA pasando del look "dashboard IA" (cristal + gradiente morado-cyan + font de sistema) a una estética "Editorial Bold" (superficies sólidas + acento lima eléctrica + Space Grotesk/JetBrains Mono + constelación de partículas que dibuja el isotipo).

**Architecture:** Sitio Astro 6 estático. Todo se alimenta de tokens CSS en `src/layouts/Base.astro` más estilos `<style>` inline por página y valores morados hardcodeados. La estrategia es: (1) cambiar tokens + fuentes + grano en `Base.astro` para propagar el 70% globalmente, (2) restilar archivo por archivo aplicando un mapa de migración de color determinista + cambios creativos concretos por fase.

**Tech Stack:** Astro 6, CSS vanilla, canvas 2D vanilla (constelación), `@fontsource-variable` (fuentes self-hosted).

## Global Constraints

- **Modo oscuro únicamente.** El modo claro fue eliminado a propósito; NO reintroducir.
- **Solo capa visual.** No tocar: lógica de quiz, datos JSON, rutas/navegación, parsing de commits para "Novedades", SEO/meta/canonical/OG, lógica de búsqueda y filtros.
- **Acento lima `#c6f135`.** Sustituye al gradiente morado-cyan en todo el sitio.
- **Texto oscuro sobre lima.** La lima es un color claro: cualquier fondo lima usa texto `#0c1400` (`--on-accent`), nunca `#fff`.
- **Tipografía:** Space Grotesk (titulares/UI/cuerpo) + JetBrains Mono (micro-labels/números/datos), self-hosted vía `@fontsource-variable`.
- **`--correct` = `#3ddc84`** (verde), distinto de la lima, para no confundir en el quiz.
- **`logo.png` solo como favicon/OG** (legado morado), no como elemento visual en pantalla.
- **No hay framework de tests.** Verificación de cada tarea = `npm run build` sin errores + `grep` (ausencia de morado antiguo en el archivo tocado) + revisión visual con `npm run dev`.
- `prefers-reduced-motion`: respetar (constelación en frame estático).

## Mapa de migración de color (referencia para TODAS las tareas)

Sustituciones literales a aplicar en cada archivo que se toque. `A` = valor alfa que se conserva igual.

| Antiguo | Nuevo |
|---|---|
| `rgba(108,99,255, A)` | `rgba(198,241,53, A)` |
| `rgba(124,109,254, A)` | `rgba(198,241,53, A)` |
| `rgba(124,58,237, A)` | `rgba(198,241,53, A)` |
| `rgba(168,85,247, A)` | `rgba(198,241,53, A)` |
| `rgba(34,211,238, A)` (cyan) | `rgba(198,241,53, A)` |
| `#7c6dfe` | `#c6f135` |
| `#6b5cf0` | `#b4e02e` |
| `#c4b5fd` | `#c6f135` |
| `#a78bfa` | `#c6f135` |
| `#7c5cff` | `#c6f135` |
| `#22d3ee` / `#67e8f9` | `#c6f135` |

**Gradientes morado→cyan** (`linear-gradient(...,#7c6dfe...#22d3ee)`, `linear-gradient(135deg,var(--accent),var(--accent2))`, etc.): NO convertir a "gradiente lima→lima" (queda plano). Sustituir por **lima sólida**: `color: var(--accent)` para texto, `background: var(--accent)` para rellenos. Cada aparición se indica en su tarea.

---

## Task 1: Cimientos — fuentes, tokens y grano en Base.astro

**Files:**
- Modify: `package.json` (dependencias de fuentes)
- Modify: `src/layouts/Base.astro:42-78` (bloque `<style is:global>` y `:root`)

**Interfaces:**
- Produces: tokens CSS nuevos (`--bg`, `--surface`, `--surface2`, `--border`, `--accent`, `--accent-hover`, `--accent-soft`, `--accent-line`, `--on-accent`, `--text`, `--text-muted`, `--correct`, `--wrong`, `--font-display`, `--font-mono`) consumidos por todas las tareas siguientes. Capa de grano global (`body::after`).

- [ ] **Step 1: Instalar fuentes self-hosted**

Run:
```bash
npm install @fontsource-variable/space-grotesk @fontsource-variable/jetbrains-mono
```
Expected: se añaden a `dependencies` en `package.json` sin errores.

- [ ] **Step 2: Importar fuentes y reescribir tokens en `Base.astro`**

En `src/layouts/Base.astro`, dentro del frontmatter (entre las líneas `---` de arriba, junto al `import { ClientRouter }`), añadir:
```js
import '@fontsource-variable/space-grotesk';
import '@fontsource-variable/jetbrains-mono';
```

Reemplazar el bloque `:root { ... }` (líneas 43-63) por:
```css
    :root {
      --bg:           #060608;
      --surface:      #0d0d12;
      --surface2:     #15151c;
      --border:       rgba(255,255,255,0.08);
      --glass:        #0d0d12;            /* compat: ya no es cristal, es sólido */
      --glass-hi:     #15151c;
      --glass-border: rgba(255,255,255,0.08);
      --accent:       #c6f135;            /* lima eléctrica */
      --accent2:      #c6f135;            /* compat: ya no hay 2º color de gradiente */
      --accent-hover: #b4e02e;
      --accent-soft:  rgba(198,241,53,0.12);
      --accent-line:  rgba(198,241,53,0.30);
      --on-accent:    #0c1400;            /* texto sobre fondos lima */
      --cyan:         #c6f135;            /* compat */
      --correct:      #3ddc84;
      --wrong:        #ff5468;
      --reveal:       #f5b800;
      --text:         #f4f5f0;
      --text-muted:   #8b8f86;
      --radius:       16px;
      --radius-lg:    24px;
      --header-bg:    rgba(6,6,8,0.80);
      --font-display: 'Space Grotesk Variable', system-ui, -apple-system, sans-serif;
      --font-mono:    'JetBrains Mono Variable', ui-monospace, monospace;
    }
```

- [ ] **Step 3: Aplicar fuente base y añadir capa de grano**

En el mismo `<style is:global>`, reemplazar la regla `body { ... }` (líneas 66-71) por:
```css
    body {
      font-family: var(--font-display);
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
    }
    /* Grano editorial — película sutil sobre todo, no bloquea clics */
    body::after {
      content: ''; position: fixed; inset: 0; z-index: 9999;
      pointer-events: none; opacity: 0.045; mix-blend-mode: overlay;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    }
    @media (prefers-reduced-motion: reduce) { body::after { display: none; } }
```
Actualizar también la regla `*:focus-visible` (línea 73-77): cambiar `outline: 2px solid var(--accent);` se mantiene (ya usa el token, ahora será lima).

- [ ] **Step 4: Migrar morados hardcodeados de Base.astro**

`grep -nE '108,99,255|124,109,254|124,58,237|#7c6dfe|#22d3ee' src/layouts/Base.astro` y aplicar el mapa de migración a cada coincidencia.

- [ ] **Step 5: Verificar build + ausencia de morado**

Run:
```bash
npm run build && grep -nE '108,99,255|124,109,254|124,58,237|#7c6dfe|#22d3ee' src/layouts/Base.astro || echo "SIN MORADO"
```
Expected: build OK; el grep no devuelve coincidencias (`SIN MORADO`).

- [ ] **Step 6: Verificación visual**

Run `npm run dev`, abrir la home. Esperado: todo el texto en Space Grotesk, los acentos que antes eran morados ahora son lima, grano sutil visible, sin cristal roto. (La landing aún no está rediseñada; solo cambia color+fuente.)

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json src/layouts/Base.astro
git commit -m "feat(ui): cimientos Editorial Bold — tokens lima, fuentes Space Grotesk/JetBrains Mono, grano

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 2: SubjectCard — tarjeta sólida Editorial Bold

**Files:**
- Modify: `src/components/SubjectCard.astro:61-182` (bloque `<style>`)

**Interfaces:**
- Consumes: tokens de Task 1 (`--surface`, `--accent`, `--accent-soft`, `--accent-line`, `--font-mono`, `--on-accent`).

- [ ] **Step 1: Quitar cristal y aplicar superficie sólida**

En `.scard` (líneas 70-90): eliminar `backdrop-filter: blur(24px);` y `-webkit-backdrop-filter: blur(24px);`. Cambiar `background: var(--glass);` por `background: var(--surface);`. Mantener `border`, `border-radius`, `box-shadow`.

- [ ] **Step 2: Migrar morados a lima**

Aplicar el mapa de migración a todas las coincidencias del bloque `<style>`:
- `.scard:hover` (94-99): `border-color: rgba(168,85,247,0.50)` → `rgba(198,241,53,0.50)`; sombra `rgba(168,85,247,0.18)` → `rgba(198,241,53,0.18)`.
- `.scard-spot` (102-110): `rgba(168,85,247,0.14)` → `rgba(198,241,53,0.14)`.
- `.scard-line` (114-118): `linear-gradient(90deg,#7c6dfe,#c4b5fd,#22d3ee)` → `background: var(--accent);` (lima sólida).
- `.scard-icon` (129-136): `rgba(124,109,254,0.10)`→`var(--accent-soft)`; `rgba(124,109,254,0.18)`→`var(--accent-line)`.
- `.b-purple`,`.b-cyan`,`.b-multi` (155-160): fondos a `var(--accent-soft)`, borde `var(--accent-line)`, color `var(--accent)`. Para `.b-multi` sustituir el `linear-gradient` por `background: var(--accent-soft)`.
- `.chip` (171-175): `rgba(124,109,254,.10)`→`var(--accent-soft)`; borde→`var(--accent-line)`; `color:#c4b5fd`→`var(--accent)`.
- `.scard-arrow` (176-180): `color:#7c6dfe`→`var(--accent)`.

- [ ] **Step 3: Tipografía mono en metadatos**

`.scard-code` (139-144): añadir `font-family: var(--font-mono);` (refuerza el aire técnico en el código de asignatura).

- [ ] **Step 4: Verificar build + grep**

Run:
```bash
npm run build && grep -nE '108,99,255|124,109,254|168,85,247|#7c6dfe|#c4b5fd|#22d3ee' src/components/SubjectCard.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO`.

- [ ] **Step 5: Verificación visual + commit**

`npm run dev` → las tarjetas de asignatura son sólidas, borde y chips en lima, hover con glow lima. Luego:
```bash
git add src/components/SubjectCard.astro
git commit -m "feat(ui): SubjectCard sólida con acento lima (Editorial Bold)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 3: DegreeCard — migración de color

**Files:**
- Modify: `src/components/DegreeCard.astro:29-117` (bloque `<style>`)

**Interfaces:**
- Consumes: tokens de Task 1.

- [ ] **Step 1: Confirmar uso del componente**

Run: `grep -rn "DegreeCard" src/`
Si solo aparece su definición y no se importa en ninguna página, está sin usar: igualmente se migra (es barato) para evitar morado latente.

- [ ] **Step 2: Migrar morados a lima**

Aplicar el mapa:
- `.degree-card:hover` (38-41): `rgba(108,99,255,.08)` → `var(--accent-soft)` o `rgba(198,241,53,.08)`.
- `.degree-icon` (54-65): `rgba(108,99,255,.1)`→`var(--accent-soft)`; `rgba(108,99,255,.2)`→`var(--accent-line)`.
- `details[open] .degree-icon` (91-94): `linear-gradient(135deg, var(--accent), var(--accent2))` → `background: var(--accent); color: var(--on-accent);`.
- `details[open] .degree-title` (95-100): el bloque de `background-clip:text` con gradiente → sustituir por `color: var(--accent);` (quitar las 3 líneas de `-webkit-background-clip`/`text-fill`).

- [ ] **Step 3: Verificar build + grep + commit**

Run:
```bash
npm run build && grep -nE '108,99,255|124,109,254|#7c6dfe' src/components/DegreeCard.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO`. Luego:
```bash
git add src/components/DegreeCard.astro
git commit -m "feat(ui): DegreeCard a acento lima

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 4: Landing — superficies, hero, bento, timeline, filtros, footer

**Files:**
- Modify: `src/pages/index.astro:55-602` (bloque `<style>`) y `:687-736` (HTML del hero, para quitar el avatar)

**Interfaces:**
- Consumes: tokens de Task 1.
- Produces: el contenedor `.hero-art` (nuevo, donde la Task 5 montará el canvas de la constelación) en lugar del `<img class="hero-avatar">`.

- [ ] **Step 1: Quitar cristal global de la landing**

En la utilidad `.glass` (108-115): eliminar las dos líneas `backdrop-filter`/`-webkit-backdrop-filter`; cambiar `background: var(--glass);` → `background: var(--surface);`. La sticky `.site-header` (120-128): quitar `backdrop-filter: blur(24px)` y su prefijo `-webkit-`.

- [ ] **Step 2: Reducir las orbs y migrar el fondo**

`.orb-tl` (79-87): `rgba(124,58,237,…)` → `rgba(198,241,53,…)` (lima tenue). `.orb-br` (89-97): `rgba(6,182,212,…)` (cyan) → bajar a `rgba(198,241,53,0.06)` o eliminar la orb-br para no competir con la constelación. Partículas de fondo (script, líneas 973/986/1003): colores `rgba(168,150,255,…)`/`rgba(124,109,254,…)`/`rgba(34,211,238,…)` → tonos lima `rgba(198,241,53,…)`.

- [ ] **Step 3: Wordmark y hero en lima**

- `.site-logo` (130-136): sustituir el `linear-gradient(135deg,#7c6dfe,#c4b5fd)` + `background-clip:text` por `color: var(--text);` y dejar el `.logo-dot` (137-143) en `background: var(--accent)` con su `box-shadow` recoloreado a `rgba(198,241,53,.9)`.
- `.hero-grad` (357-361): quitar el gradiente y `background-clip`; poner `color: var(--accent);`.
- `.stat-num` (381-386): igual, `color: var(--accent);` (quitar gradiente). Añadir `font-family: var(--font-mono);` a `.stat-num` y `.stat-lbl`.
- `.hero-h1` (351-356): subir tamaño a `clamp(2.4rem,5vw,4rem)` y `letter-spacing:-2px` para el "display enorme".

- [ ] **Step 4: Migrar el resto de morados de la landing**

Aplicar el mapa de migración a todas las coincidencias restantes del `<style>` (botón neón ya es verde-emerald: dejarlo; `.btn-neon` no se toca). Revisar: `.search-wrap:focus-within`, `.live-pill`/`.live-dot`, `.cta-arrow`, `.cta-bg-icon`, timeline (`.tl-track::before`, `.tl-node.*`, `.upd-*`, `.tl-since`), `.fchip.on`, `.section-label`, `footer a`. Para los `.upd-*` (badges de commit por tipo): conservar la variedad de color semántica (verde/naranja/azul/etc.) PERO cambiar el morado `.upd-purple` y el cyan `.upd-cyan` a lima.

- [ ] **Step 5: Quitar el avatar y dejar el hueco para la constelación**

En el HTML del hero, eliminar `<img class="hero-avatar" ...>` (línea ~735) y sustituirlo por:
```html
      <canvas class="hero-art" id="hero-constellation" aria-hidden="true"></canvas>
```
Añadir al `<style>`:
```css
.hero-art {
  position: absolute; right: 18px; bottom: 0;
  width: 420px; height: 420px; display: block;
  z-index: 2; pointer-events: none;
}
@media (max-width: 700px) {
  .hero-art { position: static; width: 100%; max-width: 360px; height: 300px; margin: 12px auto 0; }
}
```
Mantener las reglas existentes que reservan ancho para el arte en desktop (`.b-hero .live-pill … { max-width: calc(100% - 460px); }`) — siguen siendo válidas con el canvas.

- [ ] **Step 6: Verificar build + grep**

Run:
```bash
npm run build && grep -nE '108,99,255|124,109,254|124,58,237|168,85,247|#7c6dfe|#c4b5fd|#22d3ee|34,211,238' src/pages/index.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO`.

- [ ] **Step 7: Verificación visual + commit**

`npm run dev` → hero con titular grande lima, tarjetas sólidas, timeline y filtros en lima, sin avatar (hueco vacío a la derecha, se llena en Task 5). Luego:
```bash
git add src/pages/index.astro
git commit -m "feat(ui): landing Editorial Bold — hero grande, superficies sólidas, lima; fuera avatar

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 5: Constelación de partículas (isotipo ✓↗ + birrete)

**Files:**
- Modify: `src/pages/index.astro` (añadir un `<script>` nuevo al final, junto al de las partículas de fondo)

**Interfaces:**
- Consumes: el `<canvas id="hero-constellation">` creado en Task 4.

- [ ] **Step 1: Añadir el script de la constelación**

Al final de `index.astro`, antes de `</Base>`, añadir un `<script>` que: (a) dibuja la silueta objetivo (check + flecha + birrete) en un canvas offscreen, (b) muestrea sus píxeles a posiciones-objetivo, (c) anima partículas hacia su destino con repulsión del ratón.

```html
<script>
  function initConstellation() {
    const canvas = document.getElementById('hero-constellation') as HTMLCanvasElement | null;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const prev = (window as any).__constellation;
    if (prev) cancelAnimationFrame(prev.raf);

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const ACCENT = '198,241,53';

    function size() {
      const r = canvas!.getBoundingClientRect();
      canvas!.width = Math.max(1, Math.floor(r.width * dpr));
      canvas!.height = Math.max(1, Math.floor(r.height * dpr));
    }
    size();

    // 1) Dibuja la silueta objetivo en un canvas offscreen y muestrea píxeles
    function sampleTargets(W: number, H: number) {
      const off = document.createElement('canvas');
      off.width = W; off.height = H;
      const o = off.getContext('2d')!;
      o.fillStyle = '#fff';
      o.strokeStyle = '#fff';
      o.lineJoin = 'round'; o.lineCap = 'round';
      const cx = W / 2, cy = H / 2, s = Math.min(W, H);

      // Birrete (mortarboard): rombo + base
      o.beginPath();
      o.moveTo(cx, cy - s * 0.34);
      o.lineTo(cx + s * 0.26, cy - s * 0.22);
      o.lineTo(cx, cy - s * 0.10);
      o.lineTo(cx - s * 0.26, cy - s * 0.22);
      o.closePath(); o.fill();
      o.lineWidth = s * 0.05;
      o.beginPath(); // borla
      o.moveTo(cx + s * 0.26, cy - s * 0.22);
      o.lineTo(cx + s * 0.26, cy - s * 0.04);
      o.stroke();

      // Check + flecha ascendente (isotipo)
      o.lineWidth = s * 0.085;
      o.beginPath();
      o.moveTo(cx - s * 0.24, cy + s * 0.06);
      o.lineTo(cx - s * 0.06, cy + s * 0.24); // valle del check
      o.lineTo(cx + s * 0.30, cy - s * 0.18); // sube a la punta (flecha)
      o.stroke();
      // Punta de flecha
      o.lineWidth = s * 0.06;
      o.beginPath();
      o.moveTo(cx + s * 0.30, cy - s * 0.18);
      o.lineTo(cx + s * 0.16, cy - s * 0.20);
      o.moveTo(cx + s * 0.30, cy - s * 0.18);
      o.lineTo(cx + s * 0.28, cy - s * 0.03);
      o.stroke();

      const img = o.getImageData(0, 0, W, H).data;
      const pts: { x: number; y: number }[] = [];
      const gap = Math.max(3, Math.floor(s / 90));
      for (let y = 0; y < H; y += gap)
        for (let x = 0; x < W; x += gap)
          if (img[(y * W + x) * 4 + 3] > 128) pts.push({ x, y });
      return pts;
    }

    type P = { x: number; y: number; tx: number; ty: number; vx: number; vy: number };
    let parts: P[] = [];
    function build() {
      size();
      const targets = sampleTargets(canvas!.width, canvas!.height);
      parts = targets.map(t => ({
        x: Math.random() * canvas!.width, y: Math.random() * canvas!.height,
        tx: t.x, ty: t.y, vx: 0, vy: 0,
      }));
    }
    build();

    const mouse = { x: -9999, y: -9999 };
    function onMove(e: PointerEvent) {
      const r = canvas!.getBoundingClientRect();
      mouse.x = (e.clientX - r.left) * dpr; mouse.y = (e.clientY - r.top) * dpr;
    }
    function onLeave() { mouse.x = -9999; mouse.y = -9999; }
    window.addEventListener('pointermove', onMove, { passive: true });
    window.addEventListener('pointerout', onLeave);

    const state: any = { raf: 0 };
    (window as any).__constellation = state;
    const R = 70 * dpr;

    function frame() {
      ctx!.clearRect(0, 0, canvas!.width, canvas!.height);
      for (const p of parts) {
        // retorno al destino
        p.vx += (p.tx - p.x) * 0.012;
        p.vy += (p.ty - p.y) * 0.012;
        // repulsión del ratón
        const dx = p.x - mouse.x, dy = p.y - mouse.y;
        const d2 = dx * dx + dy * dy;
        if (d2 < R * R && d2 > 1) {
          const d = Math.sqrt(d2), f = (1 - d / R) * 2.2;
          p.vx += (dx / d) * f; p.vy += (dy / d) * f;
        }
        p.vx *= 0.86; p.vy *= 0.86;
        p.x += p.vx; p.y += p.vy;
        ctx!.beginPath();
        ctx!.arc(p.x, p.y, 1.5 * dpr, 0, Math.PI * 2);
        ctx!.fillStyle = `rgba(${ACCENT},0.9)`;
        ctx!.fill();
      }
      state.raf = requestAnimationFrame(frame);
    }

    if (reduce) {
      for (const p of parts) { p.x = p.tx; p.y = p.ty; }
      frame(); cancelAnimationFrame(state.raf);
    } else frame();

    window.addEventListener('resize', build);
  }
  initConstellation();
  document.addEventListener('astro:after-swap', initConstellation);
</script>
```

- [ ] **Step 2: Verificar build**

Run: `npm run build`
Expected: build OK (sin errores de TypeScript en el script).

- [ ] **Step 3: Verificación visual**

`npm run dev` → en el hero, a la derecha, las partículas se agrupan formando un birrete sobre el check+flecha en lima; al mover el ratón por encima se dispersan y se recomponen. En móvil aparece debajo del texto. Con `prefers-reduced-motion` se ve la figura estática.

- [ ] **Step 4: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat(ui): constelación de partículas dibuja el isotipo + birrete en el hero

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 6: Páginas de asignatura (hub) — Editorial Bold

**Files:**
- Modify (bloque `<style is:global>` de cada una):
  - `src/pages/rrhh/index.astro`
  - `src/pages/organizacion-empresas/index.astro`
  - `src/pages/aef/index.astro`
  - `src/pages/sibw/index.astro`
  - `src/pages/mp/index.astro`
  - `src/pages/do1/index.astro`
  - `src/pages/dsd/index.astro`

**Interfaces:**
- Consumes: tokens de Task 1.

- [ ] **Step 1: Migrar las hub-cards a superficie sólida + lima**

Estas 7 páginas comparten el mismo patrón `.hub-*`. En cada una, dentro de `<style is:global>`:
- `.hub-badge`: `rgba(108,99,255,.12)`→`var(--accent-soft)`; borde→`var(--accent-line)`; `color:var(--accent2)`→`var(--accent)`.
- `.hub-title span`: sustituir `linear-gradient(...)`+`background-clip:text` por `color: var(--accent);`. Añadir `font-family: var(--font-display)` al `.hub-title` si no hereda.
- `.hub-card:hover`: `background:#1e1c35`→`var(--surface2)`; `border-color:var(--accent)` (ya); sombra `rgba(108,99,255,.2)`→`rgba(198,241,53,.12)`.
- `.hub-card::before`: `linear-gradient(90deg,var(--accent),var(--accent2))`→`background: var(--accent);`.
- `.hub-card-icon`: `rgba(108,99,255,.1)`→`var(--accent-soft)`; borde→`var(--accent-line)`.
- `.hub-chip`: fondo→`var(--accent-soft)`; borde→`var(--accent-line)`; `color:var(--accent2)`→`var(--accent)`.
- `.hub-card-arrow`: `color:var(--accent)` (ya).
- `.logo span`, `.back:hover`: usan `var(--accent)` → ya lima.
- Las `.pdf-card` (variante roja, solo en rrhh): mantener el rojo (es semántica de PDF), no tocar.

- [ ] **Step 2: Verificar build + grep en las 7**

Run:
```bash
npm run build && grep -rlnE '108,99,255|124,109,254|#7c6dfe|#c4b5fd|1e1c35' src/pages/*/index.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO` (ningún index de asignatura con morado).

- [ ] **Step 3: Verificación visual + commit**

`npm run dev` → entrar a `/rrhh/`, `/organizacion-empresas/`, etc.: hub-cards sólidas, acentos lima, coherentes con la landing. Luego:
```bash
git add src/pages/rrhh/index.astro src/pages/organizacion-empresas/index.astro src/pages/aef/index.astro src/pages/sibw/index.astro src/pages/mp/index.astro src/pages/do1/index.astro src/pages/dsd/index.astro
git commit -m "feat(ui): hubs de asignatura en Editorial Bold (lima, sólido)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 7: QuizEngine — motor de test Editorial Bold

**Files:**
- Modify: `src/components/QuizEngine.astro:21-132` (bloque `<style is:global>`)

**Interfaces:**
- Consumes: tokens de Task 1, en especial `--on-accent`, `--correct`, `--wrong`.

- [ ] **Step 1: Botones primarios con texto oscuro sobre lima**

Es el punto crítico de contraste. Cambiar a `color: var(--on-accent)` (no `#fff`) en:
- `.btn-start` (51): `background:var(--accent);color:#fff` → `color:var(--on-accent)`.
- `.btn-start:hover` (52): sombra `rgba(108,99,255,.4)`→`rgba(198,241,53,.35)`.
- `.btn-primary` (104): `background:var(--accent);color:#fff`→`color:var(--on-accent)`.
- `.opt-btn:hover .opt-letter` (90), `.chip-all.chip-on` (49): donde el fondo pase a `var(--accent)`, el texto debe ser `var(--on-accent)`.
- `.opt-letter` activos sobre `--correct`/`--wrong` ya usan `#fff` (verde/rojo son oscuros): dejar `#fff`.

- [ ] **Step 2: Migrar morados a lima en el resto**

Aplicar el mapa a todas las coincidencias `108,99,255`:
- `.mode-card:hover,.mode-card.selected` (36): `rgba(108,99,255,.08)`→`var(--accent-soft)`.
- `.mode-card.selected::after` (37): `color:var(--accent)` ya.
- `.mode-card.selected .mc-chip` (41): `rgba(108,99,255,.12)`→`var(--accent-soft)`; borde→`var(--accent-line)`.
- `.tema-chip.chip-on` (48): `rgba(108,99,255,.14)`→`var(--accent-soft)`.
- `.progress-fill` (56): `linear-gradient(90deg,var(--accent),var(--accent2))`→`background: var(--accent);`.
- `.opt-btn:hover` (87): `rgba(108,99,255,.08)`→`var(--accent-soft)`.
- `.reveal-btn`/`.quiz-answer-box`/`.quiz-answer-label` (79-83): `rgba(108,99,255,…)`→tonos lima (`var(--accent-soft)`/`var(--accent-line)`/`var(--accent)`).
- `.b-t` (124): badge "Test" del banco → `var(--accent-soft)`/`var(--accent-line)`/`var(--accent)`.
- `.github-fab:hover` (128): `background:#1e1c35`→`var(--surface2)`; sombras `rgba(108,99,255,…)`→`rgba(198,241,53,…)`; `color:var(--accent2)`→`var(--accent)`.

- [ ] **Step 3: Tipografía**

Añadir `font-family: var(--font-mono)` a `.stat-num` (111) y a `.q-tema-tag`/`.bank-meta` (datos/etiquetas). Títulos (`.mc-title`,`.hub`…) heredan Space Grotesk del body.

- [ ] **Step 4: Verificar build + grep**

Run:
```bash
npm run build && grep -nE '108,99,255|124,109,254|#7c6dfe|1e1c35|color:#fff' src/components/QuizEngine.astro
```
Expected: build OK. Revisar manualmente que las únicas `color:#fff` restantes sean sobre fondos `--correct`/`--wrong` (verde/rojo), no sobre lima.

- [ ] **Step 5: Verificación visual + commit**

`npm run dev` → entrar a un quiz (`/rrhh/quiz/`): probar V/F, tipo test y banco. Verificar: botón "Empezar →" lima con texto oscuro legible; opción seleccionada (lima) NO se confunde con correcta (verde) ni incorrecta (rojo). Luego:
```bash
git add src/components/QuizEngine.astro
git commit -m "feat(ui): QuizEngine Editorial Bold — botones lima texto oscuro, lima vs verde/rojo

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 8: Glosarios — Editorial Bold

**Files:**
- Modify (bloque `<style is:global>` de cada una):
  - `src/pages/rrhh/glosario.astro`
  - `src/pages/organizacion-empresas/glosario.astro`
  - `src/pages/aef/glosario.astro`
  - `src/pages/sibw/glosario.astro`

**Interfaces:**
- Consumes: tokens de Task 1.

- [ ] **Step 1: Migrar morados a lima en las flashcards/glosario**

En cada archivo, aplicar el mapa de migración a todas las coincidencias `108,99,255`/`124,109,254`/`#7c6dfe`/`#c4b5fd`/gradientes. Quitar cualquier `backdrop-filter: blur` si lo hubiera. Las flashcards (tarjetas que se voltean) pasan a `background: var(--surface)`; el acento de "revelar"/borde a lima. Mantener cualquier color semántico no-morado.

- [ ] **Step 2: Verificar build + grep en las 4**

Run:
```bash
npm run build && grep -rlnE '108,99,255|124,109,254|#7c6dfe|#c4b5fd' src/pages/*/glosario.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO`.

- [ ] **Step 3: Verificación visual + commit**

`npm run dev` → abrir `/rrhh/glosario/` y voltear una flashcard; comprobar filtros por tema. Coherencia lima. Luego:
```bash
git add src/pages/rrhh/glosario.astro src/pages/organizacion-empresas/glosario.astro src/pages/aef/glosario.astro src/pages/sibw/glosario.astro
git commit -m "feat(ui): glosarios/flashcards en Editorial Bold (lima)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 9: Mapa, Privacidad y Secreto

**Files:**
- Modify: `src/pages/mapa.astro`, `src/pages/privacidad.astro`, `src/pages/organizacion-empresas/secreto.astro` (bloques `<style>`)

**Interfaces:**
- Consumes: tokens de Task 1.

- [ ] **Step 1: Migrar morados a lima**

En los tres archivos, aplicar el mapa a todas las coincidencias (`108,99,255`/`124,109,254`/`124,58,237`/`#7c6dfe`/`#c4b5fd`/`#22d3ee`/`168,85,247`), quitar `backdrop-filter: blur` si lo hubiera, fondos de tarjeta a `var(--surface)`. En `secreto.astro` (protegida por contraseña): mantener la semántica de "protegido/top secret" pero con acento lima en vez de morado.

- [ ] **Step 2: Verificar build + grep**

Run:
```bash
npm run build && grep -rlnE '108,99,255|124,109,254|124,58,237|#7c6dfe|#c4b5fd|#22d3ee|168,85,247' src/pages/mapa.astro src/pages/privacidad.astro src/pages/organizacion-empresas/secreto.astro || echo "SIN MORADO"
```
Expected: build OK; `SIN MORADO`.

- [ ] **Step 3: Verificación visual + commit**

`npm run dev` → abrir `/mapa/`, `/privacidad/` y la card secreto de OE. Coherencia lima. Luego:
```bash
git add src/pages/mapa.astro src/pages/privacidad.astro src/pages/organizacion-empresas/secreto.astro
git commit -m "feat(ui): mapa, privacidad y secreto en Editorial Bold (lima)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 10: QA final — barrido global y navegación

**Files:**
- Modify: cualquier archivo con morado residual que aparezca en el barrido.

**Interfaces:**
- Consumes: todo lo anterior.

- [ ] **Step 1: Barrido global de morado/cyan antiguos**

Run:
```bash
grep -rnE '108,99,255|124,109,254|124,58,237|168,85,247|34,211,238|#7c6dfe|#6b5cf0|#c4b5fd|#a78bfa|#7c5cff|#22d3ee|#67e8f9|1e1c35' src/
```
Expected: **sin salida**. Si algo aparece, migrarlo con el mapa y volver a correr.

- [ ] **Step 2: Barrido de cristal y de texto blanco sobre lima**

Run:
```bash
grep -rn 'backdrop-filter' src/
```
Expected: sin salida (o solo en `.btn-neon` si se decidió conservarlo; revisar). Revisar manualmente que ningún `background: var(--accent)` lleve `color:#fff`.

- [ ] **Step 3: Build limpio**

Run: `npm run build`
Expected: build OK, sin warnings nuevos.

- [ ] **Step 4: Navegación visual completa**

`npm run dev` y recorrer: home → constelación reacciona al ratón → entrar a 2-3 asignaturas → quiz (V/F, test, banco, resultados) → glosario → mapa → privacidad. Verificar coherencia Editorial Bold y contraste AA en botones lima.

- [ ] **Step 5: Commit final (si hubo correcciones)**

```bash
git add -A
git commit -m "fix(ui): barrido final Editorial Bold — sin restos de morado-cyan ni cristal

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Notas de ejecución

- **Orden:** Task 1 primero (todo depende de los tokens). Tasks 2-9 son en gran parte independientes entre sí una vez hecha la 1; Task 5 depende de Task 4 (necesita el canvas). Task 10 va al final.
- **Sin tests unitarios:** la red de seguridad es `npm run build` + los `grep` de ausencia de morado + la revisión visual. Tomar capturas en cada verificación visual ayuda a comparar.
- **Reversión:** cada tarea es un commit atómico; si una fase no convence, se revierte sin afectar a las demás.
