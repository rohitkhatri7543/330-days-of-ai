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
        prefix = item.split(":")[0]
        if prefix not in roadmap_text:
            print(f"FAIL: Throughout item missing: {item}")
            return 1

    # Count days in the table
    days = re.findall(r"\|\s*(day\d+)\s*\|", roadmap_text)
    unique_days = sorted(set(days), key=lambda d: int(d.replace("day", "")))
    day_count = len(unique_days)
    print(f"Found {day_count} unique days in ROADMAP.md")
    if not (310 <= day_count <= 345):
        print(f"FAIL: Day count {day_count} outside target 315-330 days")
        return 1

    print("SUCCESS: ROADMAP coverage and day count verified!")
    return 0

if __name__ == "__main__":
    sys.exit(verify())
