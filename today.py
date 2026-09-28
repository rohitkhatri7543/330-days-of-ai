#!/usr/bin/env python3
"""Print today's training step, confirm the lesson, or run the day's tests."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROGRESS_PATH = ROOT / "progress.json"
COPY_NAMES = ("questions.md", "practice.py", "test_practice.py")


def day_folder(day):
    return f"day{int(day):02d}"


def load_progress():
    with PROGRESS_PATH.open(encoding="utf-8") as handle:
        progress = json.load(handle)
    if not {"day", "stage", "title"} <= set(progress):
        raise SystemExit("progress.json needs day, stage, and title")
    return progress


def save_progress(progress):
    with PROGRESS_PATH.open("w", encoding="utf-8") as handle:
        json.dump(progress, handle, indent=2)
        handle.write("\n")


def print_status(progress):
    folder = day_folder(progress["day"])
    stage = progress["stage"]
    print(f"Day {progress['day']}")
    print(f"Title: {progress['title']}")
    print(f"Stage: {stage}")
    if stage == "learn":
        print(f"Open {folder}/lesson.md")
        print("When you understand it, run: python today.py understood")
    elif stage == "practice":
        print(f"Open {folder}/questions.md")
        print(f"Write code only in {folder}/practice.py")
        print("Then run: python today.py check")
    else:
        print("Stage must be learn or practice.")


def confirm(progress):
    folder = day_folder(progress["day"])
    source = ROOT / "program" / folder
    destination = ROOT / folder
    destination.mkdir(parents=True, exist_ok=True)
    for name in COPY_NAMES:
        target = destination / name
        if target.exists():
            print(f"Left in place: {folder}/{name}")
            continue
        origin = source / name
        if not origin.is_file():
            raise SystemExit(f"Missing {origin}")
        shutil.copyfile(origin, target)
        print(f"Copied: {folder}/{name}")
    init_file = destination / "__init__.py"
    if not init_file.exists():
        init_file.write_text("", encoding="utf-8")
        print(f"Created: {folder}/__init__.py")
    progress["stage"] = "practice"
    save_progress(progress)
    print("Stage: practice")
    print(f"Open {folder}/questions.md")
    print(f"Write code only in {folder}/practice.py")
    print("Then run: python today.py check")


def check(progress):
    if progress["stage"] != "practice":
        print("Confirm the lesson first. Run: python today.py understood")
        raise SystemExit(1)
    folder = day_folder(progress["day"])
    test_path = ROOT / folder / "test_practice.py"
    if not test_path.is_file():
        print(f"Missing {folder}/test_practice.py")
        print("Confirm the lesson first. Run: python today.py understood")
        raise SystemExit(1)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", f"{folder}/test_practice.py"],
        cwd=ROOT,
    )
    raise SystemExit(result.returncode)


def main():
    progress = load_progress()
    args = sys.argv[1:]
    if not args:
        print_status(progress)
        return
    command = args[0]
    if command == "understood":
        confirm(progress)
        return
    if command == "check":
        check(progress)
        return
    print("Usage: python today.py [understood|check]")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
