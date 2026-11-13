"""Write one readable Markdown file per practice exam: <CODE>/exam-N.md.

Usage: python3 export_md.py <cert-id>
"""
import os, re, sys
from collections import defaultdict
from certs import CERTS, cert_dir, load_questions, domain_resolver


def main():
    cid = sys.argv[1]
    cert = CERTS[cid]
    try:
        dom = domain_resolver(cid)
    except Exception:
        dom = None
    exams = defaultdict(list)
    for x in load_questions(cid):
        exams[x['exam']].append(x)
    for exam, qs in sorted(exams.items(), key=lambda kv: int(kv[0])):
        L = [f"# {cert['name']} — Practice Exam {exam}", '', f'{len(qs)} questions.', '']
        for x in qs:
            L += [f"## Question {x['n']}", '']
            if dom:
                try:
                    n = dom(x)
                    L += [f"*Domain {n}: {cert['domains'][n]['title']}*", '']
                except ValueError:
                    pass
            L += [x['question'], '']
            for a in x['answers']:
                mark = '[x]' if a['correct'] else '[ ]'
                L.append(f'- {mark} ' + a['text'].replace('\n\n', '\n  ').replace('\n', '\n  '))
            L += ['', '### Explanation', '', re.sub(r'^(#+)', r'###\1', x['explanation'], flags=re.M), '', '---', '']
        path = os.path.join(cert_dir(cid), f'exam-{exam}.md')
        open(path, 'w', encoding='utf-8').write(re.sub(r'\n[ \t]*(\n[ \t]*){2,}', '\n\n', '\n'.join(L)))
        print(f'{path}: {len(qs)} questions')


if __name__ == '__main__':
    main()
