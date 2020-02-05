import re, functools

def count_words(phrase):
    phrase = re.sub(r'_', ' ', phrase)
    words = []
    for matched in re.finditer(r'\d+|\w+(\'\w+)?', phrase):
        words.append(matched.group().strip("'").lower())
    return functools.reduce(lambda x, y : 
                            x.update([(y, x.get(y,0) + 1)]) or x, 
                            words,
                            {})