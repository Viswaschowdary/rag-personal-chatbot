import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(context_chunks, query):
    context = "\n\n".join(context_chunks)
    prompt = f"""
You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']
