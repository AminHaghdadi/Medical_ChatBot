# Load required python libraries 
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch

# Check if GPU is available, otherwise set device to CPU
if torch.cuda.is_available():
    device = "cuda" 
else:
    device = "cpu"

device = torch.device(device) 

# Set path to data directory
DATA_PATH = 'data/'
# Set path to save FAISS index
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Function to create FAISS vector database
def create_vector_db():

  # Load PDF files from data directory 
  loader = DirectoryLoader(DATA_PATH,
                           glob='*.pdf',
                           loader_cls=PyPDFLoader)

  # Load documents 
  documents = loader.load()
  
  # Split documents into chunks of 500 characters with 50 overlap
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                 chunk_overlap=50)
  chunks = text_splitter.split_documents(documents)

  # Generate sentence embeddings for each chunk 
  embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                     model_kwargs={'device': device})

  # Create FAISS index from embeddings
  db = FAISS.from_documents(chunks, embeddings)
  
  # Save FAISS index locally
  db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
  create_vector_db()