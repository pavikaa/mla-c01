# AWS MLA-C01 Exam Prep Pack

Generated June 2026 from official AWS exam guide (April 2025 English update) and 2025–2026 community sources.

## Files

| File | Description |
|------|-------------|
| `01-executive-summary-and-study-plan.md` | ROI path, resource table, 1/2/4-week plans, pass probability |
| `02-domain-breakdown.md` | All 4 domains with traps and difficulty |
| `03-high-yield-notes.md` | SageMaker, MLOps, metrics, services |
| `04-flashcards-anki.txt` | **221** cards — import to Anki |
| `05-practice-questions.md` | **100** questions with explanations |
| `quiz.html` | **Interactive quiz** (all 100 Q — click answers, scoring, review) |
| `questions.json` | Machine-readable question bank (used by quiz) |
| `06-cheat-sheet-last-24h.md` | Print before exam |

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

1. Read `01` (30 min) → baseline practice test
2. Study `03` + hands-on SageMaker (weak domains only)
3. Daily `04` flashcards (20–40 cards/day)
4. `05` in timed blocks of 65 questions
5. Book exam at **≥85%** on two full practice runs
6. `06` the day before
