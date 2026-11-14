"""Apply <CODE>/fixes.json to <CODE>/questions.json in place (the parsers also do this on every run).

Usage: python3 fix.py <cert-id>                 apply and save
       python3 fix.py <cert-id> --check FILE    apply FILE (same format) to a copy, print the
                                                 changed questions, save nothing
"""
import json, os, sys
from certs import cert_dir, apply_fixes, load_questions

cid = sys.argv[1]
qs = load_questions(cid)
if len(sys.argv) > 3 and sys.argv[2] == '--check':
    before = json.dumps(qs)
    old = {(q['exam'], q['n']): json.dumps(q) for q in qs}
    n = apply_fixes(cid, qs, path=sys.argv[3])
    for q in qs:
        if json.dumps(q) != old[(q['exam'], q['n'])]:
            print(f"===== {q['exam']}-{q['n']}")
            print(q['question'])
            for a in q['answers']:
                print(('[x] ' if a['correct'] else '[ ] ') + a['text'])
            print('--- explanation\n' + q['explanation'])
    print(f'{cid}: {n} fixes OK (nothing saved)')
else:
    n = apply_fixes(cid, qs)
    json.dump(qs, open(os.path.join(cert_dir(cid), 'questions.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{cid}: {n} fixes applied')
