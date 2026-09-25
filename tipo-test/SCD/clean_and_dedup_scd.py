#!/usr/bin/env python3
"""
clean_and_dedup_scd.py
Limpia, valida, redacta con precisión y elimina duplicados de las preguntas tipo test de SCD.
"""

import json
import os
import re
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

MATERIAL_JSON = os.path.join(
    REPO_ROOT, "src", "content", "materials", "informatica", "sistemas-concurrentes-y-distribuidos", "test.json"
)
SCD_JSON = os.path.join(BASE_DIR, "scd.json")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
SUBJECT_MD = os.path.join(
    REPO_ROOT, "src", "content", "subjects", "informatica", "sistemas-concurrentes-y-distribuidos.md"
)

def clean_str(text: str) -> str:
    if not text:
        return ""
    # Descomponer LaTeX
    text = text.replace(r"\(", "").replace(r"\)", "")
    text = text.replace(r"\[", "").replace(r"\]", "")
    text = text.replace(r"\wedge", "∧").replace(r"\vee", "∨")
    text = text.replace(r"\leq", "≤").replace(r"\le", "≤")
    text = text.replace(r"\geq", "≥").replace(r"\ge", "≥")
    text = text.replace(r"\neq", "≠")
    text = text.replace("∗", "*").replace("’", "'").replace("“", '"').replace("”", '"')
    
    # Limpiar tags HTML
    text = re.sub(r"</?(?:pre|code|p|div|strong|span)[^>]*>", " ", text)
    
    # Reemplazar código atómico entre < y > por ⟨ y ⟩ para evitar problemas en innerHTML
    text = re.sub(r"<([^>]+)>", r"⟨\1⟩", text)
    
    # Correcciones ortográficas y de redacción
    text = text.replace("Cúal", "Cuál")
    text = text.replace("Hyman (1996)", "Hyman (1966)")
    text = text.replace(
        "preposición sobre quien asigna turn en un último lugar",
        "proposición sobre quién asigna turno en último lugar"
    )
    text = text.replace(
        "proposición sobre quien asigna turno en último lugar",
        "proposición sobre quién asigna turno en último lugar"
    )
    
    # Espacios
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)
    return text.strip()

def main():
    with open(MATERIAL_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    raw_items = data.get("items", [])
    print(f"Cargadas {len(raw_items)} preguntas iniciales.")

    # 1. Índices a eliminar por ser duplicados exactos o versiones de menor calidad
    remove_indices = {
        184, 191, 199, 176, 204, 201, 172, 166, 178, 169, 193,
        165, 198, 187, 154, 163, 190, 185, 203, 141, 158
    }

    cleaned_items = []
    for idx, item in enumerate(raw_items):
        if idx in remove_indices:
            continue
        
        q = clean_str(item["q"])
        opts = [clean_str(o) for o in item["opts"]]
        
        # Quitar prefijos a. / b. / 1.
        opts = [re.sub(r"^[a-eA-E][\.\)]\s*", "", o).strip() for o in opts]
        opts = [re.sub(r"^\d+[\.\)]\s*", "", o).strip() for o in opts]
        
        # Asegurar capitalización inicial en opciones
        opts = [(o[0].upper() + o[1:]) if len(o) > 1 and o[0].islower() else o for o in opts]
        
        correct = int(item["correct"])
        tema = clean_str(item.get("tema", "SCD"))
        
        # Caso especial: Item 156 (Demostración de corrección con Hoare)
        if "fragmento concurrente a menos que se cumpla" in q or "fragmento de programa concurrente" in q:
            q = (
                "¿Por qué no se puede demostrar la corrección del siguiente fragmento de programa concurrente a menos que se cumpla a = 0?\n"
                "{x == 0 ∧ y == 0 ∧ z == 0}; ⟨x = z + a⟩ || ⟨y = x + b⟩; {x == a ∧ (y == b ∨ y == a + b) ∧ z == 0}"
            )
            opts = [
                "b = 0 ∨ a = 0.",
                "b = 0 ∧ a = 0.",
                "a = 0.",
                "Para cualquier valor de las variables.",
                "Es siempre indemostrable."
            ]
            correct = 2
            justification = (
                "Si a = 0, el proceso ⟨x = z + a⟩ no modifica el valor de x, por lo que no interfiere "
                "con la precondición del proceso ⟨y = x + b⟩. Para a ≠ 0 existe interferencia entre los procesos "
                "y la regla de composición concurrente directa no es aplicable sin variables auxiliares."
            )
        else:
            justification = clean_str(item.get("justification", ""))

        cleaned_entry = {
            "tema": tema,
            "q": q,
            "opts": opts,
            "correct": correct
        }
        if justification:
            cleaned_entry["justification"] = justification

        cleaned_items.append(cleaned_entry)

    print(f"Preguntas finales tras deduplicación y limpieza: {len(cleaned_items)}")

    # Validar integridad estricta
    for i, it in enumerate(cleaned_items):
        assert it["q"], f"Pregunta vacía en {i}"
        assert len(it["opts"]) >= 2, f"Menos de 2 opciones en {i}"
        assert 0 <= it["correct"] < len(it["opts"]), f"Índice correcto fuera de rango en {i}"
        for o in it["opts"]:
            assert o, f"Opción vacía en pregunta {i}"

    # Guardar en test.json (Astro content collection)
    astro_data = {
        "subject": "informatica/sistemas-concurrentes-y-distribuidos",
        "type": "test",
        "title": "Tipo test",
        "order": 0,
        "items": cleaned_items
    }
    with open(MATERIAL_JSON, "w", encoding="utf-8") as f:
        json.dump(astro_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado exitoso en {MATERIAL_JSON}")

    # Guardar en scd.json
    with open(SCD_JSON, "w", encoding="utf-8") as f:
        json.dump(cleaned_items, f, ensure_ascii=False, indent=2)
    print(f"Guardado exitoso en {SCD_JSON}")

    # Actualizar index.html
    if os.path.exists(INDEX_HTML):
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            html = f.read()
        json_blob = json.dumps(cleaned_items, ensure_ascii=False)
        html = re.sub(r"let ALL = \[.*?\];", f"let ALL = {json_blob};", html, flags=re.DOTALL)
        with open(INDEX_HTML, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Actualizado {INDEX_HTML} con {len(cleaned_items)} preguntas.")

    # Actualizar frontmatter
    if os.path.exists(SUBJECT_MD):
        with open(SUBJECT_MD, "r", encoding="utf-8") as f:
            md = f.read()
        desc = f'"{len(cleaned_items)} preguntas tipo test verificadas sobre concurrencia, monitores, paso de mensajes y tiempo real."'
        md = re.sub(r'description:\s*".*?"', f'description: {desc}', md)
        with open(SUBJECT_MD, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Actualizado frontmatter en {SUBJECT_MD}")

if __name__ == "__main__":
    main()
