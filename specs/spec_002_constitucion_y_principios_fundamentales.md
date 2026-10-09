# Spec 002: Constitución y Principios Fundamentales del Proyecto

- **Fecha**: 2026-10-09
- **Estado**: Implementado
- **Ámbito**: Gobernanza / Principios / Filosofía de Proyecto

---

## 1. Contexto y Motivación

A medida que **repasaYA** crece en número de asignaturas, tipos de preguntas y colaboradores (tanto humanos como agentes de IA), es esencial contar con un **marco de principios inviolables** que fije la dirección del proyecto y prevenga desviaciones en su misión original.

Esta especificación formaliza la **Constitución de repasaYA**, estableciendo los 7 pilares supremos sobre los que se sustenta cada desarrollo técnico y adición de contenido.

---

## 2. Los 7 Principios Constitucionales

### Artículo I: Soberanía del Estudiante y Acceso Libre Universal
- **100% Gratuito y Libre**: Prohibidos muros de pago, modelos de suscripción y cuentas de pago.
- **Sin Publicidad**: La interfaz está dedicada exclusivamente al estudio, libre de anuncios y banners.
- **Sin Registro Forzoso**: El acceso al estudio es instantáneo sin necesidad de crear usuario ni iniciar sesión.
- **Privacidad Local**: Las preguntas falladas, favoritas y progresos residen exclusivamente en el almacenamiento local del navegador (`localStorage`).

### Artículo II: Rigor Académico y Fidelidad Pedagógica
- Contenidos contrastados con las guías docentes y exámenes oficiales de la **Universidad de Granada (UGR)** para ADE e Informática.
- Prioridad a la **justificación explicativa** en preguntas de test y verdadero/falso para enseñar el *porqué* de cada concepto.
- Tolerancia cero al error conceptual: las erratas reportadas se solventan con máxima prioridad.

### Artículo III: Rendimiento Extremo y Minimalismo Técnico
- **0 KB JS de Frameworks en Cliente**: Construido sobre Astro 6 estático sin frameworks pesados (React, Vue, Svelte) en cliente.
- Carga casi instantánea en dispositivos móviles y redes universitarias lentas.
- Generación estática pura (SSG precompilado en `dist/`).

### Artículo IV: Desacoplamiento y Arquitectura Declarativa
- Todo el contenido docente se gestiona en archivos JSON y Markdown dentro de `src/content/`.
- Validación estricta con esquemas **Zod** en `src/content.config.ts`. Si un dato no es válido, el build falla y no se publica.
- Independencia curricular: curso y cuatrimestre se parametrizan en el frontmatter para no romper rutas al actualizar planes de estudio.

### Artículo V: Veracidad Matemática y Control de Métricas
- Los contadores de la landing page y el mapa web deben reflejar fielmente la suma real de preguntas y fichas.
- Obligatoriedad de ejecutar la herramienta de cuantificación (`npm run stats`) antes de consolidar cambios.

### Artículo VI: Disciplina de Publicación y Respeto a Git
- **Política de Push (`PUSH_POLICY`)**: `git push` a remoto se reserva para adiciones de contenido académico de estudio o bajo indicación expresa del usuario.
- Privacidad de las metodologías internas de agentes bajo exclusión estricta en `.gitignore`.
- Registro evolutivo público a través de especificaciones secuenciales en `specs/`.

### Artículo VII: Jerarquía de Autoridad y Colaboración
- La dirección del proyecto corresponde al autor y mantenedor Julián Carrión (`@jxliian`).
- Los agentes y herramientas colaboran bajo estricta subordinación a estos principios y con vocación de servicio a la comunidad estudiantil.

---

## 3. Estado de Métricas del Contenido

| Métrica | Valor Validado |
| :--- | :--- |
| **Total Preguntas Activas** | **2.622** |
| **Total Fichas y Glosarios** | **377** |
| **Documentos PDF** | **16** |
| **Guías y Recursos** | **5** |
| **Total Asignaturas** | **64** (15 disponibles / 49 planificadas) |
| **Bloques de Material** | **39** |

---

## 4. Verificación y Pruebas

- **Métricas verificadas**: `npm run stats` completado con éxito.
- **Compilación verificada**: `npm run build` ejecutado y validado (85 páginas generadas).
