import ollama
from memory import get_memory

def generate_answer(query, context):
    memory = get_memory()

    prompt = f"""
    You are answering from a research document.

Use only the provided context.
Give a precise answer.
If multiple points exist, summarize them clearly.
If answer is uncertain, say so.
Conversation History:
{memory}

Context:
{context}

Question:
{query}

Answer precisely using context and history.
Use only provided context.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]