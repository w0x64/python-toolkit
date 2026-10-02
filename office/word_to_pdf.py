import os
import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

def convert_to_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if not file_path:
        print("No file selected. Exiting...")
        return

    # Convert the selected DOCX file to PDF
    pdf_file_path = os.path.join(os.path.expanduser("~"), "Desktop", os.path.basename(file_path)[:-5] + ".pdf")
    convert(file_path, pdf_file_path)
    print(f"Conversion complete. PDF saved to {pdf_file_path}")

if __name__ == "__main__":
    convert_to_pdf()
