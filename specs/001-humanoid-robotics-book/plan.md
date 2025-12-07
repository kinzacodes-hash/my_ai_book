# Implementation Plan: Humanoid Robotics Book

**Branch**: `001-humanoid-robotics-book` | **Date**: 2025-12-07 | **Spec**: [specs/001-humanoid-robotics-book/spec.md](specs/001-humanoid-robotics-book/spec.md)
**Input**: Feature specification from `/specs/001-humanoid-robotics-book/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The project is to create a comprehensive, 13-week, project-based textbook on humanoid robotics. The textbook will be a Docusaurus site deployed to GitHub Pages, with an integrated RAG chatbot. The content will be generated using a spec-driven approach with AI assistance.

## Technical Context

**Language/Version**: Python 3.11, Node.js 20.x
**Primary Dependencies**: Docusaurus 3.x, FastAPI, Neon, Qdrant, ChatKit SDK, Better-Auth, Claude Code
**Storage**: Neon Serverless Postgres, Qdrant Cloud
**Testing**: Playwright, Pytest
**Target Platform**: Web (Docusaurus on GitHub Pages), Ubuntu 22.04 for code examples
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Lighthouse scores >= 90, build time < 8 minutes
**Constraints**: GitHub Pages only, no external plugins for Docusaurus, spec-driven content generation.
**Scale/Scope**: 13-module book with appendices, RAG chatbot, and bonus features.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Spec-First**: Does this plan originate from a clear, approved specification in `specs/`?
- [x] **Reproducible Workflow**: Does the plan rely exclusively on the established GitHub-native workflow (spec -> generate -> build -> deploy)?
- [x] **AI-Assisted**: Is the role of AI in generation clearly defined, with human review as the final gate?
- [x] **Standards Adherence**:
    - [x] Does the plan use the official Spec-Kit Plus template and Docusaurus 3.x?
    - [x] Are there any new dependencies or plugins being introduced? (Constraint violation) - No
    - [x] Does the plan involve any manual editing of the `/docs` directory? (Constraint violation) - No
- [x] **Deployment**: Is the deployment target exclusively GitHub Pages?

## Project Structure

### Documentation (this feature)

```text
specs/001-humanoid-robotics-book/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web application (frontend + backend)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: The project will use a web application structure with a frontend for the Docusaurus site and a backend for the FastAPI services (RAG chatbot, auth, etc.).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
|           |            |                                     |
|           |            |                                     |