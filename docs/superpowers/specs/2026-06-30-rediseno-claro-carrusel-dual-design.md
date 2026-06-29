# Rediseño visual repasaYA — "Claro + Carrusel Dual"

**Fecha:** 2026-06-30
**Estado:** Aprobado en brainstorming (pendiente de plan de implementación)
**Alcance:** Sitio completo. Capa visual + nuevo componente de navegación (carrusel).
**Sustituye a:** `2026-06-27-editorial-bold-redesign-design.md` (dirección oscura/lima),
que queda obsoleta. La estructura de datos y rutas se conserva.

> **Fuente visual de verdad:** prototipos interactivos validados con el usuario en
> `.superpowers/brainstorm/18655-1782771731/content/`:
> `hero-direction.html` (hero), `carousel-dual-v3.html` (carrusel), `header.html`
> (nav), `visits.html` (píldora de visitas), `body-font.html` / `hero-font.html`
> (tipografía). El comportamiento y los valores de este spec salen de ahí.

## 1. Problema / motivación

El sitio acaba de pasar por el rediseño "Editorial Bold" (oscuro + lima). El usuario
quiere ahora un **giro radical**: una identidad **clara, suave y más divertida**, con
una **portada protagonista** y una forma nueva y memorable de elegir asignatura (un
**carrusel circular** en vez de una rejilla). La lógica (Astro, datos JSON, motor de
quiz, parseo de commits) es sólida; el cambio es de **capa visual + un componente de
navegación nuevo** en la landing.

## 2. Objetivo

- Sensación **suave, luminosa y joven**, sin perder el aire de herramienta de estudio.
- **Reintroducir tema claro.** Decisión consciente que **revierte** el "solo modo
  oscuro" de specs anteriores y de la memoria del proyecto. El modo oscuro deja de ser
  el modo del sitio.
- Portada **a pantalla completa** + navegación por **carrusel circular dual**.

## 3. Decisiones de diseño

### 3.1 Paleta (tokens nuevos en `Base.astro`)

Tema **claro** con gradientes pastel. Valores de referencia (de los prototipos):

```
--bg            #faf9fe   /* casi blanco, base */
--surface       #ffffff   /* tarjetas */
--surface2      #f5f1fd   /* elevación / hover suave */
--border        rgba(20,20,40,0.08)
--accent        #8a6bd8   /* lavanda (acento principal) */
--accent-strong #7a5bcf   /* hover/activo */
--accent-soft   #ece6fb   /* fondos de chip/badge */
--accent-line   #d7ccf5   /* bordes de acento */
--on-accent     #ffffff   /* texto sobre lavanda sólido */
--ink / --text  #1b1b2e   /* tinta principal (no negro puro) */
--text-muted    #6b6f86
--radius        18px ; --radius-lg 26px
```

**Gradientes "aurora"** (blobs suaves que derivan en hero y secciones): lavanda
`#dcd2ff`, melocotón `#ffd9e4`, menta `#cfeede`, azul `#cfe2ff` sobre base casi
blanca. Opacidad ~0.5–0.62, `filter: blur(46–60px)`.

**Tintes por carrera** (cards del carrusel):
- ADE / Economía → `--tint #efe9ff`, `--accent #7b6cf0` (lavanda).
- Ingeniería → `--tint #e7f1ff`, `--accent #4f8fd1` (azul).

**Quiz — colores de feedback (re-tuning obligatorio para fondo claro):** acierto y
error deben tener contraste AA sobre superficies claras. Referencia: `--correct
#1f9d57` (verde más oscuro que sobre fondo negro), `--wrong #e5484d`. La lavanda se
reserva para énfasis de UI (selección, hover, foco), **no** para feedback de acierto,
para no confundir.

**Regla de contraste:** texto **claro** (`--on-accent`) solo sobre lavanda **sólido**;
sobre fondos `--accent-soft` (lavanda muy claro) el texto va en lavanda oscuro
(`#6b4fc4`) o tinta. Verificar AA en todos los botones.

### 3.2 Tipografía

- **Unbounded** → titulares y wordmark. Display geométrico redondeado; aporta el punto
  "divertido y diferente". Añadir self-hosted vía `@fontsource/unbounded` (pesos
  500/700/800). Import en `Base.astro`.
- **Space Grotesk** (ya en el proyecto) → cuerpo y UI.
- **JetBrains Mono** (ya en el proyecto) → números, códigos, micro-labels.
- Fallbacks: `system-ui, -apple-system, sans-serif`.

### 3.3 Fondo de partículas

- **Se mantiene** la constelación de partículas del canvas actual, **recoloreada**
  para fondo claro: puntos y líneas en tinta translúcida (p. ej. `rgba(60,52,110,.55)`
  los puntos, líneas `rgba(70,60,120,~.10)`), baja densidad.
- `prefers-reduced-motion`: frame estático (como hoy).

### 3.4 Hero (pantalla completa)

- Sección **100vh**. Composición **"Aurora centrada"**: blobs de gradiente que derivan
  + capa de partículas + titular centrado.
- Titular en **Unbounded**: *"Estudia mejor, **aprueba de verdad.**"* (segunda parte en
  acento lavanda).
- **Aviso de scroll** abajo-centro: texto "baja" + chevron que rebota; invita a bajar
  al carrusel. Oculto/estático con `prefers-reduced-motion`.

### 3.5 Carrusel dual de asignaturas (pieza central, componente nuevo)

Aparece **al bajar** del hero. Componente nuevo (p. ej. `SubjectCarousel.astro`) con
script vanilla. Comportamiento validado en `carousel-dual-v3.html`:

**Datos.** Cada asignatura se asigna a un **grupo**: `ade` (RRHH, Organización de
Empresas, Dirección de Operaciones I, Análisis de Estados Financieros, **Economía
Española**) o `ing` (SIBW, DSD, Metodología de la Programación). Añadir `group: 'ade' |
'ing'` al interface `Subject` en `subjects.ts`. El tinte de la card lo da el grupo.

**Vista doble (overview).** Dos círculos: **ADE/Economía** a la izquierda (centro en
~27% del ancho), **Ingeniería** a la derecha (~73%). Cada uno con su **nombre encima**
(Unbounded) + nº de asignaturas, a distancia que **no choque** con las cards. Ambos
anillos **giran siempre y despacio** (≈0.0015 rad/frame), también con el cursor encima.

**Enfocar.** **Clic en cualquier zona** de la mitad izquierda enfoca ADE; de la derecha,
Ingeniería. El círculo enfocado **se superpone** sobre el otro (el otro se desvanece),
pasa al centro a tamaño grande, y aparecen:
- **Panel derecho** (cuadro) con, en este orden: **Filtros** (Tipo: Test / V/F / Ambos ·
  Extras: Con flashcards) → **buscador** → **contador** de resultados.
- **Flecha "← Volver a los grados"** arriba a la izquierda, que regresa al overview.

**Buscar.** El buscador del **panel** y el del **header/nav** están **sincronizados**
(misma query). Filtra por título y código. El buscador del header también funciona en
overview (estrecha ambos anillos a la vez).

**Reorganización.** Al filtrar/buscar, el anillo **redistribuye** las cards visibles de
forma uniforme y el **radio se adapta** al número. Con **1 resultado**, esa card salta
al **centro en grande** mostrando descripción, chips y CTA "Entrar →". Con **0**, mensaje
"sin coincidencias".

**Tope 8 y recencia.** Cada círculo muestra **máximo 8** asignaturas. Hoy hay ≤8 por
grupo, así que se muestran todas. Cuando un grupo supere 8, muestra las **8 con cambios
más recientes**; el resto se alcanza por buscador/filtros. Implementación recencia
(diferida, simple): campo opcional `updatedAt` por asignatura, orden descendente, tomar
8. (El mapeo commit→asignatura del timeline de Novedades queda como mejora futura, no
bloquea: con ≤8 no aplica.)

**Motor.** Un único bucle `requestAnimationFrame` con interpolación (lerp) de
`{x,y,scale,opacity}` por card hacia su objetivo; un mismo motor maneja rotación,
reorganización y transiciones entre overview/focus/solo. `prefers-reduced-motion`:
**no rota**; anillo estático y reorganización instantánea.

**Cards minimalistas.** Icono (emoji) en tile tintado por grupo + título + código
(área). En estado "solo" se ensanchan y revelan descripción + chips + CTA.

### 3.6 Header / nav (claro)

Reconstruir el header en claro (ver `header.html`):
- Izquierda: **logo** "repasaYA" en Unbounded + punto de acento.
- Centro: **buscador** (sincronizado con el del carrusel; conserva atajo ⌘K).
- Derecha, en este orden: **Seguir** (GitHub follow) · **★ Star** · **＋ Solicitar**
  (issue, ahora **lavanda sólido**, fuera el neón verde) · **Visitas**.
- **Seguir** y **Star** son **enlaces estáticos** (sin contadores en vivo → cero
  llamadas externas, coherente con privacidad). Mantienen `REPO_URL` / `PROFILE_URL`.
- **Móvil:** solo **logo + buscador + Solicitar (icono)**. Seguir, Star y Visitas
  **ocultos**. **Arreglar el bug** de solapamiento del header móvil (Solicitar pisando
  la píldora de visitas): el header no debe solaparse a ningún ancho — usar flex con
  `flex-shrink` correctos y ocultar limpiamente los elementos no-móviles.

**Píldora de visitas (`hits.sh`), estilo "segmentado".** Badge de dos bloques en claro
(ver `visits.html`, opción C): bloque izquierdo "VISITAS" en gris claro + bloque derecho
con el número en lavanda. El número sigue saliendo **en vivo de `hits.sh`**, recoloreado
con `?style=flat-square&label=visitas&color=8a6bd8&labelColor=ece6fb` (o servido dentro
de una píldora propia con el número de hits.sh). Mantener `loading="lazy"`.

### 3.7 Novedades (timeline de commits)

**Se mantiene**, recoloreada a claro, como **sección debajo del carrusel** (al seguir
bajando). Conserva el parseo de commits actual y, opcionalmente, una fila de stats
ligera dentro de la misma sección. No reintroduce el look glass/oscuro.

### 3.8 Footer

**Se mantiene** tal cual (contenido y enlaces: jxliian, GitHub, Privacidad, Mapa,
© UGR · Doble Grado ADE+Informática), **recoloreado** a la paleta clara.

## 4. Estructura de la landing (orden de secciones)

1. **Header** sticky (claro).
2. **Hero** 100vh (aurora + partículas + "baja ↓").
3. **Carrusel dual** (overview → focus).
4. **Novedades** (timeline recoloreada).
5. **Footer**.

## 5. Alcance por fases

- **Fase 1 — Cimientos** (`Base.astro`): tokens claros, import de Unbounded, recolor de
  la capa de partículas y grano, reemplazo global de los valores oscuros/lima
  hardcodeados. Tras esta fase, todo el sitio luce claro aunque no esté rediseñado pieza
  a pieza.
- **Fase 2 — Header/nav** (`index.astro` y, si aplica, layout compartido): botones
  GitHub en la nav, "Solicitar" lavanda, píldora de visitas segmentada, **fix móvil**.
- **Fase 3 — Hero**: sección a pantalla completa, aurora animada, partículas
  recoloreadas, aviso de scroll.
- **Fase 4 — Carrusel dual** (`SubjectCarousel.astro` nuevo + `subjects.ts` con
  `group`): overview, focus/superposición, panel de filtros+buscador, buscador
  sincronizado con header, estado "solo", tope 8 + recencia (campo `updatedAt`),
  `prefers-reduced-motion`.
- **Fase 5 — Novedades + footer** en claro.
- **Fase 6 — Resto del sitio**: hubs de asignatura (`*/index.astro`), `QuizEngine.astro`
  (con re-tuning de acierto/error para fondo claro), glosarios, `mapa`, `privacidad`,
  `organizacion-empresas/secreto`. Coherencia final.

## 6. Fuera de alcance (NO se toca)

- Lógica del quiz, parseo de commits, datos JSON, estructura de rutas y navegación a
  hubs.
- SEO / meta / canonical / Open Graph (el `og:image` con `logo.png` legado se mantiene).
- Funcionalidad de búsqueda/atajos (solo su estilo y el nuevo enganche con el carrusel).

## 7. Riesgos y mitigaciones

- **Contraste en claro:** lo más delicado del cambio. Texto siempre con suficiente
  contraste; verificar AA en botones lavanda y en feedback de quiz. La lavanda clara
  (`--accent-soft`) **nunca** lleva texto blanco.
- **Quiz acierto vs error sobre claro:** re-tunear verdes/rojos para que sigan siendo
  legibles y distinguibles sobre superficies blancas.
- **Rendimiento del carrusel:** un solo `rAF` con lerp; sin sombras/blur excesivos por
  card. En móvil, reducir densidad de partículas.
- **Accesibilidad de movimiento:** `prefers-reduced-motion` desactiva rotación del
  carrusel, animación de aurora y partículas (estados estáticos).
- **Header móvil:** garantizar que a **ningún ancho** se solapen elementos (causa del
  bug actual). Ocultar Seguir/Star/Visitas en móvil de forma limpia.
- **`hits.sh` es una llamada externa:** se mantiene (decisión del usuario), aunque el
  resto de botones GitHub se dejan estáticos por privacidad.

## 8. Criterios de éxito

- Ningún resto del tema oscuro/lima ni del glassmorphism: todo el sitio en claro.
- Unbounded + Space Grotesk + JetBrains Mono aplicadas coherentemente.
- Hero a pantalla completa con aurora + partículas + aviso de scroll.
- Carrusel dual funcionando: overview girando, enfoque por clic con superposición,
  panel filtros+buscador, buscador del header sincronizado, estado "solo", tope 8.
- Header con botones GitHub, "Solicitar" lavanda y visitas segmentadas; **móvil sin
  solapes**.
- Novedades y footer recoloreados; contraste AA verificado; `astro build` sin errores y
  navegación coherente landing → asignatura → quiz → glosario.
