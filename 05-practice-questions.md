# MLA-C01 Practice Questions (100)
**Instructions:** Timed 130 min for full set. Review every wrong answer.
---
## Question 1 [D1] — Single
A fintech stores 5 TB of transaction data in S3 as CSV. Training jobs read the same columns repeatedly. What is the MOST cost-effective format change to improve training I/O?
- A) Convert to JSON lines
- B) Convert to Apache Parquet
- C) Store as Avro only in Kinesis
- D) Duplicate data in DynamoDB

**Correct answer(s):** B
**Explanation:** Parquet is columnar and compressed, reducing scan cost and SageMaker training time for tabular ML.
**Why others are wrong:**
- A: JSON is row-oriented and verbose for analytics.
- C: Avro is valid but Parquet dominates S3 analytics ML.
- D: DynamoDB wrong for bulk training scans.

---
## Question 2 [D1] — Multi
A company needs low-latency feature retrieval at inference AND batch features for nightly retraining. Which TWO capabilities should they implement? (Select TWO)
- A) SageMaker Feature Store online store for real-time inference lookups
- B) Amazon Athena as the sole feature serving layer
- C) Amazon Kinesis Data Firehose to replace feature storage
- D) SageMaker Feature Store offline store for batch training pipelines
- E) AWS Glue DataBrew only, with no feature persistence layer

**Correct answer(s):** A, D
**Explanation:** Feature Store online + offline stores give consistent features for inference and batch retraining—the canonical exam pattern.
**Why others are wrong:**
- B: Athena queries data but is not a feature serving layer.
- C: Firehose ingests streams, not feature management.
- E: DataBrew prepares data but not serve features at inference.

---
## Question 3 [D1] — Single
A team must visually profile, clean, and transform data without writing Spark code. Which service should they choose?
- A) AWS Glue DataBrew
- B) AWS Batch
- C) Amazon EMR only
- D) AWS Lambda exclusively

**Correct answer(s):** A
**Explanation:** DataBrew is the visual data preparation service.
**Why others are wrong:**
- B: Batch runs jobs but no visual prep.
- C: EMR needs Spark coding.
- D: Lambda limited for large transforms.

---
## Question 4 [D1] — Single
Before training a credit model, engineers must detect if one demographic has disproportionately fewer positive labels. Which metric/tool pair is appropriate?
- A) RMSE with Debugger
- B) Difference in Proportions of Labels (DPL) with SageMaker Clarify
- C) ROC-AUC with Model Monitor
- D) RMSE with Ground Truth

**Correct answer(s):** B
**Explanation:** DPL is a pre-training bias metric; Clarify detects label proportion bias.
**Why others are wrong:**
- A: RMSE is regression metric.
- C: Model Monitor is post-deployment.
- D: Ground Truth labels data.

---
## Question 5 [D1] — Single
Real-time clickstream events must be ingested for feature computation with custom consumers. Which service?
- A) Kinesis Data Firehose
- B) Kinesis Data Streams
- C) AWS DataSync
- D) Amazon SQS only

**Correct answer(s):** B
**Explanation:** Streams allows custom real-time consumers; Firehose is fully managed delivery.
**Why others are wrong:**
- A: Firehose not for custom consumer logic.
- C: DataSync is migration.
- D: SQS not primary stream ingest.

---
## Question 6 [D1] — Single
A healthcare company must identify PHI in S3 buckets automatically. Which service?
- A) AWS Macie
- B) Amazon Rekognition
- C) AWS WAF
- D) Amazon GuardDuty

**Correct answer(s):** A
**Explanation:** Macie discovers sensitive data including PII/PHI patterns in S3.
**Why others are wrong:**
- B: Rekognition is vision.
- C: WAF protects web apps.
- D: GuardDuty is threat detection.

---
## Question 7 [D1] — Ordering
Order the steps to prepare data for SageMaker training from raw S3 CSV:
- 1) Register features in Feature Store
- 2) Ingest and validate schema
- 3) Split train/validation/test
- 4) Transform and engineer features

**Correct answer(s):** 2, 4, 3, 1
**Explanation:** Ingest/validate → transform → split → optional Feature Store registration for reuse.

---
## Question 8 [D1] — Single
A labeling project needs human annotators with workflow quality control for image bounding boxes. Best choice?
- A) SageMaker Ground Truth
- B) Amazon Polly
- C) Amazon Translate
- D) AWS CloudFormation

**Correct answer(s):** A
**Explanation:** Ground Truth manages labeling workflows at scale.
**Why others are wrong:**
- B: Polly is text-to-speech.
- C: Translate is language.
- D: CloudFormation is IaC.

---
## Question 9 [D1] — Single
Class imbalance causes poor recall on minority class. Which approach is MOST appropriate?
- A) Use accuracy as sole metric
- B) Apply stratified sampling and consider oversampling/SMOTE-class techniques
- C) Remove minority class
- D) Disable validation

**Correct answer(s):** B
**Explanation:** Stratified splits and resampling address imbalance; accuracy alone misleads.
**Why others are wrong:**
- A: Accuracy misleading.
- C: Removes critical class.
- D: Validation required.

---
## Question 10 [D1] — Single
Training data must be mounted with POSIX semantics across multiple training instances. Which storage?
- A) Amazon S3 standard
- B) Amazon EFS
- C) Amazon Glacier
- D) AWS Snowball Edge only

**Correct answer(s):** B
**Explanation:** EFS provides shared POSIX file system for multi-node training.
**Why others are wrong:**
- A: S3 object not POSIX mount.
- C: Glacier archival.
- D: Snowball migration device.

---
## Question 11 [D1] — Single
Glue Data Quality helps primarily with:
- A) Validating rules on datasets in pipelines (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** Validating rules on datasets in pipelines

---
## Question 12 [D1] — Single
Combine batch data from RDS and S3 for ETL at scale:
- A) Option A placeholder
- B) AWS Glue or EMR Spark (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** AWS Glue or EMR Spark

---
## Question 13 [D1] — Single
Encrypt S3 ML artifacts with customer-managed keys:
- A) Option A placeholder
- B) Option B
- C) SSE-KMS (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** SSE-KMS

---
## Question 14 [D1] — Multi
Select TWO for real-time stream ETL to S3:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** Firehose, Managed Flink
**Explanation:** Correct: Kinesis Data Streams and Lambda

---
## Question 15 [D1] — Single
Reduce labeling cost for low-confidence predictions:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Amazon A2I human review loops (CORRECT)

**Correct answer(s):** D
**Explanation:** Amazon A2I human review loops

---
## Question 16 [D2] — Single
Systematic HPO with Bayesian search:
- A) SageMaker Automatic Model Tuning (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** SageMaker Automatic Model Tuning

---
## Question 17 [D2] — Single
Training loss flat but gradients vanishing:
- A) Option A placeholder
- B) SageMaker Debugger (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** SageMaker Debugger

---
## Question 18 [D2] — Single
No ML team; need image label detection API:
- A) Option A placeholder
- B) Option B
- C) Amazon Rekognition (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Amazon Rekognition

---
## Question 19 [D2] — Single
Version models and require approval before prod:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) SageMaker Model Registry (CORRECT)

**Correct answer(s):** D
**Explanation:** SageMaker Model Registry

---
## Question 20 [D2] — Single
Imbalanced fraud detection metric emphasis:
- A) F1, precision, recall (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** F1, precision, recall

---
## Question 21 [D2] — Multi
Select TWO for foundation model text generation minimal ops:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** Bedrock
**Explanation:** Correct: Bedrock

---
## Question 22 [D2] — Single
Compare new model safely without user impact:
- A) Option A placeholder
- B) Shadow production variant (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** Shadow production variant

---
## Question 23 [D2] — Single
Custom PyTorch training on SageMaker:
- A) Option A placeholder
- B) Option B
- C) Script mode with ECR inference container (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Script mode with ECR inference container

---
## Question 24 [D2] — Single
Tabular classification default built-in often:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) XGBoost (CORRECT)

**Correct answer(s):** D
**Explanation:** XGBoost

---
## Question 25 [D2] — Single
Explain feature impact on predictions:
- A) Clarify SHAP (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** Clarify SHAP

---
## Question 26 [D2] — Single
Overfitting remedy:
- A) Option A placeholder
- B) Regularization and more validation data (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** Regularization and more validation data

---
## Question 27 [D2] — Single
Document entity extraction without custom NLP:
- A) Option A placeholder
- B) Option B
- C) Amazon Comprehend (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Amazon Comprehend

---
## Question 28 [D2] — Single
Autopilot vs AMT:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Autopilot AutoML end-to-end; AMT tunes your estimator (CORRECT)

**Correct answer(s):** D
**Explanation:** Autopilot AutoML end-to-end; AMT tunes your estimator

---
## Question 29 [D3] — Single
Intermittent predictions no instance management:
- A) Serverless inference (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** Serverless inference

---
## Question 30 [D3] — Single
100GB images queued long inference:
- A) Option A placeholder
- B) Async endpoint (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** Async endpoint

---
## Question 31 [D3] — Single
Score 10M records offline:
- A) Option A placeholder
- B) Option B
- C) Batch Transform (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Batch Transform

---
## Question 32 [D3] — Single
Native ML CI/CD DAG on SageMaker:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) SageMaker Pipelines (CORRECT)

**Correct answer(s):** D
**Explanation:** SageMaker Pipelines

---
## Question 33 [D3] — Single
Gradual production traffic to new model:
- A) Canary deployment (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** Canary deployment

---
## Question 34 [D3] — Multi
Select TWO for container image storage:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** ECR
**Explanation:** Correct: ECR

---
## Question 35 [D3] — Single
Edge device optimized model:
- A) Option A placeholder
- B) SageMaker Neo (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** SageMaker Neo

---
## Question 36 [D3] — Single
Right-size inference instances:
- A) Option A placeholder
- B) Option B
- C) Inference Recommender (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Inference Recommender

---
## Question 37 [D3] — Single
Multi-model on one GPU endpoint:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Multi-model endpoint (CORRECT)

**Correct answer(s):** D
**Explanation:** Multi-model endpoint

---
## Question 38 [D3] — Single
Trigger pipeline on git commit:
- A) CodePipeline integrated with SageMaker (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** CodePipeline integrated with SageMaker

---
## Question 39 [D3] — Single
Private subnet inference no public internet:
- A) Option A placeholder
- B) VPC config with endpoints (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** VPC config with endpoints

---
## Question 40 [D3] — Single
Orchestrate enterprise Airflow:
- A) Option A placeholder
- B) Option B
- C) Amazon MWAA (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Amazon MWAA

---
## Question 41 [D4] — Single
Feature distribution shift in production:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Model Monitor data quality (CORRECT)

**Correct answer(s):** D
**Explanation:** Model Monitor data quality

---
## Question 42 [D4] — Single
Audit API calls for model deployment:
- A) CloudTrail (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** CloudTrail

---
## Question 43 [D4] — Single
Alert when ML spend exceeds budget:
- A) Option A placeholder
- B) AWS Budgets (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** AWS Budgets

---
## Question 44 [D4] — Single
Least privilege SageMaker access:
- A) Option A placeholder
- B) Option B
- C) IAM role scoped to resources (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** IAM role scoped to resources

---
## Question 45 [D4] — Single
Auto retrain on drift:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) EventBridge + SageMaker Pipeline (CORRECT)

**Correct answer(s):** D
**Explanation:** EventBridge + SageMaker Pipeline

---
## Question 46 [D4] — Single
Production A/B traffic split:
- A) Production variants weights (CORRECT)
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** A
**Explanation:** Production variants weights

---
## Question 47 [D4] — Multi
Select TWO cost optimization for training:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Option D

**Correct answer(s):** Spot
**Explanation:** Correct: Spot with checkpointing

---
## Question 48 [D4] — Single
Inference latency dashboards:
- A) Option A placeholder
- B) CloudWatch metrics and alarms (CORRECT)
- C) Option C
- D) Option D

**Correct answer(s):** B
**Explanation:** CloudWatch metrics and alarms

---
## Question 49 [D4] — Single
Analyze spend by team tag:
- A) Option A placeholder
- B) Option B
- C) Cost Explorer (CORRECT)
- D) Option D

**Correct answer(s):** C
**Explanation:** Cost Explorer

---
## Question 50 [D4] — Single
Model Monitor prerequisite:
- A) Option A placeholder
- B) Option B
- C) Option C
- D) Baseline statistics (CORRECT)

**Correct answer(s):** D
**Explanation:** Baseline statistics

---
## Question 51 [D1] — Single
A startup merges clickstream (Kinesis) and customer profiles (S3 Parquet) daily. Least ops merge at scale?
- A) Incorrect option A
- B) AWS Glue ETL job
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** AWS Glue ETL job
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 52 [D1] — Single
Data scientist needs repeatable visual recipes exported to pipeline.
- A) Incorrect option A
- B) Incorrect option B
- C) SageMaker Data Wrangler
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** SageMaker Data Wrangler
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 53 [D1] — Single
Governed data lake table access across accounts.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) AWS Lake Formation

**Correct answer(s):** D
**Explanation:** AWS Lake Formation
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 54 [D1] — Multi
Select TWO to address selection bias.
- A) Opt1
- B) Opt2
- C) Opt3
- D) Opt4
- E) Opt5

**Correct answer(s):** Collect representative production samples, Stratified split
**Explanation:** Collect representative production samples

---
## Question 55 [D2] — Single
Regression house prices; metric penalizes large errors.
- A) RMSE
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** RMSE
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 56 [D2] — Single
Distributed training wall-clock reduction.
- A) Incorrect option A
- B) SageMaker distributed training jobs
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** SageMaker distributed training jobs
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 57 [D2] — Single
Speech commands to text without custom model.
- A) Incorrect option A
- B) Incorrect option B
- C) Amazon Transcribe
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Amazon Transcribe
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 58 [D2] — Single
Track 50 experiments hyperparameters metrics.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) SageMaker Experiments

**Correct answer(s):** D
**Explanation:** SageMaker Experiments
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 59 [D2] — Single
Early stopping criteria based on validation AUC plateau.
- A) Built into estimator/AMT early stopping
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Built into estimator/AMT early stopping
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 60 [D3] — Single
Steady 50ms p99 latency high QPS.
- A) Incorrect option A
- B) Real-time endpoint with auto scaling
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Real-time endpoint with auto scaling
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 61 [D3] — Single
IaC provision SageMaker Studio domain.
- A) Incorrect option A
- B) Incorrect option B
- C) CloudFormation or CDK
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** CloudFormation or CDK
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 62 [D3] — Single
Blue/green at application layer with EC2.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) CodeDeploy

**Correct answer(s):** D
**Explanation:** CodeDeploy
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 63 [D3] — Single
Schedule weekly retrain Sunday 2am.
- A) EventBridge cron rule to Pipeline
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** EventBridge cron rule to Pipeline
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 64 [D3] — Matching
Match deployment to need: Real-time low latency | Bulk offline | Bursty (Real-time | Bulk | Bursty)
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B, C, A
**Explanation:** Real-time endpoint|Batch Transform|Serverless

---
## Question 65 [D4] — Single
Prediction bias drift across facets.
- A) Incorrect option A
- B) Model Monitor bias drift
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Model Monitor bias drift
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 66 [D4] — Single
Trace microservice inference latency.
- A) Incorrect option A
- B) Incorrect option B
- C) AWS X-Ray
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** AWS X-Ray
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 67 [D4] — Single
Rightsize EC2 training instances from utilization.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) AWS Compute Optimizer

**Correct answer(s):** D
**Explanation:** AWS Compute Optimizer
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 68 [D4] — Single
Encrypt model artifacts at rest S3.
- A) SSE-KMS
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** SSE-KMS
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 69 [D4] — Single
Deny public S3 model bucket access.
- A) Incorrect option A
- B) Bucket policy Block Public Access + IAM
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Bucket policy Block Public Access + IAM
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 70 [D1] — Single
Athena appropriate when?
- A) Incorrect option A
- B) Incorrect option B
- C) Ad-hoc SQL analytics on S3 without loading cluster
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Ad-hoc SQL analytics on S3 without loading cluster
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 71 [D2] — Single
Personalize used for?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Real-time recommendation campaigns

**Correct answer(s):** D
**Explanation:** Real-time recommendation campaigns
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 72 [D2] — Single
Textract used for?
- A) Extract tables/text from PDF scans
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Extract tables/text from PDF scans
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 73 [D3] — Single
Lambda best in ML pipeline for?
- A) Incorrect option A
- B) Lightweight preprocessing trigger
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Lightweight preprocessing trigger
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 74 [D3] — Single
Heavy GPU BERT inference 24/7.
- A) Incorrect option A
- B) Incorrect option B
- C) Real-time GPU endpoint not Lambda
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Real-time GPU endpoint not Lambda
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 75 [D4] — Single
CloudWatch vs CloudTrail for error logs?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) CloudWatch Logs for application logs

**Correct answer(s):** D
**Explanation:** CloudWatch Logs for application logs
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 76 [D1] — Single
Firehose delivers to?
- A) S3, Redshift, OpenSearch destinations
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** S3, Redshift, OpenSearch destinations
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 77 [D2] — Single
Precision low recall high means?
- A) Incorrect option A
- B) Many false positives among predicted positives
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Many false positives among predicted positives
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 78 [D2] — Single
Ensemble stacking improves?
- A) Incorrect option A
- B) Incorrect option B
- C) Predictive performance combining models
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Predictive performance combining models
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 79 [D3] — Single
Pipeline step fails metric <0.8 accuracy.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Conditional step stops promotion

**Correct answer(s):** D
**Explanation:** Conditional step stops promotion
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 80 [D4] — Single
Trusted Advisor helps?
- A) Cost and performance recommendations
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Cost and performance recommendations
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 81 [D1] — Case
Case: Bank ingests daily Parquet to S3, needs GDPR PII scan before Feature Store. First step?
- A) Incorrect option A
- B) Macie scan then transform
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Macie scan then transform

---
## Question 82 [D2] — Case
Case: Startup needs chatbot FM quickly.
- A) Incorrect option A
- B) Incorrect option B
- C) Amazon Bedrock
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Amazon Bedrock

---
## Question 83 [D3] — Case
Case: Mobile app 2x/day batch user churn scores.
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Batch Transform

**Correct answer(s):** D
**Explanation:** Batch Transform

---
## Question 84 [D4] — Case
Case: Model accuracy dropped after marketing campaign changed user mix.
- A) Detect data drift retrain pipeline
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Detect data drift retrain pipeline

---
## Question 85 [D1] — Single
One-hot encoding risk with high cardinality?
- A) Incorrect option A
- B) Sparse high-dimensional features
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Sparse high-dimensional features
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 86 [D2] — Single
L2 regularization primarily prevents?
- A) Incorrect option A
- B) Incorrect option B
- C) Large weights overfitting
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Large weights overfitting
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 87 [D3] — Single
ECR image scan failure blocks deploy because?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Security compliance in CI/CD

**Correct answer(s):** D
**Explanation:** Security compliance in CI/CD
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 88 [D4] — Single
Savings Plans benefit?
- A) Flexible compute savings commitment
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Flexible compute savings commitment
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 89 [D1] — Single
Mechanical Turk integrated via?
- A) Incorrect option A
- B) Ground Truth or custom workforce
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Ground Truth or custom workforce
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 90 [D2] — Single
Heat map used for?
- A) Incorrect option A
- B) Incorrect option B
- C) Visualize confusion matrix patterns
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Visualize confusion matrix patterns
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 91 [D3] — Single
Auto scaling target invocations per instance addresses?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Traffic growth scaling out

**Correct answer(s):** D
**Explanation:** Traffic growth scaling out
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 92 [D4] — Single
QuickSight in ML ops for?
- A) Business dashboards on metrics
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** Business dashboards on metrics
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 93 [D2] — Single
Fine-tune JumpStart when?
- A) Incorrect option A
- B) Limited data similar task pre-trained model exists
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Limited data similar task pre-trained model exists
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 94 [D3] — Single
Step Functions use with?
- A) Incorrect option A
- B) Incorrect option B
- C) Orchestrate Lambda SageMaker jobs
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Orchestrate Lambda SageMaker jobs
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 95 [D4] — Single
KMS with SageMaker?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) Encrypt volumes and S3 artifacts

**Correct answer(s):** D
**Explanation:** Encrypt volumes and S3 artifacts
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 96 [D1] — Single
Provisioned IOPS for?
- A) High-performance EBS training I/O
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** High-performance EBS training I/O
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 97 [D2] — Single
Catastrophic forgetting concern in?
- A) Incorrect option A
- B) Sequential fine-tuning without replay
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** B
**Explanation:** Sequential fine-tuning without replay
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 98 [D3] — Single
GitFlow affects?
- A) Incorrect option A
- B) Incorrect option B
- C) Branch strategy triggering pipelines
- D) Incorrect option D

**Correct answer(s):** C
**Explanation:** Branch strategy triggering pipelines
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
## Question 99 [D4] — Single
Service quota increase needed for?
- A) Incorrect option A
- B) Incorrect option B
- C) Incorrect option C
- D) More concurrent training jobs

**Correct answer(s):** D
**Explanation:** More concurrent training jobs
**Why others are wrong:**
- A: Not the best AWS choice for this scenario.
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.

---
## Question 100 [Cross] — Single
Minimum passing score MLA-C01?
- A) 720 scaled score
- B) Incorrect option B
- C) Incorrect option C
- D) Incorrect option D

**Correct answer(s):** A
**Explanation:** 720 scaled score
**Why others are wrong:**
- B: Not the best AWS choice for this scenario.
- C: Not the best AWS choice for this scenario.
- D: Not the best AWS choice for this scenario.

---
