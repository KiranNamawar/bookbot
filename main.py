import sys
from stats import count_words, count_unique_chars, sort_chars


def get_book_text(path):
    content = None
    with open(path) as file:
        content = file.read()
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frankenstain = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(frankenstain)} total words")
    print("--------- Character Count -------")
    chars_count = count_unique_chars(frankenstain)
    for item in sort_chars(chars_count):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
