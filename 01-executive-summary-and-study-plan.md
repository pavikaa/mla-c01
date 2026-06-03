# AWS MLA-C01 — Executive Summary & 80/20 Study Plan

**Last updated:** June 2026 (cross-referenced with [official exam guide](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf), April 2025 English exam update, and 2025–2026 candidate reports.)

> **Official vs community:** Domain weights, question counts (50 scored + 15 unscored = 65 total), 130 minutes, pass 720 — **official**. “60–80% SageMaker,” “easier than MLS,” “Tutorials Dojo essential” — **community consensus** (treat as strong signal, not guarantee).

---

## 1. Executive Summary

### Exam facts (official)

| Item | Value |
|------|--------|
| Code | MLA-C01 |
| Level | Associate (MLOps / production ML) |
| Questions | 65 total (**50 scored**, 15 unscored pilot) |
| Time | **130 minutes** (~2 min/question) |
| Pass score | **720** / 1000 (compensatory — no per-domain minimum) |
| Cost | $150 USD |
| Formats | Multiple choice, multiple response, **ordering**, **matching**, **case study** (MLA-C01 was among first exams with new types) |
| Experience | ~1 year SageMaker + related AWS; ~1 year ML engineering–adjacent role |
| Validity | 3 years |
| April 2025 update | English exam skills list refreshed — use post–April 2025 objectives on [AWS certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) |

### Estimated study time (by experience)

| Profile | Hours | Calendar (2h/day) |
|---------|-------|-------------------|
| Strong SageMaker + MLOps on AWS | **40–60** | 3–4 weeks |
| Some AWS + some ML, not production MLOps | **60–90** | 4–6 weeks |
| New to AWS ML / mostly theory | **90–120+** | 6–10 weeks |

**Community shortcut (working full-time):** Many pass in **2–4 weeks** with Tutorials Dojo + targeted SageMaker labs if they already use AWS daily; **4–8 weeks** is the safer default.

### Most efficient path to pass

1. Read **official exam guide PDF** once (2–3h) — map gaps only.
2. **Practice exams first as diagnostics** (Tutorials Dojo or Skill Builder official) — don’t marathon video courses upfront.
3. **Deep-dive weak domains** via cheat sheet + hands-on SageMaker Studio (Feature Store, Pipelines, endpoints, Model Monitor, Clarify).
4. **4+ timed 65-question runs** at **≥80–85%** before booking; one **official practice exam** if subscribed.
5. Day before: service short names list (in-exam Help), endpoint types, monitor baselines, IAM/VPC patterns.

### Highest ROI resources

| Priority | Resource | Why |
|----------|----------|-----|
| 1 | [Official Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf) | Source of truth for domains, in/out of scope |
| 2 | **Tutorials Dojo** practice exams + explanations | Most cited for realistic scenario wording |
| 3 | **AWS Skill Builder** Exam Prep Plan (free question set + pretest; paid enhanced + official practice exam) | Aligns to current blueprint |
| 4 | **[Greciano MLA-C01 Notion notes](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0)** (free v3) + `07-notion-study-crosswalk.md` | Deep study; author passed Jan 2025; ~45-day path |
| 5 | **Hands-on:** SageMaker Pipelines, Model Registry, Model Monitor, deployment modes | Exam is operational, not math-heavy |
| 6 | Stephane Maarek + Kane Udemy (optional) | Matches Notion source material; video if you want lectures |

### Topics = most exam questions

| Rank | Topic cluster | ~Exam share |
|------|----------------|-------------|
| 1 | **Amazon SageMaker** (Studio, training, tuning, registry, endpoints) | **50–70%** of scenarios (community) |
| 2 | Data prep: S3, Glue/DataBrew, Wrangler, Feature Store, formats | Domain 1 **28%** |
| 3 | Model Monitor, Clarify, drift, A/B, retraining triggers | Domain 4 **24%** |
| 4 | Endpoint types, auto scaling, Neo, batch vs real-time vs async | Domain 3 **22%** |
| 5 | CI/CD: Pipelines, CodePipeline, CodeBuild, EventBridge | Domain 3 |
| 6 | IAM, VPC, encryption, least privilege for ML artifacts | Domain 4 |
| 7 | Cost: Spot, Savings Plans, Inference Recommender, rightsizing | Domain 4 |
| 8 | When to use **AI services** (Rekognition, Comprehend, Bedrock, etc.) vs custom SageMaker | Domain 2 |

### Safe to deprioritize (official out-of-scope / low yield)

- Full solution **architecture** design (high-level “choose the platform” only)
- **Deep NLP + CV theory** (use managed AI services instead)
- **Model quantization** impact analysis
- Out-of-scope services: IoT suite, Chime, Connect, DeepRacer, Monitron, Panorama, App Runner, Lightsail, etc. (see exam guide appendix)
- **MLS-C01** deep math / exhaustive algorithm derivations (MLS retired; MLA is MLOps)
- Memorizing every SageMaker **built-in algorithm** hyperparameter — know **when** to pick XGBoost/Linear Learner/BlazingText/Image Classification at a decision level
- Long Udemy courses cover-to-cover without practice exams

### Outdated materials warning

- Any content using **170 min / 85 questions** for MLA-C01 (that was **MLS-C01** or blog errors)
- Pre–**April 2025** skill lists on third-party sites
- **MLS-C01** courses as primary prep (different exam; retired)
- Blog posts with wrong domain splits (e.g. “Feature Engineering 20%” only) — use official **28/26/22/24**

---

## 2. Resource ranking table

| Resource | Cost | Time | Exam coverage | Difficulty | Overall value | Priority |
|----------|------|------|---------------|------------|---------------|----------|
| Official Exam Guide + AWS docs | Free | 3–5h | 100% blueprint | — | ★★★★★ | **P0** |
| AWS Skill Builder Exam Prep Plan | Free tier + sub ~$29/mo | 15–40h | High (official) | Easy–Med | ★★★★☆ | **P0–P1** |
| Tutorials Dojo Practice Exams | ~$15–20 | 20–30h | Very high | Hard vs exam | ★★★★★ | **P0** |
| Tutorials Dojo Study Guide eBook | ~$10–15 | 10–15h | High | Med | ★★★★☆ | P1 |
| Stephane Maarek + Frank Kane Udemy | ~$15–20 (sale) | 25–40h | High | Med | ★★★☆☆ | P2 (skip if experienced) |
| AWS Official Practice Exam (Skill Builder) | Sub / ~$20 | 3h | High | Close | ★★★★☆ | P1 before exam |
| Whizlabs MLA-C01 | ~$15 | 10–15h | Medium | Med | ★★★☆☆ | P2 supplement |
| Nikolai Schuler practice tests | ~$15 | 15h | Medium–High | Med | ★★★☆☆ | P2 |
| ExamTopics (free) | Free | 5–10h | Medium | Variable | ★★☆☆☆ | P3 — verify answers |
| A Cloud Guru / Pluralsight paths | Subscription | 30–50h | Medium | Easy | ★★★☆☆ | P2 if employer pays |
| Coursera AWS ML | Subscription | 40h+ | Low–Med for MLA | Easy | ★★☆☆☆ | Skip for exam-only |
| YouTube (free summaries) | Free | 5–10h | Spotty | Easy | ★★☆☆☆ | P3 review only |
| Maarek course practice tests only | Bundled | 8h | Medium | Med | ★★★☆☆ | After TD |

---

## 3. Exam domain breakdown (summary)

See **02-domain-breakdown.md** for full task-level detail.

| Domain | Weight | Difficulty (1–10) | Highest-yield subtopics |
|--------|--------|-------------------|-------------------------|
| 1 Data Preparation | **28%** | 7 | Parquet/ORC, Glue/DataBrew, Feature Store, bias (CI/DPL), Ground Truth |
| 2 Model Development | **26%** | 7 | Built-in algos vs JumpStart/Bedrock, AMT, Debugger, Clarify metrics, Registry |
| 3 Deployment & Orchestration | **22%** | 8 | Endpoint types, multi-model, Pipelines, CodePipeline, blue/green/canary |
| 4 Monitoring, Security, Cost | **24%** | 8 | Model Monitor baselines, drift, IAM/VPC, Cost Explorer, Inference Recommender |

**Question style patterns:** “Company needs lowest latency / lowest cost / least ops” → one best AWS service; ordering CI/CD or pipeline steps; matching metric → use case; case study with 2–3 questions on same architecture.

**Common traps:** Confusing **async** vs **batch** inference; **serverless** endpoint limits; **Feature Store** online vs offline; **Model Monitor** baseline requirements; using **custom training** when **managed AI** fits; **SageMaker Role** vs bucket policy; **Spot** for training but not always for critical real-time inference.

---

## 4. 80/20 study plans

### Milestones (all tracks)

| Checkpoint | Target |
|------------|--------|
| Day 0 | Read exam guide; 1 untimed practice set (baseline) |
| Mid | ≥70% on domain-section quizzes |
| Pre-book | **≥80–85%** on two consecutive timed 65-Q full tests |
| Final | Official practice exam or TD “Final Test” ≥80% |
| Exam week | Cheat sheet only + 1 light practice set |

### 1-week crash (50–60h total — only if strong AWS background)

| Day | Focus | Hours |
|-----|--------|-------|
| Mon | Exam guide + Domain 1 notes + S3/Glue/Feature Store lab | 8 |
| Tue | Domain 2 + training/tuning/Clarify lab | 8 |
| Wed | Domain 3 + endpoints + Pipelines lab | 8 |
| Thu | Domain 4 + Model Monitor + IAM/VPC | 8 |
| Fri | TD Practice Test 1 (timed) + review misses | 8 |
| Sat | TD Practice Test 2 + weak domains | 8 |
| Sun | TD Final Test + cheat sheet | 6 |

### 2-week plan (recommended minimum for most)

| Week | Mon–Fri (2h/day) | Weekend (6h/day) |
|------|------------------|------------------|
| 1 | Domains 1–2 + Skill Builder pretest | Hands-on SageMaker + Practice Test 1 |
| 2 | Domains 3–4 + CI/CD lab | Tests 2–3 timed + review + book exam |

### 4-week plan (safest for &lt;1 year SageMaker)

| Week | Focus |
|------|--------|
| 1 | Domain 1 + data labs (Glue, Wrangler, Feature Store) |
| 2 | Domain 2 + training, AMT, Registry, Clarify |
| 3 | Domain 3 + deployments, Pipelines, CodePipeline |
| 4 | Domain 4 + practice exams + official practice test |

**Daily schedule (working professional, 2h/day):** 45m reading notes → 45m hands-on/lab → 30m flashcards → weekend block for full practice test.

---

## 5. Pass probability analysis

| Preparation level | Estimated pass probability |
|-------------------|---------------------------|
| Exam guide only | 20–30% |
| Video course only, no practice tests | 35–45% |
| TD/official practice ≥75% average | 60–70% |
| TD/official practice **≥85%** + weak-area review + some hands-on | **80–90%** |
| ≥85% + 1 year SageMaker production experience | **90%+** |

### Minimum set for ~80%+ pass probability

1. Official exam guide (full read)
2. **One** high-quality question bank (**Tutorials Dojo** OR Skill Builder enhanced official practice exam)
3. **Four** timed 65-question simulations with answer review
4. **~8–12 hours** hands-on: Feature Store, one Pipeline, one endpoint type, Model Monitor baseline
5. **06-cheat-sheet-last-24h.md** in last 48 hours

### Low-value activities to skip

- Rewatching entire Udemy course after 80% practice scores
- Deep learning math / deriving backprop
- Studying out-of-scope AWS services “just in case”
- ExamTopics without cross-checking explanations
- Building novel ML models from scratch unrelated to SageMaker operations

---

## File index

| File | Contents |
|------|----------|
| `02-domain-breakdown.md` | Per-domain deep dive |
| `03-high-yield-notes.md` | Exam-focused notes |
| `04-flashcards-anki.txt` | 200+ Anki cards |
| `05-practice-questions.md` | 100 questions + explanations |
| `06-cheat-sheet-last-24h.md` | 5-page cram sheet |
