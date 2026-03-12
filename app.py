import streamlit as st
import requests

st.title("Multi-Agent RAG Document Assistant")

# Ask question section
st.header("Ask a Question")

query = st.text_input("Enter your question")

if st.button("Submit Question"):
    if query:
        response = requests.get(
            "http://127.0.0.1:8000/ask",
            params={"query": query}
        )

        data = response.json()

        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Validation")
        st.write(data["validation"])

        st.subheader("Confidence")
        st.write(data["confidence"])

# PDF upload section
st.header("Upload PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if st.button("Upload PDF"):
    if uploaded_file:
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/upload_pdf",
            files={"file": uploaded_file}
        )

        st.success(response.json())

# Logs section
st.header("View Logs")

if st.button("Show Logs"):
    response = requests.get("http://127.0.0.1:8000/logs")

    logs = response.json()

    st.json(logs)

st.header("Reset Controls")

if st.button("Clear Memory"):
    response = requests.post("http://127.0.0.1:8000/clear_memory")
    st.success(response.json())

if st.button("Clear Logs"):
    response = requests.post("http://127.0.0.1:8000/clear_logs")
    st.success(response.json())