"""Build the study site's data bundles: docs/assets/certs.js + docs/assets/data-<cert>.js.

Sources per certification (see certs.py):
  study/<CODE>/NN-*-guide.md    -> lessons (one per "## N. Title" section), quick-reference sheets
  content/<cert>/domain-N.json  -> lesson summaries/objectives/takeaways + glossary (optional)
  <CODE>/questions.json         -> question bank (output of parse.py)

Usage: python3 build.py [cert-id ...]   (default: all certifications)
"""
import json, os, re, sys
import markdown
from certs import CERTS, REPO, study_dir, content_dir, load_questions, domain_resolver

ASSETS = os.path.join(REPO, 'docs', 'assets')
CID = None  # certification currently being built; used for citation links

CITE = re.compile(r'\b(?:Exam\s*|E)(\d)\s*·\s*Q(\d+)')


def md(text):
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists'])


LIST_ITEM = re.compile(r'\s*(?:[-*+]|\d+\.)\s')


def ensure_list_breaks(text):
    # Python-Markdown needs a blank line before a list that follows a paragraph or table.
    out = []
    for line in text.split('\n'):
        if LIST_ITEM.match(line) and out and out[-1].strip() and not LIST_ITEM.match(out[-1]) \
                and not out[-1].startswith((' ', '\t')):
            out.append('')
        out.append(line)
    return '\n'.join(out)


def bold_headings(text):
    # Guides sometimes use a lone "**Decision rules**" line as a sub-heading.
    return re.sub(r'^\*\*([^*\n]+?):?\*\*\s*$', r'### \1', text, flags=re.M)


def link_cites(html):
    html = re.sub(r'\((\s*(?:(?:Exam\s*|E)\d\s*·\s*Q\d+[,;\s]*)+)\)', r'\1', html)
    return CITE.sub(lambda m: f'<a class="cite" href="#/{CID}/q/e{m.group(1)}q{m.group(2)}">Exam {m.group(1)} · Q{m.group(2)}</a>', html)


def render(text):
    return link_cites(md(ensure_list_breaks(text)))


def subsections(body, pred):
    """Return [(heading, markdown)] for ### subsections whose heading matches pred."""
    parts = re.split(r'^### (.+)$', body, flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2) if pred(parts[i])]


def build_domain(n, meta_d):
    guide = os.path.join(study_dir(CID), f"{meta_d['slug']}-guide.md")
    text = open(guide, encoding='utf-8').read() if os.path.exists(guide) else ''
    if not text:
        print(f'warning: {guide} missing; domain {n} has no lessons yet')
    extra_path = os.path.join(content_dir(CID), f'domain-{n}.json')
    extra = json.load(open(extra_path, encoding='utf-8')) if os.path.exists(extra_path) else {}
    sections = re.split(r'^## (.+)$', text, flags=re.M)
    lessons, cheat, questionable = [], '', ''
    rules, traps = [], []
    for i in range(1, len(sections), 2):
        head, body = sections[i].strip(), bold_headings(sections[i + 1].strip().rstrip('-').strip())
        m = re.match(r'(\d+)\.\s+(.*)', head)
        if m:
            num, ltitle = m.group(1), m.group(2)
            meta = extra.get('lessons', {}).get(num, {})
            cites = sorted({f'e{a}q{b}' for a, b in CITE.findall(body)},
                           key=lambda q: tuple(map(int, re.findall(r'\d+', q))))
            lid = f'd{n}l{num}'
            lessons.append({'id': lid, 'num': int(num), 'title': ltitle, 'html': render(body),
                            'summary': meta.get('summary', ''), 'objectives': meta.get('objectives', []),
                            'takeaways': meta.get('takeaways', []), 'questions': cites})
            for h, b in subsections(body, lambda h: 'decision' in h.lower() or 'rule' in h.lower()):
                rules.append({'lesson': lid, 'title': ltitle, 'html': render(b)})
            for h, b in subsections(body, lambda h: 'trap' in h.lower()):
                traps.append({'lesson': lid, 'title': ltitle, 'html': render(b)})
        elif 'cheat sheet' in head.lower():
            cheat = render(body)
        elif 'questionable' in head.lower():
            questionable = render(body)
    glossary = [dict(g, domain=n, lesson=f"d{n}l{g['lesson']}") for g in extra.get('glossary', [])]
    return {'n': n, 'title': meta_d['title'], 'short': meta_d['short'], 'weight': meta_d['weight'], 'desc': meta_d['desc'],
            'lessons': lessons,
            'ref': {'cheat': cheat, 'rules': rules, 'traps': traps, 'questionable': questionable},
            'glossary': glossary}


def build_questions():
    dom = domain_resolver(CID)
    out = {}
    for x in load_questions(CID):
        qid = f"e{x['exam']}q{x['n']}"
        out[qid] = {'id': qid, 'exam': int(x['exam']), 'n': x['n'], 'domain': dom(x),
                    'html': md(x['question']),
                    'options': [{'html': md(a['text']), 'correct': a['correct']} for a in x['answers']],
                    'explanation': md(x['explanation'])}
    return out


def write_js(name, var, data):
    with open(os.path.join(ASSETS, name), 'w', encoding='utf-8') as f:
        f.write(f'{var} = ')
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        f.write(';\n')


def build_cert(cid):
    global CID
    CID = cid
    cert = CERTS[cid]
    domains = [build_domain(n, d) for n, d in cert['domains'].items()]
    questions = build_questions()
    # Attach each question to the lessons that cite it (for "related lesson" links on questions).
    for d in domains:
        for l in d['lessons']:
            l['questions'] = [q for q in l['questions'] if q in questions]
            for q in l['questions']:
                questions[q].setdefault('lessons', []).append(l['id'])
    write_js(f'data-{cid}.js', f'window.CERT_DATA = window.CERT_DATA || {{}}; window.CERT_DATA[{json.dumps(cid)}]',
             {'domains': domains, 'questions': questions})
    n_lessons = sum(len(d['lessons']) for d in domains)
    n_terms = sum(len(d['glossary']) for d in domains)
    print(f'{cid}: {len(domains)} domains, {n_lessons} lessons, {len(questions)} questions, {n_terms} glossary terms')
    return {'id': cid, 'code': cert['code'], 'name': cert['name'], 'questions': len(questions),
            'lessons': n_lessons, 'exams': len({q['exam'] for q in questions.values()}),
            'domains': [{'n': d['n'], 'short': d['short'], 'weight': d['weight']} for d in domains]}


def main():
    os.makedirs(ASSETS, exist_ok=True)
    manifest_path = os.path.join(ASSETS, 'certs.js')
    wanted = sys.argv[1:] or list(CERTS)
    summaries = {}
    for cid in CERTS:
        if cid in wanted:
            summaries[cid] = build_cert(cid)
    # Keep summaries of certifications not rebuilt this run.
    if os.path.exists(manifest_path):
        old = json.loads(open(manifest_path, encoding='utf-8').read().split('=', 1)[1].rstrip().rstrip(';'))
        for c in old:
            summaries.setdefault(c['id'], c)
    write_js('certs.js', 'window.CERTS', [summaries[c] for c in CERTS if c in summaries])


if __name__ == '__main__':
    main()
