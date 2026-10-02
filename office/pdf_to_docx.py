import os
import re
from pdfminer.high_level import extract_text
from docx import Document

def clean_text_for_docx(text):
    """
    Remove characters that are invalid in XML (for python-docx)
    """
    # Remove NULL bytes and other control characters except newline and tab
    return re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f]', '', text)

def pdf_to_docx():
    current_dir = os.getcwd()

    for file_name in os.listdir(current_dir):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(current_dir, file_name)
            docx_path = os.path.join(current_dir, os.path.splitext(file_name)[0] + ".docx")

            # Extract text from PDF
            raw_text = extract_text(pdf_path)
            text = clean_text_for_docx(raw_text)

            # Create a new Word document
            doc = Document()
            for line in text.split('\n'):
                doc.add_paragraph(line)

            # Save as DOCX
            doc.save(docx_path)
            print(f"Converted: {file_name} -> {os.path.basename(docx_path)}")

def main():
    pdf_to_docx()
    print("All PDF files have been converted to DOCX.")

if __name__ == "__main__":
    main()
