import pickle
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from constants import embeddings

pdf_directory = "documents"
pages= []

pdf_files = [f"\doc_{i}.pdf" for i in range(1, 6)]
for files in pdf_files:
    path = pdf_directory+files
    loader = PyPDFLoader(path)
    pages += loader.load_and_split()

faiss_index = FAISS.from_documents(pages,embeddings)

faiss.write_index(faiss_index.index, "docs.index")
with open("faiss_store.pkl", "wb") as f:
    pickle.dump(faiss_index, f)