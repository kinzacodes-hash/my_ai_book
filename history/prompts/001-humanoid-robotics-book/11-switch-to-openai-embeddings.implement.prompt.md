---
id: 11
title: Switch to OpenAI Embeddings
stage: implement
date: 2025-12-17
surface: agent
model: gemini-cli
feature: 001-humanoid-robotics-book
branch: main
user: unspecified
command: /sp.implement
labels: [backend, python, openai, embeddings]
links:
  spec: "specs/001-humanoid-robotics-book/spec.md"
  ticket: null
  adr: null
  pr: null
files:
  - "backend/index.py"
  - "backend/requirements.txt"
tests:
  - "none"
---

## Prompt

/sp.implement

Fix backend/index.py to use OpenAI embeddings instead of Gemini (because Gemini quota exceeded).

Changes:
- Remove all import google.generativeai
- Use OpenAI client for embeddings: openai.embeddings.create(model="text-embedding-3-small")
- Keep Qdrant client as is
- Use the OPENAI_API_KEY from .env
- Keep the dummy chunk if no docs found
- Keep printing number of files and chunks
- After fix, run the indexing script automatically and show output

Do it now so indexing completes successfully with OpenAI embeddings.

## Response snapshot

The indexing script `backend/index.py` has been updated to use OpenAI's `text-embedding-3-small` model for generating embeddings.

However, the script is now failing with a connection error to the Qdrant database:
`qdrant_client.http.exceptions.ResponseHandlingException: [WinError 10061] No connection could be made because the target machine actively refused it`

This indicates that the Qdrant server is not running or is not accessible at the configured URL.

## Outcome

- ✅ Impact: The indexing script now uses the OpenAI embeddings API, as requested. The vector size for the Qdrant collection has been updated to match the new embedding model's dimensions.
- 🧪 Tests: No tests were run. The script was executed directly.
- 📁 Files: `backend/index.py` was modified. `openai` was added to `backend/requirements.txt`.
- 🔁 Next prompts: The user needs to ensure that the Qdrant database is running and accessible.
- 🧠 Reflection: The switch to OpenAI embeddings was successful, but a new infrastructure-related issue has appeared. It highlights the importance of checking all external service connections.

## Evaluation notes (flywheel)

- Failure modes observed: Connection error to the vector database.
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
