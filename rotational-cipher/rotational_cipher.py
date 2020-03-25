def rotate(text, key):
    return ''.join(rotation(c, key) for c in text)


def rotation(c, k):
    if c.islower():
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    if c.isupper():
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    return c