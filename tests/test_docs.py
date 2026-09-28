# tests/test_docs.py
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_readme_contains_placement_and_extras():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "## What you do each day" in readme
    assert "## Phase Placement Rule" in readme
    assert "## Local Stand-in Policy" in readme
    assert "## Extras" in readme
    assert "Revision" in readme
    assert "Mock interview" in readme
    assert "DSA" in readme

def test_glossary_contains_day1_terms():
    glossary = (ROOT / "GLOSSARY.md").read_text(encoding="utf-8")
    assert "## Variable" in glossary
    assert "## Value" in glossary
    assert "## Assignment" in glossary
