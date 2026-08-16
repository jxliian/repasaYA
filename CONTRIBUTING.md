# Guía para Contribuir a repasaYA 🚀

¡Gracias por tu interés en contribuir a **repasaYA**! Toda ayuda es bienvenida para hacer de esta plataforma un recurso cada vez más completo para los estudiantes.

---

## 🛠️ Cómo añadir nuevo material de estudio

No necesitas saber programar en Astro ni frameworks de JavaScript. Todo el contenido vive en archivos JSON y Markdown dentro de la carpeta `src/content/`.

### 1. Revisa la asignatura
Busca tu asignatura en `src/content/subjects/<grado>/<slug>.md`.
* Grados disponibles: `ade` | `informatica`
* Si la asignatura existe, asegúrate de que en su frontmatter `status` esté marcado como `available` y que contenga los tipos de material que vas a subir en la lista `materials: [...]`.

### 2. Añade el archivo JSON de contenido
Crea tu archivo en `src/content/materials/<grado>/<slug>/<nombre>.json`.

#### Ejemplo para Test Interactivo (`type: "test"`):
```json
{
  "subject": "ade/econometria",
  "type": "test",
  "title": "Tipo Test Tema 1",
  "order": 1,
  "items": [
    {
      "tema": "Tema 1: Modelo Lineal",
      "q": "¿Qué supuesto no es necesario en MCO?",
      "opts": [
        "Homocedasticidad",
        "Normalidad de los errores para estimación puntual",
        "Ausencia de multicolinealidad perfecta"
      ],
      "correct": 1,
      "justification": "La normalidad solo se requiere para inferencia estadística en muestras pequeñas."
    }
  ]
}
```

#### Ejemplo para PDF (`type: "apuntes"` o `"examen"`):
1. Coloca el archivo PDF en `public/<slug>/tu-archivo.pdf`.
2. Crea el JSON en `src/content/materials/<grado>/<slug>/apuntes.json`:
```json
{
  "subject": "ade/econometria",
  "type": "apuntes",
  "title": "Apuntes de Teoría",
  "order": 1,
  "pdf": "econometria/tu-archivo.pdf",
  "description": "Apuntes completos del curso."
}
```

---

## 🧪 Validar tus cambios localmente

Antes de subir tu Pull Request, ejecuta el comando de validación:

```bash
npm install
npm run build
```

Si la compilación se completa sin errores, significa que el esquema Zod ha validado tu JSON correctamente.

---

## 📬 Envío de Pull Requests (PR)

1. Haz un **Fork** del repositorio.
2. Crea una rama descriptiva para tu cambio (`git checkout -b feature/material-econometria`).
3. Haz commit de tus cambios (`git commit -m "feat(econometria): añadir test tema 1"`).
4. Sube tu rama (`git push origin feature/material-econometria`).
5. Abre un **Pull Request** en GitHub hacia la rama `main`.
