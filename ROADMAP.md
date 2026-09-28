# Training Roadmap

One idea a day, about 20 to 30 minutes. This file is the order. `ROADMAP_SOURCE.md` is the original source. Every topic, project, and requirement from that source is preserved here, split so each day teaches one idea.

This curriculum contains **330 days** (~48 weeks):

- Day 7 of each full week is a consolidation check (no new idea).
- Real-world scenarios are tailored to the domain: **Northline Plant** (telemetry/backend), **Banking** (BFSI/compliance), **Healthcare** (patient vitals/false alarms), **Retail** (churn/pricing), and **Document AI** (invoices/contracts).
- Non-Python tools use local stand-ins (SQLite for SQL, config validation for Docker/Terraform, CPU models for GPU training).
- Concludes with an end-to-end capstone build, theory test, and practical test.

## Daily Curriculum

| Day | Week | Kind | Phase | Idea | Note |
| --- | --- | --- | --- | --- | --- |
| day01 | 1 | Lesson | Phase 0 | Variables: store one pump reading under a name | Scenario: Northline Plant Telemetry |
| day02 | 1 | Lesson | Phase 0 | Loops: repeat one check for every pump on the line | Scenario: Northline Plant Telemetry |
| day03 | 1 | Lesson | Phase 0 | Functions: name the reading-format step so you can call it | Scenario: Northline Plant Telemetry |
| day04 | 1 | Lesson | Phase 0 | Lists and Dicts: organize pump names and lookup tables | Scenario: Northline Plant Telemetry |
| day05 | 1 | Lesson | Phase 0 | File handling and exceptions: safely persist shift logs | Scenario: Northline Plant Telemetry |
| day06 | 1 | Lesson | Phase 0 | Classes and inheritance: bundle pump id and telemetry state | Scenario: Northline Plant Telemetry |
| day07 | 1 | Week check | Review | Week 1 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 1 |
| day08 | 2 | Lesson | Phase 0 | Modules: organize telemetry helpers into reusable files | Scenario: Northline Plant Telemetry |
| day09 | 2 | Lesson | Phase 0 | Virtual environments and pip: isolate project dependencies | Scenario: Northline Plant Telemetry |
| day10 | 2 | Lesson | Phase 0 | uv, Poetry, and Jupyter notebooks: reproducible notebook workflows | Scenario: Northline Plant Telemetry |
| day11 | 2 | Lesson | Phase 0 | Git commits and branches: safe code experimentation | Scenario: Northline Plant Telemetry |
| day12 | 2 | Lesson | Phase 0 | Git merge, pull requests, and code reviews: team collaboration | Scenario: Northline Plant Telemetry |
| day13 | 2 | Lesson | Phase 0 | Linux terminal commands, file permissions, and SSH | Scenario: Northline Plant Telemetry |
| day14 | 2 | Week check | Review | Week 2 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 2 |
| day15 | 3 | Lesson | Phase 0 | Bash scripting: automate telemetry log rotation | Scenario: Northline Plant Telemetry |
| day16 | 3 | Lesson | Phase 0 | SQL SELECT and JOIN: query machine telemetry records | Scenario: Northline Plant Telemetry |
| day17 | 3 | Lesson | Phase 0 | SQL GROUP BY and subqueries: aggregate and filter sensor metrics | Scenario: Northline Plant Telemetry |
| day18 | 3 | Lesson | Phase 0 | HTTP, JSON, REST APIs, and status codes: fetch machine status | Scenario: Northline Plant Telemetry |
| day19 | 3 | Lesson | Phase 0 | Agile and Scrum: sprints, stand-ups, and retrospectives | Scenario: Northline Plant Telemetry |
| day20 | 3 | Build | Phase 0 | Build: fetch live weather API for plant ambient conditions | Scenario: Northline Plant Telemetry |
| day21 | 3 | Week check | Review | Week 3 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 3 |
| day22 | 4 | Build | Phase 0 | Build: persist weather and pump readings into SQLite database | Scenario: Northline Plant Telemetry |
| day23 | 4 | Lesson | Phase 1 | FastAPI and Flask routes: serve machine health endpoints | Scenario: Banking & Industrial API |
| day24 | 4 | Lesson | Phase 1 | Async endpoints and auth basics: non-blocking authenticated ingestion | Scenario: Banking & Industrial API |
| day25 | 4 | Lesson | Phase 1 | Type hints and mypy: static verification of telemetry data | Scenario: Banking & Industrial API |
| day26 | 4 | Lesson | Phase 1 | Pydantic schemas: request and response validation | Scenario: Banking & Industrial API |
| day27 | 4 | Lesson | Phase 1 | TDD and pytest: write failing tests before routes | Scenario: Banking & Industrial API |
| day28 | 4 | Week check | Review | Week 4 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 4 |
| day29 | 5 | Lesson | Phase 1 | Reusable fixtures and test coverage: mock database clients | Scenario: Banking & Industrial API |
| day30 | 5 | Lesson | Phase 1 | Logging and error handling: structured JSON error responses | Scenario: Banking & Industrial API |
| day31 | 5 | Lesson | Phase 1 | Documentation and secure coding: OpenAPI specs and input sanitization | Scenario: Banking & Industrial API |
| day32 | 5 | Lesson | Phase 1 | PostgreSQL schema design and complex SQL queries | Scenario: Banking & Industrial API |
| day33 | 5 | Lesson | Phase 1 | Indexing, transactions, and query optimization (EXPLAIN ANALYZE) | Scenario: Banking & Industrial API |
| day34 | 5 | Lesson | Phase 1 | Temporal data models and system-versioned tables | Scenario: Banking & Industrial API |
| day35 | 5 | Week check | Review | Week 5 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 5 |
| day36 | 6 | Lesson | Phase 1 | Audit-log tables: append-only compliance logs for banking | Scenario: Banking & Industrial API |
| day37 | 6 | Lesson | Phase 1 | MongoDB and DynamoDB: dynamic document and key-value storage | Scenario: Banking & Industrial API |
| day38 | 6 | Lesson | Phase 1 | Redis caching and event-driven architecture with message queues | Scenario: Banking & Industrial API |
| day39 | 6 | Lesson | Phase 1 | Docker and docker-compose: containerize API and PostgreSQL | Scenario: Banking & Industrial API |
| day40 | 6 | Lesson | Phase 1 | Microservices architecture: decompose telemetry and alerts | Scenario: Banking & Industrial API |
| day41 | 6 | Lesson | Phase 1 | gRPC Protobuf communication and SOAP enterprise integration awareness | Scenario: Banking & Industrial API |
| day42 | 6 | Week check | Review | Week 6 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 6 |
| day43 | 7 | Lesson | Phase 1 | JavaScript, TypeScript, AJAX, and jQuery: dynamic status widgets | Scenario: Banking & Industrial API |
| day44 | 7 | Lesson | Phase 1 | React basics and Angular awareness: web dashboard components | Scenario: Banking & Industrial API |
| day45 | 7 | Lesson | Phase 1 | .NET awareness: C# enterprise backend architecture | Scenario: Banking & Industrial API |
| day46 | 7 | Build | Phase 1 | Build: scaffold FastAPI application with PostgreSQL connection | Scenario: Banking & Industrial API |
| day47 | 7 | Build | Phase 1 | Build: write comprehensive pytest test suite with test coverage | Scenario: Banking & Industrial API |
| day48 | 7 | Build | Phase 1 | Build: add Bootstrap dashboard displaying live telemetry | Scenario: Banking & Industrial API |
| day49 | 7 | Week check | Review | Week 7 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 7 |
| day50 | 8 | Build | Phase 1 | Build: containerize full stack with docker-compose | Scenario: Banking & Industrial API |
| day51 | 8 | Lesson | Phase 2 | Pandas and NumPy: time-series data wrangling | Scenario: Healthcare Telemetry & Retail |
| day52 | 8 | Lesson | Phase 2 | EDA and data cleaning: impute missing vital signals | Scenario: Healthcare Telemetry & Retail |
| day53 | 8 | Lesson | Phase 2 | Feature engineering: lag features and rolling averages | Scenario: Healthcare Telemetry & Retail |
| day54 | 8 | Lesson | Phase 2 | Matplotlib visualization: plot distribution and sensor drift | Scenario: Healthcare Telemetry & Retail |
| day55 | 8 | Lesson | Phase 2 | Power BI, Tableau, and executive KPI dashboards | Scenario: Healthcare Telemetry & Retail |
| day56 | 8 | Week check | Review | Week 8 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 8 |
| day57 | 9 | Lesson | Phase 2 | Descriptive statistics and probability distributions | Scenario: Healthcare Telemetry & Retail |
| day58 | 9 | Lesson | Phase 2 | Linear algebra: matrix operations and dot products | Scenario: Healthcare Telemetry & Retail |
| day59 | 9 | Lesson | Phase 2 | A/B testing, confidence intervals, and fair model comparison | Scenario: Healthcare Telemetry & Retail |
| day60 | 9 | Lesson | Phase 2 | Linear and logistic regression: predict pump pressure | Scenario: Healthcare Telemetry & Retail |
| day61 | 9 | Lesson | Phase 2 | Decision trees and random forest: robust classification | Scenario: Healthcare Telemetry & Retail |
| day62 | 9 | Lesson | Phase 2 | K-Means clustering: group machine operating regimes | Scenario: Healthcare Telemetry & Retail |
| day63 | 9 | Week check | Review | Week 9 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 9 |
| day64 | 10 | Lesson | Phase 2 | Train/val/test splits, cross-validation, and data leakage prevention | Scenario: Healthcare Telemetry & Retail |
| day65 | 10 | Lesson | Phase 2 | Hyperparameter tuning and heuristic baselines | Scenario: Healthcare Telemetry & Retail |
| day66 | 10 | Lesson | Phase 2 | Walk-forward validation and temporal lookahead leakage risks | Scenario: Healthcare Telemetry & Retail |
| day67 | 10 | Lesson | Phase 2 | Precision, Recall, F1 score, and Confusion Matrix: safety trade-offs | Scenario: Healthcare Telemetry & Retail |
| day68 | 10 | Lesson | Phase 2 | ROC-AUC and probability calibration: Brier score and reliability | Scenario: Healthcare Telemetry & Retail |
| day69 | 10 | Lesson | Phase 2 | XGBoost and LightGBM: gradient boosted decision trees for tabular telemetry | Scenario: Healthcare Telemetry & Retail |
| day70 | 10 | Week check | Review | Week 10 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 10 |
| day71 | 11 | Lesson | Phase 2 | Feature importance and SHAP values: explain individual alerts | Scenario: Healthcare Telemetry & Retail |
| day72 | 11 | Lesson | Phase 2 | Rolling statistics and ARIMA time-series modeling | Scenario: Healthcare Telemetry & Retail |
| day73 | 11 | Lesson | Phase 2 | Prophet: decompose trends and seasonal cycles | Scenario: Healthcare Telemetry & Retail |
| day74 | 11 | Lesson | Phase 2 | Forecasting evaluation: MAE, RMSE, and MAPE | Scenario: Healthcare Telemetry & Retail |
| day75 | 11 | Lesson | Phase 2 | Z-score, IQR, and Isolation Forest anomaly detection | Scenario: Healthcare Telemetry & Retail |
| day76 | 11 | Lesson | Phase 2 | Recommendation systems, personalization, and customer targeting | Scenario: Healthcare Telemetry & Retail |
| day77 | 11 | Week check | Review | Week 11 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 11 |
| day78 | 12 | Lesson | Phase 2 | Price elasticity and econometrics: causal demand modeling | Scenario: Healthcare Telemetry & Retail |
| day79 | 12 | Lesson | Phase 2 | Monte Carlo simulation: estimate component failure risk distribution | Scenario: Healthcare Telemetry & Retail |
| day80 | 12 | Lesson | Phase 2 | Linear programming and scipy.optimize: resource allocation | Scenario: Healthcare Telemetry & Retail |
| day81 | 12 | Lesson | Phase 2 | Nonlinear curve fitting and sensor calibration on noisy telemetry | Scenario: Healthcare Telemetry & Retail |
| day82 | 12 | Lesson | Phase 2 | MLflow: log parameters, metrics, and model artifacts | Scenario: Healthcare Telemetry & Retail |
| day83 | 12 | Lesson | Phase 2 | R and Scala awareness: statistical modeling and Spark ML | Scenario: Healthcare Telemetry & Retail |
| day84 | 12 | Week check | Review | Week 12 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 12 |
| day85 | 13 | Build | Phase 2 | Build: churn prediction model with precision/recall tuning | Scenario: Healthcare Telemetry & Retail |
| day86 | 13 | Build | Phase 2 | Build: multivariate sensor anomaly detector with Isolation Forest | Scenario: Healthcare Telemetry & Retail |
| day87 | 13 | Build | Phase 2 | Build: price elasticity regression model | Scenario: Healthcare Telemetry & Retail |
| day88 | 13 | Build | Phase 2 | Build: track all runs and metrics in MLflow | Scenario: Healthcare Telemetry & Retail |
| day89 | 13 | Lesson | Phase 3 | Tokens, tokenization (BPE/WordPiece), and context windows | Scenario: Plant Assistant Support Desk |
| day90 | 13 | Lesson | Phase 3 | Embeddings: dense vector representations of language | Scenario: Plant Assistant Support Desk |
| day91 | 13 | Week check | Review | Week 13 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 13 |
| day92 | 14 | Lesson | Phase 3 | Temperature, top-p, and token limits: output sampling control | Scenario: Plant Assistant Support Desk |
| day93 | 14 | Lesson | Phase 3 | OpenAI API: chat completions and client configuration | Scenario: Plant Assistant Support Desk |
| day94 | 14 | Lesson | Phase 3 | Anthropic and Gemini APIs: system prompts and multimodal inputs | Scenario: Plant Assistant Support Desk |
| day95 | 14 | Lesson | Phase 3 | Open models: LLaMA, Mistral, Qwen architecture and local weights | Scenario: Plant Assistant Support Desk |
| day96 | 14 | Lesson | Phase 3 | System prompts and few-shot in-context learning | Scenario: Plant Assistant Support Desk |
| day97 | 14 | Lesson | Phase 3 | Chain-of-thought: elicit multi-step deductive reasoning | Scenario: Plant Assistant Support Desk |
| day98 | 14 | Week check | Review | Week 14 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 14 |
| day99 | 15 | Lesson | Phase 3 | Prompt libraries and versioning with PromptLayer | Scenario: Plant Assistant Support Desk |
| day100 | 15 | Lesson | Phase 3 | Structured JSON output: enforce schemas via OpenAI and Instructor | Scenario: Plant Assistant Support Desk |
| day101 | 15 | Lesson | Phase 3 | Pydantic validation: parse and guarantee model response structure | Scenario: Plant Assistant Support Desk |
| day102 | 15 | Lesson | Phase 3 | Function calling: declare tool schemas and handle tool calls | Scenario: Plant Assistant Support Desk |
| day103 | 15 | Lesson | Phase 3 | Streaming responses: token-by-token async generators | Scenario: Plant Assistant Support Desk |
| day104 | 15 | Lesson | Phase 3 | Token counting, cost tracking, and prompt compression | Scenario: Plant Assistant Support Desk |
| day105 | 15 | Week check | Review | Week 15 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 15 |
| day106 | 16 | Lesson | Phase 3 | LLM Gateway: unified provider-agnostic interface | Scenario: Plant Assistant Support Desk |
| day107 | 16 | Lesson | Phase 3 | Image and video generation prompting and visual quality checks | Scenario: Plant Assistant Support Desk |
| day108 | 16 | Lesson | Phase 3 | AI coding assistants: effective workflows with Copilot, Claude Code, and Codex | Scenario: Plant Assistant Support Desk |
| day109 | 16 | Build | Phase 3 | Build: structured extraction engine with Pydantic schemas and tool calling | Scenario: Plant Assistant Support Desk |
| day110 | 16 | Build | Phase 3 | Build: Bootstrap web UI for structured AI report generator | Scenario: Plant Assistant Support Desk |
| day111 | 16 | Lesson | Phase 4 | Document ingestion: extract text from PDFs, HTML, and Markdown | Scenario: Banking SOPs & Plant Manuals |
| day112 | 16 | Week check | Review | Week 16 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 16 |
| day113 | 17 | Lesson | Phase 4 | Document cleaning and metadata extraction | Scenario: Banking SOPs & Plant Manuals |
| day114 | 17 | Lesson | Phase 4 | Fixed-size, recursive character, and semantic chunking strategies | Scenario: Banking SOPs & Plant Manuals |
| day115 | 17 | Lesson | Phase 4 | Embedding models: choose MTEB benchmarks and domain encoders | Scenario: Banking SOPs & Plant Manuals |
| day116 | 17 | Lesson | Phase 4 | pgvector and Chroma: relational and local vector search | Scenario: Banking SOPs & Plant Manuals |
| day117 | 17 | Lesson | Phase 4 | FAISS and Pinecone: dense index algorithms and managed indexes | Scenario: Banking SOPs & Plant Manuals |
| day118 | 17 | Lesson | Phase 4 | Weaviate and Milvus: high-scale distributed vector databases | Scenario: Banking SOPs & Plant Manuals |
| day119 | 17 | Week check | Review | Week 17 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 17 |
| day120 | 18 | Lesson | Phase 4 | Managed search: OpenSearch, Azure AI Search, Bedrock, and MongoDB | Scenario: Banking SOPs & Plant Manuals |
| day121 | 18 | Lesson | Phase 4 | Hybrid search: reciprocal rank fusion (RRF) of BM25 + dense vectors | Scenario: Banking SOPs & Plant Manuals |
| day122 | 18 | Lesson | Phase 4 | Cross-encoder reranking: re-score top-k candidates | Scenario: Banking SOPs & Plant Manuals |
| day123 | 18 | Lesson | Phase 4 | Context injection and source citations for grounded answers | Scenario: Banking SOPs & Plant Manuals |
| day124 | 18 | Lesson | Phase 4 | Retrieval confidence thresholding and honest abstention | Scenario: Banking SOPs & Plant Manuals |
| day125 | 18 | Lesson | Phase 4 | Semantic caching: reduce cost and latency using vector similarity in Redis | Scenario: Banking SOPs & Plant Manuals |
| day126 | 18 | Week check | Review | Week 18 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 18 |
| day127 | 19 | Lesson | Phase 4 | Graph databases: entity-relationship modeling with Neo4j | Scenario: Banking SOPs & Plant Manuals |
| day128 | 19 | Lesson | Phase 4 | GraphRAG: combine hierarchical entity communities and vector retrieval | Scenario: Banking SOPs & Plant Manuals |
| day129 | 19 | Lesson | Phase 4 | LangChain and LlamaIndex: chains, retrievers, and query engines | Scenario: Banking SOPs & Plant Manuals |
| day130 | 19 | Build | Phase 4 | Build: document ingestion and hybrid vector indexer | Scenario: Banking SOPs & Plant Manuals |
| day131 | 19 | Build | Phase 4 | Build: query engine with cross-encoder reranking | Scenario: Banking SOPs & Plant Manuals |
| day132 | 19 | Build | Phase 4 | Build: citation verification and low-confidence abstention guard | Scenario: Banking SOPs & Plant Manuals |
| day133 | 19 | Week check | Review | Week 19 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 19 |
| day134 | 20 | Lesson | Phase 5 | The Agent Loop: ReAct pattern (Reason, Act, Observe) | Scenario: Enterprise Operations (Salesforce/SAP) |
| day135 | 20 | Lesson | Phase 5 | Decision logic and safe tool execution | Scenario: Enterprise Operations (Salesforce/SAP) |
| day136 | 20 | Lesson | Phase 5 | LangGraph: stateful multi-actor agent workflows with cyclical graphs | Scenario: Enterprise Operations (Salesforce/SAP) |
| day137 | 20 | Lesson | Phase 5 | CrewAI and AutoGen: role-based multi-agent collaboration | Scenario: Enterprise Operations (Salesforce/SAP) |
| day138 | 20 | Lesson | Phase 5 | Semantic Kernel and Strands Agents awareness | Scenario: Enterprise Operations (Salesforce/SAP) |
| day139 | 20 | Lesson | Phase 5 | Supervisor pattern and task orchestration among specialized agents | Scenario: Enterprise Operations (Salesforce/SAP) |
| day140 | 20 | Week check | Review | Week 20 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 20 |
| day141 | 21 | Lesson | Phase 5 | Short-term, long-term, and episodic memory systems | Scenario: Enterprise Operations (Salesforce/SAP) |
| day142 | 21 | Lesson | Phase 5 | Agent memory frameworks: integrate Mem0 for personalized context | Scenario: Enterprise Operations (Salesforce/SAP) |
| day143 | 21 | Lesson | Phase 5 | Context engineering: dynamic pruning and just-in-time retrieval | Scenario: Enterprise Operations (Salesforce/SAP) |
| day144 | 21 | Lesson | Phase 5 | Human-in-the-loop approval and bounded unattended execution | Scenario: Enterprise Operations (Salesforce/SAP) |
| day145 | 21 | Lesson | Phase 5 | Model Context Protocol (MCP): architecture and protocol specification | Scenario: Enterprise Operations (Salesforce/SAP) |
| day146 | 21 | Lesson | Phase 5 | Build an MCP server: expose custom tools and resources | Scenario: Enterprise Operations (Salesforce/SAP) |
| day147 | 21 | Week check | Review | Week 21 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 21 |
| day148 | 22 | Lesson | Phase 5 | Build an MCP client connector: integrate server tools into agent | Scenario: Enterprise Operations (Salesforce/SAP) |
| day149 | 22 | Lesson | Phase 5 | Agent-to-Agent (A2A) protocol and AgentBridge awareness | Scenario: Enterprise Operations (Salesforce/SAP) |
| day150 | 22 | Lesson | Phase 5 | Low-code agent platforms: n8n, Copilot Studio, Glean, Agentforce, and DUST | Scenario: Enterprise Operations (Salesforce/SAP) |
| day151 | 22 | Lesson | Phase 5 | RPA and programmatic workflow automation | Scenario: Enterprise Operations (Salesforce/SAP) |
| day152 | 22 | Lesson | Phase 5 | Enterprise APIs: integrate Salesforce, SAP Ariba, Dynamics 365, and SuccessFactors | Scenario: Enterprise Operations (Salesforce/SAP) |
| day153 | 22 | Build | Phase 5 | Build: standalone MCP server with plant diagnostic tools | Scenario: Enterprise Operations (Salesforce/SAP) |
| day154 | 22 | Week check | Review | Week 22 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 22 |
| day155 | 23 | Build | Phase 5 | Build: LangGraph agent state machine connecting to MCP server | Scenario: Enterprise Operations (Salesforce/SAP) |
| day156 | 23 | Build | Phase 5 | Build: end-to-end multi-step tool execution with human approval | Scenario: Enterprise Operations (Salesforce/SAP) |
| day157 | 23 | Lesson | Phase 6 | Golden datasets, offline vs online evals, and human review | Scenario: Healthcare & BFSI Compliance |
| day158 | 23 | Lesson | Phase 6 | LLM-as-a-judge and model graders with rubrics | Scenario: Healthcare & BFSI Compliance |
| day159 | 23 | Lesson | Phase 6 | Retrieval metrics: Precision@k, Recall@k, Hit Rate, MRR, and nDCG | Scenario: Healthcare & BFSI Compliance |
| day160 | 23 | Lesson | Phase 6 | Context precision and context recall evaluation | Scenario: Healthcare & BFSI Compliance |
| day161 | 23 | Week check | Review | Week 23 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 23 |
| day162 | 24 | Lesson | Phase 6 | Faithfulness, groundedness, and answer relevance metrics | Scenario: Healthcare & BFSI Compliance |
| day163 | 24 | Lesson | Phase 6 | RAGAS and DeepEval: automated end-to-end evaluation pipeline | Scenario: Healthcare & BFSI Compliance |
| day164 | 24 | Lesson | Phase 6 | Agent evaluation: goal completion rate, trajectory cost, and failure modes | Scenario: Healthcare & BFSI Compliance |
| day165 | 24 | Lesson | Phase 6 | Reliability testing: temperature zero variance and edge cases | Scenario: Healthcare & BFSI Compliance |
| day166 | 24 | Lesson | Phase 6 | Multi-system test harnesses: mock complex multi-service workflows | Scenario: Healthcare & BFSI Compliance |
| day167 | 24 | Lesson | Phase 6 | CI/CD regression evaluation gates: prevent quality degradation | Scenario: Healthcare & BFSI Compliance |
| day168 | 24 | Week check | Review | Week 24 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 24 |
| day169 | 25 | Lesson | Phase 6 | Prompt A/B testing: quantitative trade-offs across cost and quality | Scenario: Healthcare & BFSI Compliance |
| day170 | 25 | Lesson | Phase 6 | Input and output guardrails: detect prompt injection and hallucination | Scenario: Healthcare & BFSI Compliance |
| day171 | 25 | Lesson | Phase 6 | PII masking and data classification under GDPR and India DPDP | Scenario: Healthcare & BFSI Compliance |
| day172 | 25 | Lesson | Phase 6 | Responsible AI: bias detection and immutable audit trails | Scenario: Healthcare & BFSI Compliance |
| day173 | 25 | Lesson | Phase 6 | Langfuse, LangSmith, Arize, and Weights & Biases observability | Scenario: Healthcare & BFSI Compliance |
| day174 | 25 | Lesson | Phase 6 | OpenTelemetry, Prometheus, Grafana, and Datadog monitoring | Scenario: Healthcare & BFSI Compliance |
| day175 | 25 | Week check | Review | Week 25 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 25 |
| day176 | 26 | Lesson | Phase 6 | FinOps: token budgets, alerts, and ServiceNow incident workflows | Scenario: Healthcare & BFSI Compliance |
| day177 | 26 | Lesson | Phase 6 | Security: RBAC, row-level security, and multi-tenant isolation | Scenario: Healthcare & BFSI Compliance |
| day178 | 26 | Build | Phase 6 | Build: sensor anomaly detection integration for Plant Assistant | Scenario: Healthcare & BFSI Compliance |
| day179 | 26 | Build | Phase 6 | Build: diagnostic MCP server with plant manual RAG index | Scenario: Healthcare & BFSI Compliance |
| day180 | 26 | Build | Phase 6 | Build: automated evaluation suite with RAGAS metrics | Scenario: Healthcare & BFSI Compliance |
| day181 | 26 | Build | Phase 6 | Build: end-to-end tracing and observability with Langfuse | Scenario: Healthcare & BFSI Compliance |
| day182 | 26 | Week check | Review | Week 26 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 26 |
| day183 | 27 | Lesson | Phase 7 | AWS IAM, S3, Lambda, and API Gateway: serverless architectures | Scenario: Live Plant Assistant Operations |
| day184 | 27 | Lesson | Phase 7 | AWS ECS/EKS, SageMaker, Bedrock, and Bedrock AgentCore | Scenario: Live Plant Assistant Operations |
| day185 | 27 | Lesson | Phase 7 | Azure OpenAI, AI Foundry, and AI Search integration | Scenario: Live Plant Assistant Operations |
| day186 | 27 | Lesson | Phase 7 | GCP Vertex AI: model garden, endpoints, and pipelines | Scenario: Live Plant Assistant Operations |
| day187 | 27 | Lesson | Phase 7 | Multi-cloud and hybrid-cloud: workload migration and latency | Scenario: Live Plant Assistant Operations |
| day188 | 27 | Lesson | Phase 7 | CI/CD with GitHub Actions, Jenkins, and Harness deployment pipelines | Scenario: Live Plant Assistant Operations |
| day189 | 27 | Week check | Review | Week 27 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 27 |
| day190 | 28 | Lesson | Phase 7 | Terraform and Ansible: declarative infrastructure provisioning | Scenario: Live Plant Assistant Operations |
| day191 | 28 | Lesson | Phase 7 | Kubernetes pods, deployments, services, and ingress | Scenario: Live Plant Assistant Operations |
| day192 | 28 | Lesson | Phase 7 | Apache Spark: distributed data processing fundamentals | Scenario: Live Plant Assistant Operations |
| day193 | 28 | Lesson | Phase 7 | Databricks and Delta Lake: lakehouse architecture | Scenario: Live Plant Assistant Operations |
| day194 | 28 | Lesson | Phase 7 | Snowflake and Teradata: cloud data warehousing | Scenario: Live Plant Assistant Operations |
| day195 | 28 | Lesson | Phase 7 | Apache Kafka: real-time event streaming and consumer groups | Scenario: Live Plant Assistant Operations |
| day196 | 28 | Week check | Review | Week 28 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 28 |
| day197 | 29 | Lesson | Phase 7 | Apache Airflow and robust ETL pipelines: DAG scheduling | Scenario: Live Plant Assistant Operations |
| day198 | 29 | Lesson | Phase 7 | Model Registry and drift detection in production | Scenario: Live Plant Assistant Operations |
| day199 | 29 | Lesson | Phase 7 | Kubeflow pipelines: automated ML training workflows | Scenario: Live Plant Assistant Operations |
| day200 | 29 | Build | Phase 7 | Build: package Plant Assistant Docker container for production | Scenario: Live Plant Assistant Operations |
| day201 | 29 | Build | Phase 7 | Build: create GitHub Actions CI/CD deployment pipeline | Scenario: Live Plant Assistant Operations |
| day202 | 29 | Build | Phase 7 | Build: health checks, canary rollout, and monitoring alerts | Scenario: Live Plant Assistant Operations |
| day203 | 29 | Week check | Review | Week 29 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 29 |
| day204 | 30 | Lesson | Phase 8 | Feedforward neural networks, activations (ReLU/GELU), and loss functions | Scenario: Sensor Signals & Vision Prep |
| day205 | 30 | Lesson | Phase 8 | Backpropagation and automatic differentiation computational graphs | Scenario: Sensor Signals & Vision Prep |
| day206 | 30 | Lesson | Phase 8 | Optimizers: SGD, Adam, AdamW, and learning rate schedules | Scenario: Sensor Signals & Vision Prep |
| day207 | 30 | Lesson | Phase 8 | Overfitting remedies: L1/L2 regularization, Dropout, and LayerNorm | Scenario: Sensor Signals & Vision Prep |
| day208 | 30 | Lesson | Phase 8 | PyTorch basics: tensors, autograd, and `nn.Module` | Scenario: Sensor Signals & Vision Prep |
| day209 | 30 | Lesson | Phase 8 | PyTorch Dataset, DataLoader, and training loop structure | Scenario: Sensor Signals & Vision Prep |
| day210 | 30 | Week check | Review | Week 30 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 30 |
| day211 | 31 | Lesson | Phase 8 | TensorFlow and Keras awareness | Scenario: Sensor Signals & Vision Prep |
| day212 | 31 | Lesson | Phase 8 | Convolutional layers and pooling: spatial feature extraction | Scenario: Sensor Signals & Vision Prep |
| day213 | 31 | Lesson | Phase 8 | ResNet and skip connections: training deep residual networks | Scenario: Sensor Signals & Vision Prep |
| day214 | 31 | Lesson | Phase 8 | RNNs and LSTMs: sequential memory and gated recurrence | Scenario: Sensor Signals & Vision Prep |
| day215 | 31 | Lesson | Phase 8 | Self-Attention mechanism: query, key, value projections | Scenario: Sensor Signals & Vision Prep |
| day216 | 31 | Lesson | Phase 8 | Multi-Head Attention and positional encodings | Scenario: Sensor Signals & Vision Prep |
| day217 | 31 | Week check | Review | Week 31 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 31 |
| day218 | 32 | Lesson | Phase 8 | Transformer architecture: Encoder (BERT) vs Decoder (GPT) | Scenario: Sensor Signals & Vision Prep |
| day219 | 32 | Lesson | Phase 8 | Hugging Face Transformers: pipelines, models, and tokenizers | Scenario: Sensor Signals & Vision Prep |
| day220 | 32 | Lesson | Phase 8 | Transfer learning: fine-tuning pretrained foundation models | Scenario: Sensor Signals & Vision Prep |
| day221 | 32 | Build | Phase 8 | Build: train BERT text classifier on telemetry tickets | Scenario: Sensor Signals & Vision Prep |
| day222 | 32 | Build | Phase 8 | Build: train ResNet image classifier on equipment defect dataset | Scenario: Sensor Signals & Vision Prep |
| day223 | 32 | Lesson | Phase 9 | Named Entity Recognition (NER) and text classification | Scenario: Legal Contracts & Document Intelligence |
| day224 | 32 | Week check | Review | Week 32 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 32 |
| day225 | 33 | Lesson | Phase 9 | PII detection in unstructured documents | Scenario: Legal Contracts & Document Intelligence |
| day226 | 33 | Lesson | Phase 9 | Semantic search and resume-to-job description matching | Scenario: Legal Contracts & Document Intelligence |
| day227 | 33 | Lesson | Phase 9 | OpenCV: image preprocessing, thresholds, and transformations | Scenario: Legal Contracts & Document Intelligence |
| day228 | 33 | Lesson | Phase 9 | Object detection fundamentals: bounding boxes and anchor points | Scenario: Legal Contracts & Document Intelligence |
| day229 | 33 | Lesson | Phase 9 | YOLO architecture: real-time single-shot detection | Scenario: Legal Contracts & Document Intelligence |
| day230 | 33 | Lesson | Phase 9 | Faster R-CNN, DETR, and Segment Anything Model (SAM) | Scenario: Legal Contracts & Document Intelligence |
| day231 | 33 | Week check | Review | Week 33 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 33 |
| day232 | 34 | Lesson | Phase 9 | Intersection over Union (IoU), NMS, and mAP evaluation | Scenario: Legal Contracts & Document Intelligence |
| day233 | 34 | Lesson | Phase 9 | Video object tracking and DeepSORT algorithm | Scenario: Legal Contracts & Document Intelligence |
| day234 | 34 | Lesson | Phase 9 | Activity recognition and video anomaly detection | Scenario: Legal Contracts & Document Intelligence |
| day235 | 34 | Lesson | Phase 9 | OCR engines: Tesseract, PaddleOCR, and docTR | Scenario: Legal Contracts & Document Intelligence |
| day236 | 34 | Lesson | Phase 9 | OCR evaluation: Character Error Rate (CER) and Word Error Rate (WER) | Scenario: Legal Contracts & Document Intelligence |
| day237 | 34 | Lesson | Phase 9 | LayoutLMv3: multimodal spatial, visual, and textual modeling | Scenario: Legal Contracts & Document Intelligence |
| day238 | 34 | Week check | Review | Week 34 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 34 |
| day239 | 35 | Lesson | Phase 9 | Donut: OCR-free end-to-end document understanding | Scenario: Legal Contracts & Document Intelligence |
| day240 | 35 | Lesson | Phase 9 | Vision LLMs and Vision AI agents: visual grounding and screenshot understanding | Scenario: Legal Contracts & Document Intelligence |
| day241 | 35 | Lesson | Phase 9 | Document AI benchmarks: RVL-CDIP, FUNSD, and SROIE | Scenario: Legal Contracts & Document Intelligence |
| day242 | 35 | Build | Phase 9 | Build: document image preprocessing and OCR extraction pipeline | Scenario: Legal Contracts & Document Intelligence |
| day243 | 35 | Build | Phase 9 | Build: LayoutLMv3 key-value pair extraction for invoices | Scenario: Legal Contracts & Document Intelligence |
| day244 | 35 | Build | Phase 9 | Build: validation schemas and confidence scoring service | Scenario: Legal Contracts & Document Intelligence |
| day245 | 35 | Week check | Review | Week 35 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 35 |
| day246 | 36 | Build | Phase 9 | Build: FastAPI endpoint serving Document Intelligence API | Scenario: Legal Contracts & Document Intelligence |
| day247 | 36 | Lesson | Phase 10 | Decision framework: RAG vs Prompting vs Fine-Tuning | Scenario: RLHF Annotation Platform |
| day248 | 36 | Lesson | Phase 10 | Supervised Fine-Tuning (SFT) principles and dataset formats | Scenario: RLHF Annotation Platform |
| day249 | 36 | Lesson | Phase 10 | Low-Rank Adaptation (LoRA): rank selection and alpha scaling | Scenario: RLHF Annotation Platform |
| day250 | 36 | Lesson | Phase 10 | QLoRA: 4-bit NormalFloat quantization and page optimizers | Scenario: RLHF Annotation Platform |
| day251 | 36 | Lesson | Phase 10 | Fine-tuning with Hugging Face `peft` and `trl` libraries | Scenario: RLHF Annotation Platform |
| day252 | 36 | Week check | Review | Week 36 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 36 |
| day253 | 37 | Lesson | Phase 10 | RLHF pipeline: Supervised fine-tuning step | Scenario: RLHF Annotation Platform |
| day254 | 37 | Lesson | Phase 10 | Reward model training: ranking loss and pairwise comparison | Scenario: RLHF Annotation Platform |
| day255 | 37 | Lesson | Phase 10 | Proximal Policy Optimization (PPO) for LLM alignment | Scenario: RLHF Annotation Platform |
| day256 | 37 | Lesson | Phase 10 | Direct Preference Optimization (DPO): math and advantages over PPO | Scenario: RLHF Annotation Platform |
| day257 | 37 | Lesson | Phase 10 | DPO dataset engineering and RLAIF principles | Scenario: RLHF Annotation Platform |
| day258 | 37 | Lesson | Phase 10 | Data annotation workflows with Label Studio | Scenario: RLHF Annotation Platform |
| day259 | 37 | Week check | Review | Week 37 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 37 |
| day260 | 38 | Lesson | Phase 10 | Active learning strategies: uncertainty, entropy, and margin sampling | Scenario: RLHF Annotation Platform |
| day261 | 38 | Lesson | Phase 10 | Inter-annotator agreement: Cohen's Kappa and Fleiss' Kappa | Scenario: RLHF Annotation Platform |
| day262 | 38 | Lesson | Phase 10 | Label noise mitigation: majority voting and gold standard checks | Scenario: RLHF Annotation Platform |
| day263 | 38 | Build | Phase 10 | Build: dataset ingestion and pairwise preference annotation UI | Scenario: RLHF Annotation Platform |
| day264 | 38 | Build | Phase 10 | Build: inter-annotator agreement scoring engine | Scenario: RLHF Annotation Platform |
| day265 | 38 | Build | Phase 10 | Build: automated DPO export and validation pipeline | Scenario: RLHF Annotation Platform |
| day266 | 38 | Week check | Review | Week 38 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 38 |
| day267 | 39 | Lesson | Phase 11 | Model quantization: INT8, INT4, AWQ, and GGUF formats | Scenario: Edge Cameras & Low-Latency Serving |
| day268 | 39 | Lesson | Phase 11 | vLLM: PagedAttention and high-throughput serving | Scenario: Edge Cameras & Low-Latency Serving |
| day269 | 39 | Lesson | Phase 11 | Ollama and TGI: local model execution and containerized serving | Scenario: Edge Cameras & Low-Latency Serving |
| day270 | 39 | Lesson | Phase 11 | ONNX: cross-platform model graph export and runtime | Scenario: Edge Cameras & Low-Latency Serving |
| day271 | 39 | Lesson | Phase 11 | TensorRT and OpenVINO: GPU engine and CPU acceleration | Scenario: Edge Cameras & Low-Latency Serving |
| day272 | 39 | Lesson | Phase 11 | KV cache management, continuous batching, and VRAM sizing | Scenario: Edge Cameras & Low-Latency Serving |
| day273 | 39 | Week check | Review | Week 39 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 39 |
| day274 | 40 | Lesson | Phase 11 | Edge deployment: optimize models for resource-constrained hardware | Scenario: Edge Cameras & Low-Latency Serving |
| day275 | 40 | Lesson | Phase 11 | Air-gapped and on-prem packaging for regulated environments | Scenario: Edge Cameras & Low-Latency Serving |
| day276 | 40 | Build | Phase 11 | Build: serve Plant Assistant via local quantized model in vLLM | Scenario: Edge Cameras & Low-Latency Serving |
| day277 | 40 | Build | Phase 11 | Build: export Document API model to ONNX and benchmark latency | Scenario: Edge Cameras & Low-Latency Serving |
| day278 | 40 | Lesson | Phase 12 | Harness engineering: robust tool interfaces and failure handling | Scenario: AutoML Research Agent |
| day279 | 40 | Lesson | Phase 12 | Verification steps: validate tool results before execution continues | Scenario: AutoML Research Agent |
| day280 | 40 | Week check | Review | Week 40 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 40 |
| day281 | 41 | Lesson | Phase 12 | Sub-agents: specialize child agents for bounded sub-problems | Scenario: AutoML Research Agent |
| day282 | 41 | Lesson | Phase 12 | Long-horizon tasks: manage compounding errors across steps | Scenario: AutoML Research Agent |
| day283 | 41 | Lesson | Phase 12 | State persistence and crash recovery: save and resume multi-step agent plans | Scenario: AutoML Research Agent |
| day284 | 41 | Lesson | Phase 12 | Context compression: summarize trajectory history | Scenario: AutoML Research Agent |
| day285 | 41 | Lesson | Phase 12 | Budget enforcement: step caps, cost limits, and execution timeouts | Scenario: AutoML Research Agent |
| day286 | 41 | Lesson | Phase 12 | Loop detection, goal drift, and reward hacking prevention | Scenario: AutoML Research Agent |
| day287 | 41 | Week check | Review | Week 41 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 41 |
| day288 | 42 | Lesson | Phase 12 | Immutable audit logs and deterministic trace replay | Scenario: AutoML Research Agent |
| day289 | 42 | Lesson | Phase 12 | Sandboxed code execution: secure containerized code interpreters | Scenario: AutoML Research Agent |
| day290 | 42 | Lesson | Phase 12 | Mechanistic interpretability: inspecting internal activation patterns | Scenario: AutoML Research Agent |
| day291 | 42 | Build | Phase 12 | Build: iterative ML experiment planning and harness engine | Scenario: AutoML Research Agent |
| day292 | 42 | Build | Phase 12 | Build: sandboxed execution and metric validation tool | Scenario: AutoML Research Agent |
| day293 | 42 | Build | Phase 12 | Build: budget-capped autonomous hyperparameter optimization run | Scenario: AutoML Research Agent |
| day294 | 42 | Week check | Review | Week 42 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 42 |
| day295 | 43 | Lesson | Phase 13 | C and C++ systems code awareness for AI runtime backends | Scenario: High-Scale Infrastructure |
| day296 | 43 | Lesson | Phase 13 | CUDA programming: GPU threads, blocks, and shared memory | Scenario: High-Scale Infrastructure |
| day297 | 43 | Lesson | Phase 13 | GPU architecture: memory bandwidth vs compute utilization | Scenario: High-Scale Infrastructure |
| day298 | 43 | Lesson | Phase 13 | Real-time control loops and embedded systems deadlines | Scenario: High-Scale Infrastructure |
| day299 | 43 | Lesson | Phase 13 | Multi-sensor fusion: Kalman filters and sensor complementary fusion | Scenario: High-Scale Infrastructure |
| day300 | 43 | Lesson | Phase 13 | Sensor calibration against ground truth standards | Scenario: High-Scale Infrastructure |
| day301 | 43 | Week check | Review | Week 43 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 43 |
| day302 | 44 | Lesson | Phase 13 | Control logic and closed-loop feedback systems | Scenario: High-Scale Infrastructure |
| day303 | 44 | Lesson | Phase 13 | Go, Java, and Rust for high-concurrency AI microservices | Scenario: High-Scale Infrastructure |
| day304 | 44 | Lesson | Phase 13 | Virtualization, containers, and Linux network namespaces | Scenario: High-Scale Infrastructure |
| day305 | 44 | Lesson | Phase 13 | High-throughput storage for distributed model training | Scenario: High-Scale Infrastructure |
| day306 | 44 | Lesson | Phase 13 | Private cloud infrastructure: OpenStack and advanced Kubernetes operators | Scenario: High-Scale Infrastructure |
| day307 | 44 | Lesson | Phase 13 | Distributed ML: Data Parallelism vs Model Parallelism | Scenario: High-Scale Infrastructure |
| day308 | 44 | Week check | Review | Week 44 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 44 |
| day309 | 45 | Lesson | Phase 13 | Distributed communication: AllReduce, ZeRO, and Megatron-LM | Scenario: High-Scale Infrastructure |
| day310 | 45 | Lesson | Phase 13 | Private cloud deployments for proprietary data compliance | Scenario: High-Scale Infrastructure |
| day311 | 45 | Lesson | Phase 13 | Enterprise AI reference architectures: end-to-end blue printing | Scenario: High-Scale Infrastructure |
| day312 | 45 | Lesson | Phase 13 | Conducting enterprise AI design reviews and compliance audits | Scenario: High-Scale Infrastructure |
| day313 | 45 | Lesson | Phase 13 | Domain-specific constraints: BFSI, healthcare, and manufacturing | Scenario: High-Scale Infrastructure |
| day314 | 45 | Lesson | Phase 13 | Technical strategy, executive presentations, and engineer mentoring | Scenario: High-Scale Infrastructure |
| day315 | 45 | Week check | Review | Week 45 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 45 |
| day316 | 46 | Lesson | Throughout all phases | DSA: algorithmic problem-solving patterns (Two Pointers, Sliding Window) | Scenario: Career & Engineering Excellence |
| day317 | 46 | Lesson | Throughout all phases | DSA: graph and tree traversals for interview coding | Scenario: Career & Engineering Excellence |
| day318 | 46 | Lesson | Throughout all phases | System Design: scalable backend architecture for high-QPS APIs | Scenario: Career & Engineering Excellence |
| day319 | 46 | Lesson | Throughout all phases | System Design: high-throughput production LLM service | Scenario: Career & Engineering Excellence |
| day320 | 46 | Lesson | Throughout all phases | Technical Communication: demoing systems and articulating trade-offs | Scenario: Career & Engineering Excellence |
| day321 | 46 | Lesson | Throughout all phases | Build in Public: engineering blogs and LinkedIn architecture logs | Scenario: Career & Engineering Excellence |
| day322 | 46 | Week check | Review | Week 46 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 46 |
| day323 | 47 | Lesson | Throughout all phases | Open Source: contributing bug fixes and connectors to AI libraries | Scenario: Career & Engineering Excellence |
| day324 | 47 | Build | Capstone & Final Evaluation | Capstone: build multi-modal ingestion and hybrid RAG indexing | Scenario: Enterprise Multi-Modal System |
| day325 | 47 | Build | Capstone & Final Evaluation | Capstone: build autonomous diagnostic agent with MCP tools | Scenario: Enterprise Multi-Modal System |
| day326 | 47 | Build | Capstone & Final Evaluation | Capstone: implement input/output guardrails and PII masking | Scenario: Enterprise Multi-Modal System |
| day327 | 47 | Build | Capstone & Final Evaluation | Capstone: deploy full service with CI/CD and automated evals | Scenario: Enterprise Multi-Modal System |
| day328 | 47 | Theory test | Capstone & Final Evaluation | Comprehensive Theory Examination: 30-job system design and trade-offs | Scenario: Enterprise Multi-Modal System |
| day329 | 47 | Week check | Review | Week 47 check. Consolidate that week's ideas in words and code. No new idea. | Consolidate week 47 |
| day330 | 48 | Practical test | Capstone & Final Evaluation | Practical Coding Examination: timed implementation on fresh production scenarios | Scenario: Enterprise Multi-Modal System |

## Coverage Table

Mapping every topic and requirement from `ROADMAP_SOURCE.md` to its corresponding day numbers in this daily schedule:

| Phase | Source Topic / Project / Requirement | Day(s) |
| --- | --- | --- |
| Phase 0 | Python basics: variables, loops, functions, lists and dicts, file handling, exceptions | day01–day05 |
| Phase 0 | Python OOP: classes, inheritance, modules | day06–day08 |
| Phase 0 | Python environment: virtual environments, pip, uv/Poetry, Jupyter notebooks | day09–day10 |
| Phase 0 | Git and GitHub: commit, branch, merge, pull requests, code reviews | day11–day12 |
| Phase 0 | Linux: terminal commands, bash and shell scripting, file permissions, SSH | day13–day15 |
| Phase 0 | SQL basics: SELECT, JOIN, GROUP BY, subqueries | day16–day17 |
| Phase 0 | Web basics: HTTP, JSON, REST APIs, status codes | day18 |
| Phase 0 | Agile / Scrum: sprints, stand-ups, retrospectives | day19 |
| Phase 0 | Mini project: a script that calls a public API and saves the results to a database. | day20–day22 |
| Phase 1 | FastAPI and Flask: routes, async endpoints, auth basics | day23–day24 |
| Phase 1 | Type hints and mypy; schema-first data models with Pydantic | day25–day26 |
| Phase 1 | Testing: TDD (write tests first), pytest, reusable fixtures, test coverage | day27–day29 |
| Phase 1 | Clean code: logging, error handling, documentation, secure coding | day30–day31 |
| Phase 1 | PostgreSQL: complex SQL, schema design, indexing, transactions, query optimization | day32–day33 |
| Phase 1 | Special table designs: temporal data models, system-versioned tables, audit-log tables | day34–day36 |
| Phase 1 | NoSQL: MongoDB, DynamoDB basics | day37 |
| Phase 1 | Caching and eventing: Redis, event-driven design, message queues | day38 |
| Phase 1 | Docker and docker-compose | day39 |
| Phase 1 | Service design: microservices basics | day40 |
| Phase 1 | Other API styles: gRPC, and SOAP awareness | day41 |
| Phase 1 | Frontend: JavaScript, TypeScript, AJAX, jQuery, React basics, Angular awareness | day42–day44 |
| Phase 1 | .NET: awareness level (for Optum) | day45 |
| Phase 1 | Mini project: a FastAPI + PostgreSQL app with tests and a Bootstrap frontend, running in Docker. | day46–day50 |
| Phase 2 | Data work: Pandas, NumPy, EDA, data cleaning, feature engineering | day51–day53 |
| Phase 2 | Visualization and dashboards: Matplotlib, Power BI, Tableau, KPI dashboards | day54–day55 |
| Phase 2 | Math: statistics, probability, linear algebra basics | day56–day58 |
| Phase 2 | Experiment design: A/B testing, confidence intervals, fair model comparison | day59 |
| Phase 2 | Scikit-learn: regression, classification, trees, random forest, clustering | day60–day62 |
| Phase 2 | ML workflow: train/validation/test split, cross-validation, hyperparameter tuning, baselines, data leakage | day63–day65 |
| Phase 2 | Time-ordered data: walk-forward validation, and leakage risks specific to time data | day66 |
| Phase 2 | Metrics: precision, recall, F1, confusion matrix, ROC-AUC, calibration | day67–day68 |
| Phase 2 | XGBoost and LightGBM | day69 |
| Phase 2 | Explainability: SHAP and feature importance | day70–day71 |
| Phase 2 | Time-series: rolling statistics, ARIMA, Prophet, forecasting | day72–day74 |
| Phase 2 | Anomaly detection: z-score, Isolation Forest | day75 |
| Phase 2 | Recommendation systems, personalization and targeting | day76 |
| Phase 2 | Pricing and economics: price elasticity, econometrics basics | day77–day78 |
| Phase 2 | Simulation: Monte Carlo | day79 |
| Phase 2 | Optimization theory: linear programming, scipy.optimize | day80 |
| Phase 2 | Model fitting and calibration on noisy sensor data | day81 |
| Phase 2 | MLflow experiment tracking | day82 |
| Phase 2 | R and Scala: awareness level (for Target) | day83 |
| Phase 2 | Mini project: a churn model, a sensor anomaly detector and a price elasticity model, all tracked in MLflow. | day84–day88 |
| Phase 3 | How LLMs work: tokens, context windows, embeddings | day89–day90 |
| Phase 3 | Generation parameters: temperature, top-p, token limits | day91–day92 |
| Phase 3 | Commercial LLM APIs: OpenAI, Anthropic, Gemini | day93–day94 |
| Phase 3 | Open models: LLaMA, Mistral, Qwen | day95 |
| Phase 3 | Prompt engineering: system prompts, few-shot, chain-of-thought | day96–day97 |
| Phase 3 | Prompt management: prompt libraries, prompt versioning with PromptLayer | day98–day99 |
| Phase 3 | Structured JSON output with Pydantic validation | day100–day101 |
| Phase 3 | Tool / function calling | day102 |
| Phase 3 | Streaming responses | day103 |
| Phase 3 | Cost tracking and token optimization | day104 |
| Phase 3 | Provider-agnostic design: an LLM gateway that lets you switch between providers | day105–day106 |
| Phase 3 | Image and video generation prompting; checking visual quality | day107 |
| Phase 3 | AI coding tools: GitHub Copilot, Codex, Claude Code, Microsoft 365 Copilot | day108 |
| Phase 3 | Mini project: a structured-output AI tool with a Bootstrap UI. | day109–day110 |
| Phase 4 | Document ingestion: parsing, cleaning, metadata | day111–day113 |
| Phase 4 | Chunking strategies: fixed-size, recursive, semantic | day114 |
| Phase 4 | Embedding models | day115 |
| Phase 4 | Open-source vector DBs: pgvector, Chroma, FAISS, Pinecone, Weaviate, Milvus | day116–day118 |
| Phase 4 | Managed vector search: OpenSearch, Azure AI Search, Bedrock Knowledge Bases, MongoDB vector search | day119–day120 |
| Phase 4 | Better retrieval: hybrid search (keyword + vector), reranking | day121–day122 |
| Phase 4 | Grounding answers: context injection, citations | day123 |
| Phase 4 | Abstention: answering "I don't know" when retrieval confidence is low | day124 |
| Phase 4 | Semantic caching with Redis | day125 |
| Phase 4 | Knowledge graphs and graph DBs: Neo4j, GraphRAG | day126–day128 |
| Phase 4 | Frameworks: LangChain, LlamaIndex | day129 |
| Phase 4 | Mini project: a RAG app with citations and abstention. | day130–day132 |
| Phase 5 | Agent loop: plan, act, observe | day133–day134 |
| Phase 5 | Decision logic and tool use | day135 |
| Phase 5 | Frameworks: LangGraph, CrewAI, AutoGen, Semantic Kernel, Strands Agents | day136–day138 |
| Phase 5 | Multi-agent systems: supervisor pattern, shared memory, task orchestration | day139 |
| Phase 5 | Memory: short-term, long-term and episodic memory; agent memory frameworks like Mem0 | day140–day142 |
| Phase 5 | Context engineering: giving the agent just-in-time context | day143 |
| Phase 5 | Human-in-the-loop approval; unattended (fully automatic) mode | day144 |
| Phase 5 | MCP: building servers and connectors | day145–day148 |
| Phase 5 | A2A protocol, and AgentBridge awareness | day149 |
| Phase 5 | Low-code platforms: n8n, Copilot Studio, Glean, Agentforce, DUST | day150 |
| Phase 5 | RPA and workflow automation | day151 |
| Phase 5 | Enterprise integrations: Salesforce, SAP Ariba, D365, SuccessFactors through their APIs | day152 |
| Phase 5 | Mini project: an MCP server with a LangGraph agent that uses it. | day153–day156 |
| Phase 6 | Eval basics: golden datasets, offline and online evals, human review, LLM-as-judge, model graders | day157–day158 |
| Phase 6 | RAG retrieval metrics: Precision@k, Recall@k, MRR, nDCG, hit rate, context precision and recall | day159–day160 |
| Phase 6 | RAG answer metrics: faithfulness, answer relevance, groundedness | day161–day162 |
| Phase 6 | RAG eval tools: RAGAS, DeepEval | day163 |
| Phase 6 | Agent evals: success rate, number of steps, cost, types of failure | day164 |
| Phase 6 | Reliability testing: determinism and non-determinism tests, edge cases | day165 |
| Phase 6 | Multi-system test harnesses: simulating whole workflows across several apps | day166 |
| Phase 6 | Regression checks and release gates in CI | day167 |
| Phase 6 | A/B testing prompts: comparing accuracy, latency and cost | day168–day169 |
| Phase 6 | Guardrails: hallucination control, input and output filters, prompt injection defense | day170 |
| Phase 6 | Privacy: PII masking, data classification, GDPR and India's DPDP law | day171 |
| Phase 6 | Responsible AI: bias, fairness, governance, audit logs | day172 |
| Phase 6 | LLM observability: Langfuse, LangSmith, Arize, Weights & Biases | day173 |
| Phase 6 | System observability: OpenTelemetry, Prometheus, Grafana, ELK, Datadog, structured logging, distributed tracing | day174 |
| Phase 6 | Incident management: ServiceNow; FinOps and cost monitoring | day175–day176 |
| Phase 6 | Security: authentication, RBAC, row-level security, multi-tenant isolation | day177 |
| Phase 6 | Big project: Plant Assistant (Job 1). Sensor anomalies, an MCP server, RAG with abstention, evals and Langfuse tracing. | day178–day181 |
| Phase 7 | AWS: IAM, S3, Lambda, API Gateway, ECS/EKS, DynamoDB, SageMaker, Bedrock, Bedrock AgentCore | day182–day184 |
| Phase 7 | Azure: Azure OpenAI, AI Foundry, AI Search, Cognitive Services, App Service | day185 |
| Phase 7 | GCP: Vertex AI | day186 |
| Phase 7 | Multi-cloud and hybrid-cloud basics | day187 |
| Phase 7 | CI/CD: GitHub Actions, Jenkins, Harness | day188 |
| Phase 7 | Infrastructure as code: Terraform, Ansible | day189–day190 |
| Phase 7 | Kubernetes basics | day191 |
| Phase 7 | Data platforms: Spark, Hadoop, Databricks, lakehouse architecture, Snowflake, Teradata | day192–day194 |
| Phase 7 | Data pipelines: Kafka, Airflow, ETL | day195–day197 |
| Phase 7 | MLOps: model registry, model monitoring, drift detection, Kubeflow | day198–day199 |
| Phase 7 | Milestone: deploy the Plant Assistant live with CI/CD. Start applying to jobs here (about 6 months in). | day200–day202 |
| Phase 8 | Neural networks: activations, loss functions, backpropagation | day203–day205 |
| Phase 8 | Optimizers: SGD and Adam; learning rate schedules | day206 |
| Phase 8 | Training problems: overfitting, dropout, batch norm, regularization | day207 |
| Phase 8 | Frameworks: PyTorch, TensorFlow and Keras | day208–day211 |
| Phase 8 | CNNs: convolution, pooling, ResNet, skip connections | day212–day213 |
| Phase 8 | RNNs and LSTMs: the vanishing gradient problem | day214 |
| Phase 8 | Transformers: attention, BERT vs GPT, tokenization | day215–day218 |
| Phase 8 | Hugging Face and transfer learning | day219–day220 |
| Phase 8 | Mini project: a BERT text classifier and a ResNet image classifier. | day221–day222 |
| Phase 9 | NLP tasks: NER, text classification, PII detection, semantic search, resume/job matching | day223–day226 |
| Phase 9 | OpenCV basics | day227 |
| Phase 9 | Object detection: YOLO, Faster R-CNN, DETR, SAM | day228–day230 |
| Phase 9 | Detection metrics: IoU, non-max suppression, mAP | day231–day232 |
| Phase 9 | Video tasks: object tracking, multi-object tracking, activity recognition, video anomaly detection | day233–day234 |
| Phase 9 | OCR: Tesseract, PaddleOCR, docTR, character error rate | day235–day236 |
| Phase 9 | Document models: LayoutLMv3, Donut | day237–day239 |
| Phase 9 | Multimodal: vision + LLM models and Vision AI agents | day240 |
| Phase 9 | Public datasets: RVL-CDIP, FUNSD, SROIE, Tobacco800 | day241 |
| Phase 9 | Big project: Document Intelligence API (Job 4). | day242–day246 |
| Phase 10 | When to choose fine-tuning over RAG | day247 |
| Phase 10 | LoRA and QLoRA with peft; SFT with trl | day248–day251 |
| Phase 10 | RLHF pipeline: SFT, then a reward model, then PPO | day252–day255 |
| Phase 10 | Preference methods: DPO (prompt / chosen / rejected format), RLAIF | day256–day257 |
| Phase 10 | Labeling tools: Label Studio | day258 |
| Phase 10 | Active learning: uncertainty, entropy and margin sampling | day259–day260 |
| Phase 10 | Label quality: Cohen's kappa, majority voting, gold questions, noisy labels | day261–day262 |
| Phase 10 | Big project: RLHF Labeling Platform (Job 2). | day263–day265 |
| Phase 11 | Model compression and quantization: GGUF, AWQ, 4-bit and 8-bit | day266–day267 |
| Phase 11 | Model serving: Ollama, vLLM, TGI | day268–day269 |
| Phase 11 | Speed-up tools: ONNX, TensorRT, OpenVINO | day270–day271 |
| Phase 11 | Batching and GPU memory | day272 |
| Phase 11 | Real-time and edge deployment on cameras and devices | day273–day274 |
| Phase 11 | On-prem and air-gapped packaging for regulated environments | day275 |
| Phase 11 | Mini project: run the Plant Assistant on a local model, and benchmark ONNX speed for the Document API. | day276–day277 |
| Phase 12 | Harness engineering: tools, retries, verification steps, sub-agents | day278–day281 |
| Phase 12 | Long-horizon tasks: context compression, saving state, crash recovery | day282–day284 |
| Phase 12 | Budget limits: steps, cost and time | day285 |
| Phase 12 | Failure control: loop detection, goal drift, reward hacking | day286 |
| Phase 12 | Audit trails and replayable traces | day287–day288 |
| Phase 12 | Sandboxed code execution | day289 |
| Phase 12 | Mechanistic interpretability: awareness level | day290 |
| Phase 12 | Big project: AutoML Agent (Job 3). | day291–day293 |
| Phase 13 | C/C++, CUDA and GPU programming | day294–day297 |
| Phase 13 | Real-time and embedded systems | day298 |
| Phase 13 | Sensors: multi-sensor fusion and sensor calibration | day299–day300 |
| Phase 13 | Control logic for physical machines | day301–day302 |
| Phase 13 | Other languages: Go, Java, Rust | day303 |
| Phase 13 | Linux infrastructure: virtualization, networking, storage | day304–day305 |
| Phase 13 | Infrastructure platforms: OpenStack, deeper Kubernetes | day306 |
| Phase 13 | Distributed systems and distributed ML; private cloud | day307–day310 |
| Phase 13 | Enterprise AI architecture: reference architectures, design reviews | day311–day312 |
| Phase 13 | Domain knowledge: BFSI, healthcare, GRC, SOC, retail/ad-tech, manufacturing | day313 |
| Phase 13 | Leadership: mentoring, technical strategy, customer workshops and presentations | day314 |
| Throughout all phases | DSA: LeetCode easy/medium, 3–4 problems a week | day315–day317 |
| Throughout all phases | System design: general backend first, then LLM system design | day318–day319 |
| Throughout all phases | Communication: English, demos, explaining trade-offs to non-technical people | day320 |
| Throughout all phases | Build in public: LinkedIn build logs for your projects | day321 |
| Throughout all phases | Open source: contributions to LangChain, LlamaIndex or Hugging Face | day322–day323 |
| Capstone & Final Evaluation | Capstone Build | day324–day327 |
| Capstone & Final Evaluation | Final Examinations | day328–day330 |

### Unmapped topics

None (all topics from ROADMAP_SOURCE.md are 100% mapped above).
