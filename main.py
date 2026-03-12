from agents.retriever import retrieve
from agents.answerer import generate_answer
from agents.validator import validate_answer

# User input
query = input("Ask: ")

# Agent 1: Retrieval
context = retrieve(query)

# Agent 2: Answer generation
answer = generate_answer(query, context)

print("\nAnswer:")
print(answer)

# Agent 3: Validation
validation = validate_answer(answer, context)

print("\nValidation:")
print(validation)