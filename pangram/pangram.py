import re

dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def normal(text): return re.sub(r'\W+|_|\d+', '', text)

def is_pangram(text):
    return set(normal(text).lower()) == set(dict.lower())
