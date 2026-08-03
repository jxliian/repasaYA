<div align="center">
  <img src="logo.png" alt="repasaYA" width="300" />

  <p><strong>Tests, verdadero/falso y flashcards para el Doble Grado ADE + Ingeniería Informática.</strong></p>
  <p>Gratis, sin registro, sin anuncios y sin cuentas premium de nada.</p>

  <p>
    <a href="https://jxliian.github.io/repasaYA/"><strong>Abrir repasaYA</strong></a>
    ·
    <a href="#cómo-contribuir-material">Contribuir</a>
    ·
    <a href="https://github.com/jxliian/repasaYA/issues/new">Pedir una asignatura</a>
  </p>

  <p>
    <img alt="Astro" src="https://img.shields.io/badge/Astro-6-BC52EE?logo=astro&logoColor=white" />
    <img alt="Sin dependencias de UI" src="https://img.shields.io/badge/JS_de_framework-0_KB-2fd47f" />
    <img alt="Deploy" src="https://img.shields.io/badge/Deploy-GitHub%20Pages-222?logo=github" />
    <img alt="Licencia" src="https://img.shields.io/badge/licencia-MIT-a78bea" />
  </p>
</div>

---

## Qué hay dentro

|  |  |
|---|---|
| **64 asignaturas** | El plan completo de los dos grados: 5 cursos × 2 cuatrimestres |
| **2.045 preguntas y fichas** | Tipo test, V/F con justificación, flashcards, glosarios y apuntes |
| **8 asignaturas con material** | El resto está listado y esperando a que alguien lo suba |

Todo el contenido vive en archivos de texto bajo `src/content/`. **Añadir material es abrir un JSON y mandar un pull request** — no hace falta tocar ni un componente.

---

## Empezar

```bash
git clone https://github.com/jxliian/repasaYA.git
cd repasaYA
npm install
npm run dev      # http://localhost:4321/repasaYA/
```

| Comando | Qué hace |
|---|---|
| `npm run dev` | Servidor de desarrollo con recarga en caliente |
| `npm run build` | Genera el sitio estático en `dist/` y valida todo el contenido |
| `npm run preview` | Sirve `dist/` para comprobar el build |

Requiere Node 20 o superior.

---

## Cómo contribuir material

Este es el flujo entero. No necesitas saber Astro.

### 1. Busca la asignatura

Están en `src/content/subjects/<grado>/<slug>.md`. Si la tuya ya existe, salta al paso 3.

### 2. Si no existe, créala

```markdown
---
title: "Álgebra Lineal y Estructuras Matemáticas"
degree: informatica          # ade | informatica
year: 1                      # 1-5
semester: 2                  # 1 | 2
credits: 6
icon: "📐"
status: available            # available en cuanto tenga material
description: "Espacios vectoriales, diagonalización y formas canónicas."
materials: [test]            # tipos que aporta
---
```

> El curso y el cuatrimestre van **en el frontmatter, no en la ruta del archivo**. Si una asignatura cambia de cuatrimestre, editas una línea y la URL se regenera sola.

### 3. Añade el material

Un archivo por bloque, en `src/content/materials/<grado>/<slug>/<nombre>.json`:

```json
{
  "subject": "informatica/algebra-lineal-y-estructuras-matematicas",
  "type": "test",
  "title": "Tipo test",
  "order": 0,
  "items": [
    {
      "tema": "T2: Diagonalización",
      "q": "¿Cuándo es diagonalizable una matriz cuadrada?",
      "opts": [
        "Cuando su determinante es distinto de cero",
        "Cuando tiene n autovectores linealmente independientes",
        "Cuando es simétrica"
      ],
      "correct": 1,
      "justification": "Necesita una base completa de autovectores."
    }
  ]
}
```

### 4. Comprueba y abre el PR

```bash
npm run build
```

Si el build pasa, el material es válido. Si falla, el error dice exactamente qué campo está mal y en qué pregunta.

### Tipos de material

| `type` | Forma de cada ítem | Se ve como |
|---|---|---|
| `test` | `tema`, `q`, `opts[]`, `correct` (índice base 0), `justification?` | Test con corrección al momento |
| `vf` | `tema`, `q`, `answer` (`"V"` o `"F"`), `justification?` | Verdadero/falso |
| `reveal` | `tema`, `q`, `answer` (texto libre) | Pregunta con respuesta que se destapa |
| `flashcards` | `tema`, `term`, `def` | Tarjetas que giran |
| `glosario` | `tema`, `term`, `def` | Igual, pero abre en modo lista |
| `apuntes` | *(sin ítems)* — `pdf`: ruta dentro de `public/` | Visor de PDF |
| `guia` | *(sin ítems)* — `href`: página propia | Enlace desde el hub |

Campos comunes: `subject`, `title`, `order` (posición en el hub) y `hidden` (genera página, pero no se lista ni se indexa).

Los esquemas están en [`src/content.config.ts`](src/content.config.ts) y se validan con Zod en cada build.

---

## Estructura

```
src/
├─ content.config.ts          Esquemas Zod — la "API" para quien contribuye
├─ content/
│  ├─ degrees/                ade.json · informatica.json
│  ├─ subjects/<grado>/*.md   64 asignaturas, metadatos en frontmatter
│  └─ materials/<grado>/<asignatura>/*.json
│
├─ layouts/
│  ├─ Shell.astro             Catálogo: cabecera, fondo y pie
│  └─ QuizShell.astro         Material interactivo: sin cromo, pantalla completa
│
├─ components/
│  ├─ boot/                   Secuencia de carga con el logo 3D
│  ├─ hero/                   Portada
│  ├─ search/                 Buscador global (⌘K)
│  ├─ nav/                    Cabecera, migas de pan, tema
│  ├─ catalog/                Tarjetas, filtros y rejillas
│  ├─ study/                  CardDeck — flashcards y glosarios
│  ├─ fx/                     Campo de partículas del fondo
│  ├─ sections/               Novedades y "sobre mí"
│  └─ QuizEngine.astro        Motor de tests, V/F y quiz
│
├─ lib/
│  ├─ routes.ts               Único sitio donde se construyen URLs
│  └─ wordmark3d.ts           Wordmark 3D compartido (Three.js)
│
├─ styles/
│  ├─ tokens.css              Colores, radios, sombras y easings
│  └─ base.css                Reset y primitivas (.glass, .btn, .pill)
│
└─ pages/
   ├─ index.astro
   ├─ mapa.astro · privacidad.astro
   ├─ search-index.json.ts    Índice de búsqueda, generado en build
   └─ [degree]/[year]/[semester]/[subject]/[material].astro
```

### URLs

```
/repasaYA/ade/                    Grado, con filtros por curso y tipo
/repasaYA/ade/4/                  Curso
/repasaYA/ade/4/c2/               Cuatrimestre
/repasaYA/ade/4/c2/rrhh/          Asignatura
/repasaYA/ade/4/c2/rrhh/vf/       Material
```

Las rutas planas anteriores (`/repasaYA/rrhh/quiz/`) siguen funcionando: son redirecciones declaradas en [`astro.config.mjs`](astro.config.mjs).

---

## Decisiones técnicas

**Sin framework de CSS.** Un sistema de tokens en variables CSS y estilos con ámbito por componente. La estética —cristal, neón, espacio profundo— no sale de ninguna plantilla.

**Sin JavaScript de framework.** Astro genera HTML estático y los comportamientos interactivos son JS de toda la vida. El motor de tests, el buscador y las flashcards no cargan React ni nada parecido.

**El buscador no lastra la portada.** `search-index.json` se genera en build (~21 KB) y solo se descarga la primera vez que escribes algo.

**Three.js solo cuando toca.** El logo 3D se importa de forma dinámica y lo comparten la pantalla de carga y la portada. Sin WebGL o con `prefers-reduced-motion`, cae a un wordmark en CSS y no descarga nada.

**El CSS del motor de tests está acotado** bajo `:root[data-quiz]`. Sus reglas globales (`html,body{overflow:hidden}`, `main{max-width:860px}`) se colaban en cualquier página que lo importase —aunque no lo pintara— y le rompían el layout.

---

## Accesibilidad y rendimiento

- Navegación completa por teclado: `⌘K` para buscar, flechas y `espacio` en las flashcards, `Tab` en todo lo demás.
- `prefers-reduced-motion` desactiva partículas, animación de bienvenida y transiciones.
- Migas de pan con `BreadcrumbList` en JSON-LD.
- Sin JS, se ve el catálogo completo, los glosarios en modo lista y todas las páginas de contenido.

---

## Privacidad

Sin cuentas, sin cookies, sin analítica y sin anuncios. Lo único que se guarda son dos claves en tu navegador: el tema elegido y una marca para no repetir la animación de bienvenida.

El único tercero es el contador de visitas de [hits.sh](https://hits.sh), que se carga solo en la portada y recibe la IP para sumar uno. Detalle completo en [/privacidad](https://jxliian.github.io/repasaYA/privacidad/).

---

## Despliegue

Cada push a `main` dispara [`.github/workflows/static.yml`](.github/workflows/static.yml), que construye el sitio y lo publica en GitHub Pages.

---

## Licencia

Código bajo licencia MIT.

El material de estudio son resúmenes y preguntas elaborados a partir del temario de las asignaturas, con fines educativos. Si eres docente o titular de derechos y consideras que algo no debería estar publicado, [escríbeme](mailto:e.carrionjuliann@go.ugr.es) y lo retiro.

---

<div align="center">
  Hecho con ganas por <strong>Julián Carrión</strong> · <a href="https://github.com/jxliian">@jxliian</a><br>
  <sub>Universidad de Granada · Doble Grado ADE + Ingeniería Informática</sub>
</div>
