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