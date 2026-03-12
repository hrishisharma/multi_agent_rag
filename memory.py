import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(chat_history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(chat_history, f, indent=2)

def add_to_memory(question, answer):
    chat_history = load_memory()

    chat_history.append({
        "question": question,
        "answer": answer
    })

    if len(chat_history) > 3:
        chat_history.pop(0)

    save_memory(chat_history)


def get_memory():
    chat_history = load_memory()

    memory_text = ""

    for item in chat_history:
        memory_text += f"Question: {item['question']}\n"
        memory_text += f"Answer: {item['answer']}\n"

    return memory_text
def clear_memory():
    with open("memory.json", "w") as f:
        f.write("[]")
