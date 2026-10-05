# WELCOME TO THE MULTI PDF RAG ASSISTANT

from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

print(os.listdir())

# =====================================================
# LLM Calling
# =====================================================

print("=" * 60)
print("         WELCOME TO THE MULTI PDF RAG ASSISTANT")
print("=" * 60)

try:

    load_dotenv()

    client = genai.Client(
        api_key=os.getenv("API_KEY")
    )

except Exception as e:
    print(f"ERROR OCCURS : {e}")
    exit()

# =====================================================
# Empty Chunks and Metadata
# =====================================================

all_chunks = []
metadata = []

# =====================================================
# PDF Reading
# =====================================================

chunk_size = 10
overlap = 2
step = chunk_size - overlap

try:
    pdf_folder = [file for file in os.listdir() if file.endswith(".pdf")]

    for pdf_file in pdf_folder:
        reader = PdfReader(pdf_file)
        chunk_number = 1

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text() or ""
            words = page_text.split()

            # -----------------------------
            # Creating Chunks
            # -----------------------------

            

            for start in range(0, len(words), step):

                print("PDF :", pdf_file)
                print("PAGE NUMBER :", page_number)
                print("CHUNK :", start)
                print("-" * 60)

                chunk_text = " ".join(words[start:start + chunk_size])

                all_chunks.append(chunk_text)

                metadata.append({
                    "pdf": pdf_file,
                    "page": page_number,
                    "chunk": chunk_number
                })

                chunk_number += 1

except Exception as e:
    print(f"ERROR OCCURS : {e}")
    exit()

# =====================================================
# Load Embedding Model
# =====================================================

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # =====================================================
    # Creating Embeddings
    # =====================================================

    embeddings = model.encode(all_chunks)

    embeddings = np.array(embeddings).astype("float32")

    print(f"TOTAL EMBEDDINGS : {len(embeddings)}")

except Exception as e:
    print(f"ERROR OCCURS : {e}")
    exit()

context = ""

# =====================================================
# Creating FAISS Index
# =====================================================

try:
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    # Store Embeddings
    index.add(embeddings)

except Exception as e:
    print(f"ERROR OCCURS : {e}")
    exit()

# =====================================================
# Chat Loop
# =====================================================

try:
    while True:

        # -----------------------------
        # User Question
        # -----------------------------
        
        print("-"*60)
        query = input("ASK QUESTIONS : ")

        if query.lower() == "exit":
            print("THANK YOU FOR USING OUR PROGRAM")
            break

        # -----------------------------
        # Query Embedding
        # -----------------------------

        query_embeddings = model.encode([query])
        query_embeddings = np.array(query_embeddings).astype("float32")

        # -----------------------------
        # Similarity Search
        # -----------------------------

        TOP_K = 2
        distances, indices = index.search(query_embeddings, k=TOP_K)

        for i in indices[0]:
            print("-" * 60)
            print(all_chunks[i])

        relevant_chunks = []

        for i in indices[0]:
            relevant_chunks.append(all_chunks[i])

        context = "\n".join(relevant_chunks)

        for i in indices[0]:
            print(metadata[i])

        # -----------------------------
        # Gemini Calling
        # -----------------------------

        prompt = f"""
Give me the answer based on:

Query:
{query}

Context:
{context}

Instructions:
- Very simple format
- Very short in 1 line only
- No technical jargons
"""

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        print(response.text)

except Exception as e:
    print(f"ERROR OCCURS : {e}")


print("-"*60)
print("THANK YOU FOR USING OUR PROGRAM")