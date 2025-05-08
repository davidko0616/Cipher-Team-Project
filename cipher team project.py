import re

def get_original_text():
    file_path = "input.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return ""

def get_shift_amount():
    parser = argparse.ArgumentParser(description="Caesar cipher shift amount.")
    parser.add_argument(
        "--shift", type=int, required=True,
        help="Integer shift amount for Caesar cipher"
    )
    args = parser.parse_args()
    return args.shift

def remove_nonletters(input_text):
    removed_letter = re.sub(r'\W+', '', input_text)
    return removed_letter

def cipher(text, shift_amount):
    return 'zxvc'

def decipher(text, shift_amount):
    return 'asdf'

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'{cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'{decipher_text=}')
