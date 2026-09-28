# 315–330 Day AI/ML Engineer Training Workspace Specification

- **Date:** 2026-09-27
- **Target:** AI/ML Engineer (beginner to senior) — teach in the simplest words that still do the real work
- **Curriculum Duration:** ~315–330 Days (~45–47 Weeks)

---

## 1. Overview & Objectives

This workspace trains an engineer from fundamentals to senior level across 30 AI/ML/Data roles (covering classical ML, backend pipelines, production RAG, multi-agent systems, evals/guardrails, CV/document AI, fine-tuning/RLHF, inference optimization, and systems engineering).

The training system follows a deterministic, hands-on, test-driven daily cadence orchestrated by `today.py` and structured in `ROADMAP.md`.

---

## 2. Core Constraints & User Requirements

1. **Target Duration:** **~315–330 days** (~45–47 weeks).
   - Every phase has enough learning days for all topics from `ROADMAP_SOURCE.md` plus dedicated project days.
   - Phase 1 includes project build days (FastAPI + PostgreSQL + tests + Bootstrap + Docker).
   - Phase 3 includes at least 1 additional learning day plus structured-output UI build days.
   - Phase 6 includes project days for the *Plant Assistant (Job 1)*.
   - Phase 7 includes milestone project days for *live CI/CD deployment*.
   - Split a topic only when it truly contains 2+ distinct ideas.
   - Awareness topics receive exactly 1 dedicated day.
   - Day 7 of every full week is a consolidation check (no new idea).
   - Concludes with an end-to-end capstone build, theory test, and practical test.
2. **Exhaustive Coverage Verification Table:**
   - At the end of `ROADMAP.md`, include a complete **Coverage Table** mapping every single topic from `ROADMAP_SOURCE.md` directly to its corresponding day number, including all phase topics, mini/big projects, and all five "Throughout all phases" items (DSA, System design, Communication, Build in public, Open source).
   - Explicitly list any topic without a day: **this list must be strictly empty (0 unmapped topics)**.
3. **Phase Placement Rule (Fast-Tracking Known Topics):**
   - The learner can test out of multiple days in a single session.
   - The strict "one-new-lesson-per-day" gate applies **only to lessons the user actually reads**.
   - A placement pass requires:
     1. Answering `questions.md` in chat to prove conceptual understanding and failure-mode awareness.
     2. Passing `python today.py check` to verify functional code.
     3. Upon passing both, the learner advances immediately to the next day in that same session.
   - If the check fails or questions reveal gaps, fast-tracking halts; the mentor teaches the topic via the Hinglish lesson.
4. **Mandatory Day Creation Test Gate (Stub vs. Solution Verification):**
   - Every time a new day folder/challenge is created (during normal progression or placement):
     1. Verify the stub raises `NotImplementedError` and fails `pytest`.
     2. Verify a correct reference solution passes all `pytest` checks.
     3. Restore the stub before presenting the day to the learner.
5. **Multi-Domain Scenarios:**
   - **Primary Baseline Scenario:** *Northline Plant* (industrial pumps, telemetry, predictive maintenance, growing into the Plant Assistant).
   - **Domain-Specific Scenarios (aligned to target jobs):**
     - **Banking & FinOps (BFSI):** Transaction auditing, credit/fraud risk, audit-log tables, compliance (*Wells Fargo, Axis Bank*).
     - **Healthcare & Clinical IoT:** Patient vital telemetry, health risk scoring, false-alarm reduction (*Medico, Optum, health tech roles*).
     - **Retail & E-commerce:** Dynamic pricing, churn prediction, recommendation systems, price elasticity (*Target, Criteo*).
     - **Document AI & LegalTech:** Invoice parsing, contract analysis, OCR, entity extraction, LayoutLM (*Leegality, Document Intelligence API*).

---

## 3. Curriculum Architecture (~315–330 Days / ~45–47 Weeks)

| Phase | Est. Days | Project / Milestone Days Included | Core Domain Scenario | High-Level Focus & Target Roles |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 0: Foundations** | ~21 days | Mini-project: API script to database | Northline Plant Telemetry | Python OOP, Linux, Bash, Git, SQL basics, HTTP/REST. |
| **Phase 1: Backend Engineering** | ~24 days | Mini-project: FastAPI + Postgres + Docker | Banking & Industrial API | FastAPI, Pydantic, TDD, PostgreSQL, Redis, Docker, microservices (*Tachyon, Ingersoll Rand*). |
| **Phase 2: Data, Math & Classical ML** | ~37 days | Mini-project: Churn, Anomaly & Elasticity in MLflow | Healthcare Telemetry & Retail | EDA, Scikit-learn, XGBoost/LightGBM, SHAP, Time-series, Churn & Elasticity (*Medico, Target, Trailytics*). |
| **Phase 3: LLMs & Prompt Engineering** | ~17 days | Mini-project: Structured JSON AI tool + Bootstrap UI | Plant Assistant Support Desk | Tokenomics, Prompt patterns, Structured JSON output, Function calling (*KeyValue, Accenture*). |
| **Phase 4: Production RAG** | ~23 days | Mini-project: RAG app with citations & abstention | Banking SOPs & Plant Manuals | Chunking, pgvector/Chroma/FAISS, Hybrid search, Reranking, Citations & Abstention (*Wells Fargo, Altraize*). |
| **Phase 5: Agents, MCP & Automation** | ~23 days | Mini-project: MCP server + LangGraph agent | Enterprise Operations (Salesforce/SAP) | LangGraph, Tool loops, Memory (Mem0), Model Context Protocol (MCP) (*XenonStack, Optum*). |
| **Phase 6: Evals, Guardrails & Security** | ~25 days | Big Project: Plant Assistant (Job 1) | Healthcare & BFSI Compliance | Golden datasets, RAGAS, LLM-as-judge, Guardrails, PII masking, Langfuse tracing (*IndustryOS, Whatfix*). |
| **Phase 7: Cloud, DevOps & Data Platforms** | ~25 days | Milestone: Deploy Plant Assistant live with CI/CD | Live Plant Assistant Operations | AWS/Azure, CI/CD, Terraform, Databricks/Spark, MLOps registry (*DataEconomy, Konovo*). |
| **Phase 8: Deep Learning Fundamentals** | ~23 days | Mini-project: BERT text & ResNet image classifiers | Sensor Signals & Vision Prep | PyTorch, Backpropagation, CNNs (ResNet), Transformers (BERT), Hugging Face. |
| **Phase 9: NLP, CV & Document AI** | ~30 days | Big Project: Document Intelligence API (Job 4) | Legal Contracts & Document Intelligence | OpenCV, YOLO, OCR (docTR/PaddleOCR), LayoutLMv3, Multimodal AI (*Leegality, Accenture CV*). |
| **Phase 10: Fine-Tuning & RLHF** | ~23 days | Big Project: RLHF Labeling Platform (Job 2) | RLHF Annotation Platform | LoRA, QLoRA (`peft`), SFT (`trl`), DPO, Active learning (*CoreLabel.AI, Cardboard*). |
| **Phase 11: Inference Optimization** | ~16 days | Mini-project: Local plant assistant + ONNX benchmark | Edge Cameras & Low-Latency Serving | Quantization (GGUF/AWQ), vLLM, ONNX, TensorRT, local runtimes (*NAYAN, Edge deployments*). |
| **Phase 12: Advanced Agent Engineering** | ~23 days | Big Project: AutoML Agent (Job 3) | AutoML Research Agent | Sub-agents, Sandboxed execution, Crash recovery, Loop detection, Budget guards (*Lexsi Labs*). |
| **Phase 13: Specialist & Senior Topics** | ~23 days | Architecture reviews & Distributed ML | High-Scale Infrastructure | C/C++/CUDA stand-ins, Distributed ML, Multi-sensor fusion, Architecture reviews (*Senior Architect roles*). |
| **Throughout, Capstone & Final Tests** | ~16 days | Final End-to-End Build + Theory Test + Practical Test | Enterprise Multi-Modal Assistant | System design, DSA, Capstone pipeline, final examinations. |

---

## 4. Daily Learning, Placement & Extras Workflow

### A. The Standard Daily Cadence (When Reading Lessons)
1. **Learn:** Open `dayNN/lesson.md`. Read the Hinglish narrative and line-by-line code explanation.
2. **Confirm:** Run `python today.py understood`. This copies `questions.md`, `practice.py`, and `test_practice.py` from `program/dayNN/` into `dayNN/`, and unlocks the `practice` stage.
3. **Practice:**
   - Answer `questions.md` in chat (testing conceptual trade-offs and failure modes).
   - Implement the solution in `dayNN/practice.py`.
   - Run `python today.py check` (executes `pytest dayNN/test_practice.py`).
4. **Advance:** Upon passing the check, stop. Next lesson waits for tomorrow.

### B. The Phase Placement Rule (Testing Out of Known Days)
* At the beginning of a Phase, or anytime the learner states they know the concept:
  1. The learner skips reading `lesson.md`.
  2. Runs `python today.py understood` to spawn the day's challenge.
  3. Answers `questions.md` in chat and runs `python today.py check`.
  4. **Placement Pass:** If tests pass and conceptual questions are correct, the day is marked complete. The learner **may immediately proceed to the next day in that same session**.
  5. **Placement Fail:** If the check fails or questions reveal gaps, the fast-track halts. The mentor steps in, activates the full Hinglish lesson, and walks through the concept.

### C. Extras (Exactly as Written in PROMPT.md)
These extras happen in chat or in a separate `extras/` folder. They never edit `progress.json`, never add commands to `today.py`, never open a new day, and never quiz the learner before confirming a lesson:
- **Placement:** If the learner knows a day's idea, they can skip reading the lesson, run `python today.py understood`, and take the normal `check`. Passing counts as passing that day.
- **Revision:** After passing a day's `check`, chat asks 3 short Hinglish questions from earlier days. They are not graded and never block the next day.
- **Mock Interview:** After passing each week's day-7 check, and again after the final tests, chat runs a 10-minute mock interview in chat on everything taught so far. Feedback is given in Hinglish. It never blocks the next day.
- **DSA:** Once a week, after the day-7 check, create `extras/dsaNN/` with `problem.md`, a `solution.py` stub that raises `NotImplementedError`, and `test_solution.py`. Add empty `__init__.py` files in `extras/` and `extras/dsaNN/`, and import the stub as `from extras.dsaNN.solution import ...`. Before giving it to the learner, confirm the stub fails and a correct solution passes, then restore the stub. Run with `python -m pytest extras/dsaNN`.

---

## 5. File System & Tooling Specifications

| Path | Purpose | Behavior |
| :--- | :--- | :--- |
| `ROADMAP_SOURCE.md` | Archival Source | Unaltered backup of the original 258-line master roadmap. |
| `ROADMAP.md` | Active 315–330 Day Plan | Table with columns `Day`, `Week`, `Kind`, `Phase`, `Idea`, `Note`. Strict 1 idea/day, Day 7 week checks, mini/big projects, and final Coverage Table mapping every source topic. |
| `today.py` | State Machine CLI | Supports `python today.py`, `python today.py understood`, and `python today.py check`. Uses `f"day{day:02d}"`. |
| `progress.json` | Progress State | Stores `day`, `stage` (`learn` or `practice`), and `title`. |
| `README.md` | Workspace Guide | Full instructions, setup commands, placement workflow, local stand-in policy, and extras. |
| `GLOSSARY.md` | Incremental Dictionary | Words taught so far in Hinglish. |
| `requirements.txt` | Dependencies | Starts minimal with `pytest`. |
| `.gitignore` | Cache Exclusions | Ignores `.venv/`, `__pycache__/`, `.pytest_cache/`, `*.pyc`. |
| `day01/lesson.md` | Day 1 Lesson | Hinglish narrative on Variables & stale telemetry failure modes in standard English. |
| `program/day01/` | Day 1 Challenge Pack | `questions.md`, `practice.py` (stub with `NotImplementedError`), and `test_practice.py` (pytest suite). |

---

## 6. Pedagogical & Technical Standards

* **Target Audience:** AI/ML Engineer (beginner to senior). Explanations stay simple, intuitive, and grounded in concrete reality, avoiding dry academic jargon.
* **Language Policy:**
  - Explanations, analogies, and questions in natural, conversational **Hinglish** (e.g., *"Jab sensor naya reading bhejta hai aur variable update nahi hota..."*).
  - All technical terms, code identifiers, variables, functions, and commands strictly in standard **English** (e.g., `Feature`, `Label`, `XGBoost`, `temperature_celsius`, `pytest`).
* **Local Stand-In Policy:**
  - Non-Python tools (SQL, Docker, Terraform, Spark, CUDA, Cloud platforms) test Python stand-ins locally (e.g., SQLite for SQL, AST/regex validator for Dockerfiles/Terraform configs, tiny PyTorch CPU tensors for CUDA).
* **Test Isolation:**
  - The worked example in `lesson.md` and the challenge in `practice.py` must use different inputs/formats so that copy-pasting from the lesson fails the tests.
  - Tests import via `from dayNN.practice import ...`.
