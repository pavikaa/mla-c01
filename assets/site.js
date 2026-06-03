/** Shared nav + markdown reader for MLA-C01 hub */
const DOCS = [
  { section: 'Start here', items: [
    { file: '01-executive-summary-and-study-plan.md', title: 'Executive summary & study plan', desc: 'ROI, timelines, resources' },
    { file: '07-notion-study-crosswalk.md', title: 'Notion study crosswalk', desc: '45-day flow with Greciano notes' },
  ]},
  { section: 'Study guides', items: [
    { file: '02-domain-breakdown.md', title: 'Domain breakdown', desc: 'All 4 exam domains' },
    { file: '03-high-yield-notes.md', title: 'High-yield notes', desc: 'SageMaker, MLOps, metrics' },
    { file: '08-supplemental-topics.md', title: 'Supplemental topics', desc: 'Bedrock, FSx, MSK, traps' },
    { file: '06-cheat-sheet-last-24h.md', title: 'Last 24h cheat sheet', desc: 'Pre-exam cram' },
  ]},
  { section: 'Practice', items: [
    { file: '05-practice-questions.md', title: 'Practice questions (120)', desc: 'Full Q&A text' },
  ]},
];

const EXTERNAL = [
  { href: 'https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0', title: 'Greciano Notion notes', desc: 'Free deep-dive (external)' },
  { href: 'https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf', title: 'Official exam guide PDF', desc: 'AWS' },
];

function renderNavLinks(activeFile) {
  let html = '';
  for (const sec of DOCS) {
    html += `<div class="nav-section">${sec.section}</div>`;
    for (const item of sec.items) {
      const active = item.file === activeFile ? ' active' : '';
      html += `<a class="nav-link${active}" href="learn.html?doc=${encodeURIComponent(item.file)}">${item.title}</a>`;
    }
  }
  html += `<div class="nav-section">Tools</div>`;
  html += `<a class="nav-link" href="quiz.html">Interactive quiz</a>`;
  html += `<a class="nav-link" href="index.html">Home</a>`;
  html += `<div class="nav-section">External</div>`;
  for (const ex of EXTERNAL) {
    html += `<a class="nav-link" href="${ex.href}" target="_blank" rel="noopener">${ex.title} ↗</a>`;
  }
  return html;
}

function initMobileNav() {
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('site-nav');
  const overlay = document.getElementById('nav-overlay');
  if (!toggle || !nav) return;

  const close = () => {
    nav.classList.remove('open');
    overlay?.classList.remove('show');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    overlay?.classList.toggle('show', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  overlay?.addEventListener('click', close);
  nav.querySelectorAll('.nav-link').forEach((a) => {
    a.addEventListener('click', () => {
      if (!a.target || a.target === '_self') close();
    });
  });
}

async function loadMarkdown(file) {
  const el = document.getElementById('doc-content');
  const titleEl = document.getElementById('doc-title');
  if (!el) return;

  el.innerHTML = '<p class="loading">Loading…</p>';
  try {
    const res = await fetch(file);
    if (!res.ok) throw new Error(`Could not load ${file} (${res.status})`);
    const md = await res.text();
    if (typeof marked === 'undefined') throw new Error('Markdown parser failed to load');
    marked.setOptions({ gfm: true, breaks: false, headerIds: true, mangle: false });
    el.innerHTML = `<article class="prose">${marked.parse(md)}</article>`;
    const h1 = el.querySelector('h1');
    if (titleEl && h1) titleEl.textContent = h1.textContent;
    else if (titleEl) titleEl.textContent = file.replace(/\.md$/, '').replace(/^\d+-/, '').replace(/-/g, ' ');
    document.title = `${titleEl?.textContent || 'Study'} — MLA-C01`;
    window.scrollTo(0, 0);
  } catch (err) {
    el.innerHTML = `<div class="error-box"><p>${err.message}</p><p><a href="index.html">Back to home</a></p></div>`;
  }
}

function initLearnPage() {
  const params = new URLSearchParams(location.search);
  const doc = params.get('doc') || '01-executive-summary-and-study-plan.md';
  const nav = document.getElementById('site-nav');
  if (nav) nav.innerHTML = renderNavLinks(doc);
  initMobileNav();
  loadMarkdown(doc);
}

function initHomePage() {
  initMobileNav();
}

document.addEventListener('DOMContentLoaded', () => {
  if (document.body.dataset.page === 'learn') initLearnPage();
  else if (document.body.dataset.page === 'home') initHomePage();
});
