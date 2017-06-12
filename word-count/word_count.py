import re, functools

def just_words(input):
    return re.sub(r"[^a-zA-Z0-9]+", " ", input).lower()

def word_count(list):
    return functools.reduce( lambda x, y: x.update([(y, x.get(y,0)+1)]) or x, just_words(list).split(), {})