import os
import random
import string

def generate_password(length, excluded_chars):
    # Define character sets for generating passwords
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Remove any excluded characters from the sets
    if excluded_chars:
        all_chars = ''.join(
            char for char in (uppercase_letters + lowercase_letters + digits + special_chars)
            if char not in excluded_chars
        )
    else:
        all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    # Generate password
    password = ''.join(random.choices(all_chars, k=length))
    
    return password

def write_passwords_to_file(passwords, file_path):
    with open(file_path, 'w') as file:
        for index, password in enumerate(passwords, start=1):
            file.write(f"{index}. {password}\n")

def main():
    # Get user input for password length and number of passwords
    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    
    # Ask for characters to exclude from the password
    excluded_chars = input("Please enter any characters to exclude from creating passwords (e.g., !, *, ., &): ")
    
    # Generate unique passwords
    passwords = set()
    while len(passwords) < num_passwords:
        passwords.add(generate_password(length, excluded_chars))
    
    # Convert set to list to preserve the order for enumeration
    passwords = list(passwords)
    
    # Write passwords to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'generated_passwords.txt')
    write_passwords_to_file(passwords, file_path)
    
    print(f"{num_passwords} unique passwords of length {length} have been generated and saved to {file_path}, excluding '{excluded_chars}'")

if __name__ == "__main__":
    main()
