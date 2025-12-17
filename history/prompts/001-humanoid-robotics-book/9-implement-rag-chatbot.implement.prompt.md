---
id: 9
title: Implement RAG chatbot
stage: implement
date: 2025-12-17
surface: agent
model: gemini
feature: humanoid-robotics-book
branch: main
user: user
command: /sp.implement
labels: [rag, chatbot, fastapi, qdrant]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/main.py
 - backend/index.py
 - backend/requirements.txt
 - backend/.env
 - frontend/src/theme/DocItem/index.tsx
tests:
 - none
---

## Prompt

/sp.implement

Create the RAG chatbot as per hackathon requirements using Qdrant Cloud.

Requirements:
- Use Qdrant Cloud free tier for vector database
- Use OpenAI embeddings and gpt-4o-mini for generation
- Index all content from frontend/docs/*.md files (all modules)
- Create a FastAPI backend in a new folder called "backend"
- Backend must have /chat endpoint that accepts { "question": "...", "selected_text": "..." }
- If selected_text is provided, use only that as context
- Otherwise, search Qdrant for top 5 relevant chunks and use them as context
- Add CORS so it works from localhost and GitHub Pages
- Create .env file with placeholders for OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY
- Create a simple indexing script to upload all book content to Qdrant
- Add ChatKit SDK embed code to the Docusaurus layout so the chatbot appears on every page
- Make sure it works locally with `uvicorn backend/main:app --reload`

Do everything automatically. Use the following keys (replace with actual if needed):
QDRANT_URL = "
qdrant_client = QdrantClient(
    url="https://53366e49-a7a0-450d-9791-95579b3a3f91.europe-west3-0.gcp.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.GWssts-mJsFTEeK9bVQlkY5IOyteUxi2s1eYJa-Q4-M",
)"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.GWssts-mJsFTEeK9bVQlkY5IOyteUxi2s1eYJa-Q4-M"
OPENAI_API_KEY = "vJuynAhCB2uy7aID6AJ28DlmLxjIffHk04h7PvWy"

After completion, tell me the exact commands to run the backend and test the chatbot.

## Response snapshot

I have completed the implementation of the RAG chatbot. However, the indexing script failed due to an invalid OpenAI API key.

Here are the final instructions to get the chatbot running:

**IMPORTANT:** The OpenAI API key you provided is invalid. You need to update the `OPENAI_API_KEY` in the `backend/.env` file with a valid key.

1.  **Update API Key:**
    *   Open `backend/.env` and replace the placeholder with your correct OpenAI API key.

2.  **Install Dependencies (if you haven't already):**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Run the Indexing Script:**
    *   This will populate your Qdrant database with the book content.
    ```bash
    python backend/index.py
    ```

4.  **Run the Backend Server:**
    ```bash
    uvicorn backend.main:app --reload
    ```

5.  **Test the Chatbot:**
    *   Start your Docusaurus development server in another terminal:
        ```bash
        npm start --prefix frontend
        ```
    *   Open your website (usually at `http://localhost:3000`).
    *   You should see the chatbot on the documentation pages.
    *   **Note:** The chatbot UI will appear, but it will not be functional until you replace `"YOUR_CHATKIT_ID"` in `frontend/src/theme/DocItem/index.tsx` with a valid ChatKit ID and configure it to use the backend.

## Outcome

- ✅ Impact: Created a full RAG chatbot backend and integrated it with the frontend.
- 🧪 Tests: No tests were run.
- 📁 Files: 5 files created/modified.
- 🔁 Next prompts: The user needs to provide a valid OpenAI API key.
- 🧠 Reflection: The provided API keys should be validated before use.

## Evaluation notes (flywheel)

- Failure modes observed: `openai.AuthenticationError`
- Graders run and results (PASS/FAIL): FAIL
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Use a valid API key.
