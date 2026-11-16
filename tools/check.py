"""Consistency checks for every certification (or the ones named). Run before committing.

Usage: python3 check.py [cert-id ...]
Exits non-zero if any ERROR is found. WARN lines are worth a look but don't fail.

Checks:
  - questions.json: each question has a stem, >= 2 options, >= 1 correct option, an explanation,
    and resolves to a domain (domain-map.json / Udemy label)
  - fixes.json: applies cleanly, and questions.json already contains the result (run fix.py if not)
  - guides: every (Exam N · QM) citation points to a real question; every question is cited
    somewhere; citations outside the guide's own domain are reported as WARN
  - content/<id>/domain-N.json: valid JSON; lesson keys and glossary 'lesson' numbers match
    the guide's "## N. Title" lessons
"""
import copy, json, os, re, sys
from certs import CERTS, cert_dir, study_dir, content_dir, load_questions, domain_resolver, apply_fixes

CITE = re.compile(r'\b(?:Exam\s*|E)(\d+)\s*·\s*Q(\d+)')
errors = 0


def report(level, cid, msg):
    global errors
    errors += level == 'ERROR'
    print(f'{level:5} {cid}: {msg}')


def check(cid):
    cert = CERTS[cid]
    qs = load_questions(cid)
    ids = {f"{q['exam']}-{q['n']}" for q in qs}
    try:
        dom = domain_resolver(cid)
    except Exception as e:
        report('ERROR', cid, e); return
    qdom = {}
    for q in qs:
        k = f"{q['exam']}-{q['n']}"
        if not q['question'].strip():
            report('ERROR', cid, f'{k}: empty stem')
        if len(q['answers']) < 2 or not any(a['correct'] for a in q['answers']):
            report('ERROR', cid, f'{k}: needs >= 2 options and >= 1 correct')
        if not q['explanation'].strip():
            report('WARN', cid, f'{k}: no explanation')
        try:
            qdom[k] = dom(q)
        except ValueError as e:
            report('ERROR', cid, e)

    fixed = copy.deepcopy(qs)
    try:
        n = apply_fixes(cid, fixed)
        if n and fixed != qs:
            changed = [f"{a['exam']}-{a['n']}" for a, b in zip(fixed, qs) if a != b]
            report('ERROR', cid, f'questions.json is missing fixes for {changed[:5]}; run: python3 fix.py {cid}')
    except ValueError as e:
        report('ERROR', cid, e)

    cited = set()
    for n, d in cert['domains'].items():
        guide = os.path.join(study_dir(cid), f"{d['slug']}-guide.md")
        if not os.path.exists(guide):
            report('WARN', cid, f'domain {n}: no guide yet ({os.path.relpath(guide)})'); continue
        text = open(guide, encoding='utf-8').read()
        lessons = {int(m) for m in re.findall(r'^## (\d+)\.\s', text, re.M)}
        if lessons != set(range(1, len(lessons) + 1)):
            report('ERROR', cid, f'domain {n}: lesson numbers {sorted(lessons)} are not 1..N')
        for e, q in CITE.findall(text):
            k = f'{e}-{q}'
            cited.add(k)
            if k not in ids:
                report('ERROR', cid, f'domain {n} guide cites Exam {e} · Q{q}, which does not exist')
            elif qdom.get(k) != n:
                report('WARN', cid, f'domain {n} guide cites Exam {e} · Q{q} from domain {qdom.get(k)}')
        path = os.path.join(content_dir(cid), f'domain-{n}.json')
        if not os.path.exists(path):
            continue
        try:
            extra = json.load(open(path, encoding='utf-8'))
        except ValueError as e:
            report('ERROR', cid, f'{os.path.relpath(path)}: invalid JSON: {e}'); continue
        extra_lessons = {int(k) for k in extra.get('lessons', {})}
        if extra_lessons - lessons:
            report('ERROR', cid, f'{os.path.relpath(path)}: lessons {sorted(extra_lessons - lessons)} not in the guide')
        if lessons - extra_lessons:
            report('WARN', cid, f'{os.path.relpath(path)}: no summary for lessons {sorted(lessons - extra_lessons)}')
        for g in extra.get('glossary', []):
            if g.get('lesson') not in lessons:
                report('ERROR', cid, f"{os.path.relpath(path)}: glossary term {g.get('term')!r} points to lesson {g.get('lesson')}")
    uncited = sorted(ids - cited, key=lambda k: tuple(map(int, k.split('-'))))
    if uncited:
        report('WARN', cid, f'{len(uncited)} questions not cited by any guide: {uncited[:10]}')
    print(f'ok    {cid}: {len(qs)} questions checked')


if __name__ == '__main__':
    for cid in sys.argv[1:] or CERTS:
        check(cid)
    sys.exit(1 if errors else 0)
