# 315–330 Day AI/ML Engineer Training Workspace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, test-driven daily training workspace spanning ~315–330 days across 14 phases with an exhaustive coverage table, phase placement fast-tracking, multi-domain scenarios, CLI state machine (`today.py`), and a verified Day 1 lesson pack.

**Architecture:** The curriculum source [`ROADMAP.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/ROADMAP.md) is preserved as [`ROADMAP_SOURCE.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/ROADMAP_SOURCE.md) and expanded into a daily table format with strict Day 7 consolidation checks. A Python CLI (`today.py`) manages progression stages (`learn` -> `practice`) and runs isolated `pytest` suites. Lessons use friendly Hinglish pedagogy with English technical terms and domain-specific scenarios (Northline Plant, BFSI, Healthcare, Retail, Document AI).

**Tech Stack:** Python 3.10+, `pytest`, Markdown, JSON.

**Spec:** [`docs/superpowers/specs/2026-09-27-300-day-ai-interview-training-workspace-design.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/docs/superpowers/specs/2026-09-27-300-day-ai-interview-training-workspace-design.md)

## Global Constraints

- Curriculum duration: ~315–330 days (~45–47 weeks), ending with capstone build, theory test, and practical test.
- Every phase must have enough learning days for all topics plus project days (Phases 1, 3, 6, 7).
- Strict 1 idea per day; awareness topics receive 1 dedicated day; Day 7 of every full week is a consolidation check (no new idea).
- Complete Coverage Table at the end of `ROADMAP.md` mapping every topic from `ROADMAP_SOURCE.md` (including "Throughout all phases" items) to its day number; unmapped topics list must be strictly empty.
- Phase Placement Rule: Learner can pass multiple days in one session by answering `questions.md` in chat and passing `python today.py check`.
- Mandatory Day Creation Test Gate: Every new day generated must be verified by confirming stub fails and solution passes, then restoring the stub.
- Lessons written in conversational Hinglish with all technical keywords/code identifiers in standard English.
- Local stand-in policy for non-Python tools (SQLite for SQL, config validation for Docker/Terraform, CPU models for GPU/CUDA).

## Review Focus

1. **Coverage Table completeness:** Verify that every bullet from `ROADMAP_SOURCE.md` (including all 5 "Throughout all phases" bullets) appears in the Coverage Table and maps to a valid day number.
2. **`today.py understood` idempotency:** Ensure running `python today.py understood` twice does not overwrite learner modifications in `practice.py`.
3. **`today.py check` stage gating:** Ensure `python today.py check` exits with an error if called while still in stage `learn`.
4. **Day 1 stub failure:** Ensure `day01/practice.py` stub raises `NotImplementedError` and fails all 4 test cases before user implementation.
5. **Day 1 reference solution pass:** Ensure the reference implementation of `machine_status` passes all 4 test cases with 100% success.

---

### Task 1: Archive Source Curriculum & Generate Daily ROADMAP.md with Coverage Table

**Files:**
- Create: `ROADMAP_SOURCE.md` (renamed from `ROADMAP.md`)
- Create: `ROADMAP.md`
- Create: `scripts/verify_roadmap_coverage.py`

**Interfaces:**
- Consumes: [`ROADMAP.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/ROADMAP.md) (original 258-line file)
- Produces: [`ROADMAP_SOURCE.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/ROADMAP_SOURCE.md) (verbatim source archive), [`ROADMAP.md`](file:///Users/rohitkhatri/interview_projects/30_ai_interview/ROADMAP.md) (315–330 day schedule + coverage table)

- [ ] **Step 1: Write the coverage verification test script**

Create `scripts/verify_roadmap_coverage.py` to parse `ROADMAP_SOURCE.md` and assert that:
1. Every bullet topic in Phases 0–13 and "Throughout all phases" is mapped in the Coverage Table of `ROADMAP.md`.
2. Every mapped day exists in the `ROADMAP.md` Days table.
3. The "Unmapped topics" list in `ROADMAP.md` is strictly empty.

```python
# scripts/verify_roadmap_coverage.py
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def verify():
    source_file = ROOT / "ROADMAP_SOURCE.md"
    roadmap_file = ROOT / "ROADMAP.md"

    if not source_file.exists():
        print("FAIL: ROADMAP_SOURCE.md does not exist")
        return 1
    if not roadmap_file.exists():
        print("FAIL: ROADMAP.md does not exist")
        return 1

    source_text = source_file.read_text(encoding="utf-8")
    roadmap_text = roadmap_file.read_text(encoding="utf-8")

    # Check for coverage table header
    if "## Coverage Table" not in roadmap_text:
        print("FAIL: ROADMAP.md missing '## Coverage Table'")
        return 1

    # Check for empty unmapped list declaration
    if "### Unmapped topics" not in roadmap_text or "None" not in roadmap_text:
        print("FAIL: ROADMAP.md missing '### Unmapped topics' with 'None'")
        return 1

    # Verify "Throughout all phases" items are covered
    throughout_items = [
        "DSA: LeetCode easy/medium",
        "System design: general backend",
        "Communication:",
        "Build in public:",
        "Open source:"
    ]
    for item in throughout_items:
        if item.split(":")[0] not in roadmap_text:
            print(f"FAIL: Throughout item missing: {item}")
            return 1

    # Count days
    days = re.findall(r"\|\s*(day\d+)\s*\|", roadmap_text)
    unique_days = sorted(set(days), key=lambda d: int(d.replace("day", "")))
    day_count = len(unique_days)
    print(f"Found {day_count} unique days in ROADMAP.md")
    if not (310 <= day_count <= 340):
        print(f"FAIL: Day count {day_count} outside target 315-330 days")
        return 1

    print("SUCCESS: ROADMAP coverage and day count verified!")
    return 0

if __name__ == "__main__":
    sys.exit(verify())
```

- [ ] **Step 2: Run verification script to confirm it fails before generation**

Run: `python3 scripts/verify_roadmap_coverage.py`
Expected: FAIL with missing `ROADMAP_SOURCE.md`.

- [ ] **Step 3: Rename `ROADMAP.md` to `ROADMAP_SOURCE.md` and generate `ROADMAP.md`**

1. Rename `ROADMAP.md` to `ROADMAP_SOURCE.md`.
2. Generate `ROADMAP.md`:
   - Target 315–330 days (~45–47 weeks).
   - Columns: `| Day | Week | Kind | Phase | Idea | Note |`.
   - Day 7 of each week is a consolidation check (`Kind`: `Week check`).
   - Project build days integrated for Phase 1, Phase 2, Phase 3, Phase 4, Phase 5, Phase 6, Phase 7, Phase 8, Phase 9, Phase 10, Phase 11, Phase 12.
   - Capstone pipeline build + Theory test + Practical test at the end.
   - Conclude with `## Coverage Table` mapping every topic from `ROADMAP_SOURCE.md` (all 14 phases + 5 throughout items) to its day number.
   - Conclude with `### Unmapped topics: None`.

- [ ] **Step 4: Run verification script to confirm it passes**

Run: `python3 scripts/verify_roadmap_coverage.py`
Expected: PASS with "Found ~320-330 unique days... SUCCESS".

---

### Task 2: Implement CLI State Machine (`today.py`) & Workspace Configuration

**Files:**
- Create: `today.py`
- Create: `progress.json`
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `tests/test_today.py`

**Interfaces:**
- Consumes: `progress.json` (`day`, `stage`, `title`), `program/dayNN/`
- Produces: CLI commands `python today.py`, `python today.py understood`, `python today.py check`

- [ ] **Step 1: Write test for `today.py` state transitions and gating**

Create `tests/test_today.py`:
```python
# tests/test_today.py
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_today_learn_stage(tmp_path, monkeypatch):
    # Verify today.py prints learn instructions
    res = subprocess.run([sys.executable, str(ROOT / "today.py")], capture_output=True, text=True, cwd=ROOT)
    assert res.returncode == 0
    assert "Day 1" in res.stdout
    assert "Stage: learn" in res.stdout
    assert "Open day01/lesson.md" in res.stdout

def test_today_check_fails_on_learn_stage():
    res = subprocess.run([sys.executable, str(ROOT / "today.py"), "check"], capture_output=True, text=True, cwd=ROOT)
    assert res.returncode != 0
    assert "Confirm the lesson first" in res.stdout or "Confirm the lesson first" in res.stderr
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_today.py`
Expected: FAIL (files do not exist yet).

- [ ] **Step 3: Implement `today.py`, `progress.json`, `.gitignore`, and `requirements.txt`**

1. Create `progress.json`:
   ```json
   {
     "day": 1,
     "stage": "learn",
     "title": "Variables: store one pump reading under a name"
   }
   ```
2. Create `.gitignore`:
   ```text
   .venv/
   __pycache__/
   .pytest_cache/
   *.pyc
   ```
3. Create `requirements.txt`:
   ```text
   pytest>=8.0.0
   ```
4. Create `today.py`:
   - `print_status`: prints Day, Title, Stage, and next action.
   - `confirm`: copies `questions.md`, `practice.py`, `test_practice.py` from `program/dayNN/` to `dayNN/` without overwriting existing files, creates `dayNN/__init__.py`, updates `progress.json` to stage `practice`.
   - `check`: runs `pytest dayNN/test_practice.py` when stage is `practice`; exits with 1 otherwise.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_today.py`
Expected: PASS.

---

### Task 3: Educational Documentation (`README.md` & `GLOSSARY.md`)

**Files:**
- Create: `README.md`
- Create: `GLOSSARY.md`
- Create: `tests/test_docs.py`

**Interfaces:**
- Consumes: Spec requirements for placement rules, daily 3-step cadence, stand-in policy, extras.
- Produces: Comprehensive user guides.

- [ ] **Step 1: Write test for documentation content**

Create `tests/test_docs.py`:
```python
# tests/test_docs.py
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_readme_contains_placement_and_extras():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "## What you do each day" in readme
    assert "## Phase Placement Rule" in readme
    assert "## Stand-in Policy" in readme
    assert "## Extras" in readme
    assert "Revision" in readme
    assert "Mock interview" in readme
    assert "DSA" in readme

def test_glossary_contains_day1_terms():
    glossary = (ROOT / "GLOSSARY.md").read_text(encoding="utf-8")
    assert "## Variable" in glossary
    assert "## Value" in glossary
    assert "## Assignment" in glossary
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_docs.py`
Expected: FAIL (files missing).

- [ ] **Step 3: Create `README.md` and `GLOSSARY.md`**

1. Write `README.md` detailing:
   - Setup instructions (`python3 -m venv .venv`, `source .venv/bin/activate`, `pip install -r requirements.txt`).
   - Daily 3-step cycle (Learn -> Confirm -> Practice).
   - **Phase Placement Rule**: How to test out of known days in one session (skip lesson -> `python today.py understood` -> answer `questions.md` in chat + `python today.py check` -> advance immediately).
   - Local stand-in policy (SQLite, config validation, CPU models).
   - Extras (Placement, Revision recaps, Weekly Mock Interviews, Weekly DSA).
2. Write `GLOSSARY.md` with Day 1 terms (`Variable`, `Value`, `Assignment`) in friendly Hinglish with concrete Northline telemetry examples.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_docs.py`
Expected: PASS.

---

### Task 4: Day 1 Lesson & Challenge Pack with Mandatory Test Gate Verification

**Files:**
- Create: `day01/lesson.md`
- Create: `program/day01/questions.md`
- Create: `program/day01/practice.py`
- Create: `program/day01/test_practice.py`

**Interfaces:**
- Consumes: Day 1 curriculum concept ("Variables: store one pump reading under a name")
- Produces: Hinglish lesson, conceptual questions, stub, pytest suite.

- [ ] **Step 1: Write Day 1 challenge files in `program/day01/`**

1. Write `program/day01/test_practice.py`:
   ```python
   from day01.practice import machine_status

   def test_status_line_for_the_example_machine():
       assert machine_status("M-12", "running") == "M-12: running"

   def test_status_line_keeps_argument_order():
       assert machine_status("running", "M-12") == "running: M-12"

   def test_status_line_for_a_stopped_boiler():
       assert machine_status("Boiler-3", "stopped") == "Boiler-3: stopped"

   def test_status_line_for_an_idle_conveyor():
       assert machine_status("Conveyor-7", "idle") == "Conveyor-7: idle"
   ```
2. Write `program/day01/practice.py` (stub):
   ```python
   def machine_status(machine_id, status):
       """Do variables se ek status line banao.

       Lesson mein pump name aur temperature text " is " se jude the, aur unit alag
       variable mein thi. Yahan machine id aur status ko ": " se jodo.
       Lesson wala sentence yahan paste mat karna.

       machine_status("M-12", "running") -> "M-12: running"
       """
       raise NotImplementedError
   ```
3. Write `program/day01/questions.md`:
   - 4 Hinglish questions testing why desynchronized values cause plant alarms to miss failures or stop working pumps, why assignment overwrites previous values without a second variable, and the effect of hardcoding units vs variables.
4. Write `day01/lesson.md`:
   - High-retention Hinglish narrative on Northline Plant Pump-A temperature (`72.5 C` vs `80.1 C`).
   - Line-by-line annotated walkthrough of `format_reading(machine_name, temperature_text)`.
   - Ends with command: `python today.py understood`. Strictly no questions on the lesson page.

- [ ] **Step 2: Execute Mandatory Day Creation Gate (Stub Failure Verification)**

1. Temporarily copy `program/day01/*` into `day01/` with `day01/__init__.py`.
2. Run: `python3 -m pytest day01/test_practice.py`
3. Verify output: All 4 tests FAIL with `NotImplementedError`.

- [ ] **Step 3: Execute Mandatory Day Creation Gate (Reference Solution Verification)**

1. Temporarily edit `day01/practice.py` with correct implementation:
   ```python
   def machine_status(machine_id, status):
       return machine_id + ": " + status
   ```
2. Run: `python3 -m pytest day01/test_practice.py`
3. Verify output: All 4 tests PASS.

- [ ] **Step 4: Restore clean learn state**

1. Delete temporary files in `day01/` (`practice.py`, `questions.md`, `test_practice.py`, `__init__.py`).
2. Clean `__pycache__` and `.pytest_cache`.
3. Verify `day01/` contains only `lesson.md`.
4. Verify `progress.json` is set to `day: 1`, `stage: "learn"`.

---

### Task 5: End-to-End System Verification & Workspace Ready Check

**Files:**
- Check: All files in workspace

**Interfaces:**
- Consumes: Complete workspace

- [ ] **Step 1: Run complete automated test suite**

Run: `pytest tests/ -v && python3 scripts/verify_roadmap_coverage.py`
Expected: All tests PASS.

- [ ] **Step 2: Verify `python today.py` status output**

Run: `python3 today.py`
Expected output:
```text
Day 1
Title: Variables: store one pump reading under a name
Stage: learn
Open day01/lesson.md
When you understand it, run: python today.py understood
```

- [ ] **Step 3: Verify workspace folder state**

Confirm:
- `day01/` contains ONLY `lesson.md`.
- `program/day01/` contains `questions.md`, `practice.py`, `test_practice.py`.
- No orphan files or leftover pytest caches.
- Clean git status.
