import re

def abbreviate(words):
    return ''.join(select_first(word) for word in re.split('\W+', words))

def select_first(word):
    return word[0].upper() + ''.join(letter for letter in word[1:] if letter.isupper()) \
           if (not all(letter.isupper() for letter in word)) else word[0]

