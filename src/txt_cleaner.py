import re


def clean_text(text):
    """
    Clean text extracted from a PDF page.

    Parameters
    ----------
    text : str
        Raw text extracted from a PDF page.

    Returns
    -------
    str
        Cleaned text.
    """

    # Remove leading and trailing whitespace
    text = text.strip()

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace 3 or more consecutive newlines with 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def clean_document(pages):
    """
    Clean all pages in a document.

    Parameters
    ----------
    pages : list
        List of dictionaries returned by extract_pdf().

    Returns
    -------
    list
        Cleaned pages.
    """

    cleaned_pages = []

    for page in pages:
        cleaned_pages.append({
            "page": page["page"],
            "text": clean_text(page["text"])
        })

    return cleaned_pages