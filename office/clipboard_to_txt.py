import os
import pyperclip
import re

def save_text_file(text, filename):
    # Get the desktop path
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    # Full path for the file
    full_path = os.path.join(desktop_path, filename + '.txt')
    # Open the file and write text
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(text)

def preprocess_text(text):
    # Replace multiple spaces with a single space in each line
    text = '\n'.join(re.sub(r'\s+', ' ', line.strip()) for line in text.split('\n'))
    return text

def main():
    # Get copied text from clipboard
    copied_text = pyperclip.paste()
    
    # Preprocess the text to clean up within lines but preserve line breaks
    processed_text = preprocess_text(copied_text)

    # Ask user for filename
    filename = input("Enter the name for the file (without extension): ")

    # Save the text to a .txt file
    save_text_file(processed_text, filename)
    print("Text file saved successfully!")

if __name__ == "__main__":
    main()
