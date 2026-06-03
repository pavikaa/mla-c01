#!/usr/bin/env python3
"""Rewrite all practice questions with exam-realistic stems and distractors."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Full rewrites: id -> dict (stem, options, correct, explanation, wrongWhy, type?, domain?)
REWRITES = {
    16: {
        "stem": "A data scientist needs to run hundreds of training jobs to find optimal hyperparameters using Bayesian optimization. Which SageMaker capability should they use?",
        "options": {"A": "SageMaker Automatic Model Tuning (AMT)", "B": "SageMaker Autopilot", "C": "SageMaker Model Monitor", "D": "SageMaker Ground Truth"},
        "correct": ["A"],
        "explanation": "AMT performs hyperparameter optimization with Bayesian search and early stopping.",
        "wrongWhy": {"B": "Autopilot automates end-to-end model building, not tuning your existing estimator.", "C": "Model Monitor watches production endpoints.", "D": "Ground Truth is for labeling data."},
    },
    17: {
        "stem": "During training, loss stops improving and Debugger reports vanishing gradients. Which service helped detect this issue?",
        "options": {"A": "SageMaker Model Monitor", "B": "SageMaker Debugger", "C": "AWS CloudTrail", "D": "Amazon Macie"},
        "correct": ["B"],
        "explanation": "Debugger captures tensors and applies rules for convergence problems.",
        "wrongWhy": {"A": "Model Monitor is for production inference.", "C": "CloudTrail logs API activity.", "D": "Macie finds sensitive data in S3."},
    },
    18: {
        "stem": "A startup needs to detect objects in images via API without building custom CV models or managing training infrastructure. What should they use?",
        "options": {"A": "Train Image Classification built-in algorithm from scratch", "B": "Amazon SageMaker Data Wrangler", "C": "Amazon Rekognition", "D": "AWS Glue DataBrew"},
        "correct": ["C"],
        "explanation": "Rekognition provides pre-built computer vision APIs.",
        "wrongWhy": {"A": "Requires ML expertise and training ops.", "B": "Data prep tool, not inference API.", "D": "Visual ETL, not image detection API."},
    },
    19: {
        "stem": "An enterprise requires versioned model artifacts and manual approval before any model reaches production endpoints. Which feature addresses this?",
        "options": {"A": "SageMaker Experiments only", "B": "Amazon S3 versioning alone", "C": "AWS CodeDeploy", "D": "SageMaker Model Registry"},
        "correct": ["D"],
        "explanation": "Model Registry tracks versions, metadata, and approval status for deployment governance.",
        "wrongWhy": {"A": "Experiments track trials but not formal approval workflow.", "B": "S3 versioning lacks ML approval workflow.", "C": "CodeDeploy deploys applications, not ML registry governance."},
    },
    20: {
        "stem": "A fraud detection model has 0.5% positive class rate. Which evaluation metrics should the team prioritize?",
        "options": {"A": "F1 score, precision, and recall", "B": "Accuracy only", "C": "RMSE and MAE", "D": "R-squared"},
        "correct": ["A"],
        "explanation": "Imbalanced classification requires precision/recall/F1, not accuracy alone.",
        "wrongWhy": {"B": "Accuracy is misleading with extreme imbalance.", "C": "Regression metrics for classification.", "D": "R-squared is for regression."},
    },
    22: {
        "stem": "A bank wants to evaluate a new fraud model against the current production model without sending the new model's predictions to customers. What deployment pattern should they use?",
        "options": {"A": "Replace production variant with 100% traffic immediately", "B": "Add a shadow variant that receives copied inference requests", "C": "Delete the production endpoint", "D": "Use Batch Transform only"},
        "correct": ["B"],
        "explanation": "Shadow variants process duplicate traffic without affecting live responses.",
        "wrongWhy": {"A": "Immediate cutover risks customer impact.", "C": "Removes serving capability.", "D": "Batch is offline, not live A/B comparison."},
    },
    23: {
        "stem": "A team must train a custom PyTorch model on SageMaker and deploy it with a custom inference container. Which approach is required?",
        "options": {"A": "SageMaker Autopilot only", "B": "Built-in Linear Learner algorithm", "C": "Script mode with training code and an ECR inference image", "D": "Amazon Bedrock fine-tuning only"},
        "correct": ["C"],
        "explanation": "Script mode (BYO framework) plus ECR container is the standard custom model path.",
        "wrongWhy": {"A": "Autopilot does not support arbitrary custom PyTorch.", "B": "Linear Learner is tabular built-in.", "D": "Bedrock is for foundation models, not arbitrary PyTorch."},
    },
    24: {
        "stem": "A data scientist needs strong performance on large tabular classification datasets with minimal algorithm tuning. Which SageMaker built-in algorithm is often appropriate?",
        "options": {"A": "BlazingText", "B": "Object Detection", "C": "Seq2Seq", "D": "XGBoost"},
        "correct": ["D"],
        "explanation": "XGBoost is the common built-in choice for tabular classification/regression at scale.",
        "wrongWhy": {"A": "BlazingText is for text.", "B": "Object Detection is for images.", "C": "Seq2Seq is for sequence generation."},
    },
    25: {
        "stem": "Regulators require explaining which input features most influenced individual predictions from a SageMaker endpoint. Which tool should be used?",
        "options": {"A": "SageMaker Clarify with SHAP explanations", "B": "AWS CloudTrail", "C": "Amazon Athena", "D": "AWS Cost Explorer"},
        "correct": ["A"],
        "explanation": "Clarify provides SHAP-based feature attributions for explainability.",
        "wrongWhy": {"B": "Audit logs, not model explanations.", "C": "SQL query service.", "D": "Cost analysis tool."},
    },
    26: {
        "stem": "A model shows excellent training accuracy but poor validation performance. Which actions are MOST appropriate to reduce overfitting?",
        "options": {"A": "Remove the validation set", "B": "Apply regularization and gather more representative validation data", "C": "Increase model complexity only", "D": "Disable early stopping"},
        "correct": ["B"],
        "explanation": "Regularization and better validation data address overfitting.",
        "wrongWhy": {"A": "Validation is essential.", "C": "More complexity worsens overfitting.", "D": "Early stopping helps prevent overfitting."},
    },
    27: {
        "stem": "A company must extract entities and key phrases from support tickets without training custom NLP models. Which service should they choose?",
        "options": {"A": "Amazon Comprehend", "B": "Amazon Rekognition", "C": "SageMaker Neo", "D": "Amazon Kinesis Data Streams"},
        "correct": ["A"],
        "explanation": "Comprehend provides managed NLP entity and phrase extraction.",
        "wrongWhy": {"B": "Vision service.", "C": "Neo compiles models for edge.", "D": "Streaming ingestion."},
    },
    28: {
        "stem": "What is the PRIMARY difference between SageMaker Autopilot and SageMaker Automatic Model Tuning (AMT)?",
        "options": {"A": "AMT only works with images", "B": "Autopilot requires manual endpoint creation only", "C": "They are identical services", "D": "Autopilot automates end-to-end model building; AMT tunes hyperparameters of your chosen estimator"},
        "correct": ["D"],
        "explanation": "Autopilot is AutoML pipeline; AMT optimizes hyperparameters for an algorithm you specify.",
        "wrongWhy": {"A": "AMT works with many algorithms.", "B": "Autopilot can propose deployment steps.", "C": "Different purposes."},
    },
    29: {
        "stem": "An application sends predictions sporadically (a few times per hour) and the team wants minimal instance fleet management with pay-per-inference pricing. Which deployment option is BEST?",
        "options": {"A": "SageMaker serverless inference", "B": "Real-time endpoint with 24/7 ml.g5.12xlarge instances", "C": "SageMaker Batch Transform on a schedule", "D": "Multi-AZ Amazon RDS"},
        "correct": ["A"],
        "explanation": "Serverless inference scales to zero between requests and charges per invocation.",
        "wrongWhy": {"B": "Always-on instances are costly for sporadic traffic.", "C": "Batch is for bulk offline scoring, not interactive sporadic API calls.", "D": "RDS is a database, not model hosting."},
    },
    30: {
        "stem": "A computer vision app uploads 100 GB image batches and can wait up to 24 hours for results using a queue-based pattern. Which inference approach fits BEST?",
        "options": {"A": "Real-time endpoint with auto scaling", "B": "Asynchronous SageMaker endpoint with S3 input/output", "C": "SageMaker serverless inference with 1 MB payload limit", "D": "Amazon API Gateway HTTP proxy only"},
        "correct": ["B"],
        "explanation": "Async endpoints queue large payloads and write results to S3.",
        "wrongWhy": {"A": "Real-time is for low-latency steady traffic, not 100 GB batches.", "C": "Serverless has payload/memory limits.", "D": "API Gateway does not host models."},
    },
    31: {
        "stem": "A retailer must score 10 million customer records nightly with no persistent inference endpoint. What should they use?",
        "options": {"A": "SageMaker real-time endpoint", "B": "Amazon Lex bot", "C": "SageMaker Batch Transform reading from and writing to S3", "D": "AWS Lambda with 15-minute timeout for each record individually"},
        "correct": ["C"],
        "explanation": "Batch Transform processes large offline datasets without a standing endpoint.",
        "wrongWhy": {"A": "Real-time endpoints are for online inference.", "B": "Lex is conversational AI.", "D": "Lambda is not suited for bulk scoring millions of rows."},
    },
    32: {
        "stem": "An MLOps team needs a native AWS DAG to chain data processing, training, evaluation, and conditional deployment steps with artifact caching. Which service should they use?",
        "options": {"A": "Amazon SNS", "B": "Amazon SQS", "C": "AWS Step Functions only without SageMaker integration", "D": "SageMaker Pipelines"},
        "correct": ["D"],
        "explanation": "SageMaker Pipelines is the ML-native orchestration DAG on AWS.",
        "wrongWhy": {"A": "SNS is pub/sub notifications.", "B": "SQS is a message queue.", "C": "Step Functions can orchestrate but Pipelines is ML-first with step caching."},
    },
    33: {
        "stem": "A team wants to shift a small percentage of live traffic to a new model variant before full rollout to limit blast radius. Which strategy matches this requirement?",
        "options": {"A": "Canary deployment with gradual traffic increase", "B": "Immediate blue/green cutover of 100% traffic day one", "C": "Delete the old model artifact from S3", "D": "Train a second model on unlabeled data only"},
        "correct": ["A"],
        "explanation": "Canary gradually increases traffic to the new variant.",
        "wrongWhy": {"B": "Full immediate cutover is higher risk.", "C": "Deleting artifacts is not a traffic strategy.", "D": "Unlabeled-only training is unrelated."},
    },
    35: {
        "stem": "A manufacturer must compile and optimize an ML model to run on constrained edge devices with limited compute. Which SageMaker feature should they use?",
        "options": {"A": "SageMaker Ground Truth", "B": "SageMaker Neo", "C": "SageMaker Autopilot", "D": "Amazon Kendra"},
        "correct": ["B"],
        "explanation": "Neo compiles models for edge deployment targets.",
        "wrongWhy": {"A": "Labeling service.", "C": "AutoML.", "D": "Enterprise search."},
    },
    36: {
        "stem": "Before production launch, an team wants load tests and instance type recommendations for a new deep learning endpoint. Which tool should they use?",
        "options": {"A": "AWS Trusted Advisor only", "B": "Amazon Macie", "C": "SageMaker Inference Recommender", "D": "AWS Artifact compliance reports"},
        "correct": ["C"],
        "explanation": "Inference Recommender runs load tests and suggests instance configurations.",
        "wrongWhy": {"A": "Trusted Advisor gives broad best practices, not model-specific load tests.", "B": "Macie is for data security.", "D": "Artifact provides compliance documents."},
    },
    37: {
        "stem": "A company hosts dozens of small models that share similar latency profiles and wants to reduce costs by sharing GPU infrastructure on one endpoint. What should they deploy?",
        "options": {"A": "Separate real-time endpoint per model", "B": "Amazon S3 Glacier", "C": "AWS DataSync", "D": "SageMaker multi-model endpoint"},
        "correct": ["D"],
        "explanation": "Multi-model endpoints host multiple models on shared inference instances.",
        "wrongWhy": {"A": "Many endpoints increase cost and ops.", "B": "Archival storage.", "C": "Data transfer service."},
    },
    38: {
        "stem": "Developers push code to Git and need an automated workflow to build containers, run tests, and trigger SageMaker training when main branch updates. Which service orchestrates this?",
        "options": {"A": "AWS CodePipeline integrated with CodeBuild and SageMaker", "B": "Amazon CloudFront", "C": "AWS Snowball", "D": "Amazon ElastiCache"},
        "correct": ["A"],
        "explanation": "CodePipeline orchestrates CI/CD stages including builds and SageMaker job triggers.",
        "wrongWhy": {"B": "CDN.", "C": "Offline data transfer.", "D": "In-memory cache."},
    },
    39: {
        "stem": "Security policy requires SageMaker inference in private subnets with no direct internet access, using interface endpoints for AWS service traffic. What must be configured?",
        "options": {"A": "Public subnet endpoint with 0.0.0.0/0 security group", "B": "VPC configuration with private subnets, security groups, and VPC endpoints", "C": "Disable IAM entirely", "D": "Store models in a public S3 bucket"},
        "correct": ["B"],
        "explanation": "VPC mode isolates endpoints; VPC endpoints allow private AWS API access.",
        "wrongWhy": {"A": "Violates private-only requirement.", "C": "IAM is required for SageMaker.", "D": "Public buckets violate security policy."},
    },
    40: {
        "stem": "An enterprise already standardized on Apache Airflow DAGs and needs a managed AWS service to run them. Which option should they select?",
        "options": {"A": "Amazon MWAA (Managed Workflows for Apache Airflow)", "B": "Amazon SQS", "C": "Amazon SNS", "D": "AWS Amplify"},
        "correct": ["A"],
        "explanation": "MWAA is the managed Airflow offering on AWS.",
        "wrongWhy": {"B": "Message queue.", "C": "Notifications.", "D": "Front-end hosting."},
    },
    41: {
        "stem": "In production, input feature distributions drift compared to training baselines. Which SageMaker Model Monitor type should alert the team?",
        "options": {"A": "Model Monitor — data quality", "B": "AWS Budgets", "C": "Amazon Polly", "D": "AWS CloudFormation drift detection only"},
        "correct": ["A"],
        "explanation": "Data quality monitoring compares live features to baseline statistics.",
        "wrongWhy": {"B": "Budgets track spend.", "C": "Text-to-speech.", "D": "CloudFormation drift is for infrastructure templates, not ML features."},
    },
    42: {
        "stem": "Compliance requires an immutable record of who created or updated SageMaker endpoints and training jobs. Which service provides this?",
        "options": {"A": "AWS CloudTrail", "B": "Amazon CloudWatch metrics only", "C": "SageMaker Model Monitor", "D": "Amazon Personalize"},
        "correct": ["A"],
        "explanation": "CloudTrail logs AWS API calls for audit.",
        "wrongWhy": {"B": "Metrics lack detailed API caller audit trail.", "C": "Monitors model quality in production.", "D": "Recommendation service."},
    },
    43: {
        "stem": "Finance needs email alerts when total SageMaker spend exceeds $50,000 in a month. What should they configure?",
        "options": {"A": "SageMaker Debugger", "B": "AWS Budgets with cost alerts", "C": "Amazon GuardDuty", "D": "SageMaker Feature Store"},
        "correct": ["B"],
        "explanation": "AWS Budgets supports threshold alerts on spend.",
        "wrongWhy": {"A": "Training debugger.", "C": "Threat detection.", "D": "Feature storage."},
    },
    44: {
        "stem": "A SageMaker notebook must read only specific S3 prefixes and decrypt artifacts with a specific KMS key. What implements least privilege?",
        "options": {"A": "Attach AdministratorAccess to all users", "B": "Use a public S3 ACL", "C": "IAM execution role with scoped policies for S3 prefixes and KMS keys", "D": "Disable encryption"},
        "correct": ["C"],
        "explanation": "Scoped IAM roles enforce least privilege for notebooks and jobs.",
        "wrongWhy": {"A": "AdministratorAccess violates least privilege.", "B": "Public ACLs are insecure.", "D": "Encryption should remain enabled."},
    },
    45: {
        "stem": "When Model Monitor detects data drift beyond a threshold, an automated retraining pipeline must start. Which integration is MOST appropriate?",
        "options": {"A": "Manual weekly spreadsheet review", "B": "Amazon Rekognition", "C": "Disable Model Monitor", "D": "Amazon EventBridge rule triggering a SageMaker Pipeline"},
        "correct": ["D"],
        "explanation": "EventBridge can react to Monitor alerts and invoke Pipelines.",
        "wrongWhy": {"A": "Not automated.", "B": "Unrelated vision API.", "C": "Removes detection capability."},
    },
    46: {
        "stem": "Two model versions should receive 90% and 10% of live inference traffic on the same endpoint for comparison. How is this configured?",
        "options": {"A": "Production variant traffic weights", "B": "Delete the older model from ECR", "C": "Use S3 lifecycle policies", "D": "Enable S3 Transfer Acceleration"},
        "correct": ["A"],
        "explanation": "Production variants support weighted traffic splits for A/B tests.",
        "wrongWhy": {"B": "Deleting images breaks rollback.", "C": "S3 lifecycle is storage tiering.", "D": "Transfer Acceleration is upload speed."},
    },
    48: {
        "stem": "Operations needs dashboards and alarms when endpoint ModelLatency exceeds 500 ms. Which services should they use?",
        "options": {"A": "Amazon Macie", "B": "Amazon CloudWatch metrics and alarms", "C": "AWS Artifact", "D": "Amazon Translate"},
        "correct": ["B"],
        "explanation": "CloudWatch captures SageMaker endpoint latency metrics and supports alarms.",
        "wrongWhy": {"A": "PII discovery.", "C": "Compliance documents.", "D": "Translation API."},
    },
    49: {
        "stem": "FinOps must break down ML spending by cost center using resource tags across accounts. Which tool should they use?",
        "options": {"A": "SageMaker Debugger", "B": "Amazon Lex", "C": "AWS Cost Explorer with cost allocation tags", "D": "SageMaker Ground Truth"},
        "correct": ["C"],
        "explanation": "Cost Explorer analyzes spend filtered by tags.",
        "wrongWhy": {"A": "Training debug tool.", "B": "Chatbot service.", "D": "Labeling."},
    },
    50: {
        "stem": "An engineer enables SageMaker Model Monitor on an endpoint but no constraints trigger. What prerequisite is MOST likely missing?",
        "options": {"A": "A baseline dataset with statistics from training or prior production data", "B": "Public internet on the endpoint", "C": "Deleting CloudWatch logs", "D": "Disabling the execution role"},
        "correct": ["A"],
        "explanation": "Model Monitor requires a baseline to compare production data against.",
        "wrongWhy": {"B": "Internet not required for baselines.", "C": "Logs help troubleshooting.", "D": "Execution role is required."},
    },
    51: {
        "stem": "A startup merges daily clickstream from Kinesis with customer profiles in S3 Parquet using minimal custom code. Which service is BEST?",
        "options": {"A": "Amazon SNS", "B": "AWS Glue ETL job", "C": "Amazon Route 53", "D": "AWS WAF"},
        "correct": ["B"],
        "explanation": "Glue provides serverless Spark ETL to join streaming/batch sources.",
        "wrongWhy": {"A": "Notifications only.", "C": "DNS.", "D": "Web firewall."},
    },
    52: {
        "stem": "A data scientist builds visual data prep recipes and must export them into an automated SageMaker Pipeline. Which tool supports this workflow?",
        "options": {"A": "Amazon Athena", "B": "AWS CloudTrail", "C": "SageMaker Data Wrangler", "D": "Amazon Polly"},
        "correct": ["C"],
        "explanation": "Data Wrangler exports recipes to Python or Pipeline steps.",
        "wrongWhy": {"A": "SQL queries only.", "B": "Audit logs.", "D": "Speech synthesis."},
    },
    53: {
        "stem": "A multi-account data lake needs centralized table-level permissions and governance. Which service should be used?",
        "options": {"A": "Amazon API Gateway", "B": "Amazon CloudFront", "C": "AWS Lambda", "D": "AWS Lake Formation"},
        "correct": ["D"],
        "explanation": "Lake Formation manages fine-grained data lake access.",
        "wrongWhy": {"A": "API management.", "B": "CDN.", "C": "Functions, not lake governance layer."},
    },
    55: {
        "stem": "A housing price regression model must penalize large prediction errors more than small ones. Which metric is MOST appropriate?",
        "options": {"A": "Root Mean Square Error (RMSE)", "B": "Accuracy", "C": "F1 score", "D": "Top-5 categorical accuracy"},
        "correct": ["A"],
        "explanation": "RMSE squares errors, penalizing large mistakes.",
        "wrongWhy": {"B": "Classification metric.", "C": "Classification metric.", "D": "Multi-class classification metric."},
    },
    56: {
        "stem": "Training on a single GPU instance would take two weeks. The team wants to reduce wall-clock time using multiple GPUs across instances. What should they enable?",
        "options": {"A": "SageMaker distributed training", "B": "Amazon S3 Glacier archival", "C": "Disable checkpointing", "D": "Use only AWS Lambda"},
        "correct": ["A"],
        "explanation": "SageMaker supports distributed data-parallel training across instances.",
        "wrongWhy": {"B": "Archival storage.", "C": "Checkpointing helps Spot recovery.", "D": "Lambda cannot run multi-week GPU training."},
    },
    57: {
        "stem": "A mobile app needs speech-to-text with no model training or endpoint management by the app team. Which AWS service fits?",
        "options": {"A": "Amazon SageMaker Neo", "B": "Amazon Transcribe", "C": "Amazon Fraud Detector", "D": "AWS Outposts"},
        "correct": ["B"],
        "explanation": "Transcribe is the managed speech-to-text API.",
        "wrongWhy": {"A": "Edge compilation.", "C": "Fraud ML service.", "D": "On-premises AWS hardware."},
    },
    58: {
        "stem": "A team runs dozens of training trials with different hyperparameters and must compare metrics and artifacts centrally. Which SageMaker feature helps?",
        "options": {"A": "SageMaker Ground Truth", "B": "Amazon Macie", "C": "AWS Budgets", "D": "SageMaker Experiments"},
        "correct": ["D"],
        "explanation": "Experiments organizes trials, parameters, and metrics.",
        "wrongWhy": {"A": "Labeling.", "B": "PII scanning.", "C": "Cost alerts."},
    },
    59: {
        "stem": "Validation AUC stops improving for several epochs during training. Which built-in mechanism should stop training to save cost?",
        "options": {"A": "Early stopping based on validation metric plateau", "B": "Delete the training dataset", "C": "Disable automatic model tuning", "D": "Remove IAM roles"},
        "correct": ["A"],
        "explanation": "Early stopping halts training when validation metrics plateau.",
        "wrongWhy": {"B": "Destroys training data.", "C": "AMT is separate from early stopping.", "D": "IAM is required."},
    },
    60: {
        "stem": "An API requires steady p99 latency under 50 ms at thousands of requests per second. Which deployment is MOST appropriate?",
        "options": {"A": "SageMaker Batch Transform nightly", "B": "Real-time endpoint with auto scaling on appropriate instance types", "C": "SageMaker serverless inference only", "D": "AWS Snowball Edge"},
        "correct": ["B"],
        "explanation": "Real-time provisioned endpoints with auto scaling meet strict low-latency SLAs.",
        "wrongWhy": {"A": "Batch is offline.", "C": "Serverless has cold start and concurrency limits.", "D": "Migration appliance."},
    },
    61: {
        "stem": "Infrastructure engineers want to provision a SageMaker Studio domain using version-controlled templates integrated with their Git repo. Which tools are appropriate?",
        "options": {"A": "AWS CloudFormation or AWS CDK", "B": "Amazon Rekognition", "C": "Amazon Polly", "D": "AWS DeepRacer"},
        "correct": ["A"],
        "explanation": "CloudFormation and CDK provide IaC for Studio and supporting resources.",
        "wrongWhy": {"B": "Vision API.", "C": "Speech.", "D": "Reinforcement learning toy car."},
    },
    62: {
        "stem": "An application team deploys EC2-based services and needs blue/green deployments with traffic shifting at the application deployment layer. Which AWS service is designed for this?",
        "options": {"A": "SageMaker Model Monitor", "B": "Amazon S3 Intelligent-Tiering", "C": "AWS Glue DataBrew", "D": "AWS CodeDeploy"},
        "correct": ["D"],
        "explanation": "CodeDeploy supports blue/green and in-place deployment patterns for compute.",
        "wrongWhy": {"A": "ML monitoring.", "B": "Storage class automation.", "C": "Data prep."},
    },
    63: {
        "stem": "A retraining SageMaker Pipeline must run every Sunday at 2:00 AM UTC automatically. What should trigger it?",
        "options": {"A": "Amazon EventBridge scheduled rule", "B": "Manual console click only", "C": "Amazon CloudFront cache invalidation", "D": "AWS Artifact download"},
        "correct": ["A"],
        "explanation": "EventBridge cron schedules automate Pipeline execution.",
        "wrongWhy": {"B": "Not automated.", "C": "CDN operation.", "D": "Compliance PDFs."},
    },
    65: {
        "stem": "Model Monitor reports increasing bias metrics across demographic facets compared to baseline. Which monitor type is this?",
        "options": {"A": "Data quality only", "B": "Bias drift monitoring", "C": "AWS Cost Explorer", "D": "S3 lifecycle transition"},
        "correct": ["B"],
        "explanation": "Bias drift tracks fairness metric changes over time.",
        "wrongWhy": {"A": "Data quality tracks feature stats, not fairness facets.", "C": "Cost tool.", "D": "Storage policy."},
    },
    66: {
        "stem": "Microservices around a SageMaker endpoint show high end-to-end latency and the team needs distributed tracing across calls. Which service should they enable?",
        "options": {"A": "AWS X-Ray", "B": "Amazon Macie", "C": "AWS Artifact", "D": "Amazon Mechanical Turk"},
        "correct": ["A"],
        "explanation": "X-Ray traces requests across services.",
        "wrongWhy": {"B": "S3 security.", "C": "Compliance reports.", "D": "Crowd workforce."},
    },
    67: {
        "stem": "Training jobs consistently use only 20% of provisioned CPU on ml.m5.4xlarge instances. Which AWS service recommends better instance choices?",
        "options": {"A": "Amazon Rekognition", "B": "Amazon Translate", "C": "Amazon Polly", "D": "AWS Compute Optimizer"},
        "correct": ["D"],
        "explanation": "Compute Optimizer rightsizing recommendations use utilization history.",
        "wrongWhy": {"A": "Vision.", "B": "Translation.", "C": "Speech."},
    },
    68: {
        "stem": "Security requires customer-managed keys for all model artifacts stored in Amazon S3. What encryption should be configured?",
        "options": {"A": "SSE-KMS with a customer managed key (CMK)", "B": "No encryption to improve performance", "C": "HTTP without TLS for internal traffic only", "D": "Public-read ACL on the bucket"},
        "correct": ["A"],
        "explanation": "SSE-KMS with CMK meets customer-managed encryption requirements.",
        "wrongWhy": {"B": "Violates policy.", "C": "TLS required in transit.", "D": "Public ACL is insecure."},
    },
    69: {
        "stem": "A model artifact bucket must never be accessible from the public internet. Which controls should be applied?",
        "options": {"A": "Enable anonymous read on bucket policy", "B": "S3 Block Public Access, bucket policy deny public principals, and least-privilege IAM", "C": "Share root account access keys with the team", "D": "Disable versioning"},
        "correct": ["B"],
        "explanation": "Block Public Access plus restrictive policies and IAM prevent public exposure.",
        "wrongWhy": {"A": "Allows public access.", "C": "Root keys are a critical security risk.", "D": "Versioning aids recovery."},
    },
    70: {
        "stem": "An analyst needs to run ad-hoc SQL queries directly on data stored in S3 without provisioning a cluster. Which service should they use?",
        "options": {"A": "Amazon EMR always-on cluster", "B": "Amazon Redshift provisioned warehouse only", "C": "Amazon Athena", "D": "AWS Snowmobile"},
        "correct": ["C"],
        "explanation": "Athena is serverless SQL over S3.",
        "wrongWhy": {"A": "Cluster ops overhead.", "B": "Warehouse for sustained analytics workloads.", "D": "Exabyte-scale physical transfer."},
    },
    71: {
        "stem": "An e-commerce site needs real-time product recommendations without building custom collaborative filtering infrastructure. Which service fits?",
        "options": {"A": "Amazon Personalize", "B": "Amazon Textract", "C": "AWS Glue Data Quality", "D": "Amazon Macie"},
        "correct": ["A"],
        "explanation": "Personalize provides real-time recommendation campaigns.",
        "wrongWhy": {"B": "Document OCR.", "C": "Data validation rules.", "D": "PII discovery."},
    },
    72: {
        "stem": "A insurance firm must extract tables and text from scanned PDF claim forms automatically. Which service should they use?",
        "options": {"A": "Amazon Textract", "B": "Amazon Polly", "C": "Amazon Kendra", "D": "AWS DeepRacer"},
        "correct": ["A"],
        "explanation": "Textract extracts text and structured data from documents.",
        "wrongWhy": {"B": "Speech output.", "C": "Enterprise search.", "D": "RL toy."},
    },
    73: {
        "stem": "Lightweight event-driven preprocessing (thumbnail generation, JSON validation) must run when objects land in S3. What is the BEST fit?",
        "options": {"A": "SageMaker multi-GPU training cluster", "B": "AWS Lambda triggered by S3 events", "C": "Amazon Redshift Spectrum only", "D": "SageMaker Batch Transform"},
        "correct": ["B"],
        "explanation": "Lambda handles small event-driven transforms efficiently.",
        "wrongWhy": {"A": "Overkill for light preprocessing.", "C": "Analytics SQL engine.", "D": "Bulk batch scoring."},
    },
    74: {
        "stem": "A BERT model requires GPU inference 24/7 at high throughput with predictable latency. Why is AWS Lambda a poor choice?",
        "options": {"A": "Lambda cannot meet sustained GPU inference and memory needs for large transformers", "B": "Lambda is always cheaper for GPU workloads", "C": "Lambda automatically scales GPU memory to 2 TB", "D": "Lambda hosts multi-model endpoints natively"},
        "correct": ["A"],
        "explanation": "Lambda has limits on duration, memory, and no GPU; real-time GPU endpoints are appropriate.",
        "wrongWhy": {"B": "GPU inference at scale is not Lambda's strength.", "C": "Lambda memory cap is far below 2 TB and no GPU.", "D": "Multi-model endpoints are SageMaker feature."},
    },
    75: {
        "stem": "Engineers need to search application inference logs for ERROR patterns and stack traces. Which service should they use?",
        "options": {"A": "AWS CloudTrail only", "B": "Amazon S3 Glacier", "C": "Amazon Route 53", "D": "Amazon CloudWatch Logs (and Logs Insights)"},
        "correct": ["D"],
        "explanation": "CloudWatch Logs stores and queries application log data.",
        "wrongWhy": {"A": "CloudTrail is API audit, not app log search.", "B": "Archival.", "C": "DNS."},
    },
    76: {
        "stem": "Streaming data must be delivered near-real-time to Amazon S3 and Amazon Redshift without writing custom consumers. Which service is appropriate?",
        "options": {"A": "Amazon Kinesis Data Firehose", "B": "AWS Snowball", "C": "Amazon EBS snapshots", "D": "AWS Artifact"},
        "correct": ["A"],
        "explanation": "Firehose is fully managed delivery to S3, Redshift, OpenSearch, etc.",
        "wrongWhy": {"B": "Offline transfer.", "C": "Block storage backup.", "D": "Compliance downloads."},
    },
    77: {
        "stem": "A classification model has high precision but low recall. What does this typically indicate?",
        "options": {"A": "The model always predicts the majority class", "B": "Among positive predictions, many are wrong (false positives) relative to missed positives", "C": "RMSE is zero", "D": "The dataset has no labels"},
        "correct": ["B"],
        "explanation": "High precision + low recall often means few false positives but many false negatives (missed positives).",
        "wrongWhy": {"A": "Describes high recall bias toward majority, not this pattern.", "C": "Regression metric.", "D": "Labels exist for supervised learning."},
    },
    78: {
        "stem": "A data science team combines multiple models' predictions to improve overall accuracy. Which technique are they using?",
        "options": {"A": "Model ensembling (stacking/boosting/bagging)", "B": "S3 lifecycle expiration", "C": "VPC peering", "D": "IAM password rotation"},
        "correct": ["A"],
        "explanation": "Ensembling merges models to improve performance.",
        "wrongWhy": {"B": "Storage management.", "C": "Networking.", "D": "Identity hygiene unrelated."},
    },
    79: {
        "stem": "A SageMaker Pipeline should deploy to production only if validation accuracy exceeds 0.80; otherwise it must stop. How is this implemented?",
        "options": {"A": "Unconditional Deploy step always", "B": "Delete the training data", "C": "Disable Model Registry", "D": "Conditional pipeline step based on metric threshold"},
        "correct": ["D"],
        "explanation": "Pipelines support conditional steps on property values like accuracy.",
        "wrongWhy": {"A": "Ignores quality gate.", "B": "Destroys data.", "C": "Registry supports governance."},
    },
    80: {
        "stem": "A new AWS account wants automated checks for over-provisioned EC2 and idle resources related to ML workloads. Which service provides these recommendations?",
        "options": {"A": "AWS Trusted Advisor", "B": "Amazon Polly", "C": "Amazon Lex", "D": "AWS DeepRacer"},
        "correct": ["A"],
        "explanation": "Trusted Advisor flags cost and performance improvements.",
        "wrongWhy": {"B": "Speech.", "C": "Chatbot.", "D": "RL game."},
    },
    81: {
        "stem": "Case study: A bank loads daily Parquet into S3 for ML features and must scan for GDPR-related PII before loading into Feature Store. What is the FIRST step?",
        "options": {"A": "Deploy endpoint before any data checks", "B": "Run Amazon Macie to discover sensitive data, then transform/redact as needed", "C": "Disable all encryption", "D": "Make the bucket public for faster ingestion"},
        "correct": ["B"],
        "explanation": "Macie discovers PII; remediation occurs before Feature Store ingestion.",
        "wrongWhy": {"A": "Skips compliance.", "C": "Weakens security.", "D": "Public bucket violates policy."},
    },
    82: {
        "stem": "Case study: A startup needs a generative chatbot quickly without managing training clusters. Which service is MOST appropriate?",
        "options": {"A": "Train a transformer from scratch on Spot CPUs only", "B": "Amazon S3 Glacier Deep Archive", "C": "Amazon Bedrock foundation models", "D": "AWS Snowball Edge"},
        "correct": ["C"],
        "explanation": "Bedrock exposes FMs via API with minimal infrastructure.",
        "wrongWhy": {"A": "Slow and ops-heavy.", "B": "Archival storage.", "D": "Edge transfer device."},
    },
    83: {
        "stem": "Case study: A mobile app sends user batches twice per day for churn scoring; latency of several hours is acceptable. Which inference pattern fits?",
        "options": {"A": "Real-time endpoint with auto scaling", "B": "SageMaker serverless for sub-10ms latency", "C": "Amazon Lex", "D": "SageMaker Batch Transform"},
        "correct": ["D"],
        "explanation": "Batch Transform handles periodic bulk scoring without online endpoints.",
        "wrongWhy": {"A": "Unnecessary cost for twice-daily batch.", "B": "Serverless still online API model.", "C": "Conversational bot."},
    },
    84: {
        "stem": "Case study: Model accuracy drops after a marketing campaign changes the customer mix in production data. What should the MLOps team do FIRST?",
        "options": {"A": "Detect data drift, investigate features, and trigger retraining pipeline if needed", "B": "Delete CloudWatch logs", "C": "Remove Model Monitor baselines", "D": "Turn off encryption"},
        "correct": ["A"],
        "explanation": "Distribution shift is data drift; Monitor + retrain is the operational response.",
        "wrongWhy": {"B": "Removes observability.", "C": "Baselines required for Monitor.", "D": "Security regression."},
    },
    85: {
        "stem": "A categorical column has 10,000 unique values. Why might one-hot encoding be problematic?",
        "options": {"A": "It creates a very high-dimensional sparse feature space", "B": "It always improves GPU utilization", "C": "It is required for all SageMaker built-in algorithms", "D": "It encrypts data at rest"},
        "correct": ["A"],
        "explanation": "High cardinality one-hot explodes dimensionality and sparsity.",
        "wrongWhy": {"B": "Unrelated to encoding choice.", "C": "Not always required; embeddings or hashing may be better.", "D": "Encoding is not encryption."},
    },
    86: {
        "stem": "L2 regularization in a neural network primarily helps prevent which problem?",
        "options": {"A": "Large weights contributing to overfitting", "B": "S3 transfer failures", "C": "VPC DNS resolution", "D": "Kinesis shard throttling"},
        "correct": ["A"],
        "explanation": "L2 (weight decay) penalizes large weights to reduce overfitting.",
        "wrongWhy": {"B": "Network/storage issue.", "C": "Networking.", "D": "Streaming limits."},
    },
    87: {
        "stem": "A CI/CD pipeline blocks deployment when ECR image vulnerability scanning fails. Why is this a best practice?",
        "options": {"A": "It slows releases unnecessarily without benefit", "B": "It guarantees higher AWS bills only", "C": "It prevents known-vulnerable containers from reaching production", "D": "It replaces IAM entirely"},
        "correct": ["C"],
        "explanation": "Image scanning enforces security compliance before deploy.",
        "wrongWhy": {"A": "Security benefit outweighs delay.", "B": "Not about billing.", "D": "IAM still required."},
    },
    88: {
        "stem": "A team runs steady SageMaker training and inference year-round. Which purchasing option can reduce compute cost with a spend commitment?",
        "options": {"A": "SageMaker Savings Plans or Compute Savings Plans", "B": "Delete all CloudWatch alarms", "C": "Use only Spot for real-time low-latency endpoints", "D": "Disable auto scaling on all endpoints"},
        "correct": ["A"],
        "explanation": "Savings Plans provide discounted rates for consistent compute usage.",
        "wrongWhy": {"B": "Removes observability.", "C": "Spot unsuitable for strict latency SLAs.", "D": "Auto scaling optimizes cost and performance."},
    },
    89: {
        "stem": "A labeling workflow needs to integrate a human workforce for custom tasks within SageMaker. Which approach is valid?",
        "options": {"A": "Use SageMaker Ground Truth with private or vendor workforce", "B": "Use only Amazon CloudFront", "C": "Label data by renaming S3 buckets", "D": "Use AWS Artifact for bounding boxes"},
        "correct": ["A"],
        "explanation": "Ground Truth orchestrates labeling including Mechanical Turk or private workforces.",
        "wrongWhy": {"B": "CDN.", "C": "Bucket names are not labels.", "D": "Artifact is compliance documentation."},
    },
    90: {
        "stem": "A data scientist visualizes true vs predicted classes across categories using color grids. Which artifact are they likely using?",
        "options": {"A": "S3 lifecycle policy", "B": "IAM policy simulator", "C": "Confusion matrix heat map", "D": "VPC flow logs only"},
        "correct": ["C"],
        "explanation": "Heat maps visualize confusion matrices for classification evaluation.",
        "wrongWhy": {"A": "Storage management.", "B": "IAM testing tool.", "D": "Network traffic logs."},
    },
    91: {
        "stem": "Endpoint auto scaling is configured with target invocations per instance. What problem does this policy address?",
        "options": {"A": "Growing request volume requiring more instances", "B": "Encrypting data at rest", "C": "Labeling images", "D": "Compiling models with Neo"},
        "correct": ["A"],
        "explanation": "Scaling on invocations per instance adds capacity as traffic grows.",
        "wrongWhy": {"B": "Encryption separate concern.", "C": "Ground Truth task.", "D": "Neo compilation."},
    },
    92: {
        "stem": "Business stakeholders need dashboards for model KPIs without writing SQL on raw logs. Which AWS service is appropriate?",
        "options": {"A": "Amazon QuickSight dashboards fed from metrics or datasets", "B": "AWS Snowball", "C": "Amazon Inspector", "D": "AWS DeepRacer"},
        "correct": ["A"],
        "explanation": "QuickSight builds business-facing dashboards.",
        "wrongWhy": {"B": "Transfer appliance.", "C": "Vulnerability scanning.", "D": "RL game."},
    },
    93: {
        "stem": "A team has limited labeled data for a task similar to a pre-trained model in JumpStart. What approach is MOST efficient?",
        "options": {"A": "Fine-tune the JumpStart pre-trained model", "B": "Train billions of parameters from random init on CPU", "C": "Delete validation data", "D": "Use only Batch Transform for training"},
        "correct": ["A"],
        "explanation": "Fine-tuning transfer learns from pre-trained weights with fewer labels.",
        "wrongWhy": {"B": "Impractical and poor results.", "C": "Validation required.", "D": "Batch Transform is inference."},
    },
    94: {
        "stem": "An architecture must coordinate Lambda preprocessing, a SageMaker Processing job, and SNS notification in sequence. Which service orchestrates this?",
        "options": {"A": "Amazon Macie", "B": "Amazon Polly", "C": "AWS Step Functions", "D": "Amazon Glacier"},
        "correct": ["C"],
        "explanation": "Step Functions orchestrates multi-service workflows with state machines.",
        "wrongWhy": {"A": "PII service.", "B": "Speech.", "D": "Archival."},
    },
    95: {
        "stem": "Compliance requires encryption of SageMaker training volumes and model artifacts at rest. Which service manages keys?",
        "options": {"A": "Amazon Route 53", "B": "Amazon API Gateway", "C": "Amazon CloudFront", "D": "AWS KMS integrated with SageMaker and S3"},
        "correct": ["D"],
        "explanation": "KMS provides CMKs for encrypting EBS and S3 artifacts.",
        "wrongWhy": {"A": "DNS.", "B": "API management.", "C": "CDN."},
    },
    96: {
        "stem": "Training I/O is bottlenecked on a single EBS volume attached to the training instance. Which EBS feature improves throughput?",
        "options": {"A": "Provisioned IOPS (io2) volumes sized for required IOPS", "B": "Disable encryption", "C": "Use S3 Glacier for active training input", "D": "Remove the training job"},
        "correct": ["A"],
        "explanation": "Provisioned IOPS volumes deliver consistent high I/O for training.",
        "wrongWhy": {"B": "Security requirement often mandates encryption.", "C": "Glacier not for hot training data.", "D": "Does not fix I/O."},
    },
    97: {
        "stem": "A model fine-tuned sequentially on new tasks forgets earlier tasks. This phenomenon is known as:",
        "options": {"A": "Catastrophic forgetting", "B": "S3 eventual consistency", "C": "VPC peering", "D": "Kinesis resharding"},
        "correct": ["A"],
        "explanation": "Catastrophic forgetting occurs when new training overwrites prior task knowledge.",
        "wrongWhy": {"B": "Storage behavior.", "C": "Networking.", "D": "Stream scaling."},
    },
    98: {
        "stem": "A company uses long-lived Git branches and merges to main trigger production ML pipelines. Which workflow concept does this describe?",
        "options": {"A": "GitFlow-style branching integrated with CI/CD triggers", "B": "Deleting all Git history", "C": "Storing models only in CloudTrail", "D": "Disabling version control"},
        "correct": ["A"],
        "explanation": "GitFlow (or similar) defines branch policies that trigger pipelines on merge.",
        "wrongWhy": {"B": "Destroys history.", "C": "CloudTrail is audit logs.", "D": "Version control is essential."},
    },
    99: {
        "stem": "A team hits the account limit for concurrent SageMaker training jobs. What is the appropriate resolution?",
        "options": {"A": "Request a service quota increase for SageMaker training jobs", "B": "Delete all IAM users", "C": "Disable CloudWatch", "D": "Use public S3 ACLs"},
        "correct": ["A"],
        "explanation": "AWS Service Quotas can be increased via support/request console.",
        "wrongWhy": {"B": "Breaks access.", "C": "Removes monitoring.", "D": "Security violation."},
    },
    100: {
        "stem": "What is the minimum passing scaled score for the AWS Certified Machine Learning Engineer – Associate (MLA-C01) exam?",
        "options": {"A": "720", "B": "650", "C": "800", "D": "900"},
        "correct": ["A"],
        "explanation": "AWS documents a passing score of 720 on the 100–1000 scale.",
        "wrongWhy": {"B": "Below official pass line.", "C": "Higher than required.", "D": "Perfect score not required."},
    },
}

# Improve terse stems for Q11-13 if needed - already done in json
# Q7 ordering and Q64 matching - keep structure, improve text
REWRITES[7] = {
    "stem": "A team prepares raw CSV data in Amazon S3 for SageMaker training. Place the steps in the correct order.",
    "type": "ordering",
    "options": {"1": "Register features in SageMaker Feature Store", "2": "Ingest and validate schema", "3": "Split into train/validation/test sets", "4": "Transform data and engineer features"},
    "correct": ["2", "4", "3", "1"],
    "explanation": "Ingest and validate first, then transform, split, and optionally register features for reuse.",
    "wrongWhy": {},
}
REWRITES[64] = {
    "stem": "Match each inference requirement to the most appropriate SageMaker deployment option.",
    "type": "matching",
    "options": {
        "prompts": ["Steady low latency at high QPS", "Offline scoring of millions of historical records", "Intermittent traffic with minimal instance management"],
        "choices": ["Real-time endpoint with auto scaling", "Batch Transform", "Serverless inference"],
    },
    "correct": ["Real-time endpoint with auto scaling", "Batch Transform", "Serverless inference"],
    "explanation": "Real-time for SLA; Batch for bulk offline; Serverless for bursty/intermittent.",
    "wrongWhy": {},
}


def apply_rewrites(questions):
    for q in questions:
        rid = q["id"]
        if rid in REWRITES:
            r = REWRITES[rid]
            q.update({k: v for k, v in r.items() if k != "type"})
            if "type" in r:
                q["type"] = r["type"]
    return questions


def validate(questions):
    bad = []
    placeholders = ("Option B", "Option C", "Option D", "Option A placeholder", "Incorrect option", "Opt1")
    for q in questions:
        opts = q.get("options", {})
        if q["type"] == "matching":
            continue
        if q["type"] == "ordering":
            continue
        for k, v in opts.items():
            if any(p in v for p in placeholders):
                bad.append(q["id"])
                break
        if len(opts) < 4 and q["type"] != "multi":
            bad.append(q["id"])
    return bad


def main():
    questions = json.loads((ROOT / "questions.json").read_text())
    questions = apply_rewrites(questions)
    bad = validate(questions)
    if bad:
        raise SystemExit(f"Still have placeholder options in: {bad}")
    (ROOT / "questions.json").write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n")
    print(f"Updated {len(questions)} questions, 0 placeholders remaining")

    # Regenerate quiz.html
    qjson = json.dumps(questions, ensure_ascii=False)
    template = (ROOT / "quiz.html").read_text()
    import re
    new_html = re.sub(
        r"const ALL_QUESTIONS = \[.*?\];",
        f"const ALL_QUESTIONS = {qjson};",
        template,
        count=1,
        flags=re.DOTALL,
    )
    if new_html == template:
        raise SystemExit("Failed to update quiz.html embedded JSON")
    (ROOT / "quiz.html").write_text(new_html)
    print("Regenerated quiz.html")


if __name__ == "__main__":
    main()