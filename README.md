# GCP Certification Study

Study materials and a static study site for Google Cloud certifications, built from mock exams.

| Code | Certification | Questions |
|---|---|---|
| GPCDOE | Professional Cloud DevOps Engineer | 305 from 5 practice exams |
| GPCDE | Professional Cloud Developer | 255 from 5 practice exams |

## The site (`docs/`)

Served by GitHub Pages from `docs/`, or open `docs/index.html` locally. It needs no server or build step. Pick a certification on the landing page or with the switcher in the sidebar. Each certification has:

- **Curriculum**: domains → lessons. Each lesson has a summary, objectives, the material, key takeaways, the practice questions it cites, and a "Mark complete" button.
- **Practice**
  - *Drill mode*: one question at a time with instant feedback, filtered by domain, unseen questions or mistakes.
  - *Mock exam*: 50 questions with a 120-minute timer, scored per domain at the end.
  - *Review mistakes*: every question whose latest answer, in a lesson, drill or mock exam, was wrong.
- **Look Up**: *Quick Reference* (a printable sheet per domain) and *Glossary* (terms with how they're tested and a link to the lesson).
- **Search** in the top bar.

Progress is saved per certification in each visitor's browser (localStorage), so nobody sees anyone else's progress.

## Repository layout

```
GPCDOE/, GPCDE/           one folder per certification
  questions.json          canonical question bank (question, options with correct flags, explanation, domain label)
  domain-map.json         question → domain overrides ("<exam>-<n>": domain) for questions without a usable label
  exam-N.md               readable copy of each practice exam ([x] marks the correct options)
study/<CODE>/             per-domain study guides (*-guide.md) and question banks, plus a README index
content/<cert-id>/        lesson summaries/objectives/takeaways + glossary per domain (domain-N.json)
docs/                     the published site; assets/data-<cert-id>.js is generated
tools/                    the pipeline (needs Python with beautifulsoup4, html2text, markdown)
```

## Pipeline

All scripts are run from `tools/`. Certifications and their domains are defined in `tools/certs.py`.

```bash
# 1. Parse saved Udemy result pages (exam number = file name, e.g. 3.html → exam 3).
#    Merges into <CODE>/questions.json. The test-taker's own answers are never recorded.
python3 parse.py gpcde ../GPCDE/5.html

# 2. Untagged questions need a domain: add "<exam>-<n>": <domain> to <CODE>/domain-map.json.

# 3. Regenerate the readable exams, the question banks and the site data.
python3 export_md.py gpcde
python3 gen.py gpcde
python3 build.py            # all certifications, or: python3 build.py gpcde
```

The study guides (`study/<CODE>/*-guide.md`) and `content/<cert-id>/*.json` are written by hand or with an assistant. `build.py` turns each guide's `## N. Title` sections into lessons. It collects the `### Decision rules` and `### Traps` subsections, `## ⚠️ Questionable answers` and `## Last-minute cheat sheet` into the Quick Reference, and turns `(Exam N · QM)` citations into links to the questions.

To add a certification, add an entry to `CERTS` in `tools/certs.py`, create its folder with the mock exam result pages, and run the pipeline.

Raw `.html` mock exam pages are git-ignored because they contain the answers of whoever took the test. Delete them after parsing.
