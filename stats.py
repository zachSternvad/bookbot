def word_count(text):
    return len(text.split())

def char_count(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
 
def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_by_count(item):
        return item["num"]

    char_list.sort(key=sort_by_count, reverse=True)
    return char_list
