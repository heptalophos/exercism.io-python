def rotate(text, key):
    return ''.join(shift(ch, key) for ch in text)


def shift(c, k):
    if c.islower():
        return chr((diff(c, 'a') + k) % 26 + ord('a'))
    if c.isupper():
        return chr((diff(c, 'A') + k) % 26 + ord('A'))
    return c

# Auxiliary
diff = lambda c1, c2: ord(c1) - ord(c2)