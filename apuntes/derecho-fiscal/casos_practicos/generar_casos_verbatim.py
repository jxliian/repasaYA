import subprocess, re

# 1. Extraer textos exactos del PDF oficial
pdf_path = '/home/jxlig0d/Escritorio/QUINTO/FIS/apuntes/Supuestos_Clase_IRPF_DERECHO_FISCAL_2026-27.pdf'
out = subprocess.check_output(['pdftotext', pdf_path, '-'], text=True)
cleaned = re.sub(r'\n\d+\s*\n\s*\x0c', '\n', out)

markers = [
    'PRÁCTICA Nº1',
    'PRÁCTICA Nº2',
    'PRÁCTICA Nº 3',
    'PRÁCTICA Nº4',
    'PRÁCTICA Nº5',
    'PRÁCTICA Nº6',
    'PRÁCTICA Nº7',
    'PRACTICA Nº 8',
    'PRÁCTICA Nº 9',
    'PRÁCTICA Nº 10',
    'PRÁCTICA Nº 11',
    'PRÁCTICA Nº12',
    'PRÁCTICA Nº 13',
    'PRÁCTICA Nº 14',
    'PRÁCTICA Nº 15',
    'PRÁCTICA Nº 16',
    '2.2. Rendimientos de Capital Mobiliario.'
]

enunciados_exactos = {}
for i in range(16):
    m_c = markers[i]
    m_n = markers[i+1]
    raw = cleaned[cleaned.find(m_c) + len(m_c):cleaned.find(m_n)].strip()
    for sec_title in [
        '2. Sujeción, Exención y no sujeción.',
        '2. Rendimientos Trabajo personal.',
        '2. Rendimientos del capital.',
        '2.1. Rendimientos de Capital Inmobiliario e Imputación de Rentas.'
    ]:
        if raw.endswith(sec_title):
            raw = raw[:-len(sec_title)].strip()
    enunciados_exactos[i+1] = raw

def latex_escape_text(text):
    # Reemplazos unicode y latex
    text = text.replace('€', r'\euro{}')
    text = text.replace('%', r'\%')
    text = text.replace('&', r'\&')
    text = text.replace('_', r'\_')
    text = text.replace('#', r'\#')
    text = text.replace('“', "``").replace('”', "''")
    text = text.replace('«', "``").replace('»', "''")
    # Separar párrafos en LaTeX
    paras = text.split('\n\n')
    formatted_paras = []
    for p in paras:
        # Reemplazar saltos de línea simples por espacio
        lines = [l.strip() for l in p.split('\n') if l.strip()]
        formatted_paras.append(' '.join(lines))
    return '\n\n'.join(formatted_paras)

print("Extracción completada. Comprobando P1:")
print(latex_escape_text(enunciados_exactos[1]))
