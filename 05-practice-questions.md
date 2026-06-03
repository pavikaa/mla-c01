# MLA-C01 Practice Questions (120)
**Instructions:** Timed 130 min for 65-question exam mode in `quiz.html`. Full bank = 120.

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
A team prepares raw CSV data in Amazon S3 for SageMaker training. Place the steps in the correct order.
- 1) Register features in SageMaker Feature Store
- 2) Ingest and validate schema
- 3) Split into train/validation/test sets
- 4) Transform data and engineer features

**Correct answer(s):** 2, 4, 3, 1
**Explanation:** Ingest and validate first, then transform, split, and optionally register features for reuse.

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
Which service helps validate data quality rules in ML pipelines?
- A) AWS Glue Data Quality
- B) Amazon Macie
- C) AWS CloudTrail
- D) Amazon Rekognition

**Correct answer(s):** A
**Explanation:** Validating rules on datasets in pipelines
**Why others are wrong:**
- B: Macie finds sensitive data, not pipeline quality rules.
- C: CloudTrail audits API calls.
- D: Rekognition is computer vision.

---
## Question 12 [D1] — Single
A team must combine batch data from Amazon RDS and Amazon S3 for ETL at scale. Best approach?
- A) Amazon Athena only
- B) AWS Glue or Amazon EMR with Spark
- C) Amazon SNS
- D) AWS Lambda only

**Correct answer(s):** B
**Explanation:** AWS Glue or EMR Spark
**Why others are wrong:**
- A: Athena queries but does not orchestrate large multi-source ETL.
- C: SNS is messaging.
- D: Lambda alone is poor for large batch ETL.

---
## Question 13 [D1] — Single
ML model artifacts in S3 must use customer-managed encryption keys. What should you configure?
- A) SSE-S3 only
- B) Public bucket ACL
- C) SSE-KMS with CMK
- D) Disable encryption

**Correct answer(s):** C
**Explanation:** SSE-KMS
**Why others are wrong:**
- A: SSE-S3 does not use customer-managed KMS CMK.
- B: Public buckets violate security best practices.
- D: Encryption required for compliance scenarios.

---
## Question 14 [D1] — Multi
Select TWO services suitable for streaming ETL into Amazon S3 (Select TWO).
- A) Amazon Kinesis Data Firehose
- B) Amazon S3 Glacier
- C) Amazon Managed Service for Apache Flink
- D) Amazon Route 53
- E) AWS Snowball

**Correct answer(s):** A, C
**Explanation:** Firehose delivers streams to S3; Managed Flink processes streams with stateful ETL.
**Why others are wrong:**
- B: Glacier is archival.
- D: Route 53 is DNS.
- E: Snowball is offline migration.

---
## Question 15 [D1] — Single
A fraud model flags many uncertain predictions. How reduce labeling cost while keeping quality?
- A) Delete all uncertain predictions
- B) Train without labels
- C) Disable model monitoring
- D) Amazon Augmented AI (A2I) human review loops

**Correct answer(s):** D
**Explanation:** Amazon A2I human review loops
**Why others are wrong:**
- A: Throws away valuable edge cases.
- B: Supervised problems need labels.
- C: Monitoring does not solve labeling.

---
## Question 16 [D2] — Single
A data scientist needs to run hundreds of training jobs to find optimal hyperparameters using Bayesian optimization. Which SageMaker capability should they use?
- A) SageMaker Automatic Model Tuning (AMT)
- B) SageMaker Autopilot
- C) SageMaker Model Monitor
- D) SageMaker Ground Truth

**Correct answer(s):** A
**Explanation:** AMT performs hyperparameter optimization with Bayesian search and early stopping.
**Why others are wrong:**
- B: Autopilot automates end-to-end model building, not tuning your existing estimator.
- C: Model Monitor watches production endpoints.
- D: Ground Truth is for labeling data.

---
## Question 17 [D2] — Single
During training, loss stops improving and Debugger reports vanishing gradients. Which service helped detect this issue?
- A) SageMaker Model Monitor
- B) SageMaker Debugger
- C) AWS CloudTrail
- D) Amazon Macie

**Correct answer(s):** B
**Explanation:** Debugger captures tensors and applies rules for convergence problems.
**Why others are wrong:**
- A: Model Monitor is for production inference.
- C: CloudTrail logs API activity.
- D: Macie finds sensitive data in S3.

---
## Question 18 [D2] — Single
A startup needs to detect objects in images via API without building custom CV models or managing training infrastructure. What should they use?
- A) Train Image Classification built-in algorithm from scratch
- B) Amazon SageMaker Data Wrangler
- C) Amazon Rekognition
- D) AWS Glue DataBrew

**Correct answer(s):** C
**Explanation:** Rekognition provides pre-built computer vision APIs.
**Why others are wrong:**
- A: Requires ML expertise and training ops.
- B: Data prep tool, not inference API.
- D: Visual ETL, not image detection API.

---
## Question 19 [D2] — Single
An enterprise requires versioned model artifacts and manual approval before any model reaches production endpoints. Which feature addresses this?
- A) SageMaker Experiments only
- B) Amazon S3 versioning alone
- C) AWS CodeDeploy
- D) SageMaker Model Registry

**Correct answer(s):** D
**Explanation:** Model Registry tracks versions, metadata, and approval status for deployment governance.
**Why others are wrong:**
- A: Experiments track trials but not formal approval workflow.
- B: S3 versioning lacks ML approval workflow.
- C: CodeDeploy deploys applications, not ML registry governance.

---
## Question 20 [D2] — Single
A fraud detection model has 0.5% positive class rate. Which evaluation metrics should the team prioritize?
- A) F1 score, precision, and recall
- B) Accuracy only
- C) RMSE and MAE
- D) R-squared

**Correct answer(s):** A
**Explanation:** Imbalanced classification requires precision/recall/F1, not accuracy alone.
**Why others are wrong:**
- B: Accuracy is misleading with extreme imbalance.
- C: Regression metrics for classification.
- D: R-squared is for regression.

---
## Question 21 [D2] — Multi
A team needs foundation-model text generation with minimal ML infrastructure operations. Select TWO.
- A) Train GPT from scratch on EC2
- B) Amazon Bedrock
- C) Amazon SageMaker JumpStart foundation models
- D) AWS Snowcone
- E) Amazon EBS snapshots

**Correct answer(s):** B, C
**Explanation:** Bedrock and JumpStart provide FMs without building training clusters from scratch.
**Why others are wrong:**
- A: High ops and cost.
- D: Edge migration device.
- E: Block storage snapshots unrelated.

---
## Question 22 [D2] — Single
A bank wants to evaluate a new fraud model against the current production model without sending the new model's predictions to customers. What deployment pattern should they use?
- A) Replace production variant with 100% traffic immediately
- B) Add a shadow variant that receives copied inference requests
- C) Delete the production endpoint
- D) Use Batch Transform only

**Correct answer(s):** B
**Explanation:** Shadow variants process duplicate traffic without affecting live responses.
**Why others are wrong:**
- A: Immediate cutover risks customer impact.
- C: Removes serving capability.
- D: Batch is offline, not live A/B comparison.

---
## Question 23 [D2] — Single
A team must train a custom PyTorch model on SageMaker and deploy it with a custom inference container. Which approach is required?
- A) SageMaker Autopilot only
- B) Built-in Linear Learner algorithm
- C) Script mode with training code and an ECR inference image
- D) Amazon Bedrock fine-tuning only

**Correct answer(s):** C
**Explanation:** Script mode (BYO framework) plus ECR container is the standard custom model path.
**Why others are wrong:**
- A: Autopilot does not support arbitrary custom PyTorch.
- B: Linear Learner is tabular built-in.
- D: Bedrock is for foundation models, not arbitrary PyTorch.

---
## Question 24 [D2] — Single
A data scientist needs strong performance on large tabular classification datasets with minimal algorithm tuning. Which SageMaker built-in algorithm is often appropriate?
- A) BlazingText
- B) Object Detection
- C) Seq2Seq
- D) XGBoost

**Correct answer(s):** D
**Explanation:** XGBoost is the common built-in choice for tabular classification/regression at scale.
**Why others are wrong:**
- A: BlazingText is for text.
- B: Object Detection is for images.
- C: Seq2Seq is for sequence generation.

---
## Question 25 [D2] — Single
Regulators require explaining which input features most influenced individual predictions from a SageMaker endpoint. Which tool should be used?
- A) SageMaker Clarify with SHAP explanations
- B) AWS CloudTrail
- C) Amazon Athena
- D) AWS Cost Explorer

**Correct answer(s):** A
**Explanation:** Clarify provides SHAP-based feature attributions for explainability.
**Why others are wrong:**
- B: Audit logs, not model explanations.
- C: SQL query service.
- D: Cost analysis tool.

---
## Question 26 [D2] — Single
A model shows excellent training accuracy but poor validation performance. Which actions are MOST appropriate to reduce overfitting?
- A) Remove the validation set
- B) Apply regularization and gather more representative validation data
- C) Increase model complexity only
- D) Disable early stopping

**Correct answer(s):** B
**Explanation:** Regularization and better validation data address overfitting.
**Why others are wrong:**
- A: Validation is essential.
- C: More complexity worsens overfitting.
- D: Early stopping helps prevent overfitting.

---
## Question 27 [D2] — Single
A company must extract entities and key phrases from support tickets without training custom NLP models. Which service should they choose?
- A) Amazon Comprehend
- B) Amazon Rekognition
- C) SageMaker Neo
- D) Amazon Kinesis Data Streams

**Correct answer(s):** A
**Explanation:** Comprehend provides managed NLP entity and phrase extraction.
**Why others are wrong:**
- B: Vision service.
- C: Neo compiles models for edge.
- D: Streaming ingestion.

---
## Question 28 [D2] — Single
What is the PRIMARY difference between SageMaker Autopilot and SageMaker Automatic Model Tuning (AMT)?
- A) AMT only works with images
- B) Autopilot requires manual endpoint creation only
- C) They are identical services
- D) Autopilot automates end-to-end model building; AMT tunes hyperparameters of your chosen estimator

**Correct answer(s):** D
**Explanation:** Autopilot is AutoML pipeline; AMT optimizes hyperparameters for an algorithm you specify.
**Why others are wrong:**
- A: AMT works with many algorithms.
- B: Autopilot can propose deployment steps.
- C: Different purposes.

---
## Question 29 [D3] — Single
An application sends predictions sporadically (a few times per hour) and the team wants minimal instance fleet management with pay-per-inference pricing. Which deployment option is BEST?
- A) SageMaker serverless inference
- B) Real-time endpoint with 24/7 ml.g5.12xlarge instances
- C) SageMaker Batch Transform on a schedule
- D) Multi-AZ Amazon RDS

**Correct answer(s):** A
**Explanation:** Serverless inference scales to zero between requests and charges per invocation.
**Why others are wrong:**
- B: Always-on instances are costly for sporadic traffic.
- C: Batch is for bulk offline scoring, not interactive sporadic API calls.
- D: RDS is a database, not model hosting.

---
## Question 30 [D3] — Single
A computer vision app uploads 100 GB image batches and can wait up to 24 hours for results using a queue-based pattern. Which inference approach fits BEST?
- A) Real-time endpoint with auto scaling
- B) Asynchronous SageMaker endpoint with S3 input/output
- C) SageMaker serverless inference with 1 MB payload limit
- D) Amazon API Gateway HTTP proxy only

**Correct answer(s):** B
**Explanation:** Async endpoints queue large payloads and write results to S3.
**Why others are wrong:**
- A: Real-time is for low-latency steady traffic, not 100 GB batches.
- C: Serverless has payload/memory limits.
- D: API Gateway does not host models.

---
## Question 31 [D3] — Single
A retailer must score 10 million customer records nightly with no persistent inference endpoint. What should they use?
- A) SageMaker real-time endpoint
- B) Amazon Lex bot
- C) SageMaker Batch Transform reading from and writing to S3
- D) AWS Lambda with 15-minute timeout for each record individually

**Correct answer(s):** C
**Explanation:** Batch Transform processes large offline datasets without a standing endpoint.
**Why others are wrong:**
- A: Real-time endpoints are for online inference.
- B: Lex is conversational AI.
- D: Lambda is not suited for bulk scoring millions of rows.

---
## Question 32 [D3] — Single
An MLOps team needs a native AWS DAG to chain data processing, training, evaluation, and conditional deployment steps with artifact caching. Which service should they use?
- A) Amazon SNS
- B) Amazon SQS
- C) AWS Step Functions only without SageMaker integration
- D) SageMaker Pipelines

**Correct answer(s):** D
**Explanation:** SageMaker Pipelines is the ML-native orchestration DAG on AWS.
**Why others are wrong:**
- A: SNS is pub/sub notifications.
- B: SQS is a message queue.
- C: Step Functions can orchestrate but Pipelines is ML-first with step caching.

---
## Question 33 [D3] — Single
A team wants to shift a small percentage of live traffic to a new model variant before full rollout to limit blast radius. Which strategy matches this requirement?
- A) Canary deployment with gradual traffic increase
- B) Immediate blue/green cutover of 100% traffic day one
- C) Delete the old model artifact from S3
- D) Train a second model on unlabeled data only

**Correct answer(s):** A
**Explanation:** Canary gradually increases traffic to the new variant.
**Why others are wrong:**
- B: Full immediate cutover is higher risk.
- C: Deleting artifacts is not a traffic strategy.
- D: Unlabeled-only training is unrelated.

---
## Question 34 [D3] — Multi
Select TWO resources commonly used to build and store container images for SageMaker custom inference (Select TWO).
- A) Amazon ECR
- B) AWS CodeBuild
- C) Amazon S3 Glacier only
- D) Amazon DynamoDB
- E) Amazon Route 53

**Correct answer(s):** A, B
**Explanation:** ECR stores container images; CodeBuild often builds and pushes images in CI/CD pipelines.
**Why others are wrong:**
- C: Glacier not for container registry.
- D: DynamoDB is NoSQL.
- E: DNS service.

---
## Question 35 [D3] — Single
A manufacturer must compile and optimize an ML model to run on constrained edge devices with limited compute. Which SageMaker feature should they use?
- A) SageMaker Ground Truth
- B) SageMaker Neo
- C) SageMaker Autopilot
- D) Amazon Kendra

**Correct answer(s):** B
**Explanation:** Neo compiles models for edge deployment targets.
**Why others are wrong:**
- A: Labeling service.
- C: AutoML.
- D: Enterprise search.

---
## Question 36 [D3] — Single
Before production launch, an team wants load tests and instance type recommendations for a new deep learning endpoint. Which tool should they use?
- A) AWS Trusted Advisor only
- B) Amazon Macie
- C) SageMaker Inference Recommender
- D) AWS Artifact compliance reports

**Correct answer(s):** C
**Explanation:** Inference Recommender runs load tests and suggests instance configurations.
**Why others are wrong:**
- A: Trusted Advisor gives broad best practices, not model-specific load tests.
- B: Macie is for data security.
- D: Artifact provides compliance documents.

---
## Question 37 [D3] — Single
A company hosts dozens of small models that share similar latency profiles and wants to reduce costs by sharing GPU infrastructure on one endpoint. What should they deploy?
- A) Separate real-time endpoint per model
- B) Amazon S3 Glacier
- C) AWS DataSync
- D) SageMaker multi-model endpoint

**Correct answer(s):** D
**Explanation:** Multi-model endpoints host multiple models on shared inference instances.
**Why others are wrong:**
- A: Many endpoints increase cost and ops.
- B: Archival storage.
- C: Data transfer service.

---
## Question 38 [D3] — Single
Developers push code to Git and need an automated workflow to build containers, run tests, and trigger SageMaker training when main branch updates. Which service orchestrates this?
- A) AWS CodePipeline integrated with CodeBuild and SageMaker
- B) Amazon CloudFront
- C) AWS Snowball
- D) Amazon ElastiCache

**Correct answer(s):** A
**Explanation:** CodePipeline orchestrates CI/CD stages including builds and SageMaker job triggers.
**Why others are wrong:**
- B: CDN.
- C: Offline data transfer.
- D: In-memory cache.

---
## Question 39 [D3] — Single
Security policy requires SageMaker inference in private subnets with no direct internet access, using interface endpoints for AWS service traffic. What must be configured?
- A) Public subnet endpoint with 0.0.0.0/0 security group
- B) VPC configuration with private subnets, security groups, and VPC endpoints
- C) Disable IAM entirely
- D) Store models in a public S3 bucket

**Correct answer(s):** B
**Explanation:** VPC mode isolates endpoints; VPC endpoints allow private AWS API access.
**Why others are wrong:**
- A: Violates private-only requirement.
- C: IAM is required for SageMaker.
- D: Public buckets violate security policy.

---
## Question 40 [D3] — Single
An enterprise already standardized on Apache Airflow DAGs and needs a managed AWS service to run them. Which option should they select?
- A) Amazon MWAA (Managed Workflows for Apache Airflow)
- B) Amazon SQS
- C) Amazon SNS
- D) AWS Amplify

**Correct answer(s):** A
**Explanation:** MWAA is the managed Airflow offering on AWS.
**Why others are wrong:**
- B: Message queue.
- C: Notifications.
- D: Front-end hosting.

---
## Question 41 [D4] — Single
In production, input feature distributions drift compared to training baselines. Which SageMaker Model Monitor type should alert the team?
- A) Model Monitor — data quality
- B) AWS Budgets
- C) Amazon Polly
- D) AWS CloudFormation drift detection only

**Correct answer(s):** A
**Explanation:** Data quality monitoring compares live features to baseline statistics.
**Why others are wrong:**
- B: Budgets track spend.
- C: Text-to-speech.
- D: CloudFormation drift is for infrastructure templates, not ML features.

---
## Question 42 [D4] — Single
Compliance requires an immutable record of who created or updated SageMaker endpoints and training jobs. Which service provides this?
- A) AWS CloudTrail
- B) Amazon CloudWatch metrics only
- C) SageMaker Model Monitor
- D) Amazon Personalize

**Correct answer(s):** A
**Explanation:** CloudTrail logs AWS API calls for audit.
**Why others are wrong:**
- B: Metrics lack detailed API caller audit trail.
- C: Monitors model quality in production.
- D: Recommendation service.

---
## Question 43 [D4] — Single
Finance needs email alerts when total SageMaker spend exceeds $50,000 in a month. What should they configure?
- A) SageMaker Debugger
- B) AWS Budgets with cost alerts
- C) Amazon GuardDuty
- D) SageMaker Feature Store

**Correct answer(s):** B
**Explanation:** AWS Budgets supports threshold alerts on spend.
**Why others are wrong:**
- A: Training debugger.
- C: Threat detection.
- D: Feature storage.

---
## Question 44 [D4] — Single
A SageMaker notebook must read only specific S3 prefixes and decrypt artifacts with a specific KMS key. What implements least privilege?
- A) Attach AdministratorAccess to all users
- B) Use a public S3 ACL
- C) IAM execution role with scoped policies for S3 prefixes and KMS keys
- D) Disable encryption

**Correct answer(s):** C
**Explanation:** Scoped IAM roles enforce least privilege for notebooks and jobs.
**Why others are wrong:**
- A: AdministratorAccess violates least privilege.
- B: Public ACLs are insecure.
- D: Encryption should remain enabled.

---
## Question 45 [D4] — Single
When Model Monitor detects data drift beyond a threshold, an automated retraining pipeline must start. Which integration is MOST appropriate?
- A) Manual weekly spreadsheet review
- B) Amazon Rekognition
- C) Disable Model Monitor
- D) Amazon EventBridge rule triggering a SageMaker Pipeline

**Correct answer(s):** D
**Explanation:** EventBridge can react to Monitor alerts and invoke Pipelines.
**Why others are wrong:**
- A: Not automated.
- B: Unrelated vision API.
- C: Removes detection capability.

---
## Question 46 [D4] — Single
Two model versions should receive 90% and 10% of live inference traffic on the same endpoint for comparison. How is this configured?
- A) Production variant traffic weights
- B) Delete the older model from ECR
- C) Use S3 lifecycle policies
- D) Enable S3 Transfer Acceleration

**Correct answer(s):** A
**Explanation:** Production variants support weighted traffic splits for A/B tests.
**Why others are wrong:**
- B: Deleting images breaks rollback.
- C: S3 lifecycle is storage tiering.
- D: Transfer Acceleration is upload speed.

---
## Question 47 [D4] — Multi
Select TWO approaches to reduce SageMaker training cost while maintaining recoverability (Select TWO).
- A) Managed Spot Training with S3 checkpointing
- B) Always use largest On-Demand instance
- C) Disable all logging
- D) Use Spot Instances without checkpoints
- E) Right-size instance family for workload

**Correct answer(s):** A, E
**Explanation:** Spot + checkpoints saves money with fault tolerance; rightsizing avoids overpayment.
**Why others are wrong:**
- B: Oversized instances waste money.
- C: Logging needed for ops.
- D: Spot without checkpoints loses progress on interrupt.

---
## Question 48 [D4] — Single
Operations needs dashboards and alarms when endpoint ModelLatency exceeds 500 ms. Which services should they use?
- A) Amazon Macie
- B) Amazon CloudWatch metrics and alarms
- C) AWS Artifact
- D) Amazon Translate

**Correct answer(s):** B
**Explanation:** CloudWatch captures SageMaker endpoint latency metrics and supports alarms.
**Why others are wrong:**
- A: PII discovery.
- C: Compliance documents.
- D: Translation API.

---
## Question 49 [D4] — Single
FinOps must break down ML spending by cost center using resource tags across accounts. Which tool should they use?
- A) SageMaker Debugger
- B) Amazon Lex
- C) AWS Cost Explorer with cost allocation tags
- D) SageMaker Ground Truth

**Correct answer(s):** C
**Explanation:** Cost Explorer analyzes spend filtered by tags.
**Why others are wrong:**
- A: Training debug tool.
- B: Chatbot service.
- D: Labeling.

---
## Question 50 [D4] — Single
An engineer enables SageMaker Model Monitor on an endpoint but no constraints trigger. What prerequisite is MOST likely missing?
- A) A baseline dataset with statistics from training or prior production data
- B) Public internet on the endpoint
- C) Deleting CloudWatch logs
- D) Disabling the execution role

**Correct answer(s):** A
**Explanation:** Model Monitor requires a baseline to compare production data against.
**Why others are wrong:**
- B: Internet not required for baselines.
- C: Logs help troubleshooting.
- D: Execution role is required.

---
## Question 51 [D1] — Single
A startup merges daily clickstream from Kinesis with customer profiles in S3 Parquet using minimal custom code. Which service is BEST?
- A) Amazon SNS
- B) AWS Glue ETL job
- C) Amazon Route 53
- D) AWS WAF

**Correct answer(s):** B
**Explanation:** Glue provides serverless Spark ETL to join streaming/batch sources.
**Why others are wrong:**
- A: Notifications only.
- C: DNS.
- D: Web firewall.

---
## Question 52 [D1] — Single
A data scientist builds visual data prep recipes and must export them into an automated SageMaker Pipeline. Which tool supports this workflow?
- A) Amazon Athena
- B) AWS CloudTrail
- C) SageMaker Data Wrangler
- D) Amazon Polly

**Correct answer(s):** C
**Explanation:** Data Wrangler exports recipes to Python or Pipeline steps.
**Why others are wrong:**
- A: SQL queries only.
- B: Audit logs.
- D: Speech synthesis.

---
## Question 53 [D1] — Single
A multi-account data lake needs centralized table-level permissions and governance. Which service should be used?
- A) Amazon API Gateway
- B) Amazon CloudFront
- C) AWS Lambda
- D) AWS Lake Formation

**Correct answer(s):** D
**Explanation:** Lake Formation manages fine-grained data lake access.
**Why others are wrong:**
- A: API management.
- B: CDN.
- C: Functions, not lake governance layer.

---
## Question 54 [D1] — Multi
Select TWO practices that help address selection bias before training (Select TWO).
- A) Collect representative production samples
- B) Use only the easiest examples
- C) Stratified train/validation split
- D) Remove all validation data
- E) Disable random seed

**Correct answer(s):** A, C
**Explanation:** Representative sampling and stratified splits reduce selection bias impact.
**Why others are wrong:**
- B: Biases model further.
- D: Validation required.
- E: Seeds help reproducibility.

---
## Question 55 [D2] — Single
A housing price regression model must penalize large prediction errors more than small ones. Which metric is MOST appropriate?
- A) Root Mean Square Error (RMSE)
- B) Accuracy
- C) F1 score
- D) Top-5 categorical accuracy

**Correct answer(s):** A
**Explanation:** RMSE squares errors, penalizing large mistakes.
**Why others are wrong:**
- B: Classification metric.
- C: Classification metric.
- D: Multi-class classification metric.

---
## Question 56 [D2] — Single
Training on a single GPU instance would take two weeks. The team wants to reduce wall-clock time using multiple GPUs across instances. What should they enable?
- A) SageMaker distributed training
- B) Amazon S3 Glacier archival
- C) Disable checkpointing
- D) Use only AWS Lambda

**Correct answer(s):** A
**Explanation:** SageMaker supports distributed data-parallel training across instances.
**Why others are wrong:**
- B: Archival storage.
- C: Checkpointing helps Spot recovery.
- D: Lambda cannot run multi-week GPU training.

---
## Question 57 [D2] — Single
A mobile app needs speech-to-text with no model training or endpoint management by the app team. Which AWS service fits?
- A) Amazon SageMaker Neo
- B) Amazon Transcribe
- C) Amazon Fraud Detector
- D) AWS Outposts

**Correct answer(s):** B
**Explanation:** Transcribe is the managed speech-to-text API.
**Why others are wrong:**
- A: Edge compilation.
- C: Fraud ML service.
- D: On-premises AWS hardware.

---
## Question 58 [D2] — Single
A team runs dozens of training trials with different hyperparameters and must compare metrics and artifacts centrally. Which SageMaker feature helps?
- A) SageMaker Ground Truth
- B) Amazon Macie
- C) AWS Budgets
- D) SageMaker Experiments

**Correct answer(s):** D
**Explanation:** Experiments organizes trials, parameters, and metrics.
**Why others are wrong:**
- A: Labeling.
- B: PII scanning.
- C: Cost alerts.

---
## Question 59 [D2] — Single
Validation AUC stops improving for several epochs during training. Which built-in mechanism should stop training to save cost?
- A) Early stopping based on validation metric plateau
- B) Delete the training dataset
- C) Disable automatic model tuning
- D) Remove IAM roles

**Correct answer(s):** A
**Explanation:** Early stopping halts training when validation metrics plateau.
**Why others are wrong:**
- B: Destroys training data.
- C: AMT is separate from early stopping.
- D: IAM is required.

---
## Question 60 [D3] — Single
An API requires steady p99 latency under 50 ms at thousands of requests per second. Which deployment is MOST appropriate?
- A) SageMaker Batch Transform nightly
- B) Real-time endpoint with auto scaling on appropriate instance types
- C) SageMaker serverless inference only
- D) AWS Snowball Edge

**Correct answer(s):** B
**Explanation:** Real-time provisioned endpoints with auto scaling meet strict low-latency SLAs.
**Why others are wrong:**
- A: Batch is offline.
- C: Serverless has cold start and concurrency limits.
- D: Migration appliance.

---
## Question 61 [D3] — Single
Infrastructure engineers want to provision a SageMaker Studio domain using version-controlled templates integrated with their Git repo. Which tools are appropriate?
- A) AWS CloudFormation or AWS CDK
- B) Amazon Rekognition
- C) Amazon Polly
- D) AWS DeepRacer

**Correct answer(s):** A
**Explanation:** CloudFormation and CDK provide IaC for Studio and supporting resources.
**Why others are wrong:**
- B: Vision API.
- C: Speech.
- D: Reinforcement learning toy car.

---
## Question 62 [D3] — Single
An application team deploys EC2-based services and needs blue/green deployments with traffic shifting at the application deployment layer. Which AWS service is designed for this?
- A) SageMaker Model Monitor
- B) Amazon S3 Intelligent-Tiering
- C) AWS Glue DataBrew
- D) AWS CodeDeploy

**Correct answer(s):** D
**Explanation:** CodeDeploy supports blue/green and in-place deployment patterns for compute.
**Why others are wrong:**
- A: ML monitoring.
- B: Storage class automation.
- C: Data prep.

---
## Question 63 [D3] — Single
A retraining SageMaker Pipeline must run every Sunday at 2:00 AM UTC automatically. What should trigger it?
- A) Amazon EventBridge scheduled rule
- B) Manual console click only
- C) Amazon CloudFront cache invalidation
- D) AWS Artifact download

**Correct answer(s):** A
**Explanation:** EventBridge cron schedules automate Pipeline execution.
**Why others are wrong:**
- B: Not automated.
- C: CDN operation.
- D: Compliance PDFs.

---
## Question 64 [D3] — Matching
Match each inference requirement to the most appropriate SageMaker deployment option.
- **Steady low latency at high QPS**
- **Offline scoring of millions of historical records**
- **Intermittent traffic with minimal instance management**

Choices:
- Real-time endpoint with auto scaling
- Batch Transform
- Serverless inference

**Correct answer(s):** Real-time endpoint with auto scaling, Batch Transform, Serverless inference
**Explanation:** Real-time for SLA; Batch for bulk offline; Serverless for bursty/intermittent.

---
## Question 65 [D4] — Single
Model Monitor reports increasing bias metrics across demographic facets compared to baseline. Which monitor type is this?
- A) Data quality only
- B) Bias drift monitoring
- C) AWS Cost Explorer
- D) S3 lifecycle transition

**Correct answer(s):** B
**Explanation:** Bias drift tracks fairness metric changes over time.
**Why others are wrong:**
- A: Data quality tracks feature stats, not fairness facets.
- C: Cost tool.
- D: Storage policy.

---
## Question 66 [D4] — Single
Microservices around a SageMaker endpoint show high end-to-end latency and the team needs distributed tracing across calls. Which service should they enable?
- A) AWS X-Ray
- B) Amazon Macie
- C) AWS Artifact
- D) Amazon Mechanical Turk

**Correct answer(s):** A
**Explanation:** X-Ray traces requests across services.
**Why others are wrong:**
- B: S3 security.
- C: Compliance reports.
- D: Crowd workforce.

---
## Question 67 [D4] — Single
Training jobs consistently use only 20% of provisioned CPU on ml.m5.4xlarge instances. Which AWS service recommends better instance choices?
- A) Amazon Rekognition
- B) Amazon Translate
- C) Amazon Polly
- D) AWS Compute Optimizer

**Correct answer(s):** D
**Explanation:** Compute Optimizer rightsizing recommendations use utilization history.
**Why others are wrong:**
- A: Vision.
- B: Translation.
- C: Speech.

---
## Question 68 [D4] — Single
Security requires customer-managed keys for all model artifacts stored in Amazon S3. What encryption should be configured?
- A) SSE-KMS with a customer managed key (CMK)
- B) No encryption to improve performance
- C) HTTP without TLS for internal traffic only
- D) Public-read ACL on the bucket

**Correct answer(s):** A
**Explanation:** SSE-KMS with CMK meets customer-managed encryption requirements.
**Why others are wrong:**
- B: Violates policy.
- C: TLS required in transit.
- D: Public ACL is insecure.

---
## Question 69 [D4] — Single
A model artifact bucket must never be accessible from the public internet. Which controls should be applied?
- A) Enable anonymous read on bucket policy
- B) S3 Block Public Access, bucket policy deny public principals, and least-privilege IAM
- C) Share root account access keys with the team
- D) Disable versioning

**Correct answer(s):** B
**Explanation:** Block Public Access plus restrictive policies and IAM prevent public exposure.
**Why others are wrong:**
- A: Allows public access.
- C: Root keys are a critical security risk.
- D: Versioning aids recovery.

---
## Question 70 [D1] — Single
An analyst needs to run ad-hoc SQL queries directly on data stored in S3 without provisioning a cluster. Which service should they use?
- A) Amazon EMR always-on cluster
- B) Amazon Redshift provisioned warehouse only
- C) Amazon Athena
- D) AWS Snowmobile

**Correct answer(s):** C
**Explanation:** Athena is serverless SQL over S3.
**Why others are wrong:**
- A: Cluster ops overhead.
- B: Warehouse for sustained analytics workloads.
- D: Exabyte-scale physical transfer.

---
## Question 71 [D2] — Single
An e-commerce site needs real-time product recommendations without building custom collaborative filtering infrastructure. Which service fits?
- A) Amazon Personalize
- B) Amazon Textract
- C) AWS Glue Data Quality
- D) Amazon Macie

**Correct answer(s):** A
**Explanation:** Personalize provides real-time recommendation campaigns.
**Why others are wrong:**
- B: Document OCR.
- C: Data validation rules.
- D: PII discovery.

---
## Question 72 [D2] — Single
A insurance firm must extract tables and text from scanned PDF claim forms automatically. Which service should they use?
- A) Amazon Textract
- B) Amazon Polly
- C) Amazon Kendra
- D) AWS DeepRacer

**Correct answer(s):** A
**Explanation:** Textract extracts text and structured data from documents.
**Why others are wrong:**
- B: Speech output.
- C: Enterprise search.
- D: RL toy.

---
## Question 73 [D3] — Single
Lightweight event-driven preprocessing (thumbnail generation, JSON validation) must run when objects land in S3. What is the BEST fit?
- A) SageMaker multi-GPU training cluster
- B) AWS Lambda triggered by S3 events
- C) Amazon Redshift Spectrum only
- D) SageMaker Batch Transform

**Correct answer(s):** B
**Explanation:** Lambda handles small event-driven transforms efficiently.
**Why others are wrong:**
- A: Overkill for light preprocessing.
- C: Analytics SQL engine.
- D: Bulk batch scoring.

---
## Question 74 [D3] — Single
A BERT model requires GPU inference 24/7 at high throughput with predictable latency. Why is AWS Lambda a poor choice?
- A) Lambda cannot meet sustained GPU inference and memory needs for large transformers
- B) Lambda is always cheaper for GPU workloads
- C) Lambda automatically scales GPU memory to 2 TB
- D) Lambda hosts multi-model endpoints natively

**Correct answer(s):** A
**Explanation:** Lambda has limits on duration, memory, and no GPU; real-time GPU endpoints are appropriate.
**Why others are wrong:**
- B: GPU inference at scale is not Lambda's strength.
- C: Lambda memory cap is far below 2 TB and no GPU.
- D: Multi-model endpoints are SageMaker feature.

---
## Question 75 [D4] — Single
Engineers need to search application inference logs for ERROR patterns and stack traces. Which service should they use?
- A) AWS CloudTrail only
- B) Amazon S3 Glacier
- C) Amazon Route 53
- D) Amazon CloudWatch Logs (and Logs Insights)

**Correct answer(s):** D
**Explanation:** CloudWatch Logs stores and queries application log data.
**Why others are wrong:**
- A: CloudTrail is API audit, not app log search.
- B: Archival.
- C: DNS.

---
## Question 76 [D1] — Single
Streaming data must be delivered near-real-time to Amazon S3 and Amazon Redshift without writing custom consumers. Which service is appropriate?
- A) Amazon Kinesis Data Firehose
- B) AWS Snowball
- C) Amazon EBS snapshots
- D) AWS Artifact

**Correct answer(s):** A
**Explanation:** Firehose is fully managed delivery to S3, Redshift, OpenSearch, etc.
**Why others are wrong:**
- B: Offline transfer.
- C: Block storage backup.
- D: Compliance downloads.

---
## Question 77 [D2] — Single
A classification model has high precision but low recall. What does this typically indicate?
- A) The model always predicts the majority class
- B) Among positive predictions, many are wrong (false positives) relative to missed positives
- C) RMSE is zero
- D) The dataset has no labels

**Correct answer(s):** B
**Explanation:** High precision + low recall often means few false positives but many false negatives (missed positives).
**Why others are wrong:**
- A: Describes high recall bias toward majority, not this pattern.
- C: Regression metric.
- D: Labels exist for supervised learning.

---
## Question 78 [D2] — Single
A data science team combines multiple models' predictions to improve overall accuracy. Which technique are they using?
- A) Model ensembling (stacking/boosting/bagging)
- B) S3 lifecycle expiration
- C) VPC peering
- D) IAM password rotation

**Correct answer(s):** A
**Explanation:** Ensembling merges models to improve performance.
**Why others are wrong:**
- B: Storage management.
- C: Networking.
- D: Identity hygiene unrelated.

---
## Question 79 [D3] — Single
A SageMaker Pipeline should deploy to production only if validation accuracy exceeds 0.80; otherwise it must stop. How is this implemented?
- A) Unconditional Deploy step always
- B) Delete the training data
- C) Disable Model Registry
- D) Conditional pipeline step based on metric threshold

**Correct answer(s):** D
**Explanation:** Pipelines support conditional steps on property values like accuracy.
**Why others are wrong:**
- A: Ignores quality gate.
- B: Destroys data.
- C: Registry supports governance.

---
## Question 80 [D4] — Single
A new AWS account wants automated checks for over-provisioned EC2 and idle resources related to ML workloads. Which service provides these recommendations?
- A) AWS Trusted Advisor
- B) Amazon Polly
- C) Amazon Lex
- D) AWS DeepRacer

**Correct answer(s):** A
**Explanation:** Trusted Advisor flags cost and performance improvements.
**Why others are wrong:**
- B: Speech.
- C: Chatbot.
- D: RL game.

---
## Question 81 [D1] — Single
Case study: A bank loads daily Parquet into S3 for ML features and must scan for GDPR-related PII before loading into Feature Store. What is the FIRST step?
- A) Deploy endpoint before any data checks
- B) Run Amazon Macie to discover sensitive data, then transform/redact as needed
- C) Disable all encryption
- D) Make the bucket public for faster ingestion

**Correct answer(s):** B
**Explanation:** Macie discovers PII; remediation occurs before Feature Store ingestion.
**Why others are wrong:**
- A: Skips compliance.
- C: Weakens security.
- D: Public bucket violates policy.

---
## Question 82 [D2] — Single
Case study: A startup needs a generative chatbot quickly without managing training clusters. Which service is MOST appropriate?
- A) Train a transformer from scratch on Spot CPUs only
- B) Amazon S3 Glacier Deep Archive
- C) Amazon Bedrock foundation models
- D) AWS Snowball Edge

**Correct answer(s):** C
**Explanation:** Bedrock exposes FMs via API with minimal infrastructure.
**Why others are wrong:**
- A: Slow and ops-heavy.
- B: Archival storage.
- D: Edge transfer device.

---
## Question 83 [D3] — Single
Case study: A mobile app sends user batches twice per day for churn scoring; latency of several hours is acceptable. Which inference pattern fits?
- A) Real-time endpoint with auto scaling
- B) SageMaker serverless for sub-10ms latency
- C) Amazon Lex
- D) SageMaker Batch Transform

**Correct answer(s):** D
**Explanation:** Batch Transform handles periodic bulk scoring without online endpoints.
**Why others are wrong:**
- A: Unnecessary cost for twice-daily batch.
- B: Serverless still online API model.
- C: Conversational bot.

---
## Question 84 [D4] — Single
Case study: Model accuracy drops after a marketing campaign changes the customer mix in production data. What should the MLOps team do FIRST?
- A) Detect data drift, investigate features, and trigger retraining pipeline if needed
- B) Delete CloudWatch logs
- C) Remove Model Monitor baselines
- D) Turn off encryption

**Correct answer(s):** A
**Explanation:** Distribution shift is data drift; Monitor + retrain is the operational response.
**Why others are wrong:**
- B: Removes observability.
- C: Baselines required for Monitor.
- D: Security regression.

---
## Question 85 [D1] — Single
A categorical column has 10,000 unique values. Why might one-hot encoding be problematic?
- A) It creates a very high-dimensional sparse feature space
- B) It always improves GPU utilization
- C) It is required for all SageMaker built-in algorithms
- D) It encrypts data at rest

**Correct answer(s):** A
**Explanation:** High cardinality one-hot explodes dimensionality and sparsity.
**Why others are wrong:**
- B: Unrelated to encoding choice.
- C: Not always required; embeddings or hashing may be better.
- D: Encoding is not encryption.

---
## Question 86 [D2] — Single
L2 regularization in a neural network primarily helps prevent which problem?
- A) Large weights contributing to overfitting
- B) S3 transfer failures
- C) VPC DNS resolution
- D) Kinesis shard throttling

**Correct answer(s):** A
**Explanation:** L2 (weight decay) penalizes large weights to reduce overfitting.
**Why others are wrong:**
- B: Network/storage issue.
- C: Networking.
- D: Streaming limits.

---
## Question 87 [D3] — Single
A CI/CD pipeline blocks deployment when ECR image vulnerability scanning fails. Why is this a best practice?
- A) It slows releases unnecessarily without benefit
- B) It guarantees higher AWS bills only
- C) It prevents known-vulnerable containers from reaching production
- D) It replaces IAM entirely

**Correct answer(s):** C
**Explanation:** Image scanning enforces security compliance before deploy.
**Why others are wrong:**
- A: Security benefit outweighs delay.
- B: Not about billing.
- D: IAM still required.

---
## Question 88 [D4] — Single
A team runs steady SageMaker training and inference year-round. Which purchasing option can reduce compute cost with a spend commitment?
- A) SageMaker Savings Plans or Compute Savings Plans
- B) Delete all CloudWatch alarms
- C) Use only Spot for real-time low-latency endpoints
- D) Disable auto scaling on all endpoints

**Correct answer(s):** A
**Explanation:** Savings Plans provide discounted rates for consistent compute usage.
**Why others are wrong:**
- B: Removes observability.
- C: Spot unsuitable for strict latency SLAs.
- D: Auto scaling optimizes cost and performance.

---
## Question 89 [D1] — Single
A labeling workflow needs to integrate a human workforce for custom tasks within SageMaker. Which approach is valid?
- A) Use SageMaker Ground Truth with private or vendor workforce
- B) Use only Amazon CloudFront
- C) Label data by renaming S3 buckets
- D) Use AWS Artifact for bounding boxes

**Correct answer(s):** A
**Explanation:** Ground Truth orchestrates labeling including Mechanical Turk or private workforces.
**Why others are wrong:**
- B: CDN.
- C: Bucket names are not labels.
- D: Artifact is compliance documentation.

---
## Question 90 [D2] — Single
A data scientist visualizes true vs predicted classes across categories using color grids. Which artifact are they likely using?
- A) S3 lifecycle policy
- B) IAM policy simulator
- C) Confusion matrix heat map
- D) VPC flow logs only

**Correct answer(s):** C
**Explanation:** Heat maps visualize confusion matrices for classification evaluation.
**Why others are wrong:**
- A: Storage management.
- B: IAM testing tool.
- D: Network traffic logs.

---
## Question 91 [D3] — Single
Endpoint auto scaling is configured with target invocations per instance. What problem does this policy address?
- A) Growing request volume requiring more instances
- B) Encrypting data at rest
- C) Labeling images
- D) Compiling models with Neo

**Correct answer(s):** A
**Explanation:** Scaling on invocations per instance adds capacity as traffic grows.
**Why others are wrong:**
- B: Encryption separate concern.
- C: Ground Truth task.
- D: Neo compilation.

---
## Question 92 [D4] — Single
Business stakeholders need dashboards for model KPIs without writing SQL on raw logs. Which AWS service is appropriate?
- A) Amazon QuickSight dashboards fed from metrics or datasets
- B) AWS Snowball
- C) Amazon Inspector
- D) AWS DeepRacer

**Correct answer(s):** A
**Explanation:** QuickSight builds business-facing dashboards.
**Why others are wrong:**
- B: Transfer appliance.
- C: Vulnerability scanning.
- D: RL game.

---
## Question 93 [D2] — Single
A team has limited labeled data for a task similar to a pre-trained model in JumpStart. What approach is MOST efficient?
- A) Fine-tune the JumpStart pre-trained model
- B) Train billions of parameters from random init on CPU
- C) Delete validation data
- D) Use only Batch Transform for training

**Correct answer(s):** A
**Explanation:** Fine-tuning transfer learns from pre-trained weights with fewer labels.
**Why others are wrong:**
- B: Impractical and poor results.
- C: Validation required.
- D: Batch Transform is inference.

---
## Question 94 [D3] — Single
An architecture must coordinate Lambda preprocessing, a SageMaker Processing job, and SNS notification in sequence. Which service orchestrates this?
- A) Amazon Macie
- B) Amazon Polly
- C) AWS Step Functions
- D) Amazon Glacier

**Correct answer(s):** C
**Explanation:** Step Functions orchestrates multi-service workflows with state machines.
**Why others are wrong:**
- A: PII service.
- B: Speech.
- D: Archival.

---
## Question 95 [D4] — Single
Compliance requires encryption of SageMaker training volumes and model artifacts at rest. Which service manages keys?
- A) Amazon Route 53
- B) Amazon API Gateway
- C) Amazon CloudFront
- D) AWS KMS integrated with SageMaker and S3

**Correct answer(s):** D
**Explanation:** KMS provides CMKs for encrypting EBS and S3 artifacts.
**Why others are wrong:**
- A: DNS.
- B: API management.
- C: CDN.

---
## Question 96 [D1] — Single
Training I/O is bottlenecked on a single EBS volume attached to the training instance. Which EBS feature improves throughput?
- A) Provisioned IOPS (io2) volumes sized for required IOPS
- B) Disable encryption
- C) Use S3 Glacier for active training input
- D) Remove the training job

**Correct answer(s):** A
**Explanation:** Provisioned IOPS volumes deliver consistent high I/O for training.
**Why others are wrong:**
- B: Security requirement often mandates encryption.
- C: Glacier not for hot training data.
- D: Does not fix I/O.

---
## Question 97 [D2] — Single
A model fine-tuned sequentially on new tasks forgets earlier tasks. This phenomenon is known as:
- A) Catastrophic forgetting
- B) S3 eventual consistency
- C) VPC peering
- D) Kinesis resharding

**Correct answer(s):** A
**Explanation:** Catastrophic forgetting occurs when new training overwrites prior task knowledge.
**Why others are wrong:**
- B: Storage behavior.
- C: Networking.
- D: Stream scaling.

---
## Question 98 [D3] — Single
A company uses long-lived Git branches and merges to main trigger production ML pipelines. Which workflow concept does this describe?
- A) GitFlow-style branching integrated with CI/CD triggers
- B) Deleting all Git history
- C) Storing models only in CloudTrail
- D) Disabling version control

**Correct answer(s):** A
**Explanation:** GitFlow (or similar) defines branch policies that trigger pipelines on merge.
**Why others are wrong:**
- B: Destroys history.
- C: CloudTrail is audit logs.
- D: Version control is essential.

---
## Question 99 [D4] — Single
A team hits the account limit for concurrent SageMaker training jobs. What is the appropriate resolution?
- A) Request a service quota increase for SageMaker training jobs
- B) Delete all IAM users
- C) Disable CloudWatch
- D) Use public S3 ACLs

**Correct answer(s):** A
**Explanation:** AWS Service Quotas can be increased via support/request console.
**Why others are wrong:**
- B: Breaks access.
- C: Removes monitoring.
- D: Security violation.

---
## Question 100 [Cross] — Single
What is the minimum passing scaled score for the AWS Certified Machine Learning Engineer – Associate (MLA-C01) exam?
- A) 720
- B) 650
- C) 800
- D) 900

**Correct answer(s):** A
**Explanation:** AWS documents a passing score of 720 on the 100–1000 scale.
**Why others are wrong:**
- B: Below official pass line.
- C: Higher than required.
- D: Perfect score not required.

---
## Question 101 [D2] — Multi
A worker pulls messages from Amazon SQS, calls Amazon Bedrock Titan Image Generator, and deletes processed messages. Select TWO required IAM permissions. (Select TWO)
- A) sqs:ReceiveMessage and sqs:DeleteMessage on the queue
- B) bedrock:InvokeModel on the model
- C) sagemaker:CreateTrainingJob
- D) ec2:TerminateInstances
- E) cloudfront:CreateDistribution

**Correct answer(s):** A, B
**Explanation:** Queue consumption needs ReceiveMessage/DeleteMessage; generation needs bedrock:InvokeModel.
**Why others are wrong:**
- C: Training API not used at inference.
- D: Unrelated.
- E: CDN unrelated.

---
## Question 102 [D1] — Single
RAG over text files already in S3 requires semantic search with minimal custom vector infrastructure. Which solution has the LEAST operational overhead?
- A) Amazon Kendra S3 connector or Bedrock Knowledge Base
- B) Textract only
- C) Athena SQL LIKE queries
- D) AWS Snowball

**Correct answer(s):** A
**Explanation:** Kendra and Bedrock Knowledge Bases provide managed semantic retrieval.
**Why others are wrong:**
- B: Textract extracts text, not semantic search.
- C: SQL keyword match is not semantic RAG.
- D: Migration appliance.

---
## Question 103 [D1] — Single
An ML engineer must run ETL to discover schema and store metadata in a central catalog with minimal manual effort. What should they use?
- A) AWS Glue job with Glue Data Catalog
- B) Amazon Macie only
- C) Amazon CloudFront
- D) AWS WAF

**Correct answer(s):** A
**Explanation:** Glue discovers schema and persists metadata in the Data Catalog.
**Why others are wrong:**
- B: Macie finds sensitive data.
- C: CDN.
- D: Firewall.

---
## Question 104 [D1] — Single
A company needs near-real-time analytics on streams, Apache Kafka compatibility, and no broker cluster capacity planning. Which service fits?
- A) Amazon MSK Serverless
- B) Amazon S3 Glacier
- C) AWS Snowcone
- D) Amazon EBS snapshots

**Correct answer(s):** A
**Explanation:** MSK Serverless offers Kafka API without provisioning brokers.
**Why others are wrong:**
- B: Archival.
- C: Edge device.
- D: Block storage backups.

---
## Question 105 [D2] — Single
Compliance prohibits SageMaker from collecting aggregated metadata from training jobs. What should the ML engineer configure?
- A) Opt out of metadata tracking when submitting training jobs
- B) Use only public S3 buckets
- C) Disable VPC
- D) Remove IAM roles

**Correct answer(s):** A
**Explanation:** Training jobs support metadata collection opt-out for compliance scenarios.
**Why others are wrong:**
- B: Public buckets worsen security.
- C: VPC unrelated to metadata collection flag.
- D: IAM required.

---
## Question 106 [D1] — Single
6 TB of training data lives on Amazon FSx for ONTAP in the same VPC as SageMaker. How should the data be made accessible to training jobs?
- A) Mount the FSx for ONTAP file system to the training instance
- B) Email CSV files to support
- C) Use only Amazon CloudWatch
- D) Disable encryption

**Correct answer(s):** A
**Explanation:** FSx ONTAP provides POSIX mount for large shared training datasets in VPC.
**Why others are wrong:**
- B: Not a data access pattern.
- C: Monitoring service.
- D: Encryption still required.

---
## Question 107 [D2] — Single
A neural network overfits (great training accuracy, poor validation). A colleague suggests removing all dropout layers. What is the BEST response?
- A) Remove dropout and add more layers
- B) Keep or add regularization such as dropout/L2 and use early stopping
- C) Delete the validation set
- D) Disable early stopping and train longer

**Correct answer(s):** B
**Explanation:** Dropout reduces overfitting; removing it worsens the problem. Regularization and early stopping help.
**Why others are wrong:**
- A: More layers increases capacity/overfitting risk.
- C: Validation required.
- D: Longer training without guardrails increases overfitting.

---
## Question 108 [D1] — Single
Extract unique keywords from thousands of support documents with the LEAST operational overhead.
- A) Custom NLTK on self-managed EC2 only
- B) Manual spreadsheet review
- C) Amazon Comprehend key phrase extraction
- D) AWS CloudTrail

**Correct answer(s):** C
**Explanation:** Comprehend provides managed key phrase and entity APIs.
**Why others are wrong:**
- A: High ops vs managed API.
- B: Not scalable.
- D: API audit logs.

---
## Question 109 [D3] — Single
SageMaker Studio must run in a corporate VPC without internet access to data planes. What is required?
- A) Domain in VPC with appropriate interface VPC endpoints and security groups
- B) Store all artifacts in public S3
- C) Use root account access keys in notebooks
- D) Disable CloudWatch

**Correct answer(s):** A
**Explanation:** VPC-only Studio uses private subnets and VPC endpoints for AWS services.
**Why others are wrong:**
- B: Public storage violates policy.
- C: Root keys forbidden.
- D: Logging still needed.

---
## Question 110 [D2] — Single
5 TB mixed CSV/JSON/Parquet/text requires multi-hour NLP transforms in an automated multi-step pipeline. Which approach is MOST appropriate?
- A) Single AWS Lambda function only
- B) Manual copy to USB drives
- C) SageMaker Pipelines with Processing steps (and/or Glue/EMR as needed)
- D) Amazon Route 53 health checks

**Correct answer(s):** C
**Explanation:** Long multi-step automated ML workflows use SageMaker Pipelines; Lambda alone is insufficient at this scale/complexity.
**Why others are wrong:**
- A: Lambda time/memory limits.
- B: Not automated cloud pipeline.
- D: DNS health checks.

---
## Question 111 [D2] — Single
Polynomial regression has many irrelevant high-order terms; coefficients should shrink to zero for unused terms. Which regularization is BEST?
- A) L1 regularization
- B) L2 regularization only
- C) No regularization
- D) Increase learning rate only

**Correct answer(s):** A
**Explanation:** L1 promotes sparsity, eliminating irrelevant coefficients.
**Why others are wrong:**
- B: L2 shrinks but rarely zeroes coefficients.
- C: Allows overfitting.
- D: Does not address feature elimination.

---
## Question 112 [D2] — Single
Logistic regression with highly correlated features: eliminate redundant predictors. Which regularization is MOST appropriate?
- A) L1 regularization (sparsity)
- B) Disable all regularization
- C) Use only S3 lifecycle
- D) Increase batch size only

**Correct answer(s):** A
**Explanation:** Exam pattern: eliminate redundant predictors → L1 sparsity (L2 stabilizes correlated weights but keeps all features).
**Why others are wrong:**
- B: Correlated features remain.
- C: Unrelated.
- D: Batch size does not remove features.

---
## Question 113 [D3] — Single
New training data uploaded to S3 should automatically invoke retraining and deployment via CI/CD. What is the FIRST step in the workflow?
- A) S3 event notification to invoke CodePipeline or Lambda
- B) S3 Lifecycle expiration rule only
- C) Delete the Model Registry
- D) Disable CloudTrail

**Correct answer(s):** A
**Explanation:** Event-driven pipelines start with S3 event notifications to orchestration.
**Why others are wrong:**
- B: Lifecycle manages storage class, not ML CI/CD trigger.
- C: Registry required for governance.
- D: Audit needed.

---
## Question 114 [D4] — Single
A GenAI app must block toxic outputs and filter PII in model responses on AWS. Which Bedrock feature helps?
- A) Bedrock Guardrails
- B) Amazon Macie only
- C) AWS Snowball
- D) Amazon EBS

**Correct answer(s):** A
**Explanation:** Guardrails apply safety and privacy filters to Bedrock model output.
**Why others are wrong:**
- B: Macie scans S3 data at rest, not live GenAI output filtering.
- C: Transfer device.
- D: Block storage.

---
## Question 115 [D1] — Single
MSK Provisioned vs MSK Serverless: when is Provisioned MORE appropriate?
- A) When you need fine-grained broker sizing and Kafka version control at scale with predictable throughput
- B) When you want zero Kafka compatibility
- C) When you only need S3 archival
- D) When you need DNS routing

**Correct answer(s):** A
**Explanation:** Provisioned clusters give control over broker capacity; Serverless for variable/ops-light Kafka.
**Why others are wrong:**
- B: Both are Kafka-compatible.
- C: Use Firehose/Glue for archival.
- D: Route 53 unrelated.

---
## Question 116 [D3] — Single
After approval in Model Registry, a model must reach production with traffic shifting. What components are involved?
- A) Approved model package + production variant on endpoint (possibly canary weights)
- B) Delete all CloudWatch alarms
- C) Public S3 ACL on artifacts
- D) Disable IAM

**Correct answer(s):** A
**Explanation:** Registry approval gates promotion; endpoints use production variants for traffic.
**Why others are wrong:**
- B: Monitoring required.
- C: Insecure.
- D: IAM required.

---
## Question 117 [D2] — Single
A team needs embeddings from Bedrock for RAG but wants AWS to manage chunking and retrieval orchestration. They should evaluate:
- A) Bedrock Knowledge Bases
- B) Amazon Polly
- C) AWS DeepRacer
- D) Amazon MQ only

**Correct answer(s):** A
**Explanation:** Knowledge Bases provide managed RAG ingestion, embedding, and retrieval for Bedrock.
**Why others are wrong:**
- B: Speech synthesis.
- C: RL toy.
- D: Message broker not RAG.

---
## Question 118 [D4] — Single
Centralized table permissions across accounts for analytics on a data lake are required. Which service?
- A) AWS Lake Formation
- B) Amazon Rekognition
- C) Amazon Transcribe
- D) AWS DeepRacer

**Correct answer(s):** A
**Explanation:** Lake Formation manages fine-grained permissions on data lake tables.
**Why others are wrong:**
- B: Vision.
- C: Speech.
- D: RL game.

---
## Question 119 [D3] — Single
Holiday flight promo inference: millions of users, seasonal spikes, minimal idle cost. Best endpoint type?
- A) Serverless inference
- B) Always-on ml.p4d.24xlarge real-time only
- C) Batch only for live clicks
- D) Amazon RDS read replica

**Correct answer(s):** A
**Explanation:** Spiky seasonal traffic fits serverless pay-per-use scaling.
**Why others are wrong:**
- B: Expensive idle capacity.
- C: Batch not for interactive promo clicks.
- D: Database not inference.

---
## Question 120 [D3] — Single
Online image/audio stories for passengers: large media, processing may take minutes, near-real-time acceptable with queue. Best choice?
- A) Asynchronous inference endpoint
- B) Real-time CPU endpoint with 10ms SLA
- C) SageMaker Ground Truth
- D) AWS Budgets

**Correct answer(s):** A
**Explanation:** Async handles large payloads and queued long-running inference.
**Why others are wrong:**
- B: Strict ms SLA wrong for minutes-long media jobs.
- C: Labeling service.
- D: Cost alerts.

---
