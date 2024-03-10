def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_chars_dict_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in document")
    print(" ")
    for item in chars_sorted_list:
        if item["name"].isalpha():
            print(f"The '{item['name']}' character was found {item['count']} times")


def get_chars_dict_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"name": char, "count": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["count"]


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
