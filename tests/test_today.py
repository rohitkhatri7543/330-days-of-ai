# tests/test_today.py
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_today_learn_stage():
    res = subprocess.run([sys.executable, str(ROOT / "today.py")], capture_output=True, text=True, cwd=ROOT)
    assert res.returncode == 0
    assert "Day 1" in res.stdout
    assert "Stage: learn" in res.stdout
    assert "Open day01/lesson.md" in res.stdout

def test_today_check_fails_on_learn_stage():
    res = subprocess.run([sys.executable, str(ROOT / "today.py"), "check"], capture_output=True, text=True, cwd=ROOT)
    assert res.returncode != 0
    assert "Confirm the lesson first" in res.stdout or "Confirm the lesson first" in res.stderr
