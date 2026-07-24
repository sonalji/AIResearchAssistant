import faiss
import json
from typing import List, Dict, Any, Tuple
from src.vector_store import search_vector_store

def embed_query(query, model):
    # Question and embedding
    query_embedding = model.encode(query, convert_to_numpy=True).tolist()
    return query_embedding


def retrieve_chunks(query,model,index,metadata,top_k=3):
    # Embed the query
    query_embedding = embed_query(query, model)

    # Search the vector store
    results = search_vector_store(
        query_embedding,
        index,
        metadata,
        top_k=top_k
    )
    
    return results