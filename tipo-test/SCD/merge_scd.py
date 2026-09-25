#!/usr/bin/env python3
"""
merge_scd.py - Script de integración y combinación segura de preguntas tipo test de SCD.
Combina preguntas de autoevaluación, exámenes y fuentes web evitando duplicados y
garantizando que ninguna ejecución paralela sobrescriba o pierda preguntas.
"""

import os
import sys
import json
import glob
import re
import string
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

SCD_DIR = BASE_DIR
SCD_JSON = os.path.join(SCD_DIR, "scd.json")

MATERIALS_DIR = os.path.join(
    REPO_ROOT, "src", "content", "materials", "informatica", "sistemas-concurrentes-y-distribuidos"
)
MATERIAL_TEST_JSON = os.path.join(MATERIALS_DIR, "test.json")

SUBJECT_MD = os.path.join(
    REPO_ROOT, "src", "content", "subjects", "informatica", "sistemas-concurrentes-y-distribuidos.md"
)

def normalize_for_compare(text: str) -> str:
    """Normaliza texto para comparación y detección precisa de duplicados."""
    if not text:
        return ""
    # Descomponer caracteres con acentos
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    # Eliminar todos los signos de puntuación, símbolos y espacios
    return re.sub(r"[^\w]", "", text)

def atomic_write_json(file_path: str, data: object, indent: int = 2):
    """Escribe un archivo JSON de forma atómica para evitar colisiones."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    temp_path = file_path + f".tmp.{os.getpid()}"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp_path, file_path)

def load_items_from_file(file_path: str):
    """Carga preguntas desde un archivo JSON (lista o estructura de material)."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "items" in data and isinstance(data["items"], list):
                return data["items"]
    except Exception as e:
        print(f"Error cargando {file_path}: {e}", file=sys.stderr)
    return []

def main():
    merged_items = []
    seen_keys = set()

    def add_item(item):
        if not isinstance(item, dict):
            return False
        q = item.get("q", "").strip()
        opts = item.get("opts", [])
        correct = item.get("correct")

        if not q or not isinstance(opts, list) or len(opts) < 2 or correct is None:
            return False

        key = normalize_for_compare(q)
        if not key or key in seen_keys:
            return False

        seen_keys.add(key)
        tema = item.get("tema", "SCD").strip()
        cleaned_item = {
            "tema": tema,
            "q": q,
            "opts": [str(o).strip() for o in opts],
            "correct": int(correct)
        }
        if "justification" in item and item["justification"]:
            cleaned_item["justification"] = str(item["justification"]).strip()

        merged_items.append(cleaned_item)
        return True

    # 1. Cargar preguntas existentes en scd.json si existen
    if os.path.exists(SCD_JSON):
        existing_scd = load_items_from_file(SCD_JSON)
        for it in existing_scd:
            add_item(it)

    # 2. Cargar preguntas existentes en el material de Astro si existe
    if os.path.exists(MATERIAL_TEST_JSON):
        existing_mat = load_items_from_file(MATERIAL_TEST_JSON)
        for it in existing_mat:
            add_item(it)

    # 3. Cargar todos los archivos .json en tipo-test/SCD/ (autoevaluaciones, tests web, etc.)
    json_files = sorted(glob.glob(os.path.join(SCD_DIR, "*.json")))
    for jf in json_files:
        if os.path.abspath(jf) == os.path.abspath(SCD_JSON):
            continue
        items = load_items_from_file(jf)
        added_count = 0
        for it in items:
            if add_item(it):
                added_count += 1
        print(f"Leído {os.path.basename(jf)}: {len(items)} preguntas ({added_count} añadidas)")

    print(f"\nTotal preguntas consolidadas: {len(merged_items)}")

    # 4. Guardar atómicamente en tipo-test/SCD/scd.json
    atomic_write_json(SCD_JSON, merged_items)
    print(f"Guardado exitoso en: {SCD_JSON}")

    # 5. Guardar en src/content/materials/.../test.json
    os.makedirs(MATERIALS_DIR, exist_ok=True)
    astro_material = {
        "subject": "informatica/sistemas-concurrentes-y-distribuidos",
        "type": "test",
        "title": "Tipo test",
        "order": 0,
        "items": merged_items
    }
    atomic_write_json(MATERIAL_TEST_JSON, astro_material)
    print(f"Guardado exitoso en: {MATERIAL_TEST_JSON}")

    # 6. Actualizar frontmatter de la asignatura
    if os.path.exists(SUBJECT_MD):
        with open(SUBJECT_MD, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Asegurar status: available y materials: [test]
        md_content = re.sub(r"status:\s*planned", "status: available", md_content)
        if "materials: []" in md_content:
            md_content = md_content.replace("materials: []", "materials: [test]")
        elif "materials:" in md_content and "test" not in md_content:
            md_content = re.sub(r"materials:\s*\[(.*?)\]", r"materials: [\1, test]", md_content)

        desc = f'"{len(merged_items)} preguntas tipo test de autoevaluación y exámenes sobre concurrencia, monitores, paso de mensajes y tiempo real."'
        if "description:" in md_content:
            md_content = re.sub(r'description:\s*".*?"', f'description: {desc}', md_content)
        else:
            # Añadir description después de status
            md_content = re.sub(r'(status:\s*\w+)', r'\1\ndescription: ' + desc, md_content)

        with open(SUBJECT_MD, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Actualizado frontmatter en: {SUBJECT_MD}")

    # 7. Actualizar datos embebidos en index.html si existe
    index_html = os.path.join(SCD_DIR, "index.html")
    if os.path.exists(index_html):
        try:
            with open(index_html, "r", encoding="utf-8") as f:
                html_code = f.read()
            json_blob = json.dumps(merged_items, ensure_ascii=False)
            html_code = re.sub(
                r"let ALL = \[.*?\];",
                f"let ALL = {json_blob};",
                html_code,
                flags=re.DOTALL
            )
            with open(index_html, "w", encoding="utf-8") as f:
                f.write(html_code)
            print(f"Actualizado index.html con {len(merged_items)} preguntas.")
        except Exception as e:
            print(f"Error actualizando index.html: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
