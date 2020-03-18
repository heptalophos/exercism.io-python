import re

dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def normal(text): 
    return re.sub(r'\W+|_|\d+', '', text)

def is_pangram(text):
    txt = set(normal(text).lower()) 
    dct = set(dict.lower())
    return txt == dct 