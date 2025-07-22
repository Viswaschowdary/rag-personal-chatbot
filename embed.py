import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-3-small"
        )
        embeddings.append(response["data"][0]["embedding"])
    return embeddings
