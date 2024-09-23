from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from constants import *
import pickle
import faiss
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
faiss_store_path = os.path.join(current_dir, "faiss_store.pkl")
docs_index_path = os.path.join(current_dir, "docs.index")

with open(faiss_store_path, "rb") as f:
    store = pickle.load(f)
    store.index = faiss.read_index(docs_index_path)

def med_gpt(query):
    context = store.similarity_search(query, k=3)
    medical_prompt_template = f"""
    You are a medical assistant specialized in providing information about health-related queries.
    Please analyze the following symptoms and provide a relevant medical response based on the context provided.

    Symptoms: {query}
    Relevant context: {context}
    """ 

    try:
        response = model.generate_content(medical_prompt_template)
        return response.text
    except Exception as e:
        return "An error occurred during processing."