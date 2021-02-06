from string import ascii_lowercase as al

translation = lambda t : \
    t.translate(str.maketrans(al, al[::-1]))

def encode(plain_text):
    normalized = [c for c in plain_text 
                    if c.isalnum()]
    enc = translation(''.join(normalized).lower())
    return " ".join([enc[i:i + 5] 
                    for i in range(0, len(enc), 5)])

def decode(cipher_text):
    normalized = [c for c in cipher_text 
                    if c.isalnum()]
    return translation(''.join(normalized).lower())