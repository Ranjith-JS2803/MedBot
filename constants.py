import google.generativeai as genAI
from langchain_huggingface import HuggingFaceEmbeddings

genAI.configure(api_key = "AIzaSyBax99HsgKFsikv5hLGzM3K0I90Q8qBE8M")
model = genAI.GenerativeModel("gemini-1.5-flash")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")