from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings

embeddings = get_embeddings()

db = FAISS.load_local(
    "/home/hrishi/ai-data-analyst/Project1/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

def retrieve(query):
    results = db.similarity_search_with_score(query, k=8)

    filtered_docs = []

    

    for doc, score in results:

        if score < 2.0:
            filtered_docs.append(doc)

    if not filtered_docs:
        filtered_docs = [results[0][0]]

    context = "\n".join([doc.page_content for doc in filtered_docs[:5]])

    return context