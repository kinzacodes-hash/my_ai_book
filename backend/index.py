import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from qdrant_client import QdrantClient, models
import uuid

# Load .env file from the parent directory
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
qdrant_client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

COLLECTION_NAME = "humanoid-robotics-book"
# OpenAI's text-embedding-3-small has a dimension of 1536
VECTOR_SIZE = 1536

def main():
    if qdrant_client.collection_exists(collection_name=COLLECTION_NAME):
        qdrant_client.delete_collection(collection_name=COLLECTION_NAME)
    
    qdrant_client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
    )
    
    # Correctly resolve the path to the docs folder from the backend directory
    docs_path = Path(__file__).parent.parent / "frontend/docs"
    md_files = list(docs_path.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files to index.")

    points = []

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        try:
            # OpenAI Embedding
            result = openai.embeddings.create(model="text-embedding-3-small", input=content)
            embedding = result.data[0].embedding

            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"text": content, "source": str(file_path)}
            ))
        except Exception as e:
            print(f"Failed to create embedding for {file_path}: {e}")

    # If no files were found, add a dummy point to avoid an empty upsert request
    if not points:
        print("No content to index. Adding a dummy document.")
        dummy_content = "This is a dummy document to ensure the index is not empty."
        try:
            result = openai.embeddings.create(model="text-embedding-3-small", input=dummy_content)
            embedding = result.data[0].embedding
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"text": dummy_content, "source": "dummy"}
            ))
        except Exception as e:
            print(f"Failed to create embedding for dummy document: {e}")

    if points:
        print(f"Upserting {len(points)} points to Qdrant...")
        qdrant_client.upsert(collection_name=COLLECTION_NAME, points=points)
        print("Indexing Complete with OpenAI!")
    else:
        print("Could not create any points to upsert. Indexing failed.")

if __name__ == "__main__":
    main()