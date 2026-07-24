import numpy as np
import faiss
from typing import List, Dict, Any, Tuple
import json

#    Creates a FAISS index, adds vector embeddings, and maps them to metadata.
def create_vector_store(
    embeddings: List[List[float]], 
    metadata_list: List[Dict[str, Any]]
) -> Tuple[faiss.IndexFlatIP, Dict[int, Dict[str, Any]]]:
    
    # Create a FAISS index
    #1. Convert embeddings into a 2D float32 NumPy array (Required by FAISS)
    embeddings_array = np.array(embeddings).astype('float32')
    #2. Get the vector dimension size
    d = len(embeddings[0])  # Dimension of the vectors
    # 3. Initialize a flat IP (Inner Product) FAISS index
    index = faiss.IndexFlatIP(d)

    # 4. Add the embeddings to the index
    index.add(embeddings_array)

    # Create a mapping from indices to metadata
    index_to_metadata = {i: metadata_list[i] for i in range(len(metadata_list))}

    return index, index_to_metadata


def save_vector_store( index: faiss.Index, 
    metadata: Dict[int, Dict[str, Any]], 
    base_filename: str
) -> None:
    # Placeholder for saving the FAISS index and metadata mapping to disk
    # 1. Define file paths for both index and metadata
    index_path = f"{base_filename}.faiss"
    metadata_path = f"{base_filename}_metadata.json"
    
    # 2. Save the FAISS index using native binary writer
    faiss.write_index(index, index_path)
    # 3. Standardize metadata keys to strings for valid JSON formatting
    # (JSON keys must be strings, whereas FAISS lookups use integer IDs)
    stringified_metadata = {str(key): value for key, value in metadata.items()}
    
    # 4. Write metadata to disk as a JSON file
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(stringified_metadata, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully saved FAISS index to: {index_path}")
    print(f"Successfully saved metadata to: {metadata_path}")

def load_vector_store(base_filename: str) -> Tuple[faiss.Index, Dict[int, Dict[str, Any]]]:
        # Placeholder for loading the FAISS index and metadata mapping from disk
        # 1. Define file paths for both index and metadata
        index_path = f"{base_filename}.faiss"
        metadata_path = f"{base_filename}_metadata.json"
        
        # 2. Load the FAISS index from disk
        index = faiss.read_index(index_path)
        
        # 3. Load the metadata from disk
        with open(metadata_path, 'r', encoding='utf-8') as f:
            stringified_metadata = json.load(f)
        
        # 4. Convert string keys back to integers for proper indexing
        metadata = {int(key): value for key, value in stringified_metadata.items()}
        
        print(f"Successfully loaded FAISS index from: {index_path}")
        print(f"Successfully loaded metadata from: {metadata_path}")
        
        return index, metadata
def search_vector_store(
    query_embedding: List[float], 
    index: faiss.Index, 
    metadata: Dict[int, Dict[str, Any]], 
    top_k: int = 10
) -> List[Dict[str, Any]]:
    # Searches a FAISS index for the most similar chunks and maps results to metadata.
     # 1. Format the single query vector into a 2D float32 NumPy array
    query_np = np.array([query_embedding], dtype="float32")
    
    # 2. Limit top_k if the index contains fewer total items
    k = min(top_k, index.ntotal)
    if k == 0:
        return []
    
    # 3. Query the index (returns distances and corresponding internal integer IDs)
    distances, ids = index.search(query_np, k)
    # 4. Compile the ranked results
    results = []
    for rank in range(k):
        vector_id = int(ids[0][rank])
        
        # FAISS returns -1 if it cannot find enough valid neighbors
        if vector_id == -1:
            continue
            
        # Extract distance score and cross-reference the item's metadata
        score = float(distances[0][rank])
        chunk_metadata = metadata.get(vector_id, {"error": "Metadata missing"})
        
        results.append({
            "rank": rank + 1,
            "vector_id": vector_id,
            "distance_score": score,
            "metadata": chunk_metadata
        })
        
    return results
