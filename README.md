# 📚 Multi PDF RAG Assistant

A beginner-friendly Retrieval-Augmented Generation (RAG) project built while learning AI Automation.

This project reads multiple PDF files, converts them into embeddings, stores them in a FAISS vector database, retrieves the most relevant chunks based on the user's question, and uses Google Gemini to generate an answer.

---

# 🚀 Features

- Read multiple PDF files
- Page-wise text processing
- Text chunking with overlap
- Sentence Transformers embeddings
- FAISS vector search
- Metadata tracking (PDF, page, chunk)
- Semantic similarity search
- Google Gemini integration
- Interactive command-line chat

---

# 🛠 Tech Stack

- Python
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- NumPy
- Python Dotenv

---

# 📂 Project Workflow

```text
PDF Files
      │
      ▼
Read PDFs
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store Embeddings in FAISS
      │
      ▼
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Send Context to Gemini
      │
      ▼
Generate Final Answer
```

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/multi-pdf-rag-assistant.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
API_KEY=YOUR_GEMINI_API_KEY
```

Place your PDF files in the project directory.

Run

```bash
python main.py
```

---

# 📁 Project Structure

```
project/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
├── pdf1.pdf
├── pdf2.pdf
└── ...
```

---

# 📌 Learning Objectives

This project was created to understand:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embeddings
- FAISS
- Metadata
- Chunking
- LLM Integration

---

# 📖 Note

This is a learning project built while studying AI Automation and RAG concepts. It is learning assistant development, while the project workflow, implementation understanding, and iterative improvements were completed as part of the learning process.

---

# 📜 License

MIT License
