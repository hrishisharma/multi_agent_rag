from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings

def build_index(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    filtered_docs = documents[:10]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    docs = splitter.split_documents(filtered_docs)

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)

    db.save_local("faiss_index")

    return "FAISS index created successfully"