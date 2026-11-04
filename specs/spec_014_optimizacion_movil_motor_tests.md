# Spec 014: Optimización Responsiva Móvil y Limpieza Visual en el Motor de Tests

- **Fecha**: 2026-11-04
- **Estado**: Implementado
- **Ámbito**: UI/UX / Motor de Tests / Responsivo Móvil (`QuizEngine.astro`, `QuizShell.astro`)

---

## 1. Contexto y Motivación

En pantallas de dispositivos móviles (teléfonos inteligentes de 360px a 430px de ancho), la interfaz del motor de tests presentaba una sobrecarga de elementos auxiliares fijos y cabeceras redundantes que reducían el espacio útil para responder cómodamente a las preguntas:
1. El botón flotante de **RepasaBot** (*"¿Dudas? 💬"*) y el botón de **GitHub** (*"Sígueme en GitHub ⭐"*) solapaban botones de opciones o controles de navegación.
2. La cabecera superior mostraba duplicidad de información (`← Derecho Fiscal | DF · Derecho Fiscal`), ocupando múltiples líneas en pantallas pequeñas.
3. Al realizar activamente un test, coexistían dos flechas de navegación a la vez: la de la cabecera superior (para salir a la asignatura) y la de la cabecera del test (`← Menú`, para salir al menú del test).
4. La pestaña *"Banco"* y el contador de estadísticas (`#hdr-stats`) recargaban la vista superior sin aportar valor al flujo ágil de estudio móvil.

---

## 2. Descripción de los Cambios

1. **Supresión de Elementos Flotantes en Móvil (`@media (max-width: 768px)`)**:
   - Ocultación completa de RepasaBot (`#repasa-bot-root`) en [`QuizShell.astro`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/layouts/QuizShell.astro) y [`QuizEngine.astro`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/components/QuizEngine.astro).
   - Ocultación del botón flotante `.github-fab` en [`QuizEngine.astro`](file:///home/jxlig0d/Escritorio/PROYECTOS/repasaya/repasaYA/src/components/QuizEngine.astro).

2. **Cabecera Simplificada y Desduplicada en el Menú Selector**:
   - Ocultación en móvil del título redundante de la asignatura junto a la flecha (`.back-label`), del separador (`.header-divider`), del logo/código derecho (`header .logo`) y del texto de estadísticas (`#hdr-stats`).
   - El botón de volver a la asignatura se estiliza como un control táctil limpio con la flecha `←`, dejando únicamente este botón a la izquierda y el interruptor de tema a la derecha.

3. **Flujo de Navegación Desduplicado entre Menú y Test**:
   - Incorporación del estado reactivo `document.documentElement.dataset.quizActive = 'true' | 'false'`.
   - **En realización del test (`quizActive = 'true'`)**: en móvil se ocultan automáticamente la cabecera superior y las pestañas, garantizando que arriba figure **únicamente** la flecha para salir al menú (`← Menú`) junto al contador de preguntas y la puntuación.
   - **En el menú selector (`quizActive = 'false'`)**: reaparece la cabecera con la flecha para salir a la asignatura.

4. **Pestañas y Espaciado Adaptado**:
   - Ocultación en móvil de la pestaña *"Banco"*; si la asignatura no dispone de supuestos adicionales, la barra de pestañas completa se oculta para no ocupar espacio innecesario.
   - Ocultación de pistas de teclado físico (`.kbd-hints`) no aplicables en dispositivos táctiles.
   - Reducción de márgenes y paddings en contenedores (`main`, `.q-card`, `.q-case-body`) para maximizar el área de lectura en pantallas pequeñas.

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
- **`npm run build`**: 103 páginas generadas en modo SSG en ~4.4s sin errores.
- **Inspección de bundles CSS/HTML**: Confirmadas las reglas minificadas para `@media (max-width: 768px)` y la activación de `data-quiz-active`.
