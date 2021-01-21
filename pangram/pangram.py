import re

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sanitized(text): 
    return re.sub(r'\W+|_|\d+', '', text)

def is_pangram(text):
    normalized = set(sanitized(text).lower() ) 
    alphabet = set(alpha.lower())
    return normalized == alphabet 