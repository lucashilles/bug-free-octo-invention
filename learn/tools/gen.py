import json, re, sys, os
d = json.load(open(sys.argv[1])); outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)
from domains import DOMAINS, dom

def section(text, name):
    m = re.search(r'\*\*' + re.escape(name) + r'\*\*\s*\n+(.*?)(?=\n\s*\*\*[A-Z][^*\n]{2,40}\*\*\s*\n|\Z)', text, re.S)
    return m.group(1).strip() if m else None

def demote(md):  # keep embedded headings below question level
    return re.sub(r'^(#+)', lambda m: '#' * min(len(m.group(1)) + 3, 6), md, flags=re.M)

by = {k: [] for k in DOMAINS}
for x in d: by[dom(x)].append(x)

index = ['# GCP Professional Cloud DevOps Engineer — Study Materials', '',
         f'Generated from {len(d)} practice-exam questions across 5 exams, grouped by exam domain.', '',
         'Start with each domain\'s **study guide** (condensed concepts, decision rules, traps), then drill the **question bank** (answers collapsed for self-testing).', '',
         '| Domain | Study guide | Questions | You missed |', '|---|---|---|---|']
missed_all = []
for k, (slug, title) in DOMAINS.items():
    qs = by[k]
    missed = [x for x in qs if x['status'] == 'Incorrect']
    missed_all += [(k, x) for x in missed]
    index.append(f'| {title} | [guide]({slug}-guide.md) | [{len(qs)} questions]({slug}.md) | {len(missed)} |')
    L = [f'# {title}', '', f'{len(qs)} questions. Answers are collapsed — try each question before expanding it.', '']
    hooks = [(x, section(x['explanation'], 'Memory Hook')) for x in qs]
    hooks = [(x, h) for x, h in hooks if h]
    if hooks:
        L += ['## Quick-review: memory hooks', '']
        for x, h in hooks:
            h = re.sub(r'\s*\*\*30-Second.*', '', re.sub(chr(10)+'+', ' ', h), flags=re.S).strip()
            L.append(f"- {h} *(Q{x['exam']}.{x['n']})*")
        L.append('')
    L += ['## Questions', '']
    for x in sorted(qs, key=lambda x: (int(x['exam']), x['n'])):
        tag = ' ❌ *you missed this*' if x['status'] == 'Incorrect' else ''
        L += [f"### Exam {x['exam']} · Q{x['n']}{tag}", '', x['question'], '']
        for a in x['answers']:
            L.append('- ' + a['text'].replace('\n\n', '\n  ').replace('\n', '\n  '))
        correct = [a['text'].split('\n')[0] for a in x['answers'] if a['correct']]
        L += ['', '<details><summary>Answer &amp; explanation</summary>', '',
              '**Correct:** ' + ' **|** '.join(correct), '', demote(x['explanation']), '', '</details>', '', '---', '']
    open(f'{outdir}/{slug}.md', 'w').write(re.sub(r'\n[ \t]*(\n[ \t]*){2,}', '\n\n', '\n'.join(L)))

index += ['', '- [Questions you got wrong](00-missed-questions.md)', '']
open(f'{outdir}/README.md', 'w').write('\n'.join(index))
M = ['# Questions You Missed', '', 'Your incorrect answers across all exams, grouped by domain.', '']
for k, x in missed_all:
    yours = [a['text'].split('\n')[0] for a in x['answers'] if a['chosen']]
    correct = [a['text'].split('\n')[0] for a in x['answers'] if a['correct']]
    M += [f"## [{DOMAINS[k][1].split(' — ')[0]}] Exam {x['exam']} · Q{x['n']}", '', x['question'], '',
          '- **Your answer:** ' + ' | '.join(yours), '- **Correct:** ' + ' | '.join(correct), '',
          f"See full explanation in [{DOMAINS[k][0]}.md]({DOMAINS[k][0]}.md).", '', '---', '']
open(f'{outdir}/00-missed-questions.md', 'w').write('\n'.join(M))
