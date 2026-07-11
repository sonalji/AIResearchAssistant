from src.pdf_loader import extract_pdf
import json

pdf = "data/papers/2017_IEEETransonCogDeve.pdf"

pages = extract_pdf(pdf)


print(f"Total Pages: {len(pages)}")
print(pages[0]["page"])
print(pages[0]["text"][:500])

with open("data/processed/EEGNet.json", "w", encoding="utf-8") as f:
    json.dump(pages, f, indent=4, ensure_ascii=False)



