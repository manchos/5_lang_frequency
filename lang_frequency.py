import os
import re
from collections import Counter


def load_utf8text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, word_count=10):
    word_list = re.findall(r'(\w+)', text)
    lower_word_list = [word.lower() for word in word_list]
    most_frequent_words = [pair[0] for pair in Counter(lower_word_list).most_common(word_count) if pair[1] > 1]
    return most_frequent_words


if __name__ == '__main__':
    filepath = input('Enter the real path to text file with utf8 encoding:')
    text = load_utf8text(filepath)
    print('10 most frequency words: %s' % get_most_frequent_words(text, 10))

