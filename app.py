from src.pdf_loader import extract_pdf
from src.txt_cleaner import clean_document
from src.chunker import chunk_document
import json

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
)



