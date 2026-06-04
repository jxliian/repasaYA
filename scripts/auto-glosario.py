#!/usr/bin/env python3
"""
auto-glosario.py — Genera un glosario JSON a partir de un PDF usando Claude API.

Uso:
  python3 scripts/auto-glosario.py <pdf> <asignatura> [output.json]

Ejemplos:
  python3 scripts/auto-glosario.py apuntes/rrhhtodo.pdf "Dirección de RRHH I"
  python3 scripts/auto-glosario.py apuntes/do1.pdf "Dirección de Operaciones I" src/data/do1-glosario.json

Requiere: ANTHROPIC_API_KEY en el entorno.
"""

import anthropic
import json
import sys
import os
import re
import pdfplumber


# ── Configuración ──────────────────────────────────────────────────────────────

MODEL   = "claude-haiku-4-5-20251001"  # rápido y barato para extracción
PAGES_PER_CHUNK = 4                    # páginas por llamada a la API
MAX_TOKENS = 4096


# ── Extracción de texto del PDF ────────────────────────────────────────────────

def extract_pages(pdf_path: str) -> list[str]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            # Normalizar espacios y saltos de línea
            text = re.sub(r'\n{3,}', '\n\n', text.strip())
            if len(text) > 50:          # ignorar páginas casi vacías (portadas, imágenes)
                pages.append(text)
    return pages


# ── Llamada a la API ───────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Eres un asistente académico especializado en extraer glosarios de apuntes universitarios.
Tu tarea es identificar TODOS los términos y conceptos importantes y devolver ÚNICAMENTE un JSON válido, sin markdown, sin explicaciones."""

def extract_terms_from_chunk(client: anthropic.Anthropic, chunk: str, subject: str, tema_hint: str) -> list[dict]:
    prompt = f"""Analiza este fragmento de apuntes universitarios de "{subject}" y extrae TODOS los términos importantes.

Para cada término devuelve un objeto JSON con:
- "term": nombre del término (exacto, en español, sin mayúsculas innecesarias)
- "def": definición clara y completa basada en el texto (2-5 frases, menciona características clave)
- "tema": "{tema_hint}"

Reglas:
- Incluye TODOS los términos: conceptos, técnicas, métodos, errores, tipos, siglas
- Si un término aparece definido explícitamente, usa esa definición
- No inventes información que no esté en el texto
- Evita duplicar términos ya vistos
- Devuelve SOLO el array JSON, sin texto adicional

Fragmento:
{chunk}"""

    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        content = message.content[0].text.strip()

        # Buscar el array JSON en la respuesta
        start = content.find('[')
        end   = content.rfind(']') + 1
        if start == -1 or end <= start:
            print(f"    ⚠  No se encontró JSON en la respuesta")
            return []

        return json.loads(content[start:end])

    except json.JSONDecodeError as e:
        print(f"    ⚠  JSON inválido: {e}")
        return []
    except anthropic.APIError as e:
        print(f"    ⚠  Error de API: {e}")
        return []


# ── Detección automática de tema por encabezado ────────────────────────────────

def detect_tema(page_text: str, current_tema: str) -> str:
    """Intenta detectar el título del tema/capítulo en la página."""
    # Busca líneas que parezcan títulos de tema (Tema N, T1:, Capítulo...)
    patterns = [
        r'(?i)^(tema\s+\d+[:\s].{5,60})$',
        r'(?i)^(t\d+[:\s].{5,60})$',
        r'(?i)^(cap[ií]tulo\s+\d+[:\s].{5,60})$',
    ]
    for line in page_text.split('\n')[:8]:  # solo primeras líneas
        for pattern in patterns:
            m = re.match(pattern, line.strip())
            if m:
                raw = m.group(1).strip()
                # Limpiar y truncar
                raw = re.sub(r'\s+', ' ', raw)[:60]
                return raw
    return current_tema


# ── Deduplicación ─────────────────────────────────────────────────────────────

def deduplicate(terms: list[dict]) -> list[dict]:
    seen = set()
    result = []
    for t in terms:
        key = t.get('term', '').lower().strip()
        # Normalizar: eliminar paréntesis y texto entre ellos para la clave
        key_clean = re.sub(r'\s*\(.*?\)', '', key).strip()
        if key_clean and key_clean not in seen:
            seen.add(key_clean)
            result.append(t)
    return result


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    subject  = sys.argv[2]
    output   = sys.argv[3] if len(sys.argv) > 3 else 'glosario-output.json'

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Falta la variable de entorno ANTHROPIC_API_KEY")
        print("   Añádela con: export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    if not os.path.exists(pdf_path):
        print(f"❌ No se encuentra el PDF: {pdf_path}")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # ── 1. Extraer texto del PDF
    print(f"\n📄 Extrayendo texto de {pdf_path}...")
    pages = extract_pages(pdf_path)
    print(f"   {len(pages)} páginas con contenido")

    # ── 2. Procesar en chunks
    all_terms   = []
    current_tema = f"T1: {subject}"
    total_chunks = (len(pages) + PAGES_PER_CHUNK - 1) // PAGES_PER_CHUNK

    print(f"\n🤖 Extrayendo términos con Claude ({MODEL})...")
    print(f"   {total_chunks} chunks de {PAGES_PER_CHUNK} páginas\n")

    for i in range(0, len(pages), PAGES_PER_CHUNK):
        chunk_pages = pages[i:i + PAGES_PER_CHUNK]
        chunk_num   = (i // PAGES_PER_CHUNK) + 1

        # Detectar tema del chunk
        for p in chunk_pages:
            detected = detect_tema(p, current_tema)
            if detected != current_tema:
                current_tema = detected
                print(f"   📌 Nuevo tema detectado: {current_tema}")

        chunk_text = '\n\n---\n\n'.join(chunk_pages)
        page_range = f"{i+1}-{min(i+PAGES_PER_CHUNK, len(pages))}"
        print(f"   Chunk {chunk_num}/{total_chunks} (páginas {page_range}, tema: {current_tema[:40]})...", end=' ', flush=True)

        terms = extract_terms_from_chunk(client, chunk_text, subject, current_tema)
        all_terms.extend(terms)
        print(f"✓ {len(terms)} términos")

    # ── 3. Deduplicar y limpiar
    unique_terms = deduplicate(all_terms)
    print(f"\n✅ Total: {len(all_terms)} términos extraídos → {len(unique_terms)} únicos tras deduplicar")

    # ── 4. Guardar JSON
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(unique_terms, f, ensure_ascii=False, indent=2)

    print(f"💾 Guardado en: {output}")

    # ── 5. Resumen por tema
    temas = {}
    for t in unique_terms:
        tema = t.get('tema', 'Sin tema')
        temas[tema] = temas.get(tema, 0) + 1
    print("\n📊 Distribución por tema:")
    for tema, count in temas.items():
        print(f"   {tema[:50]:<50} {count:>3} términos")


if __name__ == '__main__':
    main()
