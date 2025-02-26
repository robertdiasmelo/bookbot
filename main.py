import sys
from stats import get_number_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_number_words(text)
    num_characters = get_number_characters(text)

    print_report(book_path, num_words, num_characters)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_characters(text):
    lowered_text = text.lower()
    characters_number = {}
    for character in lowered_text:
        if character in characters_number:
            characters_number[character] += 1
        else:
            characters_number[character] = 1
    return characters_number


def print_report(path, num_words, num_characters):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    print()

    number_characters_list = chars_dict_to_sorted_list(num_characters)
    
    for character_num_dict in number_characters_list:
        if character_num_dict["character"].isalpha():
            print(f"'{character_num_dict["character"]}: {character_num_dict["num"]}' ")
        else:
            continue
    print("--- End report ---")


def chars_dict_to_sorted_list(my_dict):
    my_list = []
    for letter, number in my_dict.items():
        my_list.append({"character": letter, "num": number})
    my_list.sort(reverse=True, key=sort_on)
    return my_list


def sort_on(dict):
    return dict["num"]


main()
