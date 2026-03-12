from fastapi import FastAPI
from agents.retriever import retrieve
from agents.answerer import generate_answer
from agents.validator import validate_answer
from memory import add_to_memory, clear_memory
from logger import log_query, get_logs, clear_logs
from fastapi import FastAPI, UploadFile, File
from vectorstore.build_index import build_index
import shutil


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent RAG API running"}

@app.get("/ask")
def ask_question(query: str):
    # Retrieve relevant context
    context = retrieve(query)

    # Generate answer
    answer = generate_answer(query, context)

    # Save to memory
    add_to_memory(query, answer)

    # Validate answer + confidence
    validation, confidence = validate_answer(answer, context)

    # Log query
    log_query(query, answer, validation, confidence)

    # Return response
    return {
        "query": query,
        #"retrieved_context": context,
        "answer": answer,
        "validation": validation,
        "confidence": confidence
    }

@app.get("/logs")
def view_logs():
    return get_logs()
@app.post("/clear_memory")
def reset_memory():
    clear_memory()
    return {"status": "Memory cleared"}

@app.post("/clear_logs")
def reset_logs():
    clear_logs()
    return {"status": "Logs cleared"}

@app.post("/upload_pdf")
def upload_pdf(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = build_index(file_path)

    return {
        "filename": file.filename,
        "status": result
    }