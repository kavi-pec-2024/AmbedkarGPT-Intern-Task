# -AmbedkarGPT-Intern-Task
AmbedkarGPT is a local Retrieval-Augmented Generation (RAG) system that answers questions based on a provided speech.txt file of Dr. B.R. Ambedkar.
It uses:

LangChain (community version)

Ollama (Local LLM inference)

ChromaDB (vector store)

HuggingFace Embeddings

Python CLI interface

This project was built as part of an AI/ML internship assignment to demonstrate skills in embeddings, vector databases, LLM integration, and retrieval pipelines.

🚀 Features

Load and chunk text from speech.txt

Generate embeddings using all-MiniLM-L6-v2

Store vectors in ChromaDB

Query using Mistral LLM (via Ollama)

Fully offline / local execution

Interactive CLI chatbot

Clean and modular RAG pipeline

📁 Project Structure
AmbedkarGPT-Intern-Task/
│── main.py
│── speech.txt
│── requirements.txt
│── chroma_db/        # Auto-generated after first run
│── .venv/            # Python virtual environment
│── README.md

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone <repo-url>
cd AmbedkarGPT-Intern-Task

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.\.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install & run Ollama

Download Ollama (Windows/macOS/Linux):
https://ollama.com/download

Start the Ollama server:

ollama serve


Pull the mistral model:

ollama pull mistral

▶️ Running the Project

Execute the script:

python main.py


You will see:

AmbedkarGPT Ready! Ask any question.


Now type your questions based on the speech content, for example:

You: What are the key points discussed in the speech?
You: Explain Dr. Ambedkar’s views on democracy.
You: exit

🧠 How It Works (RAG Flow)

Load Data

Reads speech.txt using LangChain TextLoader

Chunking

Splits text into 300-character segments

Embedding

Uses HuggingFace all-MiniLM-L6-v2

Vector Store

Stores chunks in Chroma DB

Retriever

Gets most relevant chunks for any question

LLM

Mistral (via Ollama) generates final answer

RAG Pipeline

Combines LLM + retrieved text to answer accurately

📌 Example Code (Already in main.py)
result = qa_chain.invoke({"query": query})
print("\nAnswer:", result["result"])

🧩 Dependencies

Python 3.10+

langchain-community

langchain-core

chromadb

sentence-transformers

ollama (local LLM engine)

huggingface embeddings

📝 Requirements File (Sample)
langchain
langchain-community
chromadb
sentence-transformers
huggingface-hub

❗ Troubleshooting
❌ Ollama not found

Install from: https://ollama.com/download

❌ Port already in use

Stop existing Ollama instance:

taskkill /F /IM ollama.exe

❌ LangChain deprecation warnings

Use updated imports from langchain-community.

📜 License

This project is built for educational and internship purposes.
Free to modify and use for learning.

🙏 Acknowledgements

Dr. B.R. Ambedkar’s writings

LangChain community

ChromaDB developers

Mistral AI

Ollama open-source contributors