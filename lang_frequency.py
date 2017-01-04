import os
import re
from collections import Counter


def load_utf8text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'(\w+)', text)
    return [pair[0] for pair in Counter(words).most_common(10)]


if __name__ == '__main__':
    filepath = input('Enter the real path to text file with utf8 encoding:')
    text = load_utf8text(filepath)
    print('10 most frequency words: %s' % get_most_frequent_words(text))

