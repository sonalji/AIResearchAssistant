""" from src.pdf_loader import extract_pdf
from src.txt_cleaner import clean_document
from src.chunker import chunk_document
from src.embedding import load_embedding_model, generate_embeddings
from src.llm import generate_research_response
import json
from src.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
    search_vector_store
)

pdf = "data/papers/2017_IEEETransonCogDeve.pdf"

pages = extract_pdf(pdf)
cleaned_pages = clean_document(pages)
chunks = chunk_document(cleaned_pages, chunk_size=500)

print(cleaned_pages[0]["text"])
print(f"Total pages : {len(cleaned_pages)}")
print(f"Total chunks: {len(chunks)}")

print("\nFirst Chunk\n")
print(chunks[0])

print("\nLast Chunk\n")
print(chunks[-1])
with open("data/processed/EEGNet_chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write("=" * 100 + "\n")
        f.write(f"Chunk ID: {chunk['chunk_id']} | Page: {chunk['page']}\n")
        f.write("=" * 100 + "\n\n")
        f.write(chunk["text"])
        f.write("\n\n")
   
with open("data/processed/EEGNet.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_pages, f, indent=4, ensure_ascii=False)

with open("data/processed/EEGNet.txt", "w", encoding="utf-8") as f:
    for page in cleaned_pages:
        f.write("=" * 80 + "\n")
        f.write(f"Page {page['page']}\n")
        f.write("=" * 80 + "\n\n")
        f.write(page["text"])
        f.write("\n\n")

from src.embedding import (
    load_embedding_model,
    generate_embeddings
)

model = load_embedding_model()

embedded_chunks = generate_embeddings(chunks, model)

print(f"Total embedded chunks: {len(embedded_chunks)}")

print(embedded_chunks[0]["chunk_id"])
print(embedded_chunks[0]["page"])
print(embedded_chunks[0]["text"][:100])

print(len(embedded_chunks[0]["embedding"]))

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(
    texts,
    convert_to_numpy=True
) """



from src.pdf_loader import extract_pdf
from src.txt_cleaner import clean_document
from src.chunker import chunk_document
from src.embedding import load_embedding_model, generate_embeddings
from src.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
    search_vector_store
)
from typing import List, Dict, Any, Tuple
from src.retrieval import retrieve_chunks
from src.llm import generate_research_response
# -------------------------------------------------
# Step 1 : Extract PDF
# -------------------------------------------------

pdf_path = "data/papers/2019_IEEETransonHaptics.pdf"

pages = extract_pdf(pdf_path)

# -------------------------------------------------
# Step 2 : Clean text
# -------------------------------------------------

clean_pages = clean_document(pages)

# -------------------------------------------------
# Step 3 : Chunking
# -------------------------------------------------

chunks = chunk_document(
    clean_pages,
    chunk_size=500,
    chunk_overlap=100
)

print(f"Total Chunks: {len(chunks)}")

# -------------------------------------------------
# Step 4 : Load embedding model
# -------------------------------------------------

model = load_embedding_model()

# -------------------------------------------------
# Step 5 : Generate embeddings
# -------------------------------------------------

embedded_chunks = generate_embeddings(chunks, model)

# -------------------------------------------------
# Step 6 : Separate embeddings and metadata
# -------------------------------------------------

embeddings = []
metadata = []
for chunk in embedded_chunks:

    embeddings.append(chunk["embedding"])

    metadata.append({
        "chunk_id": chunk["chunk_id"],
        "page": chunk["page"],
        "text": chunk["text"]
    })

# -------------------------------------------------
# Step 7 : Create Vector Store
# -------------------------------------------------

index, metadata_mapping = create_vector_store(
    embeddings,
    metadata
)

print("Vector Store Created")
print("Total vectors:", index.ntotal)

# -------------------------------------------------
# Step 8 : Save
# -------------------------------------------------

save_vector_store(
    index,
    metadata_mapping,
    "data/processed/eeg_vector_store"
)

# -------------------------------------------------
# Step 9 : Load Again
# -------------------------------------------------

index, metadata_mapping = load_vector_store(
    "data/processed/eeg_vector_store"
)

print("Vector Store Loaded")
print("Vectors:", index.ntotal)


# -------------------------------------------------
# Step 10 : User Query
# -------------------------------------------------

query = "What happen in active non assist mode?"

results = retrieve_chunks(query,model, index,metadata_mapping,top_k=5)
print("Sending payload to Groq...")
answer = generate_research_response(query, results)
print("\n--- Assistant Response ---")
print(answer)

# print("\nTop Results\n")

# with open("data/processed/Response.txt", "a", encoding="utf-8") as f:
#     for result in results:
#         f.write("=" * 100 + "\n")
#         f.write(f"Rank : {result['rank']} | Distance : {result['distance_score']:.4f}\n")
#         f.write(f"Chunk ID: {result['metadata']['chunk_id']} | Page: {result['metadata']['page']}\n")
#         f.write(result["metadata"]["text"][:300])
#         f.write("\n\n")

# for result in results:

#     print("-" * 60)

#     print("Rank :", result["rank"],"Distance :", result["distance_score"])
#     print("Chunk ID :", result["metadata"]["chunk_id"],"Page :", result["metadata"]["page"])
#     print(result["metadata"]["text"][:300])



