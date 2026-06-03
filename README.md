# AWS MLA-C01 Exam Prep Pack

Generated June 2026 from official AWS exam guide (April 2025 English update), community sources, and crosswalk to [Christian Greciano’s free MLA-C01 Notion notes](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0) (v3).

## Files

| File | Description |
|------|-------------|
| `01-executive-summary-and-study-plan.md` | ROI path, resource table, 1/2/4-week plans, pass probability |
| `02-domain-breakdown.md` | All 4 domains with traps and difficulty |
| `03-high-yield-notes.md` | SageMaker, MLOps, metrics, services |
| `04-flashcards-anki.txt` | **235** cards — import to Anki |
| `05-practice-questions.md` | **120** questions with explanations |
| `quiz.html` | **Interactive quiz** (120 Q — click answers, scoring, review) |
| `questions.json` | Machine-readable question bank (used by quiz) |
| `06-cheat-sheet-last-24h.md` | Print before exam |
| `07-notion-study-crosswalk.md` | Maps free Notion notes → repo study flow (~45 days) |
| `08-supplemental-topics.md` | Bedrock, Domain, FSx, MSK, pitfalls (Notion-aligned) |

## Interactive practice quiz

Open **`quiz.html`** in a browser (double-click works — questions are embedded).

**Features:** single & multi-select, ordering, matching · filter by domain · 65-question exam mode · optional timer · explanations · review incorrect

**GitHub Pages:** enable Pages on repo → source `main` / root → quiz at  
`https://pavikaa.github.io/mla-c01/quiz.html`

**Local server (optional):**
```bash
cd aws-mla-c01-prep && python3 -m http.server 8080
# http://localhost:8080/quiz.html
```

## Anki import

1. Anki → File → Import → `04-flashcards-anki.txt`
2. Type: **Basic** (or Cloze if you convert)
3. Field separator: **Tab**
4. Allow HTML: off
5. Tags column maps to `mla-c01::Domain*`
6. Cards marked `[HF]` = high-frequency

## Official links

- [Certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)
- [Exam guide PDF](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)
- [Skill Builder exam prep plan](https://skillbuilder.aws/learning-plan/A2FGY8CH1P/exam-prep-plan-aws-certified-machine-learning-engineer--associate-mlac01--english/3YFU86SSKN)

## Suggested workflow

**With free Notion notes (recommended parallel read):**

1. Open `07-notion-study-crosswalk.md` → follow Notion sections in order  
2. Read [Greciano Notion MLA-C01](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0) for depth · `08-supplemental-topics.md` for exam traps  
3. Daily `04` flashcards (20 new/day ≈ 12 days for full deck)  
4. `quiz.html` — domain filters while learning; **exam mode (65)** when ready  
5. Add **Tutorials Dojo** or Skill Builder official practice exams  
6. Book real exam at **≥85%** on two timed runs · `06` cheat sheet last 24h  

**Repo-only fast path:** `01` → `03` → `quiz.html` → `06`
