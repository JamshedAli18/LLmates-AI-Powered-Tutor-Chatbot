# rag_pipeline.py
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import streamlit as st

@st.cache_resource
def create_vector_store(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.create_documents(texts)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")
    return FAISS.from_documents(docs, embeddings)

def process_pdf(uploaded_file):
    """Reads PDF, processes first 10 pages, creates FAISS vectorstore."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()[:10]  # limit for speed
    text_data = " ".join([page.page_content for page in pages])
    return create_vector_store([text_data])

def retrieve_context(vectorstore, query, k=3):
    """Retrieve relevant chunks for query."""
    results = vectorstore.similarity_search(query, k=k)
    return "\n".join([r.page_content for r in results])
