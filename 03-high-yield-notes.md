# MLA-C01 High-Yield Exam Notes

Exam-only focus. Not a general ML course.

---

## SageMaker (core)

| Component | Exam takeaway |
|-----------|----------------|
| **Studio** | Unified IDE; notebooks, experiments, pipelines |
| **Data Wrangler** | Visual feature engineering; export to Python/recipe |
| **Feature Store** | Offline (training batches) + Online (low-latency inference); feature groups |
| **Training** | Built-in algorithms, script mode (BYO framework), distributed, **Spot** for cost |
| **AMT** | Automatic Model Tuning; Bayesian optimization |
| **Debugger** | Captures tensors; rules for vanishing/exploding gradients, overfitting |
| **Experiments** | Track trials, parameters, artifacts |
| **Model Registry** | Versioning, metadata, **approval status** before prod deploy |
| **Pipelines** | CI/CD for ML steps; conditional steps; parallel |
| **Endpoints** | Real-time, **Serverless**, **Async**, **Batch Transform**, multi-model |
| **Model Monitor** | Baseline required; schedules on endpoints; data/model/bias drift |
| **Clarify** | Pre/post training bias; SHAP; PDP |
| **JumpStart** | Pre-trained models/solutions |
| **Inference Recommender** | Load test + instance recommendation |
| **Neo** | Compile model for edge devices |
| **Ground Truth** | Managed labeling workforce + workflows |

### Endpoint cheat sheet

| Need | Choice |
|------|--------|
| Steady low-latency, full control | Real-time + auto scaling |
| Intermittent traffic, pay per invoke | Serverless |
| Large payloads, long processing, queue | Async |
| Offline bulk scoring | Batch Transform |
| Many small models one instance | Multi-model endpoint |

---

## Feature engineering & data prep

- **Parquet/ORC**: columnar, compressed — default for S3-based ML pipelines  
- **Imputation / outliers**: DataBrew, Wrangler, Spark  
- **Encoding**: one-hot (low cardinality), label (tree models), embeddings (deep learning — awareness)  
- **Class imbalance**: oversample, undersample, SMOTE-class strategies, **synthetic data**, stratified split  
- **Bias metrics**: **CI** (class imbalance), **DPL** (difference in proportions of labels)  
- **Split**: train/val/test; shuffle; stratify for classification  
- **Compliance**: PII → Macie; encryption KMS; residency constraints in scenario  

---

## Model training & tuning

- **Epoch / batch size / learning rate** — affect convergence and time  
- **Early stopping** — stop when val metric plateaus  
- **Regularization**: L1 (sparsity), L2 (weight decay), dropout (NN)  
- **Distributed**: data parallel vs model parallel (large models)  
- **Spot training**: checkpoint to S3 to avoid losing progress  
- **Bring custom model**: script mode + inference container (BYOC)  

### Built-in algorithm hints (selection level)

| Problem | Often-cited built-in |
|---------|---------------------|
| Tabular classification/regression | XGBoost, Linear Learner |
| Text classification | BlazingText, Linear Learner |
| Image classification | Image Classification, Object Detection |
| Clustering | K-Means, PCA |

---

## Hyperparameter tuning

- **AMT**: runs many jobs; Bayesian search; early stopping bad runs  
- **Random search**: baseline HPO  
- **Grid**: small spaces only — exam rarely prefers for large spaces  

---

## Model deployment

- **Production variants**: weights for A/B on same endpoint  
- **Shadow variant**: copy traffic, no customer impact  
- **Blue/green / canary**: CodeDeploy terms + SageMaker variant traffic shifting  
- **VPC**: private subnets + security groups + VPC endpoints for S3/ECR  
- **Auto scaling**: target metric invocations per instance or custom latency  

---

## Monitoring & observability

| Monitor type | Detects |
|--------------|---------|
| Data quality | Feature stats drift vs baseline |
| Model quality | Prediction distribution / performance drift |
| Bias drift | Fairness metric changes |

- **CloudWatch**: alarms on invocations, errors, latency, CPU/GPU  
- **CloudTrail**: API audit — who deployed model  
- **EventBridge**: react to Monitor alerts → trigger Pipeline retrain  

---

## MLOps on AWS

```
Data (S3/Glue) → Features (Feature Store) → Train (SageMaker) → Register (Registry)
    → Deploy (Endpoint) → Monitor (Model Monitor) → Retrain (Pipeline + EventBridge)
```

- **CodePipeline**: orchestrate build/test/deploy **non-ML** and trigger SageMaker jobs  
- **SageMaker Pipelines**: native ML DAG — **preferred** for ML-specific orchestration in exam scenarios  

---

## Security & IAM

- SageMaker execution **role** needs least privilege: S3 prefixes, ECR, logs, KMS decrypt  
- **VPC mode**: training/inference in private VPC; no public internet if scenario requires  
- **Encryption**: S3 SSE-KMS; EBS volumes; inference HTTPS  
- **IAM policies**: deny `s3:*` wildcard; scope to `arn:aws:s3:::bucket/prefix/*`  

---

## Data governance

- **Lake Formation**: fine-grained access on data lake  
- **Macie**: discover PII in S3  
- **Lineage**: Model Registry + Pipeline artifacts (awareness)  

---

## Cost optimization

| Workload | Cost tactic |
|----------|-------------|
| Training | Spot instances, right-size instance, pipe input via FSx/EFS efficiently |
| Inference steady | Reserved / Savings Plans, right-size with Inference Recommender |
| Inference spiky | Serverless or auto scale-to-zero patterns |
| Storage | S3 Intelligent-Tiering, lifecycle to Glacier for old datasets |
| ETL | Glue job bookmarks, partition pruning in Athena |

---

## ML evaluation metrics (pick correct metric)

| Problem | Metrics |
|---------|---------|
| Imbalanced classification | Precision, Recall, F1, PR-AUC |
| Balanced classification | Accuracy, F1, ROC-AUC |
| Regression | RMSE, MAE, MAPE |
| Ranking | AUC |

- **Confusion matrix** → TP/FP/FN/TN for threshold decisions  
- **Overfitting**: train >> val performance → regularization, more data, simpler model  

---

## AWS ML / AI services (when to use managed vs SageMaker custom)

| Use case | Service |
|----------|---------|
| Images — faces, labels | Rekognition |
| Text — entities, sentiment | Comprehend |
| Speech-to-text | Transcribe |
| Translation | Translate |
| Documents — OCR/forms | Textract |
| Recommendations | Personalize |
| Foundation models / GenAI | Bedrock |
| Custom tabular/deep learning | SageMaker |

**Exam rule:** If scenario says “no ML expertise” or “pre-built API” → managed service first.

---

## Amazon Bedrock (GenAI — see also `08-supplemental-topics.md`)

| Topic | Exam takeaway |
|-------|----------------|
| **InvokeModel** | IAM for running FM inference |
| **Knowledge Bases** | Managed RAG over your documents |
| **Agents** | Tool-using GenAI workflows |
| **Guardrails** | Safety / PII filters on outputs |
| **vs SageMaker custom** | Bedrock when FM + API suffices; SageMaker when full training control needed |

---

## Services likely on exam (in-scope appendix summary)

**Must know:** SageMaker, S3, IAM, VPC, CloudWatch, CloudTrail, Glue, CodePipeline/CodeBuild, EventBridge, ECR, Step Functions, KMS, Lambda (orchestration), EC2, EFS, Feature Store ecosystem  

**Know at decision level:** Bedrock, Rekognition, Comprehend, Transcribe, Translate, Textract, Personalize, Athena, EMR, Kinesis, Firehose, DataBrew, QuickSight, X-Ray, Cost Explorer, Budgets, Trusted Advisor, MWAA  

**Deprioritize:** Everything in official **out-of-scope** appendix (IoT, Chime, DeepRacer, etc.)
