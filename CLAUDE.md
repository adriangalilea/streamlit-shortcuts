# streamlit-shortcuts Maintenance Guide

## Core Files
- @streamlit_shortcuts.py
- @pyproject.toml
- @README.md

## Issue/PR Workflow

### 1. Evaluate Request
- Check if it genuinely improves the package
- Reject bloat - this is meant to be simple

### 2. Implementation
- No hacks or patches - only clean solutions
- Test changes in @example/example.py or provided repro code

### 3. Release Process
- Update version in @pyproject.toml
- Commit with conventional commits (feat/fix/chore)
- Push to main - @.github/workflows/ci.yml handles:
  - Auto-tagging
  - PyPI publishing
  - GitHub release with changelog per @.github/cliff.toml

## Philosophy
- Simple > Feature-rich
- Clean code > Quick fixes
- User experience > Edge cases
- If it can't be done cleanly, close with explanation