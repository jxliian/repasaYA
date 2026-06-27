# Rediseño visual repasaYA — "Editorial Bold"

**Fecha:** 2026-06-27
**Estado:** Aprobado (pendiente de plan de implementación)
**Alcance:** Sitio completo, por fases. Solo capa visual.

## 1. Problema

La web es funcional y "bonita", pero tiene el aspecto genérico de un *dashboard
generado con IA*. Tres rasgos lo delatan:

1. **Glassmorphism oscuro** — `rgba(255,255,255,0.05)` + `backdrop-filter: blur(24px)`.
2. **Gradiente morado→cyan** — `#7c6dfe → #22d3ee`, la paleta "firma" de lo generado por IA.
3. **Tipografía de sistema** — `Segoe UI`, sin personalidad.

La estructura (Astro, componentes, datos JSON, motor de quiz) es sólida. El
problema es 100% de capa visual.

## 2. Objetivo

Conseguir una sensación **seria y limpia** (herramienta de estudio) **+ joven y
vibrante** (energía, color, interacción), rompiendo el look "IA". Se mantiene el
**modo oscuro** (el modo claro fue eliminado a propósito y no se reintroduce).

Dirección elegida: **Editorial Bold** — tipografía protagonista, superficies
sólidas, un único acento eléctrico. Es la ruptura más limpia porque ataca los
tres pilares del look IA a la vez.

## 3. Decisiones de diseño

### 3.1 Paleta (tokens nuevos en `Base.astro`)

```
--bg          #060608   /* casi negro, base */
--surface     #0d0d12   /* tarjetas sólidas, SIN blur */
--surface2    #15151c   /* elevación */
--border      rgba(255,255,255,.08)
--accent      #c6f135   /* lima eléctrica (sustituye morado-cyan) */
--accent-soft rgba(198,241,53,.12)
--accent-line rgba(198,241,53,.30)
--on-accent   #0c1400   /* texto OSCURO sobre superficies lima */
--text        #f4f5f0   /* blanco cálido, no #fff puro */
--text-muted  #8b8f86
--correct     #3ddc84   /* verde, distinto de la lima para no confundir */
--wrong       #ff5468
```

**Regla crítica:** la lima es un color *claro*. Cualquier botón/badge con fondo
lima debe usar texto oscuro (`--on-accent`), nunca blanco. El código actual usa
`color:#fff` sobre `--accent` en varios sitios; hay que corregirlo.

**Migración de morados hardcodeados:** además de los tokens, hay que reemplazar
en todos los archivos los valores literales del morado antiguo:
- `rgba(108,99,255, …)`
- `rgba(124,109,254, …)` y `rgba(124,58,237, …)`
- `#7c6dfe`, `#6b5cf0`, `#c4b5fd`, `#a78bfa`, `#7c5cff`
- gradientes `linear-gradient(135deg, var(--accent), var(--accent2))` → revisar
  uno a uno (muchos pueden pasar a lima plano, sin degradado).

`--accent2`/`--cyan` desaparecen como gradiente; si se conservan como variable,
apuntan a tonos derivados de la lima para no romper referencias.

### 3.2 Tipografía

- **Space Grotesk** → titulares, UI y cuerpo. Grotesca con carácter, técnica y
  fresca; encaja con el acento lima "deportivo".
- **JetBrains Mono** → micro-labels en mayúsculas, números de stats, chips de
  datos. Aporta aire técnico/dev sin recargar.
- **Self-hosted** vía `@fontsource-variable/space-grotesk` y
  `@fontsource-variable/jetbrains-mono` (sin llamadas externas → coherente con la
  página de privacidad y el ethos "sin rastreo"). Import en `Base.astro`.
- Fallback: `system-ui, -apple-system, sans-serif` por si falla la fuente.

### 3.3 Superficie y textura

- Eliminar `backdrop-filter: blur(...)` en todo el sitio (cliché + coste de
  render). Tarjetas **sólidas** sobre `--surface` con borde de 1px `--border`.
- Capa de **grano/ruido SVG** muy sutil (opacity baja, `pointer-events:none`,
  `position:fixed`) sobre el fondo, para textura editorial.
- Hover de tarjeta: borde lima + glow lima tenue (sustituye el spotlight radial
  morado). El mecanismo `--mx/--my` de spotlight puede conservarse recoloreado a
  lima o simplificarse a un borde+glow.

### 3.4 Hero + constelación de partículas

- Titular **grande** en Space Grotesk: "Estudia mejor, **aprueba de verdad.**"
  (segunda línea en lima).
- **Eliminar** el avatar `yo.webp` (no escala, ata el diseño a una foto).
- A la derecha del hero, las partículas del canvas existente **forman el isotipo
  de la marca (check ✓ + flecha ascendente ↗) rematado con un birrete 🎓**, en
  lima monocromo. Al pasar el ratón se dispersan y se recomponen.
- Implementación: reutilizar el motor de canvas vanilla actual. Añadir un set de
  **posiciones-objetivo** muestreadas de una silueta (dibujada en un canvas
  offscreen a partir de un path/SVG del check+flecha+birrete). Cada partícula
  tiene su destino; fuerza de retorno al destino + repulsión del ratón. Respetar
  `prefers-reduced-motion` (frame estático).

### 3.5 Identidad de marca

- El `logo.png` (violeta-azul) se mantiene **solo como favicon** y `og:image`
  (legado). No se usa como elemento visual en pantalla.
- El wordmark del header pasa de gradiente violeta a **Space Grotesk bold** en
  texto claro con el punto/acento en lima.

## 4. Alcance por fases

Cada fase es revisable de forma independiente y deja el sitio en estado
coherente (gracias a que la Fase 1 propaga color y tipografía globalmente).

- **Fase 1 — Cimientos** (`Base.astro`): nuevos tokens, import de fuentes, capa
  de grano, reemplazo global de morados hardcodeados. Tras esta fase, todo el
  sitio ya luce lima + Space Grotesk aunque sus layouts no estén rediseñados.
- **Fase 2 — Landing** (`index.astro`, `SubjectCard.astro`, `DegreeCard.astro`):
  hero + constelación, bento sólido, timeline de novedades, barra de filtros,
  secciones de asignatura, footer.
- **Fase 3 — Páginas de asignatura** (las 8 `*/index.astro`: hub-cards estilo
  Editorial Bold).
- **Fase 4 — Motor de test** (`QuizEngine.astro`): tabs, mode-cards, opciones,
  V/F, quiz reveal, banco, resultados. Atención especial al contraste de botones
  lima (texto oscuro) y a la distinción lima vs verde-correcto.
- **Fase 5 — Resto** (`*/glosario.astro`, `mapa.astro`, `privacidad.astro`,
  `organizacion-empresas/secreto.astro`): coherencia final.

## 5. Fuera de alcance (NO se toca)

- Lógica del quiz, parsing de commits para "Novedades", datos JSON.
- Estructura de rutas y navegación.
- SEO / meta tags / canonical / Open Graph.
- Funcionalidad de búsqueda, filtros y atajos de teclado (solo su estilo).

## 6. Riesgos y mitigaciones

- **Lima vs verde "correcto" en el quiz:** podrían confundirse. Mitigación:
  `--correct` a un verde más puro (`#3ddc84`) y reservar la lima para énfasis de
  UI (selección, hover, foco), no para feedback de acierto.
- **Contraste de texto sobre lima:** la lima es clara; texto siempre oscuro
  (`--on-accent`). Verificar AA en botones primarios.
- **Peso de fuentes:** usar variable fonts self-hosted y `font-display: swap`;
  precargar solo los pesos usados.
- **Constelación en móvil:** reducir densidad de partículas y, si hace falta,
  mostrar la silueta estática (ya hay lógica de densidad por área en el canvas).
- **Accesibilidad de movimiento:** `prefers-reduced-motion` desactiva la
  animación de partículas (frame estático), como ya hace el código actual.

## 7. Criterios de éxito

- Ningún resto del gradiente morado-cyan ni del glassmorphism en todo el sitio.
- Tipografía Space Grotesk + JetBrains Mono aplicada coherentemente.
- La constelación dibuja el isotipo+birrete y reacciona al ratón.
- Contraste AA en textos sobre lima y sobre superficies.
- El sitio compila (`astro build`) sin errores y se ve coherente al navegar
  entre landing → asignatura → quiz → glosario.
