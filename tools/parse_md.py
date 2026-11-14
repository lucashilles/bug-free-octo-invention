"""Parse Markdown practice-exam dumps into <CODE>/questions.json.

Usage: python3 parse_md.py <cert-id> <dump.md>...
The exam number is the leading digits of the file name ("03-Practice Test 3 ... .md" -> exam 3).
Expected dump format:

    ## Question N
    **question text**
    - [ ] **A. option**
    - [x] **B. option** *(correct answer)*

Corrections to the dumps (wrong keys, broken stems or options) go in <CODE>/fixes.json and
are applied on every run.
Dumps carry no explanation or domain label, so domains go in domain-map.json and
explanations are written into questions.json afterwards. Questions from the given exams
replace any already in questions.json (keeping an existing explanation when the question
text is unchanged); other exams are kept.
"""
import json, os, re, sys
from certs import cert_dir, apply_fixes

Q_RE = re.compile(r'^## Question (\d+)\s*$', re.M)
OPT_RE = re.compile(r'^- \[( |x)\] (.*)$')


def clean(text):
    text = re.sub(r'\s*\*\(correct answer\)\*\s*$', '', text.strip())
    m = re.fullmatch(r'\*\*(.*)\*\*', text, re.S)
    text = m.group(1) if m else text
    return text.lstrip('-*').strip()


def parse_file(path):
    exam = str(int(re.match(r'\d+', os.path.basename(path)).group()))
    src = open(path, encoding='utf-8').read()
    parts = Q_RE.split(src)[1:]
    out = []
    for num, body in zip(parts[::2], parts[1::2]):
        qlines, answers = [], []
        for line in body.strip().splitlines():
            m = OPT_RE.match(line)
            if m:
                answers.append({'text': clean(m.group(2)), 'correct': m.group(1) == 'x'})
            elif line.strip() and not answers:
                qlines.append(line.strip())
        question = clean(' '.join(qlines))
        n = int(num)
        if not question or len(answers) < 2 or not any(a['correct'] for a in answers):
            raise ValueError(f'{path}: question {n} is malformed')
        out.append({'exam': exam, 'n': n, 'question': f'**{question}**', 'answers': answers,
                    'explanation': '', 'domain': 'Unknown'})
    return exam, out


def main():
    cid, files = sys.argv[1], sys.argv[2:]
    path = os.path.join(cert_dir(cid), 'questions.json')
    existing = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else []
    parsed = {}
    for f in files:
        exam, qs = parse_file(f)
        parsed[exam] = qs
        print(f'{f}: exam {exam}, {len(qs)} questions')
    for qs in parsed.values():
        apply_fixes(cid, qs, strict=False)  # before matching explanations, which are keyed on the fixed stem
    # Dumps have no explanations; keep ones already written for the same question.
    kept = {(x['exam'], x['n'], x['question']): x['explanation'] for x in existing if x['explanation']}
    for qs in parsed.values():
        for q in qs:
            q['explanation'] = kept.get((q['exam'], q['n'], q['question']), '')
    merged = [x for x in existing if x['exam'] not in parsed] + [q for qs in parsed.values() for q in qs]
    merged.sort(key=lambda x: (int(x['exam']), x['n']))
    apply_fixes(cid, merged)
    json.dump(merged, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{path}: {len(merged)} questions')


if __name__ == '__main__':
    main()
