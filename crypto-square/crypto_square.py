from string import whitespace, punctuation
from itertools import zip_longest

def cipher_text(plain_text):
    sanitized, othercharacters = '', whitespace + punctuation
    chunkify = lambda n, ls: zip_longest(*[iter(ls)] * n, fillvalue=' ')
    transpose = lambda m: zip(*m)
    for character in plain_text.casefold().strip():
        if character in othercharacters:
            continue
        sanitized += character
    if not sanitized:
        return ''
    sq_side = int(-1 * (len(sanitized) ** 0.5) // 1 * -1)
    rows = chunkify(sq_side, sanitized)
    return ' '.join(''.join(c) for c in transpose(rows))