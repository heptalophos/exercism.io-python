import re

dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def normal(text): 
    return re.sub(r'\W+|_|\d+', '', text)

def is_pangram(text):
    normalized = set( normal(text).lower() ) 
    alphabet = set( dict.lower() )
    return normalized == alphabet 