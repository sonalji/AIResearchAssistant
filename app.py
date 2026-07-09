from src.pdf_loader import extract_pdf


pdf = "data/papers/2017_IEEETransonCogDeve.pdf"

pages = extract_pdf(pdf)


print(f"Total Pages: {len(pages)}")
print(pages[0]["page"])
print(pages[0]["text"][:500])



