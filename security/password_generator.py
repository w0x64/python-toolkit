import random
import string
import os
from pathlib import Path

def generate_password(length, use_numbers, use_symbols, custom_words):
    base_characters = string.ascii_letters
    if use_numbers:
        base_characters += string.digits
    if use_symbols:
        base_characters += string.punctuation

    if not base_characters:
        raise ValueError("Character set is empty. Enable numbers, symbols, or both.")

    # Ensure stronger randomness by using SystemRandom
    secure_random = random.SystemRandom()

    password = ''.join(secure_random.choice(base_characters) for _ in range(length))

    if custom_words:
        # Mix multiple custom words randomly into the password
        for word in custom_words:
            insert_at = secure_random.randint(0, len(password))
            password = password[:insert_at] + word + password[insert_at:]

    # Final shuffle for extra randomness
    password_list = list(password)
    secure_random.shuffle(password_list)
    return ''.join(password_list)

def get_user_input(prompt, valid_responses=None):
    while True:
        response = input(prompt).strip().lower()
        if not valid_responses or response in valid_responses:
            return response
        print("Invalid input. Please try again.")

def main():
    print("\n=== Secure Password Generator ===\n")
    try:
        length = int(input("Enter desired password length (minimum 8 recommended): "))
        count = int(input("Enter number of passwords to generate: "))

        use_numbers = get_user_input("Include numbers? (y/n): ", ['y', 'n']) == 'y'
        use_symbols = get_user_input("Include symbols? (y/n): ", ['y', 'n']) == 'y'

        custom_words = []
        if get_user_input("Would you like to add custom words? (y/n): ", ['y', 'n']) == 'y':
            words_input = input("Enter words separated by commas: ")
            custom_words = [word.strip() for word in words_input.split(',') if word.strip()]

        passwords = [generate_password(length, use_numbers, use_symbols, custom_words) for _ in range(count)]

        print("\nGenerated Passwords:")
        for idx, pwd in enumerate(passwords, 1):
            print(f"{idx}: {pwd}")

        if get_user_input("\nWould you like to save these passwords to your Desktop? (y/n): ", ['y', 'n']) == 'y':
            desktop = Path.home() / 'Desktop'
            file_path = desktop / 'generated_passwords.txt'
            with open(file_path, 'w') as file:
                for pwd in passwords:
                    file.write(pwd + '\n')
            print(f"\nPasswords successfully saved to {file_path}")

    except ValueError as e:
        print(f"\nError: {e}\nPlease restart and enter valid numeric values.")

if __name__ == "__main__":
    main()
