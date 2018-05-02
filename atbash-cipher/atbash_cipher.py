from string import ascii_lowercase

translation = lambda text: text.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))

def encode(plain_text):
    # plain_text = sub(r'\W', '', plain_text)
    cipher = translation(''.join([c for c in plain_text if c.isalnum()]).lower())
    return " ".join([cipher[i:i + 5] for i in range(0, len(cipher), 5)])

def decode(ciphered_text):
    return translation(''.join([c for c in ciphered_text if c.isalnum()]).lower())