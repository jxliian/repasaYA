# Spec 013: Renderizado y Maquetación de Fórmulas Matemáticas con KaTeX en Guías de Estudio

- **Fecha**: 2026-11-04
- **Estado**: Implementado
- **Ámbito**: Infraestructura / Markdown / Derecho Fiscal / UI & Estilos

---

## 1. Contexto y Motivación

En la guía de estudio de **Derecho Fiscal** (`/derecho-fiscal/guia/`), los supuestos prácticos de liquidación tributaria (IRPF, retribuciones en especie Art. 43, rendimientos de capital inmobiliario Art. 23, imputación de rentas Art. 85, deducciones y coeficientes de abatimiento DT 9ª) contienen numerosas fórmulas y operaciones aritméticas complejas.

Anteriormente, Astro no disponía de plugins de procesamiento matemático para Markdown, provocando que los bloques LaTeX escritos con `$ ... $` y `$$ ... $$` se mostraran como texto plano crudo o con caracteres fragmentados (p. ej. `$= 860...$`, `$<25.000$`, `$\le$`, `$\to$`). Además, no se disponía de estilos ni soporte tipográfico de KaTeX para visualización responsiva.

---

## 2. Descripción de los Cambios

1. **Configuración de Astro y Plugins Markdown**:
   - Instalación de dependencias: `remark-math@^6.0.0` y `rehype-katex@^7.0.1`.
   - En [`astro.config.mjs`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/astro.config.mjs):
     - Integración de `remarkMath` en `markdown.remarkPlugins`.
     - Integración de `rehypeKatex` con opción `{ strict: 'ignore' }` en `markdown.rehypePlugins` para permitir caracteres monetarios (`€`) y notación tributaria sin interrumpir el pipeline SSG.
     - Preservación íntegra de la filosofía 0 KB JS en cliente: KaTeX precompila las fórmulas a HTML estático + MathML durante el build.

2. **Estilos y Hoja de Estilos KaTeX en [`src/layouts/GuideLayout.astro`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/layouts/GuideLayout.astro)**:
   - Importación de la hoja de estilos nativa `'katex/dist/katex.min.css'`.
   - Reglas CSS dedicadas para `.guide-article .katex-display`:
     - Fondo con color semántico `var(--surface)` y borde suave `var(--border)`.
     - `padding: 1rem 1.25rem`, bordes redondeados (`0.5rem`).
     - Desplazamiento horizontal responsivo (`overflow-x: auto`) para que fórmulas extensas no desborden la vista en pantallas móviles.
   - Ajuste de contraste y tipografía para modo claro y oscuro.

3. **Saneamiento y Normalización de [`src/pages/derecho-fiscal/guia.md`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/pages/derecho-fiscal/guia.md)**:
   - Limpieza de operadores en prosa convertidos a caracteres Unicode limpios (`≤`, `≥`, `→`, `≠`, `≈`, `⟹`, `< 25.000 €`).
   - Normalización de las 44 fórmulas matemáticas (cuestiones teóricas y supuestos prácticos 1 a 16) con sintaxis LaTeX limpia (`\text{...}`, `\times`, `\frac{...}{...}`).
   - Formateo de ecuaciones de visualización (*display math*) en líneas independientes con delimitadores `$$ ... $$`.

---

## 3. Estado de Métricas de Contenido

- Total Preguntas: 2.972
- Total Fichas y Glosarios: 470
- Total Documentos PDF: 21
- Total Guías y Recursos: 7
- Total Asignaturas: 64
- Bloques de Material: 54

---

## 4. Verificación y Pruebas

- **`npm run stats`**: Ejecutado satisfactoriamente, métricas verificadas.
- **`npm run build`**: 103 páginas generadas correctamente en modo estático en ~3.3s sin errores de validación.
- **Verificación local**: Inspección de `/derecho-fiscal/guia/` con MathML y KaTeX CSS cargado adecuadamente.
