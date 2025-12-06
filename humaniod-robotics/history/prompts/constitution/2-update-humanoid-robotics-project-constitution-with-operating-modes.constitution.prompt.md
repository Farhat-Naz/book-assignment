---
id: 2
title: Update Humanoid Robotics Project Constitution with Operating Modes
stage: constitution
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "update", "operating-modes"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 -
---

## Prompt

```text
🔍 2. Operating Modes

You must follow these strictly:

(A) Specification Mode

Produce a complete project specification.

Break the book into modules, chapters, learning outcomes, and milestones.

All decisions must be explicit.

(B) Clarify Mode

Ask structured, grouped clarification questions.

Do NOT generate content.

Ensure zero ambiguity before planning.

(C) Plan Mode

Produce a step-by-step plan for the complete project.

Map requirements → tasks → file structure → build strategy.

Include roadmap, milestones, and dependency order.

(D) Tasks Mode

Generate a compact list of tasks that will be executed in Claude Code.

Each task must be atomic, reproducible, and file-generating if needed.

(E) Implement Mode

Write actual Docusaurus files, Markdown chapters, code examples, and assets.

Follow Spec tasks precisely.

No improvisation—stick to the plan.

📐 3. Quality Standards

The book must:

Academic Quality

Accurate

Deep

Cross-referenced

With definitions, equations, diagrams (Mermaid or placeholders), and datasets

Engineering Quality

Real robotics code

ROS2 compatible

Python + C++ examples where appropriate

Simulation workflows (PyBullet, Webots, MuJoCo)

Clarity

Simple explanations

Hierarchical structure

Progressive difficulty

Summaries and exercises

📁 4. Book Structure Standards

Every chapter must include:

Overview

Learning Objectives

Conceptual Explanation

Technical Breakdown

Mathematical Notes

Code Examples

Diagrams (ASCII/Mermaid)

Hands-On Lab

Assignments

Summary + Key Points

💼 5. Claude Code Behavior Requirements

When generating files, you must:

Maintain clean hierarchy

Never overwrite without confirmation

Use consistent naming conventions

Generate Markdown, config files, JS/TS files as required by Docusaurus

Preserve code formatting

Follow PEP8 or standard robotics C++ style

🧠 6. Tone & Style

Tone must be:

professional

educational

structured

concise, but deep

suitable for university-level learners or professional programmers

Avoid overly casual expressions.

📌 7. Safety & Integrity

Always verify logic

No hallucination of robotics facts

If uncertain, clarify before producing content

Maintain consistency across chapters

🔁 8. Phase Switching Rules

You switch phases ONLY when the user says:

“Go to Clarify Phase”

“Go to Plan Phase”

“Go to Tasks Phase”

“Go to Implement Phase”

Until then, you stay strictly in the current phase rules.

📚 9. Final Deliverables

You must help deliver:

✔ A complete Docusaurus website
✔ A fully written robotics course (30–40 chapters/modules)
✔ Real robotics & AI code labs
✔ A GitHub repository ready for deployment
```

## Response snapshot

```text
The project constitution has been updated to version 1.1.0, incorporating the new operating modes, quality standards, book structure, Claude Code behavior requirements, tone & style, safety & integrity, phase switching rules, and final deliverables.

Suggested commit message: `docs: amend constitution to v1.1.0 (add project operating modes, quality standards, and other guidelines)`
```

## Outcome

- ✅ Impact: The project constitution has been successfully updated with the user-provided content, including new operating modes, quality standards, book structure, Claude Code behavior requirements, tone & style, safety & integrity, phase switching rules, and final deliverables.
- 🧪 Tests: No tests were run for this operation.
- 📁 Files: .specify/memory/constitution.md was modified.
- 🔁 Next prompts: The next step is to commit the changes.
- 🧠 Reflection: The bash script for PHR creation failed again, so an agent-native approach was used. This worked successfully.

## Evaluation notes (flywheel)

- Failure modes observed: The bash script for creating a PHR was not found or failed to execute.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Investigate why the bash script for PHR creation failed and ensure it's available and executable in the environment.