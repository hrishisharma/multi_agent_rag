import json
import os
from datetime import datetime

LOG_FILE = "logs.json"

def log_query(query, answer, validation, confidence):
    logs = []

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    logs.append({
        "timestamp": str(datetime.now()),
        "query": query,
        "answer": answer,
        "validation": validation,
        "confidence": confidence
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def get_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)

    return []
def clear_logs():
    with open("logs.json", "w") as f:
        f.write("[]")