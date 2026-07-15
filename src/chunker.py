def chunk_document(pages, chunk_size=500,chunk_overlap=10):
    """
    Split each page into fixed-size chunks.

    Parameters
    ----------
    pages : List of dictionaries with keys:
        - page
        - text

    chunk_size : int
        Maximum number of characters per chunk.

    Returns
    -------
    list
        List of chunk dictionaries.
    """

    chunks = []
    chunk_id = 1

    for page in pages:

        page_number = page["page"]
        text = page["text"]
        step = chunk_size - chunk_overlap
        # Split the text into fixed-size chunks
        for start in range(0, len(text), step):

            chunk_text = text[start:start + chunk_size]
            if len(chunk_text) < 100:
                break
            chunks.append({
                "chunk_id": chunk_id,
                "page": page_number,
                "start_char": start,
                "end_char": start + len(chunk_text),
                "text": chunk_text
            })

            chunk_id += 1

    return chunks