import sys, json, html2text
from bs4 import BeautifulSoup

def h2md(el):
    h = html2text.HTML2Text(); h.body_width = 0; h.ignore_images = True
    return h.handle(str(el)).strip()

out = []
for f in sys.argv[2:]:
    soup = BeautifulSoup(open(f, encoding='utf-8').read(), 'html.parser')
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
        out.append({'exam': f.split('/')[-1].split('.')[0], 'n': i,
                    'question': h2md(q) if q else '', 'answers': answers,
                    'explanation': h2md(ov) if ov else '',
                    'domain': dom.text.strip() if dom else 'Unknown'})
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
