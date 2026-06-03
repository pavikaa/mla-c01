# MLA-C01 Domain Breakdown (Official Task Alignment)

Sources: [AWS MLA-C01 Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf), [AWS certification docs](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html).

---

## Domain 1: Data Preparation for ML — **28%**

### Key concepts
- Data formats: CSV, JSON, Parquet, ORC, Avro, RecordIO — **columnar (Parquet/ORC)** for analytics/ML efficiency
- Ingestion: S3, EFS, FSx, RDS, DynamoDB, Kinesis, Flink, Kafka
- Transformation: Glue ETL, Glue DataBrew (visual), EMR Spark, Lambda, Data Wrangler
- Feature engineering: scaling, normalization, binning, encoding (one-hot, label), Feature Store (online/offline)
- Integrity: Glue Data Quality, class imbalance (CI), DPL bias metrics, Clarify pre-training bias
- Labeling: Ground Truth, Mechanical Turk, A2I for human review loops

### AWS services (exam-heavy)
S3, Glue, DataBrew, EMR, Athena, Kinesis, Firehose, Lake Formation, SageMaker Data Wrangler, Feature Store, Ground Truth, Clarify (pre-training), Macie (PII), KMS

### Typical question styles
- “Best format for repeated ML training on large tabular data?” → **Parquet**
- “Centralize features for training and low-latency serving?” → **Feature Store**
- “Visual prep without code?” → **DataBrew**
- “Detect label proportion bias before training?” → **Clarify / DPL**
- Ordering: ETL steps for ingestion → validate → feature → split

### Traps & distractors
- **Athena** vs **Glue** — Athena queries; Glue catalogs/ETL
- **Kinesis Data Streams** vs **Firehose** — custom consumers vs managed delivery to S3/Redshift
- **Feature Store**: online store for inference vs offline for training
- **Over-sampling** vs **synthetic data** for class imbalance — scenario-dependent
- **EFS** vs **FSx** for training input — exam may test “shared POSIX for multi-node training” → EFS/FSx

### Difficulty: **7/10**

---

## Domain 2: ML Model Development — **26%**

### Key concepts
- Algorithm selection: built-in algos (XGBoost, Linear Learner, etc.) vs JumpStart vs **Bedrock** foundation models
- Managed AI: Rekognition, Comprehend, Translate, Transcribe, Textract, Personalize — **when not to build custom**
- Training: script mode, distributed training, Spot training, Debugger (convergence), Experiments
- Hyperparameters: AMT (Bayesian), random search, early stopping, regularization (L1/L2, dropout)
- Evaluation: precision/recall/F1, RMSE, ROC/AUC, confusion matrix, shadow variants
- Responsible AI: Clarify post-training bias, SHAP, PDP
- Model Registry: versioning, approval workflow

### AWS services
SageMaker (core), JumpStart, Bedrock, Clarify, Debugger, Model Registry, Experiments, Autopilot (awareness), built-in algorithms, CodeGuru (code quality)

### Typical question styles
- “Pre-trained FM for text generation with minimal ML ops?” → **Bedrock**
- “Image classification with limited ML team?” → **Rekognition** or JumpStart
- “Systematic HPO at scale?” → **SageMaker AMT**
- “Model not converging?” → **Debugger**
- Multi-select: metrics for **imbalanced classification** → precision, recall, F1 (not accuracy alone)

### Traps
- **Autopilot** vs **AMT** — AutoML end-to-end vs tune your own estimator
- **Ensembling** in training vs **multi-model endpoint** at inference
- **Fine-tuning** JumpStart/Bedrock vs training from scratch
- **Shadow deployment** for safe comparison vs A/B on traffic split

### Difficulty: **7/10**

---

## Domain 3: Deployment and Orchestration — **22%**

### Key concepts
- Endpoint types: real-time, **serverless**, **async** (large payloads/queuing), **batch transform**, multi-model, multi-container
- Compute: CPU vs GPU instance families, Inferentia/Trainium awareness, Neo for edge
- Scaling: auto scaling policies (invocations, latency, CPU), Spot for **training** (cost)
- Containers: BYOC, ECR, ECS/EKS as deployment targets
- IaC: CloudFormation, CDK for ML infrastructure
- CI/CD: CodePipeline, CodeBuild, CodeDeploy, GitFlow, blue/green, canary, linear
- Orchestration: **SageMaker Pipelines** (primary), MWAA/Airflow, Step Functions, EventBridge

### AWS services
SageMaker endpoints/Pipelines/Inference Recommender/Neo, ECR, ECS, EKS, Lambda (limited inference patterns), CodePipeline family, CloudFormation, CDK, EventBridge, Step Functions, MWAA

### Typical question styles
- “Bursty traffic, no always-on instance management?” → **serverless inference**
- “Large input files, queue, 15+ min inference?” → **async endpoint**
- “Score millions of records offline?” → **batch transform**
- “Automate retrain on schedule/data drift?” → **Pipeline + EventBridge / Monitor trigger**
- Matching: deployment strategy → use case

### Traps
- **Real-time** vs **async** — latency SLA vs payload size/queuing
- **Serverless** concurrency/memory limits vs **real-time** Provisioned Throughput
- **Multi-model endpoint** vs separate endpoints — cost/latency tradeoff
- **CodeDeploy** blue/green for **app** vs SageMaker **production variants** for models
- **Lambda** for heavy GPU inference — usually wrong answer

### Difficulty: **8/10**

---

## Domain 4: Monitoring, Maintenance, Security — **24%**

### Key concepts
- Model Monitor: data quality, model quality, bias drift baselines (need **baseline** from training or prior production)
- Drift: data drift vs concept drift vs prediction bias
- A/B and shadow variants for production comparison
- Observability: CloudWatch metrics/alarms/logs, X-Ray, CloudTrail for audit/retrain triggers
- Cost: Cost Explorer, Budgets, Trusted Advisor, tags, Spot/RI/Savings Plans, Inference Recommender, Compute Optimizer
- Security: IAM roles for SageMaker, VPC endpoints, security groups, KMS encryption, least privilege, secrets in Secrets Manager

### AWS services
Model Monitor, Clarify, CloudWatch, CloudTrail, X-Ray, EventBridge, QuickSight dashboards, Cost Explorer, Budgets, Trusted Advisor, IAM, KMS, Macie, VPC

### Typical question styles
- “Detect feature distribution shift in production?” → **Model Monitor – data quality**
- “Schedule retrain when drift exceeds threshold?” → **EventBridge + Pipeline**
- “Least privilege for notebook to S3 model artifacts?” → **IAM role** scoped to bucket prefix
- “Right-size inference instances?” → **Inference Recommender**

### Traps
- **Model Monitor** requires baseline — can’t skip setup
- **Clarify** bias vs **Model Monitor** bias drift — related but different lifecycle stages
- **CloudTrail** for **who changed what** vs **CloudWatch** for metrics/logs
- **Encryption at rest** (S3/KMS) vs **in transit** (TLS/VPC)
- **Reserved Instances** for steady inference vs **Spot** for fault-tolerant training

### Difficulty: **8/10**

---

## Cross-domain “super topics” (appear in multiple domains)

1. **SageMaker Pipelines** — data → train → evaluate → register → deploy  
2. **Model Registry** — approved models only to production  
3. **Feature Store** — train/serve consistency  
4. **Endpoint + auto scaling + VPC** — production triad  
5. **Cost vs latency vs availability** — every scenario question  
