<!--
---
Sync Impact Report
---
Version change: 0.0.0 → 1.0.0
Modified principles:
- PRINCIPLE_1: 100% spec-first
- PRINCIPLE_2: AI-assisted, human-in-the-loop
- PRINCIPLE_3: Fully reproducible, GitHub-native workflow
- PRINCIPLE_4: (removed)
- PRINCIPLE_5: (removed)
- PRINCIPLE_6: (removed)
Added sections:
- Key Standards and Constraints
- Success Criteria and Accountability
Removed sections:
- SECTION_2_NAME
- SECTION_3_NAME
Templates requiring updates:
- ✅ .specify/templates/plan-template.md
- ✅ .specify/templates/spec-template.md
- ✅ .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Humanoid Robotics Book (AI/Spec-Driven Creation) Constitution

## Core Principles

### I. 100% Spec-First
All content, structure, and features are driven by the living Spec-Kit Plus specification.

### II. AI-Assisted, Human-in-the-Loop
Claude Code is the primary generator; every change is reviewed and merged by the human author.

### III. Fully Reproducible, GitHub-Native Workflow
The entire workflow from specification to live site is reproducible and managed within GitHub. This includes spec changes, content generation, application builds, and deployment.

## Key Standards and Constraints

### Key Standards
- **Spec-Kit Plus**: All work must adhere to the official Spec-Kit Plus template.
- **Docusaurus**: The project uses Docusaurus 3.x with the provided configuration.
- **Builds**: Builds must be clean and successful, completing in under 8 minutes.
- **Performance**: The live site must achieve Lighthouse scores of 90 or higher across Performance, Accessibility, Best Practices, and SEO.
- **Quality**: There must be zero broken links and zero console errors in the production deployment.

### Constraints
- **Deployment**: Deployment is restricted to GitHub Pages only.
- **Dependencies**: No plugins or dependencies outside the official Spec-Kit Plus template are permitted.
- **Workflow**: Manual editing of the `/docs` directory is forbidden; all changes must originate from the spec-to-generation cycle.

## Success Criteria and Accountability

### Success Criteria
- The entire book must be regenerable from the Spec-Kit Plus specification without errors.
- The `npm run deploy` command must work on any clean clone of the repository.
- The live GitHub Pages site must be publicly accessible, fast, and fully traceable to the specification.
- Every merge into the main branch must be approved by a human, with a complete audit trail in the Git history.

### Accountability
- The human author is the sole approver for all content and merges.
- Any deviation from this constitution requires a formal amendment to the specification before implementation.

## Governance

This constitution is the authoritative document governing the project. All development activities, reviews, and deployments must comply with its principles. Amendments require a documented proposal, review, and approval, followed by a migration plan if necessary.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07