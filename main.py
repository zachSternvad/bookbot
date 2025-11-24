import sys
from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    print("----BOOKBOT----")
    print(f"Analyzing book fount at {filepath}...")
    
    total_chars = char_count(text)
    total_words = word_count(text)

    print("---Word Count---")
    print(f"Found {total_words} total words")
    
    print("---Character Count---")
    sorted_chars = sort_chars(total_chars)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("---END---")
main()
