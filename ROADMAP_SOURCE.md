## Phase 0: Programming foundations (3 weeks)

- **Python basics:** variables, loops, functions, lists and dicts, file handling, exceptions
- **Python OOP:** classes, inheritance, modules
- **Python environment:** virtual environments, pip, uv/Poetry (reproducible dependencies), Jupyter notebooks
- **Git and GitHub:** commit, branch, merge, pull requests, code reviews
- **Linux:** terminal commands, bash and shell scripting, file permissions, SSH
- **SQL basics:** SELECT, JOIN, GROUP BY, subqueries
- **Web basics:** HTTP, JSON, REST APIs, status codes
- **Agile / Scrum:** sprints, stand-ups, retrospectives

**Mini project:** a script that calls a public API and saves the results to a database.

## Phase 1: Backend engineering (3 weeks)

- **FastAPI and Flask:** routes, async endpoints, auth basics
- **Type hints and mypy; schema-first data models** with Pydantic
- **Testing:** TDD (write tests first), pytest, reusable fixtures, test coverage
- **Clean code:** logging, error handling, documentation, secure coding
- **PostgreSQL:** complex SQL, schema design, indexing, transactions, query optimization
- **Special table designs:** temporal data models, system-versioned tables, audit-log tables
- **NoSQL:** MongoDB, DynamoDB basics
- **Caching and eventing:** Redis, event-driven design, message queues
- **Docker and docker-compose**
- **Service design:** microservices basics
- **Other API styles:** gRPC, and SOAP awareness
- **Frontend:** JavaScript, TypeScript, AJAX, jQuery, React basics, Angular awareness
- **.NET:** awareness level (for Optum)

**Mini project:** a FastAPI + PostgreSQL app with tests and a Bootstrap frontend, running in Docker.

**Prepares you for:** Tachyon Senior Python Engineer and Ingersoll Rand (engineering side).

## Phase 2: Data, math and classical ML (5 weeks)

- **Data work:** Pandas, NumPy, EDA, data cleaning, feature engineering
- **Visualization and dashboards:** Matplotlib, Power BI, Tableau, KPI dashboards
- **Math:** statistics, probability, linear algebra basics
- **Experiment design:** A/B testing, confidence intervals, fair model comparison
- **Scikit-learn:** regression, classification, trees, random forest, clustering
- **ML workflow:** train/validation/test split, cross-validation, hyperparameter tuning, baselines, data leakage
- **Time-ordered data:** walk-forward validation, and leakage risks specific to time data
- **Metrics:** precision, recall, F1, confusion matrix, ROC-AUC, calibration
- **XGBoost and LightGBM**
- **Explainability:** SHAP and feature importance
- **Time-series:** rolling statistics, ARIMA, Prophet, forecasting
- **Anomaly detection:** z-score, Isolation Forest
- **Recommendation systems, personalization and targeting**
- **Pricing and economics:** price elasticity, econometrics basics
- **Simulation:** Monte Carlo
- **Optimization theory:** linear programming, scipy.optimize
- **Model fitting and calibration on noisy sensor data**
- **MLflow** experiment tracking
- **R and Scala:** awareness level (for Target)

**Mini project:** a churn model, a sensor anomaly detector and a price elasticity model, all tracked in MLflow.

**Prepares you for:** Trailytics, Medico, Corning, Target, and the Accenture ML roles.

## Phase 3: LLM basics and prompt engineering (2 weeks)

- **How LLMs work:** tokens, context windows, embeddings
- **Generation parameters:** temperature, top-p, token limits
- **Commercial LLM APIs:** OpenAI, Anthropic, Gemini
- **Open models:** LLaMA, Mistral, Qwen
- **Prompt engineering:** system prompts, few-shot, chain-of-thought
- **Prompt management:** prompt libraries, prompt versioning with PromptLayer
- **Structured JSON output** with Pydantic validation
- **Tool / function calling**
- **Streaming responses**
- **Cost tracking and token optimization**
- **Provider-agnostic design:** an LLM gateway that lets you switch between providers
- **Image and video generation prompting;** checking visual quality
- **AI coding tools:** GitHub Copilot, Codex, Claude Code, Microsoft 365 Copilot

**Mini project:** a structured-output AI tool with a Bootstrap UI.

**Prepares you for:** KeyValue Prompt Engineer and the Accenture LLM roles.

## Phase 4: RAG (3 weeks)

- **Document ingestion:** parsing, cleaning, metadata
- **Chunking strategies:** fixed-size, recursive, semantic
- **Embedding models**
- **Open-source vector DBs:** pgvector, Chroma, FAISS, Pinecone, Weaviate, Milvus
- **Managed vector search:** OpenSearch, Azure AI Search, Bedrock Knowledge Bases, MongoDB vector search
- **Better retrieval:** hybrid search (keyword + vector), reranking
- **Grounding answers:** context injection, citations
- **Abstention:** answering "I don't know" when retrieval confidence is low
- **Semantic caching** with Redis
- **Knowledge graphs and graph DBs:** Neo4j, GraphRAG
- **Frameworks:** LangChain, LlamaIndex

**Mini project:** a RAG app with citations and abstention.

**Prepares you for:** Altraize, Wells Fargo, Corning (GenAI part), Konovo.

## Phase 5: Agents, MCP and automation (3 weeks)

- **Agent loop:** plan, act, observe
- **Decision logic** and tool use
- **Frameworks:** LangGraph, CrewAI, AutoGen, Semantic Kernel, Strands Agents
- **Multi-agent systems:** supervisor pattern, shared memory, task orchestration
- **Memory:** short-term, long-term and episodic memory; agent memory frameworks like Mem0
- **Context engineering:** giving the agent just-in-time context
- **Human-in-the-loop approval;** unattended (fully automatic) mode
- **MCP:** building servers and connectors
- **A2A protocol,** and AgentBridge awareness
- **Low-code platforms:** n8n, Copilot Studio, Glean, Agentforce, DUST
- **RPA and workflow automation**
- **Enterprise integrations:** Salesforce, SAP Ariba, D365, SuccessFactors through their APIs

**Mini project:** an MCP server with a LangGraph agent that uses it.

**Prepares you for:** XenonStack Agentic, Criteo, Tachyon Lead, Optum.

## Phase 6: Evals, guardrails, observability and security (3 weeks)

- **Eval basics:** golden datasets, offline and online evals, human review, LLM-as-judge, model graders
- **RAG retrieval metrics:** Precision@k, Recall@k, MRR, nDCG, hit rate, context precision and recall
- **RAG answer metrics:** faithfulness, answer relevance, groundedness
- **RAG eval tools:** RAGAS, DeepEval
- **Agent evals:** success rate, number of steps, cost, types of failure
- **Reliability testing:** determinism and non-determinism tests, edge cases
- **Multi-system test harnesses:** simulating whole workflows across several apps
- **Regression checks and release gates** in CI
- **A/B testing prompts:** comparing accuracy, latency and cost
- **Guardrails:** hallucination control, input and output filters, prompt injection defense
- **Privacy:** PII masking, data classification, GDPR and India's DPDP law
- **Responsible AI:** bias, fairness, governance, audit logs
- **LLM observability:** Langfuse, LangSmith, Arize, Weights & Biases
- **System observability:** OpenTelemetry, Prometheus, Grafana, ELK, Datadog, structured logging, distributed tracing
- **Incident management:** ServiceNow; FinOps and cost monitoring
- **Security:** authentication, RBAC, row-level security, multi-tenant isolation

**Big project: Plant Assistant (Job 1).** Sensor anomalies, an MCP server, RAG with abstention, evals and Langfuse tracing.

**Prepares you for:** IndustryOS, Cardboard, Whatfix FDE, XenonStack Human-AI and XenonStack MLOps.

## Phase 7: Cloud, DevOps, MLOps and data platforms (4 weeks)

- **AWS:** IAM, S3, Lambda, API Gateway, ECS/EKS, DynamoDB, SageMaker, Bedrock, Bedrock AgentCore
- **Azure:** Azure OpenAI, AI Foundry, AI Search, Cognitive Services, App Service
- **GCP:** Vertex AI
- **Multi-cloud and hybrid-cloud** basics
- **CI/CD:** GitHub Actions, Jenkins, Harness
- **Infrastructure as code:** Terraform, Ansible
- **Kubernetes** basics
- **Data platforms:** Spark, Hadoop, Databricks, lakehouse architecture, Snowflake, Teradata
- **Data pipelines:** Kafka, Airflow, ETL
- **MLOps:** model registry, model monitoring, drift detection, Kubeflow

**Milestone:** deploy the Plant Assistant live with CI/CD. **Start applying to jobs here (about 6 months in).**

**Prepares you for:** DataEconomy FDE, Jobgether AI Platform, Corning, Konovo.

## Phase 8: Deep learning fundamentals (5 weeks)

- **Neural networks:** activations, loss functions, backpropagation
- **Optimizers:** SGD and Adam; learning rate schedules
- **Training problems:** overfitting, dropout, batch norm, regularization
- **Frameworks:** PyTorch, TensorFlow and Keras
- **CNNs:** convolution, pooling, ResNet, skip connections
- **RNNs and LSTMs:** the vanishing gradient problem
- **Transformers:** attention, BERT vs GPT, tokenization
- **Hugging Face** and transfer learning

**Mini project:** a BERT text classifier and a ResNet image classifier.

## Phase 9: NLP, Computer Vision and Document AI (5 weeks)

- **NLP tasks:** NER, text classification, PII detection, semantic search, resume/job matching
- **OpenCV basics**
- **Object detection:** YOLO, Faster R-CNN, DETR, SAM
- **Detection metrics:** IoU, non-max suppression, mAP
- **Video tasks:** object tracking, multi-object tracking, activity recognition, video anomaly detection
- **OCR:** Tesseract, PaddleOCR, docTR, character error rate
- **Document models:** LayoutLMv3, Donut
- **Multimodal:** vision + LLM models and Vision AI agents
- **Public datasets:** RVL-CDIP, FUNSD, SROIE, Tobacco800

**Big project: Document Intelligence API (Job 4).**

**Prepares you for:** Leegality, XenonStack CV, Accenture LLM + CV.

## Phase 10: Fine-tuning, RLHF and training data (4 weeks)

- **When to choose fine-tuning over RAG**
- **LoRA and QLoRA** with `peft`; **SFT** with `trl`
- **RLHF pipeline:** SFT, then a reward model, then PPO
- **Preference methods:** DPO (prompt / chosen / rejected format), RLAIF
- **Labeling tools:** Label Studio
- **Active learning:** uncertainty, entropy and margin sampling
- **Label quality:** Cohen's kappa, majority voting, gold questions, noisy labels

**Big project: RLHF Labeling Platform (Job 2).**

**Prepares you for:** CoreLabel.AI, and the fine-tuning requirements at Cardboard and XenonStack.

## Phase 11: Inference optimization and deployment anywhere (3 weeks)

- **Model compression and quantization:** GGUF, AWQ, 4-bit and 8-bit
- **Model serving:** Ollama, vLLM, TGI
- **Speed-up tools:** ONNX, TensorRT, OpenVINO
- **Batching and GPU memory**
- **Real-time and edge deployment** on cameras and devices
- **On-prem and air-gapped packaging** for regulated environments

**Mini project:** run the Plant Assistant on a local model, and benchmark ONNX speed for the Document API.

## Phase 12: Advanced agent engineering (4 weeks)

- **Harness engineering:** tools, retries, verification steps, sub-agents
- **Long-horizon tasks:** context compression, saving state, crash recovery
- **Budget limits:** steps, cost and time
- **Failure control:** loop detection, goal drift, reward hacking
- **Audit trails** and replayable traces
- **Sandboxed code execution**
- **Mechanistic interpretability:** awareness level

**Big project: AutoML Agent (Job 3).**

**Prepares you for:** Lexsi Labs, Cardboard, DataEconomy and Whatfix FDE roles.

## Phase 13: Specialist and senior topics (ongoing)

- **C/C++, CUDA and GPU programming**
- **Real-time and embedded systems**
- **Sensors:** multi-sensor fusion and sensor calibration
- **Control logic** for physical machines
- **Other languages:** Go, Java, Rust
- **Linux infrastructure:** virtualization, networking, storage
- **Infrastructure platforms:** OpenStack, deeper Kubernetes
- **Distributed systems** and distributed ML; private cloud
- **Enterprise AI architecture:** reference architectures, design reviews
- **Domain knowledge:** BFSI, healthcare, GRC, SOC, retail/ad-tech, manufacturing
- **Leadership:** mentoring, technical strategy, customer workshops and presentations

**Prepares you for:** NAYAN, Ingersoll Rand, the Jobgether roles, and later DHL and Axis Bank. The architect and head roles also need 10–18 years of work experience.

## Throughout all phases

- **DSA:** LeetCode easy/medium, 3–4 problems a week
- **System design:** general backend first, then LLM system design
- **Communication:** English, demos, explaining trade-offs to non-technical people
- **Build in public:** LinkedIn build logs for your projects
- **Open source:** contributions to LangChain, LlamaIndex or Hugging Face

## Summary

| Stage | Phases | Time | Job-ready for |
|---|---|---|---|
| Foundation | 0–2 | ~11 weeks | Data Scientist roles |
| Core AI Engineer | 3–7 | ~15 weeks | About 60% of the jobs, including Job 1 |
| ML depth | 8–11 | ~17 weeks | CV/NLP roles, Job 2, Job 4 |
| Advanced | 12–13 | 4+ weeks | Job 3 and senior roles |

The total is about 11 months. Start applying after Phase 7, around month 6.