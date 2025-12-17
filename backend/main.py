import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Optional
import openai
from in_memory_rag import in_memory_rag  # ← FIXED: removed the dot
# RAG System initialization happens when in_memory_rag is imported.
# It will load documents and generate embeddings on startup.

load_dotenv()

# OpenAI Setup
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ChatRequest(BaseModel):
    question: str
    selected_text: Optional[str] = None

@app.get("/")
async def root():
    return {"status": "OpenAI Backend Ready!"}

@app.post("/chat")
async def chat(request: ChatRequest):
    context = ""
    if request.selected_text:
        context = request.selected_text
    else:
        # Search in-memory RAG for relevant documents
        search_results = in_memory_rag.search(request.question)
        if search_results:
            context = "\n".join([doc["text"] for doc in search_results])

    messages = [{"role": "user", "content": f"Context: {context}\n\nQuestion: {request.question}"}]
    
    response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=messages)
    return {"answer": response.choices[0].message.content}