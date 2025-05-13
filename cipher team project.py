import re
import argparse

def get_original_text():
    file_path = "input.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def get_shift_amount():
    parser = argparse.ArgumentParser(description="Caesar cipher shift amount.")
    parser.add_argument(
        "--shift", type=int, required=True,
        help="Integer shift amount for Caesar cipher"
    )
    args = parser.parse_args()
    return args.shift

def remove_nonletters(input_text):
    return re.sub(r'[^a-zA-Z]+', '', input_text)

def cipher(text, shift_amount):
    result = ""
    count = 0

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + shift_amount) % 26
                result += chr(ord('a') + shifted)
            else:  # uppercase
                shifted = (ord(char) - ord('A') + shift_amount) % 26
                result += chr(ord('A') + shifted)
            count += 1
            if count % 5 == 0:
                result += " "

    return result.strip()

def decipher(text, shift_amount):
    deciphered = cipher(text, -shift_amount)
    clean_text = deciphered.replace(" ", "")
    return clean_text

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'{cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'{decipher_text=}')
