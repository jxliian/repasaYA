# Spec 003: Orquestación Multiagente con Ciclos de Revisión y Auditoría

- **Fecha**: 2026-10-09
- **Estado**: Implementado
- **Ámbito**: Arquitectura de Agentes / Control de Calidad / Gobernanza

---

## 1. Contexto y Motivación

En tareas de desarrollo y generación de contenido docente para **repasaYA**, la delegación de responsabilidades en un único agente puede propiciar descuidos técnicos (índices base 0 incorrectos, fallos de esquema Zod, rutas erróneas de PDFs) o desviaciones sobre las políticas de git y la Constitución del proyecto.

Esta especificación establece el **modelo de orquestación colaborativa multiagente**, definiendo una separación estricta de responsabilidades entre cuatro roles especializados: **Coordinador**, **Ejecutor(es)**, **Revisor** y **Auditor**.

---

## 2. Los Cuatro Roles del Sistema

```
                  ┌────────────────────────┐
                  │   USUARIO / MANTENEDOR │
                  └───────────┬────────────┘
                              │ Petición
                              ▼
                  ┌────────────────────────┐
                  │   AGENTE COORDINADOR   │
                  └───────────┬────────────┘
                              │ Descomposición y asignación
                              ▼
                  ┌────────────────────────┐
                  │  AGENTE(S) EJECUTOR(ES)│
                  └───────────┬────────────┘
                              │ Artefactos producidos
                              ▼
                  ┌────────────────────────┐
                  │     AGENTE REVISOR     │◄───┐
                  └───────────┬────────────┘    │
                              │ Aprobado        │ Request Changes
                              ▼                 │ (Devolver si falla)
                  ┌────────────────────────┐    │
                  │     AGENTE AUDITOR     ├────┘
                  └───────────┬────────────┘
                              │ Certificación final (Sign-off)
                              ▼
                  ┌────────────────────────┐
                  │    ENTREGA Y COMMIT    │
                  └────────────────────────┘
```

---

### 1. Agente Coordinador (Orchestrator)
- **Misión**: Planificación macro, descomposición de tareas, gestión de dependencias y síntesis de la respuesta final.
- **Responsabilidades**:
  - Analiza la solicitud del usuario y determina si se requiere trabajo en paralelo o secuencial.
  - Genera el desglose de tareas (WBS) y asigna objetivos a los Ejecutores.
  - Supervisa que el flujo avance ordenadamente por las fases de Ejecución, Revisión y Auditoría.
  - Consolida el mensaje de entrega al usuario con enlaces clicables a los archivos modificados.

---

### 2. Agente(s) Ejecutor(es) (Workers / Implementers)
- **Misión**: Producción efectiva de código, contenidos o configuración.
- **Especializaciones Posibles**:
  - **Worker de Contenido**: Creación o edición de archivos JSON de preguntas, tarjetas o asignaturas (`src/content/`).
  - **Worker de Componentes/UI**: Modificación de plantillas Astro, estilos CSS o scripts ligeros en cliente.
  - **Worker de Documentación/LaTeX**: Redacción de apuntes, problemas resueltos o documentación técnica.
- **Responsabilidades**:
  - Implementar los cambios siguiendo las especificaciones del Coordinador.
  - Respetar los estándares de código y esquemas Zod.
  - Entregar los archivos modificados al Revisor sin saltarse el filtro de calidad.

---

### 3. Agente Revisor (Technical & Pedagogical Reviewer)
- **Misión**: Verificación de exactitud técnica, sintáctica y calidad académica.
- **Filtros de Inspección**:
  - **Revisión Pedagógica**:
    * ¿Las preguntas corresponden al temario oficial de la UGR?
    * ¿Las justificaciones explican con claridad el razonamiento de fondo?
    * ¿Las opciones incorrectas son plausibles y sin ambigüedades?
  - **Revisión Técnica**:
    * En preguntas tipo test, ¿el índice `correct` está en **base 0**?
    * ¿El array `opts` contiene al menos dos opciones no vacías?
    * Si hay PDFs, ¿la ruta en el JSON es relativa a `public/` (sin escribir `public/`)?
    * ¿El frontmatter de las asignaturas concuerda con los tipos de material presentes?
- **Salida**: Aprobación (*Approval*) o Petición de Correcciones (*Request Changes* con detalle de las líneas a corregir).

---

### 4. Agente Auditor (Compliance & Quality Auditor)
- **Misión**: Garantía de cumplimiento constitucional, integridad métrica y seguridad operativa.
- **Checklist Inviolable de Auditoría**:
  1. **Auditoría Constitucional**:
     - ¿Se respeta la regla de 0 KB JS de frameworks en el cliente?
     - ¿El contenido sigue siendo 100% gratuito y sin fricciones de registro?
  2. **Auditoría de Métricas**:
     - Ejecutar `npm run stats` y verificar que los totales de preguntas y fichas concuerdan con la línea base y la landing page.
  3. **Auditoría de Compilación**:
     - Ejecutar `npm run build` y asegurar 0 errores en esquemas Zod y 85+ páginas generadas.
  4. **Auditoría de Git (`PUSH_POLICY`)**:
     - ¿Se intenta hacer push a remoto? Si no es una adición de contenido docente ni una orden expresa del usuario, **el push queda vetado**.
     - ¿Archivos privados (`.agents/`, `AGENTS.md`) permanecen ignorados en `.gitignore`?
- **Salida**: Certificación de Conformidad (*Sign-off*) que habilita la consolidación del cambio.

---

## 3. Protocolo de Ejecución Paso a Paso

1. **Recepción y Plan**: El Coordinador recibe la tarea y emite un plan enumerando los pasos de ejecución y los criterios de aceptación.
2. **Implementación**: Los Ejecutores realizan los cambios en los archivos correspondientes.
3. **Revisión Paritaria**: El Revisor analiza los diffs y emite su dictamen. Si hay fallos, el Ejecutor corrige y se repite la revisión.
4. **Auditoría Estricta**: El Auditor corre `npm run stats` y `npm run build`, verifica la Constitución y autoriza o bloquea el commit/push.
5. **Cierre**: El Coordinador actualiza la especificación en `specs/`, realiza el commit local y presenta el resumen al usuario.

---

## 4. Estado de Métricas del Contenido

| Métrica | Valor Validado |
| :--- | :--- |
| **Total Preguntas Activas** | **2.622** |
| **Total Fichas y Glosarios** | **377** |
| **Documentos PDF** | **16** |
| **Guías y Recursos** | **5** |
| **Total Asignaturas** | **64** (15 disponibles / 49 planificadas) |
| **Bloques de Material** | **39** |

---

## 5. Verificación y Pruebas

- **Herramienta de métricas**: `npm run stats` ejecutado con éxito.
- **Compilación estática**: `npm run build` validado con 85 páginas generadas.
