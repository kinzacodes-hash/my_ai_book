import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI
import uuid
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load .env file from the parent directory
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EMBEDDING_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 500  # words

class InMemoryRAG:
    def __init__(self):
        self.documents = []
        self.embeddings = []
        self.load_and_index_documents()

    def get_embedding(self, text: str):
        response = openai_client.embeddings.create(
            input=text,
            model=EMBEDDING_MODEL
        )
        return response.data[0].embedding

    def load_and_index_documents(self):
        docs_path = Path(__file__).parent.parent.parent / "frontend/docs"
        md_files = list(docs_path.rglob("*.md"))
        print(f"Found {len(md_files)} markdown files to index for in-memory RAG.")

        for file_path in md_files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            chunks = self._chunk_document(content, file_path)
            for chunk_text, chunk_metadata in chunks:
                try:
                    embedding = self.get_embedding(chunk_text)
                    self.documents.append({"text": chunk_text, "source": str(file_path)})
                    self.embeddings.append(embedding)
                except Exception as e:
                    print(f"Failed to create embedding for chunk from {file_path}: {e}")
        
        self.embeddings = np.array(self.embeddings)
        print(f"In-memory RAG indexed {len(self.documents)} document chunks.")

    def _chunk_document(self, content: str, file_path: Path):
        chunks = []
        words = content.split()
        for i in range(0, len(words), CHUNK_SIZE):
            chunk_text = " ".join(words[i:i + CHUNK_SIZE])
            chunks.append((chunk_text, {"source": str(file_path)}))
        return chunks

    def search(self, query: str, top_n: int = 5):
        query_embedding = self.get_embedding(query)
        
        if len(self.embeddings) == 0:
            return []

        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        
        # Get indices of top_n most similar chunks
        top_n_indices = similarities.argsort()[-top_n:][::-1]
        
        results = []
        for i in top_n_indices:
            results.append(self.documents[i])
        return results

# Global RAG instance
in_memory_rag = InMemoryRAG()
