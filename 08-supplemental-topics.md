# Supplemental MLA-C01 Topics (Notion v3 alignment)

Exam-focused additions commonly emphasized in community study guides (including [Greciano’s Notion TOC](https://psychedelic-cuticle-e74.notion.site/AWS-Machine-Learning-Engineer-Associate-MLA-C01-19686c7395e780e1bab0eac37d0401a0)) but light in our original notes.

---

## Amazon Bedrock (GenAI on exam)

| Concept | Exam takeaway |
|---------|----------------|
| **InvokeModel** | IAM permission for inference on foundation / custom models |
| **Knowledge Bases** | RAG: embed documents, retrieve context, augment prompts |
| **Agents** | Tool use + orchestration for multi-step GenAI apps |
| **Guardrails** | Filter harmful content / PII in GenAI responses |
| **Fine-tuning / Continued pre-training** | Customize FMs with your data (vs training from scratch on SageMaker) |
| **Titan models** | AWS FM family (text, image gen, embeddings) |
| **When to pick Bedrock** | GenAI API, minimal ML ops, FM access — vs custom SageMaker training |

**IAM pattern (image gen + SQS worker):** `bedrock:InvokeModel` on model ARN + `sqs:ReceiveMessage` + `sqs:DeleteMessage` on queue.

**RAG alternatives on exam:**

| Need | Often-correct |
|------|----------------|
| Semantic search over docs already in S3 | **Amazon Kendra** connector or Bedrock Knowledge Base |
| Custom vector DB you manage | OpenSearch + embeddings (more ops) |
| SQL on Parquet only | Athena — not semantic search |

---

## SageMaker Studio & Domain (MLOps setup)

| Piece | Purpose |
|-------|---------|
| **SageMaker Domain** | Org-wide Studio environment, SSO, shared settings |
| **User profiles** | Per-data-scientist isolation within Domain |
| **Execution roles** | IAM role Studio/notebooks/jobs assume |
| **VPC-only Domain** | No direct internet; interface endpoints for S3, ECR, etc. |

Exam angle: **least privilege execution role**, Domain in **VPC**, not “open public notebook.”

---

## Training job compliance & metadata

Some scenarios ask about **limiting metadata collection** from training jobs:

- Use official **opt-out of metadata tracking** when submitting training jobs (compliance scenarios).
- Do not confuse with: KMS encryption (protects data), private subnet (network), Nitro (platform).

---

## Data ingestion depth

| Service | Differentiator |
|---------|----------------|
| **Glue + Crawler** | Discover schema → **Glue Data Catalog** |
| **Glue ETL** | Serverless Spark transforms |
| **MSK Serverless** | Kafka-compatible streaming, **no cluster sizing**, open-source Kafka apps |
| **MSK Provisioned** | You manage capacity/brokers |
| **Kinesis Data Streams** | Custom consumers, shard scaling |
| **Firehose** | Managed delivery to S3/Redshift/OpenSearch |
| **FSx for ONTAP** | Mount **POSIX** shared storage to training (high-throughput file access) |
| **Mountpoint for S3** | POSIX-like access to S3 (different from FSx ONTAP scenarios) |

**Glue vs Athena:** Glue runs ETL and catalogs; Athena **queries** cataloged S3 data with SQL.

---

## Deep learning — exam-level only (not MLS depth)

| Topic | What to know |
|-------|----------------|
| **Overfitting** | High train / low val → regularization (L1/L2), dropout, more data, early stopping |
| **Vanishing gradients** | **Debugger** rules; tune LR/architecture |
| **Dropout** | Reduces NN overfitting — **do not remove** dropout to fix overfitting (exam trap) |
| **L1 vs L2** | L1 → sparsity (feature elimination); L2 → smaller weights |
| **Epochs** | Too many epochs without early stopping → overfitting |

You will **not** derive backprop; you **will** pick AWS tools and regularization strategies.

---

## Matching inference workloads (high-frequency pattern)

| Workload | Best fit |
|----------|----------|
| Low-latency flight status / live API | **Real-time** endpoint + auto scaling |
| Seasonal marketing spikes | **Serverless** inference |
| Quarterly bulk reports | **Batch Transform** |
| Large payload, minutes of processing, queue | **Async** inference |

---

## MLOps / CI/CD triggers

Typical **correct pipeline order:**

1. **S3 event notification** → invokes CodePipeline (or Lambda → Pipeline)  
2. SageMaker **retrains** on new data  
3. **Deploy** to endpoint or register + approve in **Model Registry** then deploy  

**Not** S3 Lifecycle as pipeline trigger for new uploads.

---

## Governance & management

| Service | Use |
|---------|------|
| **Lake Formation** | Fine-grained data lake permissions |
| **CloudTrail** | Who called `CreateTrainingJob`, `CreateEndpoint`, etc. |
| **AWS Config** | Resource configuration compliance rules |
| **Organizations + SCPs** | Account guardrails |
| **Resource tags** | Cost allocation in Cost Explorer |

---

## ML best practices (scenario triggers)

| Symptom | Likely answer direction |
|---------|-------------------------|
| Class imbalance | Stratified split, resampling, right metrics (F1 not accuracy) |
| Need keywords from text, least ops | **Comprehend** key phrases / custom NER |
| 6TB data on FSx ONTAP in same VPC as SM | **Mount** FSx to training instance |
| Complex multi-hour ETL + NLP on 5TB mixed files | **SageMaker Pipelines** (+ Processing steps), not Lambda-only |
| Model too large for edge | **Neo** compile |
| Spiky inference cost | Serverless or auto scaling |
| Drift after campaign changes user mix | Model Monitor → investigate → **retrain pipeline** |

---

## Study checklist (after reading Notion section)

- [ ] Can pick Bedrock vs SageMaker custom vs managed AI (Comprehend/Rekognition) in one sentence each  
- [ ] Can match four inference types to scenario  
- [ ] Know Glue catalog vs Athena vs DataBrew  
- [ ] Know Model Monitor needs baseline  
- [ ] Can sketch CI/CD: S3 → Pipeline → Registry/Endpoint  
- [ ] Score ≥85% on `quiz.html` exam mode (120 questions if using full bank)
