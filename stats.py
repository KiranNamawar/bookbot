def count_words(content):
    words = content.split()
    return len(words)


def count_unique_chars(content):
    chars = list(content)
    count = {}
    for char in chars:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count


def sort_on(item):
    return item["num"]


def sort_chars(count_dict):
    char_counts = list()
    for char, count in count_dict.items():
        char_dict = {"char": char, "num": count}
        char_counts.append(char_dict)

    char_counts.sort(key=sort_on, reverse=True)
    return char_counts
