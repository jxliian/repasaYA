# Spec 005: Modelo de Orquestación Concurrente y Simultánea Multiagente

- **Fecha**: 2026-10-09
- **Estado**: Implementado
- **Ámbito**: Arquitectura de Agentes / Rendimiento / Paralelismo

---

## 1. Contexto y Motivación

En pipelines de agentes tradicionales, la ejecución secuencial paso a paso (un solo agente procesando todo el archivo de principio a fin) presenta dos cuellos de botella severos:
1. **Alta latencia**: Procesar un PDF de 10 temas o cientos de preguntas de forma monohilo toma demasiado tiempo.
2. **Degradación de contexto**: Un único hilo acumulando cientos de enunciados agota su presupuesto de atención y comete más erratas.

Esta especificación formaliza el **Modelo de Concurrencia Simultánea**, donde las tareas se dividen en ramas paralelas procesadas a la vez por subagentes en segundo plano, convergiendo en una barrera de sincronización y auditoría final.

---

## 2. Arquitectura Concurrente (Map-Reduce Multiagente)

```
                            [ TAREA COMPLEJA ]
                                    │
                                    ▼
                      ┌───────────────────────────┐
                      │    COORDINADOR (Scatter)  │
                      └─────────────┬─────────────┘
                                    │ Despliegue concurrente
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
    ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
    │  EJECUTOR 1   │       │  EJECUTOR 2   │       │  EJECUTOR 3   │
    │  (Bloque T1)  │       │  (Bloque T2)  │       │  (Bloque T3)  │
    └───────┬───────┘       └───────┬───────┘       └───────┬───────┘
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
    │ REVISIÓN T1   │       │ REVISIÓN T2   │       │ REVISIÓN T3   │
    └───────┬───────┘       └───────┬───────┘       └───────┬───────┘
            └───────────────────────┼───────────────────────┘
                                    │ Convergencia
                                    ▼
                      ┌───────────────────────────┐
                      │  AUDITORÍA FINAL (Barrier)│
                      │   (npm run stats / build) │
                      └─────────────┬─────────────┘
                                    ▼
                      ┌───────────────────────────┐
                      │    COMMIT Y CONSOLIDACIÓN │
                      └───────────────────────────┘
```

---

## 3. Principios de la Ejecución Simultánea

### A. Particionamiento Horizontal y Map-Reduce
- Cuando una tarea excede un volumen manejable (p. ej. un examen de 60 preguntas o apuntes de varios temas), el Coordinador fragmenta la carga en bloques ortogonales independientes.
- Se lanzan los ejecutores simultáneamente en paralelo a través de `invoke_subagent`.

### B. Revisión Dual Concurrente
- La revisión técnica (validación de esquemas Zod, sintaxis y formato base 0) y la revisión pedagógica (fidelidad a las guías de la UGR y calidad de justificaciones) pueden correr en paralelo, reduciendo el tiempo de control de calidad a la mitad.

### C. Barrera de Sincronización Estricta (*Synchronization Barrier*)
- Los ejecutores y revisores pueden correr de forma asíncrona y simultánea, pero **ningún cambio se consolida ni se commitea** hasta que todos convergen en la barrera del Auditor:
  1. Verificación matemática unificada con `npm run stats`.
  2. Compilación estática global con `npm run build`.
  3. Verificación de los 7 Artículos de la Constitución.

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

- **Métricas**: `npm run stats` verificado.
- **Compilación estática**: `npm run build` ejecutado y validado (85 páginas generadas).
