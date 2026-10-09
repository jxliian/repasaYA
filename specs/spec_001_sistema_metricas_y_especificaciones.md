# Spec 001: Inicialización del Sistema de Especificaciones y Control de Métricas

- **Fecha**: 2026-10-09
- **Estado**: Implementado
- **Ámbito**: Infraestructura / Métricas / Especificaciones

---

## 1. Contexto y Motivación

Para mantener un desarrollo ordenado y una memoria a largo plazo clara en repasaYA:
1. Se establece el directorio `specs/` como el registro auditable de especificaciones funcionales y técnicas del proyecto.
2. Se implementa un mecanismo automatizado de recuento de contenidos para evitar la desincronización de los contadores mostrados en la landing page y el mapa web.
3. Se protegen las directrices y flujos operativos internos en `.gitignore` para preservar la privacidad de las metodologías de trabajo.

---

## 2. Descripción de los Cambios

### A. Sistema de Especificaciones (`specs/`)
- Creación de la carpeta `specs/` con su índice regulador [specs/README.md](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/specs/README.md).
- Adopción de la convención de nomenclatura `spec_XXX_<descripcion>.md`.

### B. Herramienta de Cuantificación (`scripts/count-stats.mjs`)
- Creación de un script en Node.js que recorre `src/content/materials/` y `src/content/subjects/`.
- Permite calcular en menos de 150 ms el recuento exacto de preguntas, flashcards, glosarios y PDFs sin requerir inspecciones manuales intensivas.
- Incorporación del comando `npm run stats` en [package.json](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/package.json).

### C. Privacidad y Seguridad en `.gitignore`
- Configuración de exclusión en [.gitignore](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/.gitignore) para que la carpeta de directrices del agente (`.agents/`), `AGENTS.md`, `GEMINI.md` y `.claude/` permanezcan locales y privadas, sin exponerse en el repositorio público de GitHub.

---

## 3. Línea Base de Métricas de Contenido

A fecha de esta especificación, el recuento oficial validado es:

| Métrica | Total Actual | Desglose Principal |
| :--- | :--- | :--- |
| **Preguntas Activas** | **2.622** | • Tipo Test: 1.997<br>• Verdadero / Falso: 509<br>• Respuesta Oculta (Reveal): 116 |
| **Fichas y Glosarios** | **377** | • Flashcards: 231<br>• Glosario: 146 |
| **Documentos PDF** | **16** | Exámenes oficiales, relaciones de problemas y apuntes LaTeX |
| **Guías y Recursos** | **5** | Guías de estudio interactivas y proyectos |
| **Asignaturas Totales** | **64** | 15 con material activo (`available`), 49 planificadas (`planned`) |
| **Bloques de Material** | **39** | Archivos JSON en `src/content/materials/` |

---

## 4. Verificación y Pruebas

- **Recuento de métricas**: `npm run stats` finalizado con éxito sin errores de lectura.
- **Compilación estática**: `npm run build` ejecutado y validado (85 páginas generadas).
