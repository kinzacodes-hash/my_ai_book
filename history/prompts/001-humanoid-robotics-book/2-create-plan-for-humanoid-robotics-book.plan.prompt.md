---
id: 2
title: Create Plan for Humanoid Robotics Book
stage: plan
date: 2025-12-07
surface: agent
model: Gemini
feature: 001-humanoid-robotics-book
branch: 001-humanoid-robotics-book
user: user
command: /sp.plan
labels: ["plan", "architecture"]
links:
  spec: specs/001-humanoid-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-humanoid-robotics-book/plan.md
  - specs/001-humanoid-robotics-book/research.md
  - specs/001-humanoid-robotics-book/data-model.md
  - specs/001-humanoid-robotics-book/quickstart.md
tests:
  null
---

## Prompt

/sp.plan Project: Humanoid Robotics Book – Physical AI & Humanoid Robotics Textbook
Phase: Planning → Execution (spec-driven, research-concurrent)

Architecture Sketch
├── Docusaurus 3.x site (Spec-Kit Plus template) → GitHub Pages (only allowed deployment)
├── Docs-as-code: /docs/ contains all book modules (auto-generated from spec)
├── Embedded RAG Chatbot (mandatory hackathon deliverable)
│   ├── Backend: FastAPI + Neon Serverless Postgres + Qdrant Cloud (free tier)
│   ├── Frontend: ChatKit SDK embedded in Docusaurus layout
│   └── Vector store auto-updated on every build via GitHub Actions
├── Bonus stack (modular, toggleable via feature flags)
    ├── Better-Auth signup/login + user background profiling
    ├── Per-chapter personalization button (content adaptation via user profile)
    ├── Per-chapter Urdu translation button (on-demand via LLM or pre-cached)
    └── Claude Code Subagents & reusable Skills registry

Section Structure (final – locked by /.specify)
Module 00 → Module 07 + Capstone + 6 Appendices (see /.specify for exact titles and scope)

Research Approach
- Research-concurrent: No upfront 3-month literature review
- Each module researched only when its turn comes (week-of writing)
- Primary sources: official documentation (ROS 2, Isaac Sim, NVIDIA papers), GitHub repos, Panaversity curriculum
- Secondary: latest arXiv papers on VLA, humanoid locomotion, sim-to-real (2023–2025 only)
- Citation style: APA 7th (as required by constitution)

Quality Validation & Testing Strategy
1. Build must pass: npm run build < 8 min, zero errors/warnings
2. Lighthouse ≥ 90/100 on all four metrics
3. RAG chatbot answers 10 golden questions correctly (test suite in /tests/rag-golden-set.md)
4. Every code snippet must run on clean Ubuntu 22.04 + ROS Humble + Isaac Sim 2024.1
5. End-to-end demo: voice command → humanoid action in Isaac Sim (recorded video <90 sec)
6. Bonus features tested via feature flags and automated Playwright checks

Decisions Needing Documentation
1. Translation strategy
   - Option A: Pre-translate all Urdu content → larger repo, faster load
   - Option B: On-demand LLM translation → smaller repo, needs API key
   → Chosen: Hybrid (cache first request per paragraph)

2. Personalization depth
   - Option A: Light (hide/show beginner sections)
   - Option B: Heavy (rewrite explanations based on user background)
   → Chosen: Light + optional “explain like I’m beginner/expert” toggle

3. RAG chunking strategy
   - 512-token chunks with 128 overlap vs 1024-token
   → Chosen: 800-token with 200 overlap (best quality on robotics code+text)

Phases & Timeline (hackathon deadline: Nov 30, 2025 18:00 PKT)
Phase 1 – Foundation (Days 1-3)
   → Skeleton generation, RAG backend, GitHub Pages deploy of “Hello World” book
Phase 2 – Core Content (Days 4-18)
   → Write + illustrate Modules 00-07 using Claude Code (one module every 2 days)
Phase 3 – Bonus & Polish (Days 19-24)
   → Better-Auth + personalization + Urdu buttons + Subagents
Phase 4 – Validation & Submission (Days 25-27)
   → Golden tests, Lighthouse, video demo, final deploy

Success = Live GitHub Pages URL + working embedded RAG + bonus features + <90-sec demo video submitted before deadline.

## Response snapshot

I have created the implementation plan for the Humanoid Robotics Book. The plan file is located at `specs/001-humanoid-robotics-book/plan.md`. I have also created the `research.md`, `data-model.md`, and `quickstart.md` files, and the `contracts` directory.

## Outcome

- ✅ Impact: Created the implementation plan for the Humanoid Robotics Book.
- 🧪 Tests: No tests were run.
- 📁 Files: Created 4 files.
- 🔁 Next prompts: User can now proceed with generating tasks for the implementation.
- 🧠 Reflection: The planning phase was successful. The user provided a detailed architecture sketch which made the process easier.

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment: null
