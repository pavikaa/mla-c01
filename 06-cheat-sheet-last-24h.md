# MLA-C01 — Last 24 Hours Cheat Sheet (~5 pages printed)

**Exam:** 65 Q, 130 min, pass **720**, 50 scored. Formats: MC, multi-select, ordering, matching, case study.

---

## Page 1 — Exam map & decision framework

### Domain weights
| D1 Data | D2 Model | D3 Deploy | D4 Ops |
|---------|----------|-----------|--------|
| 28% | 26% | 22% | 24% |

### Scenario decoder (read stem first)
1. **Constraint keyword** → lowest **cost** | **latency** | **ops** | **compliance**
2. **Lifecycle** → ingest | train | deploy | monitor
3. **Managed vs custom** → “no ML team” / “API” → Rekognition, Comprehend, Bedrock, etc.
4. **Batch vs real-time** → offline millions = Batch Transform; ms SLA = real-time

### Out of scope (don’t pick)
Full enterprise architecture, deep multi-domain NLP+CV theory, **quantization analysis**, IoT/Chime/DeepRacer/Monitron

---

## Page 2 — SageMaker endpoints & deployment

| Pattern | Service/mode |
|---------|----------------|
| Always-on, ms latency | Real-time endpoint + auto scaling |
| Sporadic traffic | Serverless inference |
| Large files, minutes-hours | Async endpoint + S3 in/out |
| Bulk historical scoring | Batch Transform |
| Multiple models, one GPU | Multi-model endpoint |
| Edge device | Neo compiled model |
| Right-size instances | Inference Recommender |

**CI/CD ML:** SageMaker **Pipelines** (first choice) + CodePipeline trigger + Model Registry approval

**Traffic shifting:** Production variants (A/B), shadow (no user impact), canary/blue-green (with CodeDeploy concepts)

---

## Page 3 — Data & training

| Topic | Pick |
|-------|------|
| Columnar ML data on S3 | Parquet / ORC |
| Visual ETL | Glue DataBrew |
| Code ETL at scale | Glue / EMR Spark |
| Feature reuse train+serve | Feature Store (online + offline) |
| Visual feature prep | Data Wrangler |
| Labeling at scale | Ground Truth (+ MTurk/A2I) |
| Pre-training bias | Clarify (CI, DPL) |
| HPO | SageMaker AMT |
| Non-convergence | Debugger |
| Version + approve models | Model Registry |
| FM with minimal ops | Bedrock / JumpStart |

**Imbalanced classes:** stratified split, resampling, synthetic data — not “accuracy alone”

---

## Page 4 — Monitoring, security, cost

### Model Monitor (needs baseline!)
- **Data quality** — feature drift  
- **Model quality** — output/performance drift  
- **Bias drift** — fairness metrics over time  

**React:** CloudWatch alarm → EventBridge → Pipeline retrain

### Security quick picks
- Least privilege → **IAM role** per notebook/job/endpoint  
- Private networking → **VPC** + SG + interface endpoints  
- Audit API calls → **CloudTrail**  
- Encrypt data → **KMS** + S3 bucket policies  

### Cost quick picks
- Training $ → **Spot** + checkpointing  
- Steady inference → right-size + **Savings Plans/RI**  
- Spiky inference → **serverless** or aggressive auto scaling  
- Analyze spend → **Cost Explorer** + **tags** + Budgets  

---

## Page 5 — Metrics, services, checklist

### Metrics
- **Imbalanced classification:** F1, precision, recall (NOT accuracy alone)  
- **Regression:** RMSE, MAE  
- **Ranking/binary:** AUC-ROC  

### Managed AI shortcuts
| Need | Service |
|------|---------|
| Image | Rekognition |
| Text NLP | Comprehend |
| Speech | Transcribe |
| Translate | Translate |
| Docs | Textract |
| Recommendations | Personalize |
| GenAI/FM | Bedrock |

### Common confusions
| A | B |
|---|---|
| Athena | Glue ETL |
| Kinesis Streams | Firehose |
| Async endpoint | Batch Transform |
| Autopilot | AMT |
| CloudWatch | CloudTrail |
| Feature Store online | offline store |
| Shadow variant | Production A/B traffic |

### Last-minute checklist
- [ ] Skim official **in-scope** service list (appendix)  
- [ ] Review **service short names** (exam Help button)  
- [ ] One timed 65-Q practice (optional)  
- [ ] Sleep — compensatory scoring, no per-domain pass required  
- [ ] ID ready for Pearson VUE (passport/driver license)  
- [ ] Flag hard questions, revisit — ~2 min/Q budget  

### Exam day tactics
- Read **LAST sentence** of scenario (what they ask)  
- Multi-select: select **ALL** correct — partial = wrong  
- Ordering: ML pipeline logical order (ingest → validate → feature → train → register → deploy → monitor)  
- Eliminate 2 distractors first, compare remaining on **AWS best practice** not “could work”  

---

*Good luck. Trust practice scores ≥85% and miss-rule review over cramming new topics.*
