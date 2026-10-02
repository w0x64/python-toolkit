import os
import pyperclip
from docx import Document

def create_word_document(text):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line.strip())
    return doc

def save_document(doc, filename):
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    doc.save(os.path.join(desktop_path, filename + '.docx'))

def main():
    # Get copied text from clipboard
    copied_text = pyperclip.paste()

    # Create Word document
    doc = create_word_document(copied_text)

    # Ask user for filename
    filename = input("Enter the name for the file (without extension): ")

    # Save the document
    save_document(doc, filename)
    print("Document saved successfully!")

if __name__ == "__main__":
    main()
