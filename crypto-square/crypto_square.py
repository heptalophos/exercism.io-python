from string import whitespace, punctuation
from itertools import zip_longest
from math import ceil, sqrt

def cipher_text(plain_text):
    othercharacters = whitespace + punctuation
    lower_plain, sanitized = plain_text.casefold().strip(), ''
    chunks = lambda n, ls: zip_longest(*[iter(ls)] * n, 
                                       fillvalue=' ')
    transpose = lambda m: zip(*m)
    for ch in lower_plain:
        if ch in othercharacters:
            continue
        sanitized += ch
    if not sanitized:
        return ""
    sq_side = ceil(sqrt(len(sanitized)))
    rows = chunks(sq_side, sanitized)
    return ' '.join(''.join(c) for c in transpose(rows))