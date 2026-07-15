from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    """
    Load and return the sentence embedding model.
    """
    print(f"Loading embedding model: {model_name}")
    model = SentenceTransformer(model_name)
    print("Embedding model loaded successfully.")

    return model
def generate_embeddings(chunks, model):
    """
    Generate embeddings for each text chunk.
    """

    embedded_chunks = []

    for chunk in chunks:

        embedding = model.encode(
            chunk["text"],
            convert_to_numpy=True
        )

        embedded_chunks.append({
            "chunk_id": chunk["chunk_id"],
            "page": chunk["page"],
            "text": chunk["text"],
            "embedding": embedding.tolist()
        })

    return embedded_chunks
