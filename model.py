# Load required python libraries 
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import streamlit as st
import torch

# Check if GPU is available, otherwise use CPU
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu" 

device = torch.device(device)

# Path to load FAISS index
DB_FAISS_PATH = 'vectorstore/db_faiss'  

# Custom prompt template with context and question variables
custom_prompt = '''
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}  
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
'''

# Load sentence transformer model  
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                   model_kwargs={'device': device})

# Create prompt template
prompt = PromptTemplate(template=custom_prompt, input_variables=['context', 'question'])

# Load LLama model
llama = CTransformers(
    model="llama2-7b/llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_type="llama",
    max_new_tokens=512,
    temperature=0.1)

# Load FAISS index
db_faiss = FAISS.load_local(DB_FAISS_PATH, embedding)

# Function to create retrieval chain
def chains(llm,prompt,db):
  chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", 
    retriever=db.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True,
    chain_type_kwargs={'prompt': prompt}
  )
  return chain

# Function to run QA
def qa_bot(query):
  db = db_faiss
  llm = llama
  qa_prompt = prompt
  qa = chains(llm, qa_prompt, db)
  response = qa({'query': query})
  return response

# Function to get final result
def final_result(query):
  qa_result = qa_bot()
  response = qa_result({'query': query})
  return response


