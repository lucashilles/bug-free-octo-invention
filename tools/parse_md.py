"""Parse Markdown practice-exam dumps into <CODE>/questions.json.

Usage: python3 parse_md.py <cert-id> <dump.md>...
The exam number is the leading digits of the file name ("03-Practice Test 3 ... .md" -> exam 3).
Expected dump format:

    ## Question N
    **question text**
    - [ ] **A. option**
    - [x] **B. option** *(correct answer)*

    ### Explanation        (optional)
    ...

A one-line stem is stored bolded, as before. A multi-line stem (requirement lists, case studies,
code) keeps its Markdown structure; see stem().

Corrections to the dumps (wrong keys, broken stems or options) go in <CODE>/fixes.json and
are applied on every run.
Dumps carry no domain label, so domains go in domain-map.json. Questions from the given exams
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


LIST_RE = re.compile(r'^\s*(?:[-*●•]|\d+[.)])\s+')


def stem(lines):
    """Question stem as Markdown. A one-line stem is bolded as before; a longer one (requirement
    lists, case studies, code) keeps its structure: each line is its own paragraph, consecutive
    list items stay one list, '●' bullets become '-', and fenced code is kept verbatim."""
    lines = [l.rstrip() for l in lines]
    text = [l for l in lines if l.strip()]
    if len(text) == 1:
        return f'**{clean(text[0])}**'
    out, fence, prev_item = [], False, False
    for l in lines:
        if l.lstrip().startswith('```'):
            if not fence:
                out.append('')
            out.append(l.strip())
            fence = not fence
            prev_item = False
            continue
        if fence:
            out.append(l)
            continue
        if not l.strip():
            continue
        item = bool(LIST_RE.match(l))
        if item:
            l = re.sub(r'^\s*[●•]\s*', '- ', l).strip()
            l = re.sub(r'^\s*[-*]\s+', '- ', l)
        else:
            l = l.strip()
        if not (item and prev_item):
            out.append('')
        out.append(l)
        prev_item = item
    return '\n'.join(out).strip()


def parse_file(path):
    exam = str(int(re.match(r'\d+', os.path.basename(path)).group()))
    src = open(path, encoding='utf-8').read()
    parts = Q_RE.split(src)[1:]
    out = []
    for num, body in zip(parts[::2], parts[1::2]):
        body, _, explanation = body.partition('\n### Explanation\n')
        qlines, answers = [], []
        for line in body.strip().splitlines():
            m = OPT_RE.match(line)
            if m:
                answers.append({'text': clean(m.group(2)), 'correct': m.group(1) == 'x'})
            elif not answers:
                qlines.append(line)
        question = stem(qlines)
        n = int(num)
        if question.strip('*') == '' or len(answers) < 2 or not any(a['correct'] for a in answers):
            raise ValueError(f'{path}: question {n} is malformed')
        out.append({'exam': exam, 'n': n, 'question': question, 'answers': answers,
                    'explanation': explanation.strip(), 'domain': 'Unknown'})
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
    # An explanation already in questions.json for the same question wins over the dump's
    # (it may have been edited); the dump's own `### Explanation` is used otherwise.
    kept = {(x['exam'], x['n'], x['question']): x['explanation'] for x in existing if x['explanation']}
    for qs in parsed.values():
        for q in qs:
            q['explanation'] = kept.get((q['exam'], q['n'], q['question']), q['explanation'])
    merged = [x for x in existing if x['exam'] not in parsed] + [q for qs in parsed.values() for q in qs]
    merged.sort(key=lambda x: (int(x['exam']), x['n']))
    apply_fixes(cid, merged)
    json.dump(merged, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{path}: {len(merged)} questions')


if __name__ == '__main__':
    main()
