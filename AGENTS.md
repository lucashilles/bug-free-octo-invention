# AGENTS.md

Guidance for anyone, human or coding agent, working on this repository. Read [README.md](README.md) first for what the project is and how the site works.

## What this repo is

A static study site for Google Cloud certifications, served by GitHub Pages from `docs/`. Each certification is built from practice-exam question banks. The curriculum (guides, lessons, glossary) is written from those questions and from Google Cloud documentation.

| Code | Cert id | Certification |
|---|---|---|
| GPCDOE | `gpcdoe` | Professional Cloud DevOps Engineer |
| GPCDE | `gpcde` | Professional Cloud Developer |
| GCDL | `gcdl` | Cloud Digital Leader |
| GPCA | `gpca` | Professional Cloud Architect |

Certifications and their domains are defined in `tools/certs.py`. The code (`GPCDE`) names the folders. The id (`gpcde`) is used by the tools and in site URLs (`#/gpcde/...`).

## Where things live, and who writes them

| Path | What | Edited by |
|---|---|---|
| `<CODE>/questions.json` | The question bank, and the source of truth. The raw sources are deleted after parsing. | Parsers, `fix.py` |
| `<CODE>/fixes.json` | Corrections to the bank: keys, stems, options, explanations, ⚠️ notes | **Hand** |
| `<CODE>/domain-map.json` | `"<exam>-<n>": domain` for questions without a usable domain label | **Hand** |
| `<CODE>/duplicates.json` | Groups of question ids that are the same question reused across practice exams, e.g. `[["2-12", "2-34"]]` | **Hand** |
| `<CODE>/exam-N.md` | Readable copy of each practice exam | `export_md.py` (generated) |
| `study/<CODE>/NN-*-guide.md` | Study guides: one per domain, with lessons, rules, traps and cheat sheet | **Hand** |
| `study/<CODE>/NN-*.md`, `study/<CODE>/README.md` | Per-domain question banks and index | `gen.py` (generated) |
| `content/<id>/domain-N.json` | Lesson summaries, objectives and takeaways, plus the glossary | **Hand** |
| `docs/assets/certs.js`, `docs/assets/data-<id>.js` | Site data | `build.py` (generated) |
| `docs/index.html`, `docs/assets/app.js`, `docs/assets/styles.css` | The site itself, plain HTML/CSS/JS with no build step | **Hand** |
| `docs/assets/img/<id>/` | Images used by questions, referenced from `fixes.json` as `assets/img/<id>/<file>` (relative to `docs/`). Don't hotlink images from the source site; download them here. If an image is only a screenshot of a table, write it as a Markdown table instead. | **Hand** |
| `tools/` | The Python pipeline | **Hand** |

**Never hand-edit generated files.** Change the source, then regenerate.

**Don't hand-edit `questions.json` either.** Put corrections in `fixes.json` and run `fix.py`, so they survive a re-parse and record why they were made.

## Setup

Python 3 with `beautifulsoup4`, `html2text` and `markdown`:

```bash
pip install beautifulsoup4 html2text markdown
```

Run every tool from `tools/`.

## Workflow

After any change to a question bank, fixes, guides or content:

```bash
cd tools
python3 fix.py <id>          # only if fixes.json changed
python3 export_md.py <id>    # only if questions changed
python3 gen.py <id>          # only if questions or domain-map changed
python3 build.py             # always: regenerates the site data
python3 check.py             # must report no ERROR lines
```

Commit the generated files together with the change that produced them. Open `docs/index.html` in a browser to check the result; it works from `file://` with no server.

## Conventions

### Citations
- Cite questions as `(Exam N · QM)`, for example `(Exam 4 · Q26)`. Use exactly that form, with a middle dot `·` (U+00B7). `build.py` turns citations into links, and `check.py` verifies them.
- Cite the questions that actually teach the point. Every question should be cited by at least one guide; `check.py` warns about uncited ones.

### Study guides (`study/<CODE>/NN-*-guide.md`)
- Lessons are `## N. Title`, numbered 1..N with no gaps. Each becomes a lesson on the site.
- Inside a lesson, use `### Key facts`, optional tables, `### Decision rules` and `### Traps`. The build collects the Decision rules and Traps subsections into the Quick Reference, so keep those names.
- Two special sections end the guide: `## ⚠️ Questionable answers` (doubtful keys or wording that a fix couldn't resolve) and `## Last-minute cheat sheet`.
- If you add, remove or renumber a lesson, update `content/<id>/domain-N.json` to match: its `lessons` keys and each glossary term's `lesson`.
- Write for the exam: the depth a candidate needs, in plain English and short sentences.

### Lesson content (`content/<id>/domain-N.json`)
- `lessons`: `{ "<N>": { "summary", "objectives": [], "takeaways": [] } }`
- `glossary`: `[{ "term", "definition", "exam_context", "lesson": N }]`, sorted alphabetically.
- Keep 2-space indentation and valid JSON.

### Corrections (`<CODE>/fixes.json`)
Keys are `"<exam>-<n>"`. Every field is optional except `why`:

```json
"4-13": {
  "question":    [["old text", "new text"]],
  "answers":     {"II": "II. Full new option text"},
  "correct":     "II",
  "explanation": [["old text", "new text"]],
  "note":        "Appended to the explanation as **⚠️ Note:**",
  "why":         "Why the fix was made"
}
```

- `correct` takes a label or a list of labels for multi-answer questions. Labels are the option prefixes (`A`, `IV`, ...); option order in the bank is shuffled, so always use labels, never positions.
- `explanation` can also be a single string that replaces the whole explanation.
- Fixes must be idempotent. `fix.py` and the parsers re-apply all of them on every run.
- Preview a set of fixes without saving: `python3 fix.py <id> --check my-fixes.json`.

### Duplicates (`<CODE>/duplicates.json`)
- The practice exams reuse questions, often reworded. List each set of copies as one group. A lesson shows only one copy per group: the first id in the group, or the earliest-listed one the lesson cites. Each copy links to the others ("Also asked as"). Drills and mock exams keep every copy.
- Group questions only when they have the same scenario, requirement and correct answer, so that answering one gives away the other. Questions that test the same concept with different numbers, cues or answers are not duplicates.
- Put the clearest copy first. When you add an exam, check its questions against the bank.

### When a key is wrong
- Change a key only when you can say concretely why another option is right. Back it with current Google Cloud documentation, or the same scenario keyed differently elsewhere in the bank.
- When the evidence isn't that strong, keep the key and add a `note`, and list the question under the guide's `## ⚠️ Questionable answers`.
- When you change a key, also fix the explanation, and update any guide or lesson text that taught the old answer. Search for the citation.

### Product names
Google renames products often. Prefer current names, and mention the old one where a question or a candidate might still use it, for example "Data Studio (called Looker Studio from 2022 to 2026)". Check recent renames against Google's docs before changing names in bulk. Some recent ones:

| Old | Current |
|---|---|
| Looker Studio | Data Studio (renamed back in April 2026) |
| Dataplex Universal Catalog | Knowledge Catalog (April 2026) |
| Stackdriver | Cloud Logging / Cloud Monitoring |
| Container Registry | Artifact Registry |
| Anthos Config Management | Config Sync + Policy Controller |
| Traffic Director, Anthos Service Mesh | Cloud Service Mesh |
| Cloud Functions | Cloud Run functions |
| Google Agentspace | Gemini Enterprise |

### Site (`docs/`)
- Plain JS (`app.js`) with hash routes: `#/` lists the certifications, `#/<id>/...` opens one.
- Progress is stored per browser in `localStorage`, under `gcp-study-v2`, `gcp-study-last` and `gcp-study-theme`. Don't rename these keys without migrating the stored data, as `app.js` already does for the legacy key.
- Theme colors are CSS custom properties on `:root`. Dark values are defined twice: under `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])` and under `:root[data-theme="dark"]`. Change both.
- Color components through variables, never inline styles. Badges take their color from `--c` (`style="--c:..."`), and dark mode turns that into tinted text on a translucent background. An inline `background:` breaks this.
- Check both themes, and phone width. Headless Chrome screenshots work: `google-chrome --headless=new --blink-settings=preferredColorScheme=0 --screenshot=out.png "file://$PWD/docs/index.html#/gcdl/"` (`0` = dark, `1` = light).

## Adding questions or a certification

1. For a new certification, add an entry to `CERTS` in `tools/certs.py`: code, name, domains with slug, title, short name, weight and description, and `prefix_rules` for Udemy domain labels.
2. Parse the raw sources into the bank:
   - Udemy result pages: `python3 parse.py <id> ../<CODE>/N.html`.
   - Markdown dumps: `python3 parse_md.py <id> <files>`.
3. Map untagged questions in `<CODE>/domain-map.json`, and list repeated questions in `<CODE>/duplicates.json`.
4. Write the guides and `content/<id>/domain-N.json`, then run the workflow above.
5. **Delete the raw sources** (`.html` pages, `.md` dumps, `.zip` archives). Udemy pages contain the test-taker's own answers. `.gitignore` covers `*/*.html` and `*.zip`, but not loose `.md` dumps, so check `git status` before committing.

## Don'ts

- Don't commit raw exam pages, dumps or archives, or anything that records whose answers were whose.
- Don't edit generated files: `exam-N.md`, the per-domain banks, `docs/assets/data-*.js`, `certs.js`.
- Don't change a correct-answer key without evidence (see "When a key is wrong").
- Don't add a build step, framework or server to `docs/`. It must keep working as static files from GitHub Pages and `file://`.
