import json
import re
import string

def normalize_text(text):
    text = text.replace('\n', ' ').strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def normalize_for_compare(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation + '¿?¡!'))
    return re.sub(r'\s+', '', text)

def parse_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('\x0c', '')
    questions = []

    # Block 1: Pregunta \d+: ...
    parts = re.split(r'Pregunta \d+:', content)
    for part in parts[1:]:
        if 'Respuesta Correcta:' in part:
            body, ans_block = part.split('Respuesta Correcta:', 1)
            
            # Find a) b) c) d) using regex
            # It could be 'a)', 'b)', etc.
            match = re.search(r'(.*?)(?:a\)|A\))(.*?)(?:b\)|B\))(.*?)(?:c\)|C\))(.*?)(?:d\)|D\))(.*)', body, re.DOTALL)
            if match:
                q_text = normalize_text(match.group(1))
                opt_a = normalize_text(match.group(2))
                opt_b = normalize_text(match.group(3))
                opt_c = normalize_text(match.group(4))
                opt_d = normalize_text(match.group(5))
                
                opts = [opt_a, opt_b, opt_c, opt_d]
                
                ans_char = normalize_text(ans_block).strip().lower()[0]
                if ans_char == 'a': correct = 0
                elif ans_char == 'b': correct = 1
                elif ans_char == 'c': correct = 2
                elif ans_char == 'd': correct = 3
                else: continue
                
                tema = "T1/T4/T5: Preguntas Extraídas (PDF)"
                questions.append({
                    "tema": tema,
                    "q": q_text,
                    "opts": opts,
                    "correct": correct
                })
                
    # Block 2: TIPO TEST TEMA 4
    if 'TIPO TEST TEMA 4' in content:
        tt_block = content.split('TIPO TEST TEMA 4')[1]
        if 'RESPUESTAS' in tt_block:
            q_part, a_part = tt_block.split('RESPUESTAS')
            
            responses = {}
            for line in a_part.split('\n'):
                line = line.strip()
                if re.match(r'\d+\.\s+[A-D]', line):
                    num, ans = line.split('.')
                    ans = ans.strip().lower()
                    if ans == 'a': idx = 0
                    elif ans == 'b': idx = 1
                    elif ans == 'c': idx = 2
                    elif ans == 'd': idx = 3
                    else: idx = 0
                    responses[num.strip()] = idx
            
            q_matches = re.finditer(r'(\d+)\.\s+(.*?)\nA\)\s+(.*?)\nB\)\s+(.*?)\nC\)\s+(.*?)\nD\)\s+(.*?)(?=\n\d+\.|\Z)', q_part, re.DOTALL)
            for m in q_matches:
                num = m.group(1).strip()
                q_text = normalize_text(m.group(2))
                opts = [
                    normalize_text(m.group(3)),
                    normalize_text(m.group(4)),
                    normalize_text(m.group(5)),
                    normalize_text(m.group(6))
                ]
                if num in responses:
                    questions.append({
                        "tema": "T4: Gestión de la Información (Tipo Test PDF)",
                        "q": q_text,
                        "opts": opts,
                        "correct": responses[num]
                    })

    return questions

def merge():
    new_qs = parse_txt('/home/jxlig0d/Escritorio/EE/repasaya/repasaYA/tipo-test/SIBW/merged.txt')
    
    json_path = '/home/jxlig0d/Escritorio/EE/repasaya/repasaYA/src/data/sibw.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        existing_qs = json.load(f)
        
    existing_normalized = set()
    for q in existing_qs:
        existing_normalized.add(normalize_for_compare(q['q']))
        
    added = 0
    for nq in new_qs:
        norm = normalize_for_compare(nq['q'])
        if norm not in existing_normalized:
            existing_qs.append(nq)
            existing_normalized.add(norm)
            added += 1
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(existing_qs, f, ensure_ascii=False, indent=2)
        
    print(f"Total new questions parsed: {len(new_qs)}")
    print(f"Added {added} non-duplicate questions.")
    print(f"New total: {len(existing_qs)} questions.")

if __name__ == '__main__':
    merge()
