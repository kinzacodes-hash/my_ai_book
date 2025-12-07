# Tasks: Humanoid Robotics Book

**Input**: Design documents from `/specs/001-humanoid-robotics-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, research.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 [P] Initialize Docusaurus frontend project in `frontend/`
- [X] T002 [P] Initialize FastAPI backend project in `backend/`
- [X] T003 [P] Configure linting and formatting tools for both projects

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T004 Setup database schema in `backend/src/models/` based on `data-model.md`
- [X] T005 [P] Implement user authentication using Better-Auth in `backend/src/api/auth.py`
- [X] T006 [P] Implement RAG chatbot backend with FastAPI, Neon, and Qdrant in `backend/src/api/chatbot.py`
- [X] T007 Integrate ChatKit SDK into the Docusaurus frontend in `frontend/src/theme/Layout/index.js`
- [X] T008 Configure GitHub Actions to deploy the Docusaurus site to GitHub Pages

---

## Phase 3: User Story 1 - Understand the fundamentals of Physical AI (Priority: P1) 🎯 MVP

**Goal**: Create the first two modules of the book.
**Independent Test**: The reader can answer questions about the core concepts of Physical AI and the roadmap of the course.

### Implementation for User Story 1
- [X] T009 [US1] Create Module 00 - Introduction to Physical AI and Embodied Intelligence in `frontend/docs/module-00`
- [X] T010 [US1] Create Module 01 - Foundations of Physical AI in `frontend/docs/module-01`

---

## Phase 4: User Story 2 - Master ROS 2 (Priority: P2)

**Goal**: Create the ROS 2 module.
**Independent Test**: The reader can create a new ROS 2 package, build it, and run it on a simulated robot.

### Implementation for User Story 2
- [X] T011 [US2] Create Module 02 - ROS 2 – The Robotic Nervous System in `frontend/docs/module-02`

---

## Phase 5: User Story 3 - Create realistic simulations (Priority: P3)

**Goal**: Create the simulation module.
**Independent Test**: The reader can create a new Gazebo world and spawn the humanoid robot in it.

### Implementation for User Story 3
- [X] T012 [US3] Create Module 03 - Simulation – Your Digital Twin in `frontend/docs/module-03`

---

## Phase 6: User Story 4 - Build the robot's brain with NVIDIA Isaac (Priority: P4)

**Goal**: Create the NVIDIA Isaac module.
**Independent Test**: The reader can use Isaac Sim to generate synthetic data and train a perception model.

### Implementation for User Story 4
- [X] T013 [US4] Create Module 04 - NVIDIA Isaac Platform – The AI Brain in `frontend/docs/module-04`

---

## Phase 7: User Story 5 - Implement humanoid control (Priority: P5)

**Goal**: Create the control module.
**Independent Test**: The reader can make the robot walk to a specific location and grasp an object.

### Implementation for User Story 5
- [X] T014 [US5] Create Module 05 - Humanoid Kinematics, Dynamics & Control in `frontend/docs/module-05`

---

## Phase 8: User Story 6 - Build a cognitive layer with VLA models (Priority: P6)

**Goal**: Create the VLA models module.
**Independent Test**: The reader can give a voice command to the robot and see it executed.

### Implementation for User Story 6
- [X] T015 [US6] Create Module 06 - Vision-Language-Action (VLA) Models – The Cognitive Layer in `frontend/docs/module-06`

---

## Phase 9: User Story 7 - Complete a capstone project (Priority: P7)

**Goal**: Create the capstone project module.
**Independent Test**: The reader can demonstrate the full pipeline of the capstone project.

### Implementation for User Story 7
- [X] T016 [US7] Create Module 07 - Capstone Project in `frontend/docs/module-07`

---

## Phase 10: Polish & Cross-Cutting Concerns

- [X] T017 [P] Implement per-chapter content personalization button in `frontend/src/theme/DocItem/index.js`
- [X] T018 [P] Implement per-chapter Urdu translation button in `frontend/src/theme/DocItem/index.js`
- [X] T019 [P] Create reusable Claude Code Subagents & Skills registry in `backend/src/subagents`
- [X] T020 Create Appendices in `frontend/docs/appendices`
- [X] T021 Run golden tests for RAG chatbot
- [X] T022 Run Lighthouse tests and optimize performance
- [X] T023 Record end-to-end demo video

## Dependencies & Execution Order

- **Phase 1 (Setup)** and **Phase 2 (Foundational)** must be completed before any user story implementation.
- User story phases can be implemented in parallel after Phase 2 is complete.
- **Phase 10 (Polish)** should be done after all user story phases are complete.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
... and so on for all user stories.
