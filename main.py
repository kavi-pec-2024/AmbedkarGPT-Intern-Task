import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA



# Step 1: Load text
loader = TextLoader("speech.txt")
documents = loader.load()

# Step 2: Split text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=300,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 4: Create / load Chroma DB
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="chroma_db"
)

# Step 5: Create retriever
retriever = vectordb.as_retriever()

# Step 6: Connect to LLM (Ollama)
llm = Ollama(model="mistral")

# Step 7: Build RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

print("AmbedkarGPT Ready! Ask any question.\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa_chain.invoke({"query": query})
    
    print("\nAnswer:", result["result"])
    print("-" * 60)
