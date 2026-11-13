(function () {
  'use strict';
  const DATA = window.APP_DATA;
  const Q = DATA.questions;
  const DOMAINS = DATA.domains;
  const LESSONS = DOMAINS.flatMap(d => d.lessons.map(l => Object.assign({ domain: d.n }, l)));
  const LESSON_BY_ID = Object.fromEntries(LESSONS.map(l => [l.id, l]));
  const GLOSSARY = DOMAINS.flatMap(d => d.glossary).sort((a, b) => a.term.localeCompare(b.term));
  const MOCK_SIZE = 50, MOCK_MINUTES = 120;

  // ---------- persistence ----------
  const KEY = 'gcpdevops-study-v1';
  const store = (() => {
    let s = {};
    try { s = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) {}
    s.done = s.done || {};
    s.attempts = s.attempts || {};
    s.mocks = s.mocks || [];
    return s;
  })();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  function recordAttempt(qid, ok) { store.attempts[qid] = { ok, ts: Date.now() }; save(); }
  // A question counts as a mistake while your latest answer to it (in a lesson, drill or mock exam) is wrong.
  function isMistake(qid) {
    const a = store.attempts[qid];
    return !!a && !a.ok;
  }

  // ---------- helpers ----------
  const $ = (sel, root = document) => root.querySelector(sel);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const dcolor = n => `var(--d${n})`;
  const badge = n => `<span class="badge" style="background:${dcolor(n)}">D${n}</span>`;
  const pct = (a, b) => (b ? Math.round((a / b) * 100) : 0);
  const shuffle = arr => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const lessonHref = l => `#/d/${l.domain}/${l.num}`;
  const domainDone = d => d.lessons.filter(l => store.done[l.id]).length;
  const correctSet = q => q.options.map((o, i) => (o.correct ? i : -1)).filter(i => i >= 0);
  const strip = html => html.replace(/<[^>]+>/g, ' ');

  // ---------- sidebar ----------
  function renderSidebar(route) {
    const total = LESSONS.length, done = LESSONS.filter(l => store.done[l.id]).length;
    const activeLesson = route[0] === 'd' && route[2] ? `d${route[1]}l${route[2]}` : null;
    const link = (href, label, key) => `<a class="nav-link ${location.hash === href || (key && route[0] === key) ? 'active' : ''}" href="${href}">${label}</a>`;
    $('#sidebar').innerHTML = `
      <div class="progress-box">
        <div class="label"><span>Study progress</span><span>${done} of ${total} lessons</span></div>
        <div class="bar"><span style="width:${pct(done, total)}%"></span></div>
      </div>
      <div class="nav-group"><h4>Overview</h4>${link('#/', 'Curriculum overview')}</div>
      <div class="nav-group"><h4>Curriculum</h4>
        ${DOMAINS.map(d => `
          <details class="nav-domain" ${String(d.n) === route[1] && route[0] === 'd' ? 'open' : ''}>
            <summary class="nav-link ${route[0] === 'd' && String(d.n) === route[1] && !route[2] ? 'active' : ''}">
              ${badge(d.n)}<span>${esc(d.short)}</span><span class="chev">▶</span>
            </summary>
            <div class="lessons">
              <a class="nav-link" href="#/d/${d.n}"><span class="num">··</span>Domain overview</a>
              ${d.lessons.map(l => `<a class="nav-link ${activeLesson === l.id ? 'active' : ''}" href="#/d/${d.n}/${l.num}">
                <span class="num">${d.n}.${l.num}</span><span>${esc(l.title)}</span>${store.done[l.id] ? '<span class="check">✓</span>' : ''}</a>`).join('')}
            </div>
          </details>`).join('')}
      </div>
      <div class="nav-group"><h4>Practice</h4>
        ${link('#/drill', 'Drill mode', 'drill')}${link('#/mock', 'Mock exam', 'mock')}${link('#/review', 'Review mistakes', 'review')}
      </div>
      <div class="nav-group"><h4>Look Up</h4>
        ${link('#/ref', 'Quick Reference', 'ref')}${link('#/glossary', 'Glossary', 'glossary')}
      </div>`;
    document.querySelectorAll('.topnav a').forEach(a => {
      const k = a.dataset.nav;
      a.classList.toggle('active', k === 'learn' ? (!route[0] || route[0] === 'd') : route[0] === k);
    });
  }

  // ---------- quiz component ----------
  // mode: 'practice' (instant feedback) | 'exam' (select only; feedback rendered later via reveal)
  function quizCard(qid, opts = {}) {
    const q = Q[qid];
    const multi = correctSet(q).length > 1;
    const el = document.createElement('div');
    el.className = 'quiz';
    const lessons = (q.lessons || []).map(id => LESSON_BY_ID[id]);
    el.innerHTML = `
      <div class="quiz-head">
        ${badge(q.domain)}<span class="tag">Exam ${q.exam} · Q${q.n}</span>
        ${multi ? `<span class="tag">Choose ${correctSet(q).length}</span>` : ''}
        ${isMistake(qid) ? '<span class="tag bad">In your mistakes</span>' : ''}
        ${opts.label ? `<span>${esc(opts.label)}</span>` : ''}
      </div>
      <div class="quiz-q prose">${q.html}</div>
      <div class="opts">${q.options.map((o, i) => `<button type="button" class="opt ${multi ? 'multi' : ''}" data-i="${i}"><span class="mark"></span><span>${o.html}</span></button>`).join('')}</div>
      <div class="row no-print qactions">${opts.mode === 'exam' ? '' : `<button class="btn primary" data-act="check" disabled>Check answer</button>`}</div>
      <div class="feedback"></div>`;
    const selected = new Set(opts.selected || []);
    const buttons = [...el.querySelectorAll('.opt')];
    const paint = () => buttons.forEach((b, i) => b.classList.toggle('sel', selected.has(i)));
    paint();
    const checkBtn = $('[data-act="check"]', el);
    const sync = () => { if (checkBtn) checkBtn.disabled = selected.size === 0; };
    sync();
    buttons.forEach((b, i) => b.addEventListener('click', () => {
      if (el.dataset.locked) return;
      if (multi) { selected.has(i) ? selected.delete(i) : selected.add(i); }
      else { selected.clear(); selected.add(i); }
      paint(); sync();
      if (opts.onSelect) opts.onSelect([...selected]);
    }));
    function reveal(record) {
      el.dataset.locked = '1';
      const want = correctSet(q);
      const ok = want.length === selected.size && want.every(i => selected.has(i));
      buttons.forEach((b, i) => {
        b.disabled = true; b.classList.remove('sel');
        if (want.includes(i)) b.classList.add('correct');
        else if (selected.has(i)) b.classList.add('wrong');
      });
      if (record) recordAttempt(qid, ok);
      $('.qactions', el).innerHTML = '';
      $('.feedback', el).innerHTML = `
        <p class="result ${ok ? 'ok' : 'bad'}">${selected.size === 0 ? 'Not answered' : ok ? '✓ Correct' : '✗ Incorrect'}</p>
        <details class="explain" ${opts.openExplanation === false ? '' : 'open'}><summary>Explanation</summary><div class="prose">${q.explanation}</div></details>
        ${lessons.length ? `<p class="muted" style="font-size:13.5px;margin-top:10px">Related lesson${lessons.length > 1 ? 's' : ''}: ${lessons.map(l => `<a href="${lessonHref(l)}">${l.domain}.${l.num} ${esc(l.title)}</a>`).join(' · ')}</p>` : ''}`;
      if (opts.onReveal) opts.onReveal(ok);
      return ok;
    }
    if (checkBtn) checkBtn.addEventListener('click', () => reveal(true));
    el.reveal = reveal;
    return el;
  }

  // ---------- views ----------
  function viewHome(main) {
    const total = LESSONS.length, done = LESSONS.filter(l => store.done[l.id]).length;
    const attempted = Object.keys(store.attempts).length;
    const right = Object.values(store.attempts).filter(a => a.ok).length;
    const next = LESSONS.find(l => !store.done[l.id]);
    main.innerHTML = `
      <div class="crumbs">PCDOE / Curriculum</div>
      <h1>Professional Cloud DevOps Engineer</h1>
      <p class="lead">${DOMAINS.length} domains, ${total} lessons and ${Object.keys(Q).length} practice questions from five practice exams. Work through each domain's lessons, then drill the questions and take a mock exam.</p>
      <div class="stats">
        <div class="stat"><b>${done}/${total}</b><span>Lessons complete</span></div>
        <div class="stat"><b>${attempted}</b><span>Questions attempted</span></div>
        <div class="stat"><b>${attempted ? pct(right, attempted) + '%' : '—'}</b><span>Drill accuracy</span></div>
        <div class="stat"><b>${Object.keys(Q).filter(isMistake).length}</b><span>Mistakes to review</span></div>
      </div>
      ${next ? `<div class="row"><a class="btn primary" href="${lessonHref(next)}">${done ? 'Continue' : 'Start'}: ${next.domain}.${next.num} ${esc(next.title)} →</a></div>` : ''}
      <h2>Domains</h2>
      <div class="cards">${DOMAINS.map(d => `
        <a class="card" href="#/d/${d.n}">
          <div class="card-head">${badge(d.n)}<span class="weight">${d.weight} of exam</span></div>
          <h3>${esc(d.title)}</h3>
          <p>${esc(d.desc)}</p>
          <div class="meta"><span>${d.lessons.length} lessons</span><span>${domainDone(d)}/${d.lessons.length} done</span></div>
          <div class="bar"><span style="width:${pct(domainDone(d), d.lessons.length)}%;background:${dcolor(d.n)}"></span></div>
        </a>`).join('')}
      </div>
      <h2>Practice</h2>
      <div class="cards">
        <a class="card" href="#/drill"><h3>Drill mode</h3><p>Questions one at a time with instant feedback. Filter by domain, unseen questions or mistakes.</p></a>
        <a class="card" href="#/mock"><h3>Mock exam</h3><p>${MOCK_SIZE} questions weighted by domain in ${MOCK_MINUTES} minutes, scored at the end.</p></a>
        <a class="card" href="#/review"><h3>Review mistakes</h3><p>Every question you got wrong in lessons, drills or mock exams.</p></a>
      </div>
      <h2>Look Up</h2>
      <div class="cards">
        <a class="card" href="#/ref"><h3>Quick Reference</h3><p>One printable sheet per domain: cheat sheet, decision rules, exam traps and questionable answers.</p></a>
        <a class="card" href="#/glossary"><h3>Glossary</h3><p>${GLOSSARY.length} terms with definitions, how they're tested, and links to the lesson.</p></a>
      </div>
      <p class="muted" style="font-size:13px;margin-top:28px">Exam weights are approximate. Check the current official exam guide.</p>`;
  }

  function viewDomain(main, n) {
    const d = DOMAINS.find(x => String(x.n) === n);
    if (!d) return viewNotFound(main);
    const qcount = Object.values(Q).filter(q => q.domain === d.n).length;
    main.innerHTML = `
      <div class="crumbs"><a href="#/">Curriculum</a> / Domain ${d.n}</div>
      <div class="row" style="margin-bottom:8px">${badge(d.n)}<span class="muted">${d.weight} of exam · ${d.lessons.length} lessons · ${qcount} questions</span></div>
      <h1>${esc(d.title)}</h1>
      <p class="lead">${esc(d.desc)}</p>
      <div class="row">
        <a class="btn primary" href="#/d/${d.n}/${(d.lessons.find(l => !store.done[l.id]) || d.lessons[0]).num}">${domainDone(d) ? 'Continue' : 'Start'} domain →</a>
        <a class="btn" href="#/drill/${d.n}">Drill this domain</a>
        <a class="btn" href="#/ref/${d.n}">Quick reference</a>
        <a class="btn" href="#/glossary/${d.n}">Glossary</a>
      </div>
      <ul class="lesson-list">${d.lessons.map(l => `
        <li><a href="#/d/${d.n}/${l.num}">
          <span class="num">${d.n}.${l.num}</span>
          <span style="flex:1"><div class="t">${esc(l.title)}</div>${l.summary ? `<div class="s">${esc(l.summary)}</div>` : ''}</span>
          ${store.done[l.id] ? '<span class="check">✓ Done</span>' : `<span class="muted" style="font-size:12.5px;white-space:nowrap">${l.questions.length} Qs</span>`}
        </a></li>`).join('')}
      </ul>`;
  }

  function viewLesson(main, n, num) {
    const d = DOMAINS.find(x => String(x.n) === n);
    const idx = LESSONS.findIndex(l => l.id === `d${n}l${num}`);
    if (!d || idx < 0) return viewNotFound(main);
    const l = LESSONS[idx], prev = LESSONS[idx - 1], next = LESSONS[idx + 1];
    const terms = GLOSSARY.filter(g => g.lesson === l.id);
    main.innerHTML = `
      <div class="crumbs"><a href="#/">Curriculum</a> / <a href="#/d/${d.n}">Domain ${d.n}</a> / Lesson ${d.n}.${l.num}</div>
      <div class="row" style="margin-bottom:8px">${badge(d.n)}<span class="muted">${esc(d.short)} · Lesson ${l.num} of ${d.lessons.length}</span></div>
      <h1>${esc(l.title)}</h1>
      ${l.summary ? `<p class="lead">${esc(l.summary)}</p>` : ''}
      ${l.objectives.length ? `<div class="callout objectives"><h4>After this lesson you can</h4><ul>${l.objectives.map(o => `<li>${esc(o.replace(/^After this lesson,? you (can|will be able to)\s*/i, '').replace(/^./, c => c.toUpperCase()))}</li>`).join('')}</ul></div>` : ''}
      <div class="prose">${l.html}</div>
      ${l.takeaways.length ? `<div class="callout takeaways"><h4>Key takeaways</h4><ul>${l.takeaways.map(o => `<li>${esc(o)}</li>`).join('')}</ul></div>` : ''}
      ${terms.length ? `<p class="muted" style="font-size:14px">Terms in this lesson: ${terms.map(t => `<a href="#/glossary/${d.n}/${encodeURIComponent(t.term)}">${esc(t.term)}</a>`).join(' · ')}</p>` : ''}
      ${l.questions.length ? `<h2>Practice questions <span class="muted" style="font-size:15px;font-weight:400">(${l.questions.length})</span></h2>
        <p class="muted">Questions cited in this lesson. Answer them before reading the explanation.</p><div id="lessonQs"></div>` : ''}
      <div class="row no-print" style="margin-top:28px">
        <button class="btn ${store.done[l.id] ? 'done' : 'primary'}" id="doneBtn">${store.done[l.id] ? '✓ Completed (click to undo)' : 'Mark lesson complete'}</button>
      </div>
      <nav class="pager">
        ${prev ? `<a href="${lessonHref(prev)}"><small>← Previous</small>${prev.domain}.${prev.num} ${esc(prev.title)}</a>` : '<span></span>'}
        ${next ? `<a class="next" href="${lessonHref(next)}"><small>Next →</small>${next.domain}.${next.num} ${esc(next.title)}</a>` : '<span></span>'}
      </nav>`;
    const box = $('#lessonQs');
    if (box) l.questions.forEach(qid => box.appendChild(quizCard(qid)));
    $('#doneBtn').addEventListener('click', () => {
      if (store.done[l.id]) delete store.done[l.id];
      else store.done[l.id] = Date.now();
      save();
      if (store.done[l.id] && next) location.hash = lessonHref(next).slice(1); else route();
    });
  }

  function viewQuestion(main, qid) {
    const q = Q[qid];
    if (!q) return viewNotFound(main);
    main.innerHTML = `<div class="crumbs"><a href="#/">Curriculum</a> / <a href="#/d/${q.domain}">Domain ${q.domain}</a> / Question</div>
      <h1>Exam ${q.exam} · Question ${q.n}</h1>
      <p class="muted"><a href="javascript:history.back()">← Back</a></p><div id="qbox"></div>`;
    $('#qbox').appendChild(quizCard(qid));
  }

  // Drill: setup → one question at a time → summary
  let drill = null;
  function viewDrill(main, preset) {
    if (drill && drill.active) return drillStep(main);
    const sel = new Set(preset ? [Number(preset)] : DOMAINS.map(d => d.n));
    let source = 'all', count = 20;
    function pool() {
      return Object.keys(Q).filter(id => sel.has(Q[id].domain)).filter(id =>
        source === 'unseen' ? !store.attempts[id] : source === 'mistakes' ? isMistake(id) : true);
    }
    function draw() {
      const p = pool();
      main.innerHTML = `
        <div class="crumbs">Practice / Drill mode</div>
        <h1>Drill mode</h1>
        <p class="lead">Questions one at a time with instant feedback and explanations. Your answers count toward progress and mistakes.</p>
        <div class="panel">
          <h3>Domains</h3>
          <div class="chips">${DOMAINS.map(d => `<button class="chip" data-d="${d.n}" aria-pressed="${sel.has(d.n)}">D${d.n} · ${esc(d.short)}</button>`).join('')}</div>
          <h3>Questions</h3>
          <div class="chips">${[['all', 'All'], ['unseen', 'Not yet attempted'], ['mistakes', 'My mistakes']].map(([k, v]) => `<button class="chip" data-s="${k}" aria-pressed="${source === k}">${v}</button>`).join('')}</div>
          <h3>Session length</h3>
          <div class="chips">${[10, 20, 50, 0].map(c => `<button class="chip" data-c="${c}" aria-pressed="${count === c}">${c || 'All'}</button>`).join('')}</div>
          <div class="row"><button class="btn primary" id="startDrill" ${p.length ? '' : 'disabled'}>Start drill (${count ? Math.min(count, p.length) : p.length} of ${p.length} available)</button></div>
        </div>`;
      main.querySelectorAll('[data-d]').forEach(b => b.onclick = () => { const n = Number(b.dataset.d); sel.has(n) ? sel.delete(n) : sel.add(n); draw(); });
      main.querySelectorAll('[data-s]').forEach(b => b.onclick = () => { source = b.dataset.s; draw(); });
      main.querySelectorAll('[data-c]').forEach(b => b.onclick = () => { count = Number(b.dataset.c); draw(); });
      $('#startDrill').onclick = () => {
        const ids = shuffle(p).slice(0, count || p.length);
        drill = { active: true, ids, i: 0, results: {} };
        drillStep(main);
      };
    }
    draw();
  }
  function drillStep(main) {
    const { ids, i, results } = drill;
    if (i >= ids.length) return drillSummary(main);
    const answered = Object.keys(results).length, right = Object.values(results).filter(Boolean).length;
    main.innerHTML = `
      <div class="crumbs">Practice / Drill mode</div>
      <div class="row" style="justify-content:space-between">
        <h1 style="margin:0">Question ${i + 1} <span class="muted" style="font-weight:400">of ${ids.length}</span></h1>
        <span class="muted">${right}/${answered} correct</span>
      </div>
      <div class="bar" style="margin:12px 0"><span style="width:${pct(i, ids.length)}%"></span></div>
      <div id="qbox"></div>
      <div class="row no-print"><button class="btn primary" id="nextQ" style="display:none">${i + 1 < ids.length ? 'Next question →' : 'See results'}</button>
      <button class="btn" id="quitDrill">End drill</button></div>`;
    const card = quizCard(ids[i], {
      onReveal: ok => { results[ids[i]] = ok; $('#nextQ').style.display = ''; $('#nextQ').focus(); },
    });
    $('#qbox').appendChild(card);
    $('#nextQ').onclick = () => { drill.i++; drillStep(main); window.scrollTo(0, 0); };
    $('#quitDrill').onclick = () => { drill.ids = ids.slice(0, Math.max(answered, 0)); drill.i = drill.ids.length; drillStep(main); };
  }
  function drillSummary(main) {
    const res = drill.results; drill.active = false;
    const ids = Object.keys(res), right = ids.filter(id => res[id]).length;
    main.innerHTML = `
      <div class="crumbs">Practice / Drill mode</div>
      <h1>Drill complete</h1>
      <div class="stats"><div class="stat"><b>${right}/${ids.length}</b><span>Correct</span></div><div class="stat"><b>${pct(right, ids.length)}%</b><span>Score</span></div></div>
      ${domainBreakdown(ids, id => res[id])}
      ${ids.some(id => !res[id]) ? `<h2>Missed in this drill</h2><ul>${ids.filter(id => !res[id]).map(id => `<li><a href="#/q/${id}">Exam ${Q[id].exam} · Q${Q[id].n}</a> <span class="muted">${esc(strip(Q[id].html).slice(0, 110))}…</span></li>`).join('')}</ul>` : ''}
      <div class="row" style="margin-top:20px"><a class="btn primary" href="#/drill" id="again">New drill</a><a class="btn" href="#/review">Review all mistakes</a></div>`;
    $('#again').onclick = e => { e.preventDefault(); drill = null; location.hash === '#/drill' ? route() : (location.hash = '#/drill'); };
  }
  function domainBreakdown(ids, isRight) {
    return `<table class="table prose"><thead><tr><th>Domain</th><th>Correct</th><th>Score</th></tr></thead><tbody>${DOMAINS.map(d => {
      const inD = ids.filter(id => Q[id].domain === d.n); if (!inD.length) return '';
      const r = inD.filter(isRight).length;
      return `<tr><td>${badge(d.n)} ${esc(d.short)}</td><td>${r}/${inD.length}</td><td>${pct(r, inD.length)}%</td></tr>`;
    }).join('')}</tbody></table>`;
  }

  // Mock exam: weighted sample, timer, no feedback until submit
  let mock = null;
  function viewMock(main) {
    if (mock && !mock.done) return mockStep(main);
    if (mock && mock.done) return mockResults(main);
    const history = store.mocks.slice(-5).reverse();
    main.innerHTML = `
      <div class="crumbs">Practice / Mock exam</div>
      <h1>Mock exam</h1>
      <p class="lead">${MOCK_SIZE} questions drawn across all domains in proportion to exam weight, with a ${MOCK_MINUTES}-minute timer. No feedback until you submit. You can flag questions and jump around.</p>
      <div class="row"><button class="btn primary" id="startMock">Start mock exam</button></div>
      ${history.length ? `<h2>Recent attempts</h2><table class="table prose"><thead><tr><th>Date</th><th>Score</th><th>Time used</th></tr></thead><tbody>${history.map(h => `<tr><td>${new Date(h.ts).toLocaleString()}</td><td>${h.right}/${h.total} (${pct(h.right, h.total)}%)</td><td>${Math.round(h.secs / 60)} min</td></tr>`).join('')}</tbody></table>` : ''}`;
    $('#startMock').onclick = () => {
      const weights = DOMAINS.map(d => parseFloat(d.weight.replace(/[^\d.]/g, '')) || 20);
      const wsum = weights.reduce((a, b) => a + b, 0);
      let ids = [];
      DOMAINS.forEach((d, i) => {
        const pool = shuffle(Object.keys(Q).filter(id => Q[id].domain === d.n));
        ids = ids.concat(pool.slice(0, Math.round((MOCK_SIZE * weights[i]) / wsum)));
      });
      ids = shuffle(ids).slice(0, MOCK_SIZE);
      mock = { ids, i: 0, answers: {}, flags: {}, start: Date.now(), done: false };
      mockStep(main);
    };
  }
  let timerHandle = null;
  function mockStep(main) {
    const { ids, i } = mock;
    const remaining = () => Math.max(0, MOCK_MINUTES * 60 - Math.floor((Date.now() - mock.start) / 1000));
    const fmt = s => `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
    main.innerHTML = `
      <div class="crumbs">Practice / Mock exam</div>
      <div class="row" style="justify-content:space-between">
        <h1 style="margin:0">Question ${i + 1} <span class="muted" style="font-weight:400">of ${ids.length}</span></h1>
        <span class="timer" id="timer">${fmt(remaining())}</span>
      </div>
      <div class="qnav no-print">${ids.map((id, k) => `<button data-k="${k}" class="${mock.answers[id] && mock.answers[id].length ? 'answered' : ''} ${k === i ? 'current' : ''} ${mock.flags[id] ? 'flag' : ''}" aria-label="Question ${k + 1}">${k + 1}</button>`).join('')}</div>
      <div id="qbox"></div>
      <div class="row no-print">
        <button class="btn" id="prevQ" ${i === 0 ? 'disabled' : ''}>← Previous</button>
        <button class="btn" id="flagQ">${mock.flags[ids[i]] ? '⚑ Unflag' : '⚐ Flag for review'}</button>
        <button class="btn primary" id="nextQ">${i + 1 < ids.length ? 'Next →' : 'Review & submit'}</button>
        <button class="btn" id="submitMock" style="margin-left:auto">Submit exam</button>
      </div>`;
    $('#qbox').appendChild(quizCard(ids[i], { mode: 'exam', selected: mock.answers[ids[i]], onSelect: s => { mock.answers[ids[i]] = s; } }));
    const go = k => { mock.i = k; mockStep(main); window.scrollTo(0, 0); };
    main.querySelectorAll('[data-k]').forEach(b => b.onclick = () => go(Number(b.dataset.k)));
    $('#prevQ').onclick = () => go(i - 1);
    $('#nextQ').onclick = () => (i + 1 < ids.length ? go(i + 1) : $('#submitMock').click());
    $('#flagQ').onclick = () => { mock.flags[ids[i]] = !mock.flags[ids[i]]; mockStep(main); };
    $('#submitMock').onclick = () => {
      const unanswered = ids.filter(id => !(mock.answers[id] && mock.answers[id].length)).length;
      if (unanswered && !confirm(`${unanswered} question(s) unanswered. Submit anyway?`)) return;
      finishMock(main);
    };
    clearInterval(timerHandle);
    timerHandle = setInterval(() => {
      const t = $('#timer'); if (!t || !mock || mock.done) return clearInterval(timerHandle);
      const r = remaining(); t.textContent = fmt(r);
      if (r === 0) { clearInterval(timerHandle); alert('Time is up. Your exam will be submitted.'); finishMock(main); }
    }, 1000);
  }
  function mockCorrect(id) {
    const want = correctSet(Q[id]), got = mock.answers[id] || [];
    return want.length === got.length && want.every(i => got.includes(i));
  }
  function finishMock(main) {
    clearInterval(timerHandle);
    mock.done = true;
    mock.secs = Math.floor((Date.now() - mock.start) / 1000);
    mock.ids.forEach(id => { if (mock.answers[id] && mock.answers[id].length) recordAttempt(id, mockCorrect(id)); });
    const right = mock.ids.filter(mockCorrect).length;
    store.mocks.push({ ts: Date.now(), right, total: mock.ids.length, secs: mock.secs }); save();
    mockResults(main);
  }
  function mockResults(main) {
    const ids = mock.ids, right = ids.filter(mockCorrect).length;
    main.innerHTML = `
      <div class="crumbs">Practice / Mock exam</div>
      <h1>Mock exam results</h1>
      <div class="stats">
        <div class="stat"><b>${pct(right, ids.length)}%</b><span>Score (${right}/${ids.length})</span></div>
        <div class="stat"><b>${Math.round(mock.secs / 60)} min</b><span>Time used</span></div>
      </div>
      <p class="muted">Google doesn't publish a pass mark. Aim for a steady 80%+ on mock exams before booking.</p>
      ${domainBreakdown(ids, mockCorrect)}
      <div class="row no-print"><button class="btn primary" id="newMock">New mock exam</button></div>
      <h2>Review</h2><div id="review"></div>`;
    const box = $('#review');
    ids.forEach((id, k) => {
      const card = quizCard(id, { mode: 'exam', selected: mock.answers[id], label: `Question ${k + 1}`, openExplanation: false });
      box.appendChild(card); card.reveal(false);
    });
    $('#newMock').onclick = () => { mock = null; viewMock(main); };
  }

  function viewReview(main) {
    const ids = Object.keys(Q).filter(isMistake).sort((a, b) => Q[a].domain - Q[b].domain || Q[a].exam - Q[b].exam || Q[a].n - Q[b].n);
    main.innerHTML = `
      <div class="crumbs">Practice / Review mistakes</div>
      <h1>Review mistakes</h1>
      <p class="lead">${ids.length} question${ids.length === 1 ? '' : 's'} to review: every question whose latest answer, in a lesson, drill or mock exam, was wrong. A question leaves this list once you answer it correctly.</p>
      ${ids.length ? `<div class="row"><a class="btn primary" href="#/drill" id="drillMistakes">Drill these as a session</a></div><div id="list"></div>` : '<div class="empty">No mistakes yet. Questions you get wrong in lessons, drills or mock exams will show up here.</div>'}`;
    const box = $('#list');
    if (box) ids.forEach(id => box.appendChild(quizCard(id)));
    const b = $('#drillMistakes');
    if (b) b.onclick = e => { e.preventDefault(); drill = { active: true, ids: shuffle(ids), i: 0, results: {} }; location.hash = '#/drill'; };
  }

  function viewRefIndex(main) {
    main.innerHTML = `
      <div class="crumbs">Look Up / Quick Reference</div>
      <h1>Quick Reference Sheets</h1>
      <p class="lead">Dense one-page summaries for final review: the cheat sheet, every decision rule and exam trap from the lessons, and answers from the dumps that look wrong.</p>
      <div class="cards">${DOMAINS.map(d => `
        <a class="card" href="#/ref/${d.n}">
          <div class="card-head">${badge(d.n)}<span class="weight">${d.weight}</span></div>
          <h3>${esc(d.title)}</h3><p>${d.lessons.map(l => esc(l.title)).slice(0, 4).join(' · ')}${d.lessons.length > 4 ? ' …' : ''}</p>
        </a>`).join('')}
      </div>
      <div class="callout"><h4>How to use these sheets</h4><ul>
        <li>Review a domain's sheet right after finishing its lessons, and again the day before the exam.</li>
        <li>Prioritise the <b>decision rules</b> and <b>exam traps</b>. They are the highest-value material.</li>
        <li>Print with Ctrl+P / ⌘P. Navigation is hidden in print.</li>
      </ul></div>`;
  }
  function viewRef(main, n) {
    const d = DOMAINS.find(x => String(x.n) === n);
    if (!d) return viewNotFound(main);
    const block = (items, title) => items.length ? `<h2>${title}</h2>${items.map(r => `<div class="ref-rule ref-section"><h4><a href="#/d/${d.n}/${LESSON_BY_ID[r.lesson].num}">${d.n}.${LESSON_BY_ID[r.lesson].num} ${esc(r.title)}</a></h4><div class="prose">${r.html}</div></div>`).join('')}` : '';
    main.innerHTML = `
      <div class="crumbs"><a href="#/ref">Quick Reference</a> / Domain ${d.n}</div>
      <div class="row" style="justify-content:space-between">
        <div class="row">${badge(d.n)}<span class="muted">${d.weight} of exam</span></div>
        <button class="btn no-print" onclick="window.print()">Print</button>
      </div>
      <h1>${esc(d.title)}</h1>
      <h2>Cheat sheet</h2><div class="prose ref-section">${d.ref.cheat}</div>
      ${block(d.ref.rules, 'Decision rules')}
      ${block(d.ref.traps, 'Exam traps')}
      ${d.ref.questionable ? `<div class="callout warn ref-section"><h4>⚠️ Questionable answers in the dumps</h4><div class="prose">${d.ref.questionable}</div></div>` : ''}
      ${d.glossary.length ? `<h2>Key terms</h2><table class="table prose"><tbody>${d.glossary.map(g => `<tr><th style="white-space:nowrap">${esc(g.term)}</th><td>${esc(g.definition)}</td></tr>`).join('')}</tbody></table>` : ''}`;
  }

  function viewGlossary(main, n, focus) {
    let dsel = n ? Number(n) : 0, query = '';
    main.innerHTML = `
      <div class="crumbs">Look Up / Glossary</div>
      <h1>Glossary</h1>
      <p class="lead">${GLOSSARY.length} key terms. Each has a short definition, how it shows up on the exam, and a link to the lesson.</p>
      <div class="glossary-tools no-print"><input id="gq" type="search" placeholder="Filter terms…" aria-label="Filter glossary"></div>
      <div class="chips no-print" id="gchips"></div>
      <div id="gl"></div>`;
    function draw() {
      $('#gchips').innerHTML = [[0, 'All domains'], ...DOMAINS.map(d => [d.n, `D${d.n} · ${d.short}`])].map(([k, v]) => `<button class="chip" data-g="${k}" aria-pressed="${dsel === k}">${esc(v)}</button>`).join('');
      main.querySelectorAll('[data-g]').forEach(b => b.onclick = () => { dsel = Number(b.dataset.g); draw(); });
      const ql = query.toLowerCase();
      const items = GLOSSARY.filter(g => (!dsel || g.domain === dsel) && (!ql || (g.term + ' ' + g.definition + ' ' + g.exam_context).toLowerCase().includes(ql)));
      let letter = '';
      $('#gl').innerHTML = items.length ? items.map(g => {
        const L = g.term[0].toUpperCase(), head = L !== letter ? `<div class="letter">${(letter = L)}</div>` : '';
        const l = LESSON_BY_ID[g.lesson];
        return `${head}<div class="term" id="t-${g.domain}-${encodeURIComponent(g.term)}">
          <h3>${esc(g.term)} ${badge(g.domain)}</h3>
          <p>${esc(g.definition)}</p>
          <p class="ctx"><b>On the exam:</b> ${esc(g.exam_context)}</p>
          ${l ? `<p class="ctx">Lesson: <a href="${lessonHref(l)}">${l.domain}.${l.num} ${esc(l.title)}</a></p>` : ''}
        </div>`;
      }).join('') : '<div class="empty">No matching terms.</div>';
    }
    $('#gq').addEventListener('input', e => { query = e.target.value; draw(); });
    draw();
    if (focus) {
      const t = document.getElementById(`t-${n}-${encodeURIComponent(decodeURIComponent(focus))}`);
      if (t) { t.scrollIntoView(); t.style.background = 'var(--accent-soft)'; }
    }
  }

  function viewSearch(main, raw) {
    const q = decodeURIComponent(raw || '').trim(), ql = q.toLowerCase();
    $('#searchInput').value = q;
    const lessons = LESSONS.filter(l => (l.title + ' ' + l.summary + ' ' + strip(l.html)).toLowerCase().includes(ql));
    const terms = GLOSSARY.filter(g => (g.term + ' ' + g.definition).toLowerCase().includes(ql));
    const qs = Object.values(Q).filter(x => strip(x.html + x.options.map(o => o.html).join(' ')).toLowerCase().includes(ql));
    main.innerHTML = `
      <div class="crumbs">Search</div>
      <h1>Results for “${esc(q)}”</h1>
      <h2>Glossary (${terms.length})</h2>${terms.slice(0, 20).map(g => `<div class="search-hit"><a href="#/glossary/${g.domain}/${encodeURIComponent(g.term)}">${esc(g.term)}</a> ${badge(g.domain)}<small>${esc(g.definition)}</small></div>`).join('') || '<p class="muted">None</p>'}
      <h2>Lessons (${lessons.length})</h2>${lessons.map(l => `<div class="search-hit"><a href="${lessonHref(l)}">${l.domain}.${l.num} ${esc(l.title)}</a><small>${esc(l.summary)}</small></div>`).join('') || '<p class="muted">None</p>'}
      <h2>Questions (${qs.length})</h2>${qs.slice(0, 40).map(x => `<div class="search-hit"><a href="#/q/${x.id}">Exam ${x.exam} · Q${x.n}</a> ${badge(x.domain)}<small>${esc(strip(x.html).slice(0, 180))}…</small></div>`).join('') || '<p class="muted">None</p>'}
      ${qs.length > 40 ? '<p class="muted">Showing first 40 questions. Refine your search.</p>' : ''}`;
  }

  function viewNotFound(main) {
    main.innerHTML = `<h1>Page not found</h1><p><a href="#/">Back to the curriculum</a></p>`;
  }

  // ---------- router ----------
  function route() {
    const parts = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean);
    const main = $('#main');
    if (parts[0] !== 'mock') clearInterval(timerHandle);
    renderSidebar(parts);
    document.body.classList.remove('nav-open');
    const [a, b, c] = parts;
    if (!a) viewHome(main);
    else if (a === 'd' && c) viewLesson(main, b, c);
    else if (a === 'd') viewDomain(main, b);
    else if (a === 'q') viewQuestion(main, b);
    else if (a === 'drill') viewDrill(main, b);
    else if (a === 'mock') viewMock(main);
    else if (a === 'review') viewReview(main);
    else if (a === 'ref' && b) viewRef(main, b);
    else if (a === 'ref') viewRefIndex(main);
    else if (a === 'glossary') viewGlossary(main, b, c);
    else if (a === 'search') viewSearch(main, parts.slice(1).join('/'));
    else viewNotFound(main);
    if (!(a === 'glossary' && c)) window.scrollTo(0, 0);
    const t = $('h1', main);
    document.title = (t && a ? t.textContent.trim() + ' · ' : '') + 'GCP DevOps Study';
  }

  window.addEventListener('hashchange', route);
  $('#searchForm').addEventListener('submit', e => {
    e.preventDefault();
    const v = $('#searchInput').value.trim();
    if (v) location.hash = '#/search/' + encodeURIComponent(v);
  });
  $('#menuBtn').addEventListener('click', () => {
    const open = document.body.classList.toggle('nav-open');
    $('#menuBtn').setAttribute('aria-expanded', String(open));
  });
  $('#scrim').addEventListener('click', () => document.body.classList.remove('nav-open'));
  $('#themeBtn').addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('gcpdevops-theme', root.dataset.theme); } catch (e) {}
  });
  route();
})();
