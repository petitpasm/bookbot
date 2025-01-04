def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print("Beginning of your book report...")
    words_num = get_word_num(text)
    print("-" * 40)
    print(f"In this book, there is {words_num} words.")
    print(" " * 2)
    characters_num = get_characters_num(text)
    get_report(characters_num)
    print("-" * 40)
    print("End of report.")


def get_book_path(path):
    with open(path) as f:
        book = f.read()
    return book


def get_word_num(text):
    splitted_text = text.split()
    return len(splitted_text)


def get_characters_num(text):
    lowered_text = text.lower()
    splitted_text = lowered_text.split()
    character_count = {}
    for word in splitted_text:
        for character in word:
            if character.isalpha():
                if character in character_count:
                    character_count[character] += 1
                else:
                    character_count[character] = 1
    return sorted(character_count.items(), key=lambda x: x[1], reverse=True)


def get_report(character_dict):
    for i in range(0, len(character_dict)):
        print(
            f"The letter '{character_dict[i][0]}' appears {character_dict[i][1]} times."
        )


main()
