"""Parse Udemy practice-exam result pages (saved HTML) into <CODE>/questions.json.

Usage: python3 parse.py <cert-id> <exam.html>...
The exam number comes from the file name (3.html -> exam 3). Questions from those exams
replace any already in questions.json; other exams are kept. The test-taker's own
selections and scores are deliberately not recorded.
"""
import json, os, sys
import html2text
from bs4 import BeautifulSoup
from certs import cert_dir


def h2md(el):
    h = html2text.HTML2Text(); h.body_width = 0; h.ignore_images = True
    return h.handle(str(el)).strip()


def parse_file(path):
    exam = os.path.basename(path).split('.')[0]
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    out = []
    for i, pane in enumerate(soup.select('div[class*="question-result-pane--sIcOh"]'), 1):
        q = pane.select_one('#question-prompt')
        answers = []
        for a in pane.select('div[class*="answer-result-pane--Niazi"]'):
            ad = a.select_one('[data-purpose="answer"]')
            txt = a.select_one('#answer-text')
            if not txt: continue
            cls = ' '.join(ad.get('class', []))
            label = ad.select_one('[data-purpose="answer-result-header-user-label"]')
            correct = 'answer-correct' in cls or (label and 'Correct answer' in label.text)
            answers.append({'text': h2md(txt), 'correct': bool(correct)})
        ov = pane.select_one('#overall-explanation')
        dom = pane.select_one('[data-purpose="domain-pane"] .ud-text-md')
        out.append({'exam': exam, 'n': i,
                    'question': h2md(q) if q else '', 'answers': answers,
                    'explanation': h2md(ov) if ov else '',
                    'domain': dom.text.strip() if dom else 'Unknown'})
    return exam, out


def main():
    cid, files = sys.argv[1], sys.argv[2:]
    path = os.path.join(cert_dir(cid), 'questions.json')
    existing = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else []
    parsed = {}
    for f in files:
        exam, qs = parse_file(f)
        if not qs:
            print(f'warning: no questions found in {f}; skipped')
            continue
        parsed[exam] = qs
        print(f'{f}: exam {exam}, {len(qs)} questions')
    merged = [x for x in existing if x['exam'] not in parsed] + [q for qs in parsed.values() for q in qs]
    merged.sort(key=lambda x: (int(x['exam']), x['n']))
    json.dump(merged, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{path}: {len(merged)} questions')


if __name__ == '__main__':
    main()
