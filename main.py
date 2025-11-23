def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print(text)

main()
