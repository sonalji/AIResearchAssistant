def chunk_document(pages, chunk_size=800,chunk_overlap=150):
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
            if start != 0:
                while start < len(text) and not text[start].isspace():
                    start += 1

            end = min(start + chunk_size, len(text))

            # Don't end in the middle of a word
            while end < len(text) and not text[end].isspace():
                end += 1

            chunk_text = text[start:end]
            if len(chunk_text) < 100:
                break
            chunks.append({
                "chunk_id": chunk_id,
                "page": page_number,
                "start_char": start,
                "end_char": end,
                "text": chunk_text
            })

            chunk_id += 1

    return chunks