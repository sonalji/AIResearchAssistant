import fitz

def extract_pdf(pdf_path):
    document = fitz.open(pdf_path)
    pages=[]
    #text = ""

    #for page in document:
    #    text += page.get_text()
    for page_num, page in enumerate(document, start=1):
        pages.append({
            "document": os.path.basename(pdf_path),
            "page": page_num,
            "text": page.get_text()
        })

    document.close()

    return pages