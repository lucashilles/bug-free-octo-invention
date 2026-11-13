"""Build the static study site's data bundle (learn/assets/data.js).

Sources:
  ../../study/NN-*-guide.md   -> lessons (one per "## N. Title" section), quick-reference sheets
  ../content/domain-N.json    -> lesson summaries/objectives/takeaways + glossary (optional)
  questions.json              -> question bank (output of parse.py)

Usage: python3 build.py
"""
import json, os, re
import markdown
from domains import DOMAINS, dom

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STUDY = os.path.join(os.path.dirname(ROOT), 'study')

META = {
    1: ('Organization & IaC', '~17%', 'Resource hierarchy, org policies, IAM and service accounts, Terraform and Kubernetes-native config management, environments.'),
    2: ('CI/CD Pipelines', '~23%', 'Cloud Build, Cloud Deploy, Artifact Registry, deployment strategies, secrets and software supply-chain security.'),
    3: ('SRE Practices', '~18%', 'SLIs, SLOs and error budgets, incident management, blameless postmortems, toil and capacity planning.'),
    4: ('Observability & Troubleshooting', '~23%', 'Cloud Logging and Monitoring, log-based metrics, alerting, Trace/Profiler/Error Reporting and troubleshooting.'),
    5: ('Performance & Cost', '~19%', 'Compute pricing models, network tiers, billing export and labels, rightsizing and logging cost control.'),
}

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
    return CITE.sub(lambda m: f'<a class="cite" href="#/q/e{m.group(1)}q{m.group(2)}">Exam {m.group(1)} · Q{m.group(2)}</a>', html)


def render(text):
    return link_cites(md(ensure_list_breaks(text)))


def subsections(body, pred):
    """Return [(heading, markdown)] for ### subsections whose heading matches pred."""
    parts = re.split(r'^### (.+)$', body, flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2) if pred(parts[i])]


def build_domain(n, slug, title):
    text = open(os.path.join(STUDY, f'{slug}-guide.md'), encoding='utf-8').read()
    extra_path = os.path.join(ROOT, 'content', f'domain-{n}.json')
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
    short, weight, desc = META[n]
    return {'n': n, 'title': title.split(' — ')[1], 'short': short, 'weight': weight, 'desc': desc,
            'lessons': lessons,
            'ref': {'cheat': cheat, 'rules': rules, 'traps': traps, 'questionable': questionable},
            'glossary': glossary}


def build_questions():
    qs = json.load(open(os.path.join(HERE, 'questions.json'), encoding='utf-8'))
    out = {}
    for x in qs:
        qid = f"e{x['exam']}q{x['n']}"
        out[qid] = {'id': qid, 'exam': int(x['exam']), 'n': x['n'], 'domain': dom(x),
                    'missed': x['status'] == 'Incorrect',
                    'html': md(x['question']),
                    'options': [{'html': md(a['text']), 'correct': a['correct']} for a in x['answers']],
                    'explanation': md(x['explanation'])}
    return out


def main():
    domains = [build_domain(n, slug, title) for n, (slug, title) in DOMAINS.items()]
    questions = build_questions()
    # Attach each question to the lessons that cite it (for "related lesson" links on questions).
    for d in domains:
        for l in d['lessons']:
            l['questions'] = [q for q in l['questions'] if q in questions]
            for q in l['questions']:
                questions[q].setdefault('lessons', []).append(l['id'])
    data = {'domains': domains, 'questions': questions}
    os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
    with open(os.path.join(ROOT, 'assets', 'data.js'), 'w', encoding='utf-8') as f:
        f.write('window.APP_DATA = ')
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        f.write(';\n')
    n_lessons = sum(len(d['lessons']) for d in domains)
    n_terms = sum(len(d['glossary']) for d in domains)
    print(f'{len(domains)} domains, {n_lessons} lessons, {len(questions)} questions, {n_terms} glossary terms')


if __name__ == '__main__':
    main()
