from stats import word_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
 #   print(text)
    
    total_words = word_count(text)
    print(f"Found {total_words} total words")

main()
