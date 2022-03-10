import re

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sanitized(text): 
    return re.sub(r'\W+|_|\d+', '', text)

def is_pangram(text):
    text_letters = set( sanitized(text).lower() ) 
    alphabet = set( ALPHABET.lower() )
    return text_letters == alphabet 