# MLA-C01 Study Crosswalk — Christian Greciano Notion Notes (v3)

**External resource (free):** [AWS ML Engineer Associate — Notion notes](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0) by [Christian Greciano](https://christiangreciano.com/notes.html)  
**Version referenced:** v3 (last updated 2025-07-18) · Author passed MLA-C01 Jan 29, 2025

> **How to use this file:** Read the Notion guide for depth; use **this repo** for exam-shaped practice (quiz, flashcards, cheat sheet). Do not duplicate the Notion page into Git — link to it instead.

---

## Prerequisites (from Notion — important)

Greciano assumes you already have (or study in parallel):

| Cert / knowledge | Why it matters for MLA-C01 |
|------------------|----------------------------|
| **AWS AI Practitioner (AIF-C01)** | Managed AI services (Comprehend, Rekognition, etc.) — Notion points AI service flashcards to AIF deck |
| **Solutions Architect Associate (SAA-C03)** | VPC, IAM, S3, networking, security patterns |

If you are a **senior AWS engineer**, you may skip formal certs but should still skim AIF-level “which managed AI service” decisions.

---

## Notion section → This repo

| Notion section (v3 TOC) | Official MLA domain | Read in repo |
|-------------------------|---------------------|--------------|
| Data Ingestion and Storage | D1 (28%) | `03-high-yield-notes.md`, `08-supplemental-topics.md` |
| Feature Engineering, Transformation, Integrity | D1 | `02-domain-breakdown.md` Domain 1 |
| Deep Learning & Neural Networks | D2 (awareness) | `08-supplemental-topics.md` — exam ops focus, not math depth |
| SageMaker: Training, Tuning, Evaluation | D2 (26%) | `03-high-yield-notes.md` |
| GenAI apps in **Amazon Bedrock** | D2 | `08-supplemental-topics.md` |
| AWS Products for DevOps/MLOps | D3 (22%) | `03-high-yield-notes.md`, Domain 3 in `02` |
| SageMaker MLOps | D3 | Pipelines, Registry, endpoints |
| Security and Privacy | D4 (24%) | `03-high-yield-notes.md`, Domain 4 |
| Governance and Management | D4 | Lake Formation, CloudTrail, tags |
| SageMaker Security, Identity, Compliance | D4 | VPC, IAM, KMS |
| ML Best Practices | All | `06-cheat-sheet-last-24h.md` |

---

## Recommended combined study flow (~45 days, from Notion + practice)

Aligned with Greciano’s path + this repo’s practice focus:

| Phase | Days | Notion (read) | This repo (do) |
|-------|------|---------------|----------------|
| 1 — Data | 1–10 | Ingestion, storage, features, integrity | `04-flashcards` D1 tags · Domain filter in `quiz.html` |
| 2 — Train | 11–20 | SageMaker train/tune/eval, DL basics | Hands-on Studio lab · D2 quiz |
| 3 — Bedrock & AI | 21–25 | Bedrock GenAI apps | `08-supplemental-topics.md` · AIF notes if weak on managed AI |
| 4 — Deploy/MLOps | 26–32 | DevOps products, SageMaker MLOps | Pipelines lab · D3 quiz |
| 5 — Ops/Security | 33–38 | Security, governance, SM compliance | D4 quiz · `06` cheat sheet draft |
| 6 — Practice exams | 39–45 | Review weak Notion sections only | **Tutorials Dojo** or Skill Builder · `quiz.html` exam mode ≥85% |

**Author’s practice exam scores (Tutorials Dojo, timed):** 82% then 76% before passing — use as a sanity check, not a guarantee.

---

## Video courses Notion is based on

| Course | Use if |
|--------|--------|
| **Stephane Maarek + Frank Kane** (Udemy MLA-C01) | You want video walkthroughs (~95% of Notion content source) |
| **Adrian Cantrill SAA** | VPC/IAM gaps only |

Paid courses are optional if you use Notion + this repo + Skill Builder official questions.

---

## What Notion adds vs this repo

| Notion strengths | Repo strengths |
|------------------|----------------|
| Deep narrative, lecture references, diagrams | **Timed quiz**, 120 exam-style MCQs |
| ~600 paid Anki cards (Ko-fi) | **221 free** Anki cards in `04-flashcards-anki.txt` |
| Reorganized study order (v2/v3) | Official domain weights, April 2025 guide alignment |
| Pitfall callouts in-page | `06` last-24h cram sheet |

**Use both:** Notion for learning · Repo for **testing**.

---

## Author resources (optional paid)

- [MLA-C01 PDF export](https://ko-fi.com/s/5b14415ab4) — offline Notion
- [MLA-C01 Anki deck ~600 cards](https://ko-fi.com/s/62c570b54f) — SRS review
- [Free AIF-C01 Anki deck](https://ankiweb.net/shared/info/73981918) — managed AI services

---

## Legend from Notion (apply while studying)

When reading Notion, pay extra attention to blocks marked as:

- **Core concept** — likely exam scenarios  
- **Beware / pitfalls** — common distractors (e.g. async vs batch, Feature Store online vs offline)  
- **Ideas / examples** — helps disambiguate similar services  

Map pitfalls to `02-domain-breakdown.md` “Traps” sections.

---

## Integrity note

- Notion notes are **free to read**; respect the author’s request not to bulk-duplicate the Notion workspace.  
- Do **not** substitute exam dumps (FreeCram, ExamTopics, etc.) for Notion or official practice — Greciano explicitly warns against dumps.  
- This repo adds **original** practice questions and summaries — not a copy of Notion text.
