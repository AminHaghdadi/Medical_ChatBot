from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import torch

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

device = torch.device(device)
DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt = '''
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
'''
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                   model_kwargs={'device': device})

prompt = PromptTemplate(template=custom_prompt, input_variables=['context', 'question'])

llm = CTransformers(
    model="llama2-7b/llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_type="llama",
    max_new_tokens=512,
    temperature=0.1)

db = FAISS.load_local(DB_FAISS_PATH, embeddings)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True,
    chain_type_kwargs={'prompt': prompt}
)

def final(query) :
    response = chain({'query': query})
    return response

print(final("what is Aspergillosis?"))