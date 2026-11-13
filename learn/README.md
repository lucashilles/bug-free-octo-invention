# GCP DevOps Study (learn site)

A static study site for the Google Cloud Professional Cloud DevOps Engineer exam, built from `../study/`.

**Open it:** double-click `index.html` (or `xdg-open index.html`). No server or internet connection needed. Progress, drill history and mock-exam scores are saved in your browser's localStorage.

## Sections

- **Curriculum**: 5 domains → 54 lessons. Each lesson has a summary, objectives, the material, key takeaways, the practice questions it cites, and a "Mark complete" button that updates the progress bar.
- **Practice**
  - *Drill mode*: one question at a time with instant feedback. Filter by domain, unseen questions or your mistakes.
  - *Mock exam*: 50 questions weighted by domain with a 120-minute timer. You can flag questions and jump around, and get a per-domain score at the end.
  - *Review mistakes*: questions you missed in the original exams or in drills here.
- **Look Up**
  - *Quick Reference*: a printable sheet per domain with the cheat sheet, decision rules, exam traps, questionable answers and key terms.
  - *Glossary*: 212 terms with definitions, how each is tested on the exam, and a link to the lesson. Filter by domain or text.
- **Search** (top bar) covers lessons, glossary terms and questions.

## Rebuilding

```
content/domain-N.json    lesson summaries/objectives/takeaways + glossary (hand-editable)
../study/*-guide.md      lesson bodies, decision rules, traps, cheat sheets
tools/questions.json     parsed question bank
```

After editing any of these, run `python3 tools/build.py` to regenerate `assets/data.js`. It needs the `markdown` package.

To add new exam dumps: `python3 tools/parse.py tools/questions.json <html files…>` parses them. Then `python3 tools/gen.py tools/questions.json ../study` regenerates the question-bank markdown. Then rebuild. Questions without a domain tag must be mapped in `tools/domains.py`.
