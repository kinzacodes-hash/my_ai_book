---
id: 1
title: Setup Project Constitution
stage: constitution
date: 2025-12-07
surface: agent
model: Gemini
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
tests:
  null
---

## Prompt

/sp.constitution Project: Humanoid Robotics Book (AI/Spec-Driven Creation)
Title: Humanoid Robotics Book

Platform: Docusaurus → deployed exclusively to GitHub Pages
Core tools: Spec-Kit Plus + Claude Code (Grok allowed for research & editing)

Core principles:
- 100% spec-first: All content, structure, and features are driven by the living Spec-Kit Plus specification
- AI-assisted, human-in-the-loop: Claude Code is the primary generator; every change is reviewed and merged by the human author
- Fully reproducible, GitHub-native workflow from spec → content → build → live site

Key standards:
- Exact Spec-Kit Plus template[](https://github.com/panaversity/spec-kit-plus/)
- Docusaurus 3.x with provided configuration
- Clean, passing builds (npm run build must succeed under 8 minutes)
- Lighthouse scores ≥ 90 (Performance, Accessibility, Best Practices, SEO)
- Zero broken links, zero console errors in production

Constraints:
- Deployment: GitHub Pages only (no Vercel, Netlify, or other hosts)
- No plugins or dependencies outside the official Spec-Kit Plus template
- No manual editing of /docs that bypasses the spec → generate cycle

Success criteria:
- Entire book can be regenerated from the Spec-Kit Plus spec with zero errors
- npm run deploy works on any clean clone of the repository
- Live GitHub Pages site is publicly accessible, fast, and fully spec-traceable
- Every merge is human-approved; complete audit trail in Git history

Accountability:
- The human author is the sole approver of all content and merges
- Any deviation requires a formal spec amendment first

## Response snapshot

The project constitution has been created at `.specify/memory/constitution.md` with version 1.0.0. The `plan-template.md` has been updated to reflect the new constitutional checks.

## Outcome

- ✅ Impact: Project constitution created and templates updated.
- 🧪 Tests: No tests were run.
- 📁 Files: Created/updated 2 files.
- 🔁 Next prompts: User can now proceed with feature specification.
- 🧠 Reflection: The process of updating the constitution and propagating changes to templates worked as expected.

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment: null
