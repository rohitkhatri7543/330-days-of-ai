# 330 Days of AI: Zero to Senior AI Engineer

> A 330-day, test-driven curriculum to master AI/ML Engineering from beginner to senior across 30 industry roles. Includes an interactive CLI harness (`today.py`), automated pytest suites, and zero-cost local stand-ins.

- **Cadence:** One new idea per day (~20 to 30 minutes).
- **Roadmap:** The complete schedule of days is in `ROADMAP.md`.
- **Source:** The original master syllabus is archived in `ROADMAP_SOURCE.md`.

---

## Setup (Once)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python today.py
```

---

## What you do each day

The daily order is strictly fixed:

1. **Learn:** Open `dayNN/lesson.md`. Read the lesson explanation and code walkthrough. The page asks you no questions.
2. **Confirm:** When you understand it, run:
   ```bash
   python today.py understood
   ```
   This command copies `questions.md`, `practice.py`, and `test_practice.py` into `dayNN/` without overwriting your changes, and sets the stage to `practice`.
3. **Practice:**
   - Answer `dayNN/questions.md` in chat with your mentor.
   - Implement your solution in `dayNN/practice.py`.
   - Run the automated tests:
     ```bash
     python today.py check
     ```

Check where you are anytime:
```bash
python today.py
```

---

## Phase Placement Rule (Fast-Tracking Known Topics)

If you already know a topic or want to test out of a phase:
1. Skip reading `lesson.md`.
2. Run `python today.py understood` to unlock the practice files.
3. Answer `questions.md` in chat and write `practice.py`.
4. Run `python today.py check`.
5. **Passing allows you to complete multiple days in one session!** The strict "one-new-lesson-per-day" limit applies only to lessons you actually read.
6. If the check fails or conceptual questions show gaps, fast-tracking stops, and the mentor teaches you the topic through the Hinglish lesson.

---

## Local Stand-in Policy

If a day's topic isn't Python or cannot run locally for free (such as SQL databases, Git commands, Docker images, Terraform configs, Databricks, Cloud services, or GPU training):
- `practice.py` tests a **Python stand-in** locally (e.g., SQLite for SQL, AST/config validators for Docker/Terraform, or CPU-sized toy weights for neural nets).
- `lesson.md` explains how the real production tool behaves and why it matters in engineering interviews.

---

## What a day folder holds

Day folders use at least two digits (`day01`, `day09`, `day10`, `day100`).

While you are learning:
```text
day01/
  lesson.md          # read this first
```

After you run `python today.py understood`:
```text
day01/
  lesson.md
  questions.md       # answer these in chat
  practice.py        # write your code here
  test_practice.py   # pytest suite (do not edit)
  __init__.py
```

`program/dayNN/` holds the challenge files safely until you confirm the lesson.

---

## What this course does not replace

Toy data and stand-ins live in this repository. This course does not replace real production traffic, paid enterprise cloud accounts, or years of shipping production systems.

---

## Extras

Extras happen in chat or in the `extras/` folder. They never edit `progress.json`, never add commands to `today.py`, and never block the next day:

- **Placement:** Skip reading known lessons, run `python today.py understood`, and take the check directly.
- **Revision:** After passing `python today.py check`, the mentor asks 3 short Hinglish review questions on earlier days (ungraded).
- **Mock interview:** On Day 7 of each week (and after final tests), the mentor conducts a 10-minute mock interview in chat on everything taught so far.
- **DSA:** Once a week after the Day 7 check, a coding challenge is generated under `extras/dsaNN/`. Run it with `python -m pytest extras/dsaNN`.
>>>>>>> bc186b6 (feat: initial commit of 330-day interactive AI engineer training platform)
