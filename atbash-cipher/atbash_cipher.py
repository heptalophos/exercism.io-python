from string import ascii_lowercase as al

translation = lambda t : t.translate(str.maketrans(al, al[::-1]))

def encode(plain_text):
    enc = translation(''.join([c for c in plain_text 
                                 if c.isalnum()]).lower())
    return " ".join([enc[i:i + 5] 
                    for i in range(0, len(enc), 5)])

def decode(cipher_text):
    return translation(''.join([c for c in cipher_text 
                                if c.isalnum()]).lower())