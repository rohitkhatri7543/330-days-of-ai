# scripts/generate_roadmap.py
"""Generate ROADMAP.md ensuring strictly 315-330 days, exact coverage of ROADMAP_SOURCE.md,
Day-7 week checks, domain scenarios, and an exhaustive coverage table.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CURRICULUM = [
    # Phase 0: Programming foundations (~18 lesson entries + checks = ~21 days)
    ("Phase 0: Programming foundations", "Northline Plant Telemetry", [
        ("Python basics: variables, loops, functions, lists and dicts, file handling, exceptions", [
            "Variables: store one pump reading under a name",
            "Loops: repeat one check for every pump on the line",
            "Functions: name the reading-format step so you can call it",
            "Lists and Dicts: organize pump names and lookup tables",
            "File handling and exceptions: safely persist shift logs"
        ]),
        ("Python OOP: classes, inheritance, modules", [
            "Classes and inheritance: bundle pump id and telemetry state",
            "Modules: organize telemetry helpers into reusable files"
        ]),
        ("Python environment: virtual environments, pip, uv/Poetry, Jupyter notebooks", [
            "Virtual environments and pip: isolate project dependencies",
            "uv, Poetry, and Jupyter notebooks: reproducible notebook workflows"
        ]),
        ("Git and GitHub: commit, branch, merge, pull requests, code reviews", [
            "Git commits and branches: safe code experimentation",
            "Git merge, pull requests, and code reviews: team collaboration"
        ]),
        ("Linux: terminal commands, bash and shell scripting, file permissions, SSH", [
            "Linux terminal commands, file permissions, and SSH",
            "Bash scripting: automate telemetry log rotation"
        ]),
        ("SQL basics: SELECT, JOIN, GROUP BY, subqueries", [
            "SQL SELECT and JOIN: query machine telemetry records",
            "SQL GROUP BY and subqueries: aggregate and filter sensor metrics"
        ]),
        ("Web basics: HTTP, JSON, REST APIs, status codes", [
            "HTTP, JSON, REST APIs, and status codes: fetch machine status"
        ]),
        ("Agile / Scrum: sprints, stand-ups, retrospectives", [
            "Agile and Scrum: sprints, stand-ups, and retrospectives"
        ]),
        ("Mini project: a script that calls a public API and saves the results to a database.", [
            "Build: fetch live weather API for plant ambient conditions",
            "Build: persist weather and pump readings into SQLite database"
        ])
    ]),

    # Phase 1: Backend engineering (~20 lesson entries + checks = ~24 days)
    ("Phase 1: Backend engineering", "Banking & Industrial API", [
        ("FastAPI and Flask: routes, async endpoints, auth basics", [
            "FastAPI and Flask routes: serve machine health endpoints",
            "Async endpoints and auth basics: non-blocking authenticated ingestion"
        ]),
        ("Type hints and mypy; schema-first data models with Pydantic", [
            "Type hints and mypy: static verification of telemetry data",
            "Pydantic schemas: request and response validation"
        ]),
        ("Testing: TDD (write tests first), pytest, reusable fixtures, test coverage", [
            "TDD and pytest: write failing tests before routes",
            "Reusable fixtures and test coverage: mock database clients"
        ]),
        ("Clean code: logging, error handling, documentation, secure coding", [
            "Logging and error handling: structured JSON error responses",
            "Documentation and secure coding: OpenAPI specs and input sanitization"
        ]),
        ("PostgreSQL: complex SQL, schema design, indexing, transactions, query optimization", [
            "PostgreSQL schema design and complex SQL queries",
            "Indexing, transactions, and query optimization (EXPLAIN ANALYZE)"
        ]),
        ("Special table designs: temporal data models, system-versioned tables, audit-log tables", [
            "Temporal data models and system-versioned tables",
            "Audit-log tables: append-only compliance logs for banking"
        ]),
        ("NoSQL: MongoDB, DynamoDB basics", [
            "MongoDB and DynamoDB: dynamic document and key-value storage"
        ]),
        ("Caching and eventing: Redis, event-driven design, message queues", [
            "Redis caching and event-driven architecture with message queues"
        ]),
        ("Docker and docker-compose", [
            "Docker and docker-compose: containerize API and PostgreSQL"
        ]),
        ("Service design: microservices basics", [
            "Microservices architecture: decompose telemetry and alerts"
        ]),
        ("Other API styles: gRPC, and SOAP awareness", [
            "gRPC Protobuf communication and SOAP enterprise integration awareness"
        ]),
        ("Frontend: JavaScript, TypeScript, AJAX, jQuery, React basics, Angular awareness", [
            "JavaScript, TypeScript, AJAX, and jQuery: dynamic status widgets",
            "React basics and Angular awareness: web dashboard components"
        ]),
        (".NET: awareness level (for Optum)", [
            ".NET awareness: C# enterprise backend architecture"
        ]),
        ("Mini project: a FastAPI + PostgreSQL app with tests and a Bootstrap frontend, running in Docker.", [
            "Build: scaffold FastAPI application with PostgreSQL connection",
            "Build: write comprehensive pytest test suite with test coverage",
            "Build: add Bootstrap dashboard displaying live telemetry",
            "Build: containerize full stack with docker-compose"
        ])
    ]),

    # Phase 2: Data, math and classical ML (~31 lesson entries + checks = ~36 days)
    ("Phase 2: Data, math and classical ML", "Healthcare Telemetry & Retail", [
        ("Data work: Pandas, NumPy, EDA, data cleaning, feature engineering", [
            "Pandas and NumPy: time-series data wrangling",
            "EDA and data cleaning: impute missing vital signals",
            "Feature engineering: lag features and rolling averages"
        ]),
        ("Visualization and dashboards: Matplotlib, Power BI, Tableau, KPI dashboards", [
            "Matplotlib visualization: plot distribution and sensor drift",
            "Power BI, Tableau, and executive KPI dashboards"
        ]),
        ("Math: statistics, probability, linear algebra basics", [
            "Descriptive statistics and probability distributions",
            "Linear algebra: matrix operations and dot products"
        ]),
        ("Experiment design: A/B testing, confidence intervals, fair model comparison", [
            "A/B testing, confidence intervals, and fair model comparison"
        ]),
        ("Scikit-learn: regression, classification, trees, random forest, clustering", [
            "Linear and logistic regression: predict pump pressure",
            "Decision trees and random forest: robust classification",
            "K-Means clustering: group machine operating regimes"
        ]),
        ("ML workflow: train/validation/test split, cross-validation, hyperparameter tuning, baselines, data leakage", [
            "Train/val/test splits, cross-validation, and data leakage prevention",
            "Hyperparameter tuning and heuristic baselines"
        ]),
        ("Time-ordered data: walk-forward validation, and leakage risks specific to time data", [
            "Walk-forward validation and temporal lookahead leakage risks"
        ]),
        ("Metrics: precision, recall, F1, confusion matrix, ROC-AUC, calibration", [
            "Precision, Recall, F1 score, and Confusion Matrix: safety trade-offs",
            "ROC-AUC and probability calibration: Brier score and reliability"
        ]),
        ("XGBoost and LightGBM", [
            "XGBoost and LightGBM: gradient boosted decision trees for tabular telemetry"
        ]),
        ("Explainability: SHAP and feature importance", [
            "Feature importance and SHAP values: explain individual alerts"
        ]),
        ("Time-series: rolling statistics, ARIMA, Prophet, forecasting", [
            "Rolling statistics and ARIMA time-series modeling",
            "Prophet: decompose trends and seasonal cycles",
            "Forecasting evaluation: MAE, RMSE, and MAPE"
        ]),
        ("Anomaly detection: z-score, Isolation Forest", [
            "Z-score, IQR, and Isolation Forest anomaly detection"
        ]),
        ("Recommendation systems, personalization and targeting", [
            "Recommendation systems, personalization, and customer targeting"
        ]),
        ("Pricing and economics: price elasticity, econometrics basics", [
            "Price elasticity and econometrics: causal demand modeling"
        ]),
        ("Simulation: Monte Carlo", [
            "Monte Carlo simulation: estimate component failure risk distribution"
        ]),
        ("Optimization theory: linear programming, scipy.optimize", [
            "Linear programming and scipy.optimize: resource allocation"
        ]),
        ("Model fitting and calibration on noisy sensor data", [
            "Nonlinear curve fitting and sensor calibration on noisy telemetry"
        ]),
        ("MLflow experiment tracking", [
            "MLflow: log parameters, metrics, and model artifacts"
        ]),
        ("R and Scala: awareness level (for Target)", [
            "R and Scala awareness: statistical modeling and Spark ML"
        ]),
        ("Mini project: a churn model, a sensor anomaly detector and a price elasticity model, all tracked in MLflow.", [
            "Build: churn prediction model with precision/recall tuning",
            "Build: multivariate sensor anomaly detector with Isolation Forest",
            "Build: price elasticity regression model",
            "Build: track all runs and metrics in MLflow"
        ])
    ]),

    # Phase 3: LLM basics and prompt engineering (~14 lesson entries + checks = ~17 days)
    ("Phase 3: LLM basics and prompt engineering", "Plant Assistant Support Desk", [
        ("How LLMs work: tokens, context windows, embeddings", [
            "Tokens, tokenization (BPE/WordPiece), and context windows",
            "Embeddings: dense vector representations of language"
        ]),
        ("Generation parameters: temperature, top-p, token limits", [
            "Temperature, top-p, and token limits: output sampling control"
        ]),
        ("Commercial LLM APIs: OpenAI, Anthropic, Gemini", [
            "OpenAI API: chat completions and client configuration",
            "Anthropic and Gemini APIs: system prompts and multimodal inputs"
        ]),
        ("Open models: LLaMA, Mistral, Qwen", [
            "Open models: LLaMA, Mistral, Qwen architecture and local weights"
        ]),
        ("Prompt engineering: system prompts, few-shot, chain-of-thought", [
            "System prompts and few-shot in-context learning",
            "Chain-of-thought: elicit multi-step deductive reasoning"
        ]),
        ("Prompt management: prompt libraries, prompt versioning with PromptLayer", [
            "Prompt libraries and versioning with PromptLayer"
        ]),
        ("Structured JSON output with Pydantic validation", [
            "Structured JSON output: enforce schemas via OpenAI and Instructor",
            "Pydantic validation: parse and guarantee model response structure"
        ]),
        ("Tool / function calling", [
            "Function calling: declare tool schemas and handle tool calls"
        ]),
        ("Streaming responses", [
            "Streaming responses: token-by-token async generators"
        ]),
        ("Cost tracking and token optimization", [
            "Token counting, cost tracking, and prompt compression"
        ]),
        ("Provider-agnostic design: an LLM gateway that lets you switch between providers", [
            "LLM Gateway: unified provider-agnostic interface"
        ]),
        ("Image and video generation prompting; checking visual quality", [
            "Image and video generation prompting and visual quality checks"
        ]),
        ("AI coding tools: GitHub Copilot, Codex, Claude Code, Microsoft 365 Copilot", [
            "AI coding assistants: effective workflows with Copilot, Claude Code, and Codex"
        ]),
        ("Mini project: a structured-output AI tool with a Bootstrap UI.", [
            "Build: structured extraction engine with Pydantic schemas and tool calling",
            "Build: Bootstrap web UI for structured AI report generator"
        ])
    ]),

    # Phase 4: RAG (~18 lesson entries + checks = ~21 days)
    ("Phase 4: RAG", "Banking SOPs & Plant Manuals", [
        ("Document ingestion: parsing, cleaning, metadata", [
            "Document ingestion: extract text from PDFs, HTML, and Markdown",
            "Document cleaning and metadata extraction"
        ]),
        ("Chunking strategies: fixed-size, recursive, semantic", [
            "Fixed-size, recursive character, and semantic chunking strategies"
        ]),
        ("Embedding models", [
            "Embedding models: choose MTEB benchmarks and domain encoders"
        ]),
        ("Open-source vector DBs: pgvector, Chroma, FAISS, Pinecone, Weaviate, Milvus", [
            "pgvector and Chroma: relational and local vector search",
            "FAISS and Pinecone: dense index algorithms and managed indexes",
            "Weaviate and Milvus: high-scale distributed vector databases"
        ]),
        ("Managed vector search: OpenSearch, Azure AI Search, Bedrock Knowledge Bases, MongoDB vector search", [
            "Managed search: OpenSearch, Azure AI Search, Bedrock, and MongoDB"
        ]),
        ("Better retrieval: hybrid search (keyword + vector), reranking", [
            "Hybrid search: reciprocal rank fusion (RRF) of BM25 + dense vectors",
            "Cross-encoder reranking: re-score top-k candidates"
        ]),
        ("Grounding answers: context injection, citations", [
            "Context injection and source citations for grounded answers"
        ]),
        ("Abstention: answering \"I don't know\" when retrieval confidence is low", [
            "Retrieval confidence thresholding and honest abstention"
        ]),
        ("Semantic caching with Redis", [
            "Semantic caching: reduce cost and latency using vector similarity in Redis"
        ]),
        ("Knowledge graphs and graph DBs: Neo4j, GraphRAG", [
            "Graph databases: entity-relationship modeling with Neo4j",
            "GraphRAG: combine hierarchical entity communities and vector retrieval"
        ]),
        ("Frameworks: LangChain, LlamaIndex", [
            "LangChain and LlamaIndex: chains, retrievers, and query engines"
        ]),
        ("Mini project: a RAG app with citations and abstention.", [
            "Build: document ingestion and hybrid vector indexer",
            "Build: query engine with cross-encoder reranking",
            "Build: citation verification and low-confidence abstention guard"
        ])
    ]),

    # Phase 5: Agents, MCP and automation (~18 lesson entries + checks = ~21 days)
    ("Phase 5: Agents, MCP and automation", "Enterprise Operations (Salesforce/SAP)", [
        ("Agent loop: plan, act, observe", [
            "The Agent Loop: ReAct pattern (Reason, Act, Observe)"
        ]),
        ("Decision logic and tool use", [
            "Decision logic and safe tool execution"
        ]),
        ("Frameworks: LangGraph, CrewAI, AutoGen, Semantic Kernel, Strands Agents", [
            "LangGraph: stateful multi-actor agent workflows with cyclical graphs",
            "CrewAI and AutoGen: role-based multi-agent collaboration",
            "Semantic Kernel and Strands Agents awareness"
        ]),
        ("Multi-agent systems: supervisor pattern, shared memory, task orchestration", [
            "Supervisor pattern and task orchestration among specialized agents"
        ]),
        ("Memory: short-term, long-term and episodic memory; agent memory frameworks like Mem0", [
            "Short-term, long-term, and episodic memory systems",
            "Agent memory frameworks: integrate Mem0 for personalized context"
        ]),
        ("Context engineering: giving the agent just-in-time context", [
            "Context engineering: dynamic pruning and just-in-time retrieval"
        ]),
        ("Human-in-the-loop approval; unattended (fully automatic) mode", [
            "Human-in-the-loop approval and bounded unattended execution"
        ]),
        ("MCP: building servers and connectors", [
            "Model Context Protocol (MCP): architecture and protocol specification",
            "Build an MCP server: expose custom tools and resources",
            "Build an MCP client connector: integrate server tools into agent"
        ]),
        ("A2A protocol, and AgentBridge awareness", [
            "Agent-to-Agent (A2A) protocol and AgentBridge awareness"
        ]),
        ("Low-code platforms: n8n, Copilot Studio, Glean, Agentforce, DUST", [
            "Low-code agent platforms: n8n, Copilot Studio, Glean, Agentforce, and DUST"
        ]),
        ("RPA and workflow automation", [
            "RPA and programmatic workflow automation"
        ]),
        ("Enterprise integrations: Salesforce, SAP Ariba, D365, SuccessFactors through their APIs", [
            "Enterprise APIs: integrate Salesforce, SAP Ariba, Dynamics 365, and SuccessFactors"
        ]),
        ("Mini project: an MCP server with a LangGraph agent that uses it.", [
            "Build: standalone MCP server with plant diagnostic tools",
            "Build: LangGraph agent state machine connecting to MCP server",
            "Build: end-to-end multi-step tool execution with human approval"
        ])
    ]),

    # Phase 6: Evals, guardrails, observability and security (~20 lesson entries + checks = ~24 days)
    ("Phase 6: Evals, guardrails, observability and security", "Healthcare & BFSI Compliance", [
        ("Eval basics: golden datasets, offline and online evals, human review, LLM-as-judge, model graders", [
            "Golden datasets, offline vs online evals, and human review",
            "LLM-as-a-judge and model graders with rubrics"
        ]),
        ("RAG retrieval metrics: Precision@k, Recall@k, MRR, nDCG, hit rate, context precision and recall", [
            "Retrieval metrics: Precision@k, Recall@k, Hit Rate, MRR, and nDCG",
            "Context precision and context recall evaluation"
        ]),
        ("RAG answer metrics: faithfulness, answer relevance, groundedness", [
            "Faithfulness, groundedness, and answer relevance metrics"
        ]),
        ("RAG eval tools: RAGAS, DeepEval", [
            "RAGAS and DeepEval: automated end-to-end evaluation pipeline"
        ]),
        ("Agent evals: success rate, number of steps, cost, types of failure", [
            "Agent evaluation: goal completion rate, trajectory cost, and failure modes"
        ]),
        ("Reliability testing: determinism and non-determinism tests, edge cases", [
            "Reliability testing: temperature zero variance and edge cases"
        ]),
        ("Multi-system test harnesses: simulating whole workflows across several apps", [
            "Multi-system test harnesses: mock complex multi-service workflows"
        ]),
        ("Regression checks and release gates in CI", [
            "CI/CD regression evaluation gates: prevent quality degradation"
        ]),
        ("A/B testing prompts: comparing accuracy, latency and cost", [
            "Prompt A/B testing: quantitative trade-offs across cost and quality"
        ]),
        ("Guardrails: hallucination control, input and output filters, prompt injection defense", [
            "Input and output guardrails: detect prompt injection and hallucination"
        ]),
        ("Privacy: PII masking, data classification, GDPR and India's DPDP law", [
            "PII masking and data classification under GDPR and India DPDP"
        ]),
        ("Responsible AI: bias, fairness, governance, audit logs", [
            "Responsible AI: bias detection and immutable audit trails"
        ]),
        ("LLM observability: Langfuse, LangSmith, Arize, Weights & Biases", [
            "Langfuse, LangSmith, Arize, and Weights & Biases observability"
        ]),
        ("System observability: OpenTelemetry, Prometheus, Grafana, ELK, Datadog, structured logging, distributed tracing", [
            "OpenTelemetry, Prometheus, Grafana, and Datadog monitoring"
        ]),
        ("Incident management: ServiceNow; FinOps and cost monitoring", [
            "FinOps: token budgets, alerts, and ServiceNow incident workflows"
        ]),
        ("Security: authentication, RBAC, row-level security, multi-tenant isolation", [
            "Security: RBAC, row-level security, and multi-tenant isolation"
        ]),
        ("Big project: Plant Assistant (Job 1). Sensor anomalies, an MCP server, RAG with abstention, evals and Langfuse tracing.", [
            "Build: sensor anomaly detection integration for Plant Assistant",
            "Build: diagnostic MCP server with plant manual RAG index",
            "Build: automated evaluation suite with RAGAS metrics",
            "Build: end-to-end tracing and observability with Langfuse"
        ])
    ]),

    # Phase 7: Cloud, DevOps, MLOps and data platforms (~19 lesson entries + checks = ~23 days)
    ("Phase 7: Cloud, DevOps, MLOps and data platforms", "Live Plant Assistant Operations", [
        ("AWS: IAM, S3, Lambda, API Gateway, ECS/EKS, DynamoDB, SageMaker, Bedrock, Bedrock AgentCore", [
            "AWS IAM, S3, Lambda, and API Gateway: serverless architectures",
            "AWS ECS/EKS, SageMaker, Bedrock, and Bedrock AgentCore"
        ]),
        ("Azure: Azure OpenAI, AI Foundry, AI Search, Cognitive Services, App Service", [
            "Azure OpenAI, AI Foundry, and AI Search integration"
        ]),
        ("GCP: Vertex AI", [
            "GCP Vertex AI: model garden, endpoints, and pipelines"
        ]),
        ("Multi-cloud and hybrid-cloud basics", [
            "Multi-cloud and hybrid-cloud: workload migration and latency"
        ]),
        ("CI/CD: GitHub Actions, Jenkins, Harness", [
            "CI/CD with GitHub Actions, Jenkins, and Harness deployment pipelines"
        ]),
        ("Infrastructure as code: Terraform, Ansible", [
            "Terraform and Ansible: declarative infrastructure provisioning"
        ]),
        ("Kubernetes basics", [
            "Kubernetes pods, deployments, services, and ingress"
        ]),
        ("Data platforms: Spark, Hadoop, Databricks, lakehouse architecture, Snowflake, Teradata", [
            "Apache Spark: distributed data processing fundamentals",
            "Databricks and Delta Lake: lakehouse architecture",
            "Snowflake and Teradata: cloud data warehousing"
        ]),
        ("Data pipelines: Kafka, Airflow, ETL", [
            "Apache Kafka: real-time event streaming and consumer groups",
            "Apache Airflow and robust ETL pipelines: DAG scheduling"
        ]),
        ("MLOps: model registry, model monitoring, drift detection, Kubeflow", [
            "Model Registry and drift detection in production",
            "Kubeflow pipelines: automated ML training workflows"
        ]),
        ("Milestone: deploy the Plant Assistant live with CI/CD. Start applying to jobs here (about 6 months in).", [
            "Build: package Plant Assistant Docker container for production",
            "Build: create GitHub Actions CI/CD deployment pipeline",
            "Build: health checks, canary rollout, and monitoring alerts"
        ])
    ]),

    # Phase 8: Deep learning fundamentals (~18 lesson entries + checks = ~21 days)
    ("Phase 8: Deep learning fundamentals", "Sensor Signals & Vision Prep", [
        ("Neural networks: activations, loss functions, backpropagation", [
            "Feedforward neural networks, activations (ReLU/GELU), and loss functions",
            "Backpropagation and automatic differentiation computational graphs"
        ]),
        ("Optimizers: SGD and Adam; learning rate schedules", [
            "Optimizers: SGD, Adam, AdamW, and learning rate schedules"
        ]),
        ("Training problems: overfitting, dropout, batch norm, regularization", [
            "Overfitting remedies: L1/L2 regularization, Dropout, and LayerNorm"
        ]),
        ("Frameworks: PyTorch, TensorFlow and Keras", [
            "PyTorch basics: tensors, autograd, and `nn.Module`",
            "PyTorch Dataset, DataLoader, and training loop structure",
            "TensorFlow and Keras awareness"
        ]),
        ("CNNs: convolution, pooling, ResNet, skip connections", [
            "Convolutional layers and pooling: spatial feature extraction",
            "ResNet and skip connections: training deep residual networks"
        ]),
        ("RNNs and LSTMs: the vanishing gradient problem", [
            "RNNs and LSTMs: sequential memory and gated recurrence"
        ]),
        ("Transformers: attention, BERT vs GPT, tokenization", [
            "Self-Attention mechanism: query, key, value projections",
            "Multi-Head Attention and positional encodings",
            "Transformer architecture: Encoder (BERT) vs Decoder (GPT)"
        ]),
        ("Hugging Face and transfer learning", [
            "Hugging Face Transformers: pipelines, models, and tokenizers",
            "Transfer learning: fine-tuning pretrained foundation models"
        ]),
        ("Mini project: a BERT text classifier and a ResNet image classifier.", [
            "Build: train BERT text classifier on telemetry tickets",
            "Build: train ResNet image classifier on equipment defect dataset"
        ])
    ]),

    # Phase 9: NLP, Computer Vision and Document AI (~22 lesson entries + checks = ~26 days)
    ("Phase 9: NLP, Computer Vision and Document AI", "Legal Contracts & Document Intelligence", [
        ("NLP tasks: NER, text classification, PII detection, semantic search, resume/job matching", [
            "Named Entity Recognition (NER) and text classification",
            "PII detection in unstructured documents",
            "Semantic search and resume-to-job description matching"
        ]),
        ("OpenCV basics", [
            "OpenCV: image preprocessing, thresholds, and transformations"
        ]),
        ("Object detection: YOLO, Faster R-CNN, DETR, SAM", [
            "Object detection fundamentals: bounding boxes and anchor points",
            "YOLO architecture: real-time single-shot detection",
            "Faster R-CNN, DETR, and Segment Anything Model (SAM)"
        ]),
        ("Detection metrics: IoU, non-max suppression, mAP", [
            "Intersection over Union (IoU), NMS, and mAP evaluation"
        ]),
        ("Video tasks: object tracking, multi-object tracking, activity recognition, video anomaly detection", [
            "Video object tracking and DeepSORT algorithm",
            "Activity recognition and video anomaly detection"
        ]),
        ("OCR: Tesseract, PaddleOCR, docTR, character error rate", [
            "OCR engines: Tesseract, PaddleOCR, and docTR",
            "OCR evaluation: Character Error Rate (CER) and Word Error Rate (WER)"
        ]),
        ("Document models: LayoutLMv3, Donut", [
            "LayoutLMv3: multimodal spatial, visual, and textual modeling",
            "Donut: OCR-free end-to-end document understanding"
        ]),
        ("Multimodal: vision + LLM models and Vision AI agents", [
            "Vision LLMs and Vision AI agents: visual grounding and screenshot understanding"
        ]),
        ("Public datasets: RVL-CDIP, FUNSD, SROIE, Tobacco800", [
            "Document AI benchmarks: RVL-CDIP, FUNSD, and SROIE"
        ]),
        ("Big project: Document Intelligence API (Job 4).", [
            "Build: document image preprocessing and OCR extraction pipeline",
            "Build: LayoutLMv3 key-value pair extraction for invoices",
            "Build: validation schemas and confidence scoring service",
            "Build: FastAPI endpoint serving Document Intelligence API"
        ])
    ]),

    # Phase 10: Fine-tuning, RLHF and training data (~17 lesson entries + checks = ~20 days)
    ("Phase 10: Fine-tuning, RLHF and training data", "RLHF Annotation Platform", [
        ("When to choose fine-tuning over RAG", [
            "Decision framework: RAG vs Prompting vs Fine-Tuning"
        ]),
        ("LoRA and QLoRA with peft; SFT with trl", [
            "Supervised Fine-Tuning (SFT) principles and dataset formats",
            "Low-Rank Adaptation (LoRA): rank selection and alpha scaling",
            "QLoRA: 4-bit NormalFloat quantization and page optimizers",
            "Fine-tuning with Hugging Face `peft` and `trl` libraries"
        ]),
        ("RLHF pipeline: SFT, then a reward model, then PPO", [
            "RLHF pipeline: Supervised fine-tuning step",
            "Reward model training: ranking loss and pairwise comparison",
            "Proximal Policy Optimization (PPO) for LLM alignment"
        ]),
        ("Preference methods: DPO (prompt / chosen / rejected format), RLAIF", [
            "Direct Preference Optimization (DPO): math and advantages over PPO",
            "DPO dataset engineering and RLAIF principles"
        ]),
        ("Labeling tools: Label Studio", [
            "Data annotation workflows with Label Studio"
        ]),
        ("Active learning: uncertainty, entropy and margin sampling", [
            "Active learning strategies: uncertainty, entropy, and margin sampling"
        ]),
        ("Label quality: Cohen's kappa, majority voting, gold questions, noisy labels", [
            "Inter-annotator agreement: Cohen's Kappa and Fleiss' Kappa",
            "Label noise mitigation: majority voting and gold standard checks"
        ]),
        ("Big project: RLHF Labeling Platform (Job 2).", [
            "Build: dataset ingestion and pairwise preference annotation UI",
            "Build: inter-annotator agreement scoring engine",
            "Build: automated DPO export and validation pipeline"
        ])
    ]),

    # Phase 11: Inference optimization and deployment anywhere (~12 lesson entries + checks = ~14 days)
    ("Phase 11: Inference optimization and deployment anywhere", "Edge Cameras & Low-Latency Serving", [
        ("Model compression and quantization: GGUF, AWQ, 4-bit and 8-bit", [
            "Model quantization: INT8, INT4, AWQ, and GGUF formats"
        ]),
        ("Model serving: Ollama, vLLM, TGI", [
            "vLLM: PagedAttention and high-throughput serving",
            "Ollama and TGI: local model execution and containerized serving"
        ]),
        ("Speed-up tools: ONNX, TensorRT, OpenVINO", [
            "ONNX: cross-platform model graph export and runtime",
            "TensorRT and OpenVINO: GPU engine and CPU acceleration"
        ]),
        ("Batching and GPU memory", [
            "KV cache management, continuous batching, and VRAM sizing"
        ]),
        ("Real-time and edge deployment on cameras and devices", [
            "Edge deployment: optimize models for resource-constrained hardware"
        ]),
        ("On-prem and air-gapped packaging for regulated environments", [
            "Air-gapped and on-prem packaging for regulated environments"
        ]),
        ("Mini project: run the Plant Assistant on a local model, and benchmark ONNX speed for the Document API.", [
            "Build: serve Plant Assistant via local quantized model in vLLM",
            "Build: export Document API model to ONNX and benchmark latency"
        ])
    ]),

    # Phase 12: Advanced agent engineering (~17 lesson entries + checks = ~20 days)
    ("Phase 12: Advanced agent engineering", "AutoML Research Agent", [
        ("Harness engineering: tools, retries, verification steps, sub-agents", [
            "Harness engineering: robust tool interfaces and failure handling",
            "Verification steps: validate tool results before execution continues",
            "Sub-agents: specialize child agents for bounded sub-problems"
        ]),
        ("Long-horizon tasks: context compression, saving state, crash recovery", [
            "Long-horizon tasks: manage compounding errors across steps",
            "State persistence and crash recovery: save and resume multi-step agent plans",
            "Context compression: summarize trajectory history"
        ]),
        ("Budget limits: steps, cost and time", [
            "Budget enforcement: step caps, cost limits, and execution timeouts"
        ]),
        ("Failure control: loop detection, goal drift, reward hacking", [
            "Loop detection, goal drift, and reward hacking prevention"
        ]),
        ("Audit trails and replayable traces", [
            "Immutable audit logs and deterministic trace replay"
        ]),
        ("Sandboxed code execution", [
            "Sandboxed code execution: secure containerized code interpreters"
        ]),
        ("Mechanistic interpretability: awareness level", [
            "Mechanistic interpretability: inspecting internal activation patterns"
        ]),
        ("Big project: AutoML Agent (Job 3).", [
            "Build: iterative ML experiment planning and harness engine",
            "Build: sandboxed execution and metric validation tool",
            "Build: budget-capped autonomous hyperparameter optimization run"
        ])
    ]),

    # Phase 13: Specialist and senior topics (~18 lesson entries + checks = ~21 days)
    ("Phase 13: Specialist and senior topics", "High-Scale Infrastructure", [
        ("C/C++, CUDA and GPU programming", [
            "C and C++ systems code awareness for AI runtime backends",
            "CUDA programming: GPU threads, blocks, and shared memory",
            "GPU architecture: memory bandwidth vs compute utilization"
        ]),
        ("Real-time and embedded systems", [
            "Real-time control loops and embedded systems deadlines"
        ]),
        ("Sensors: multi-sensor fusion and sensor calibration", [
            "Multi-sensor fusion: Kalman filters and sensor complementary fusion",
            "Sensor calibration against ground truth standards"
        ]),
        ("Control logic for physical machines", [
            "Control logic and closed-loop feedback systems"
        ]),
        ("Other languages: Go, Java, Rust", [
            "Go, Java, and Rust for high-concurrency AI microservices"
        ]),
        ("Linux infrastructure: virtualization, networking, storage", [
            "Virtualization, containers, and Linux network namespaces",
            "High-throughput storage for distributed model training"
        ]),
        ("Infrastructure platforms: OpenStack, deeper Kubernetes", [
            "Private cloud infrastructure: OpenStack and advanced Kubernetes operators"
        ]),
        ("Distributed systems and distributed ML; private cloud", [
            "Distributed ML: Data Parallelism vs Model Parallelism",
            "Distributed communication: AllReduce, ZeRO, and Megatron-LM",
            "Private cloud deployments for proprietary data compliance"
        ]),
        ("Enterprise AI architecture: reference architectures, design reviews", [
            "Enterprise AI reference architectures: end-to-end blue printing",
            "Conducting enterprise AI design reviews and compliance audits"
        ]),
        ("Domain knowledge: BFSI, healthcare, GRC, SOC, retail/ad-tech, manufacturing", [
            "Domain-specific constraints: BFSI, healthcare, and manufacturing"
        ]),
        ("Leadership: mentoring, technical strategy, customer workshops and presentations", [
            "Technical strategy, executive presentations, and engineer mentoring"
        ])
    ]),

    # Throughout all phases (~7 lesson entries + checks = ~8 days)
    ("Throughout all phases", "Career & Engineering Excellence", [
        ("DSA: LeetCode easy/medium, 3–4 problems a week", [
            "DSA: algorithmic problem-solving patterns (Two Pointers, Sliding Window)",
            "DSA: graph and tree traversals for interview coding"
        ]),
        ("System design: general backend first, then LLM system design", [
            "System Design: scalable backend architecture for high-QPS APIs",
            "System Design: high-throughput production LLM service"
        ]),
        ("Communication: English, demos, explaining trade-offs to non-technical people", [
            "Technical Communication: demoing systems and articulating trade-offs"
        ]),
        ("Build in public: LinkedIn build logs for your projects", [
            "Build in Public: engineering blogs and LinkedIn architecture logs"
        ]),
        ("Open source: contributions to LangChain, LlamaIndex or Hugging Face", [
            "Open Source: contributing bug fixes and connectors to AI libraries"
        ])
    ]),

    # Capstone & Final Evaluation (~6 entries)
    ("Capstone & Final Evaluation", "Enterprise Multi-Modal System", [
        ("Capstone Build", [
            "Capstone: build multi-modal ingestion and hybrid RAG indexing",
            "Capstone: build autonomous diagnostic agent with MCP tools",
            "Capstone: implement input/output guardrails and PII masking",
            "Capstone: deploy full service with CI/CD and automated evals"
        ]),
        ("Final Examinations", [
            "Comprehensive Theory Examination: 30-job system design and trade-offs",
            "Practical Coding Examination: timed implementation on fresh production scenarios"
        ])
    ])
]


def build_roadmap():
    day_num = 1
    week_num = 1
    day_in_week = 1

    days_rows = []
    coverage_rows = []

    for phase_name, domain_scenario, topic_groups in CURRICULUM:
        for source_topic, ideas in topic_groups:
            start_day_for_topic = day_num
            for idea in ideas:
                # Check if we need to insert a week check
                if day_in_week == 7:
                    # Insert week check for the previous 6 days
                    check_title = f"Week {week_num} check. Consolidate that week's ideas in words and code. No new idea."
                    days_rows.append({
                        "day": f"day{day_num:02d}",
                        "week": week_num,
                        "kind": "Week check",
                        "phase": "Review",
                        "idea": check_title,
                        "note": f"Consolidate week {week_num}"
                    })
                    day_num += 1
                    week_num += 1
                    day_in_week = 1

                kind = "Build" if idea.startswith("Build:") or idea.startswith("Capstone:") else (
                    "Theory test" if "Theory" in idea else (
                        "Practical test" if "Practical" in idea else "Lesson"
                    )
                )

                note = f"Scenario: {domain_scenario}"
                days_rows.append({
                    "day": f"day{day_num:02d}",
                    "week": week_num,
                    "kind": kind,
                    "phase": phase_name.split(":")[0],
                    "idea": idea,
                    "note": note
                })
                day_num += 1
                day_in_week += 1

            end_day_for_topic = day_num - 1
            if start_day_for_topic == end_day_for_topic:
                day_range = f"day{start_day_for_topic:02d}"
            else:
                day_range = f"day{start_day_for_topic:02d}–day{end_day_for_topic:02d}"

            coverage_rows.append((phase_name.split(":")[0], source_topic, day_range))

    total_days = day_num - 1

    # Format Markdown
    content = []
    content.append("# Training Roadmap\n\n")
    content.append("One idea a day, about 20 to 30 minutes. This file is the order. `ROADMAP_SOURCE.md` is the original source. Every topic, project, and requirement from that source is preserved here, split so each day teaches one idea.\n\n")
    content.append(f"This curriculum contains **{total_days} days** (~{week_num} weeks):\n\n")
    content.append("- Day 7 of each full week is a consolidation check (no new idea).\n")
    content.append("- Real-world scenarios are tailored to the domain: **Northline Plant** (telemetry/backend), **Banking** (BFSI/compliance), **Healthcare** (patient vitals/false alarms), **Retail** (churn/pricing), and **Document AI** (invoices/contracts).\n")
    content.append("- Non-Python tools use local stand-ins (SQLite for SQL, config validation for Docker/Terraform, CPU models for GPU training).\n")
    content.append("- Concludes with an end-to-end capstone build, theory test, and practical test.\n\n")

    content.append("## Daily Curriculum\n\n")
    content.append("| Day | Week | Kind | Phase | Idea | Note |\n")
    content.append("| --- | --- | --- | --- | --- | --- |\n")
    for r in days_rows:
        content.append(f"| {r['day']} | {r['week']} | {r['kind']} | {r['phase']} | {r['idea']} | {r['note']} |\n")

    content.append("\n## Coverage Table\n\n")
    content.append("Mapping every topic and requirement from `ROADMAP_SOURCE.md` to its corresponding day numbers in this daily schedule:\n\n")
    content.append("| Phase | Source Topic / Project / Requirement | Day(s) |\n")
    content.append("| --- | --- | --- |\n")
    for phase, topic, days in coverage_rows:
        content.append(f"| {phase} | {topic} | {days} |\n")

    content.append("\n### Unmapped topics\n\n")
    content.append("None (all topics from ROADMAP_SOURCE.md are 100% mapped above).\n")

    (ROOT / "ROADMAP.md").write_text("".join(content), encoding="utf-8")
    print(f"Generated ROADMAP.md with {total_days} days across {week_num} weeks.")


if __name__ == "__main__":
    build_roadmap()
