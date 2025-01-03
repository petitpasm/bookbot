# This was my primary response

#    def main():
#        with open("books/frankenstein.txt") as f:
#            file_contents = f.read()
#        words = file_contents.split()
#        print(len(words))
#
#
#    main()


# A cleaner way, more programmer I'd say


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("---Begin report of the book---")
    print(f"{num_words} words in this book.")
    counted_letter = get_count_words(text)
    get_report(counted_letter)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_count_words(text):
    lowered_text = text.lower()
    counted_text = {}
    for letter in lowered_text:
        if letter.isalpha():
            if letter in counted_text:
                counted_text[letter] += 1
            else:
                counted_text[letter] = 1
    return counted_text


def get_report(counted_text):
    sorted_character_list = sorted(
        counted_text.items(), key=lambda item: item[1], reverse=True
    )
    for i in range(0, len(sorted_character_list)):
        print(f"You have {sorted_character_list[i][1]} '{sorted_character_list[i][0]}'")


main()
