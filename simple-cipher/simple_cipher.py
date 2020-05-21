import random
import string

alphabet = string.ascii_lowercase

class Cipher(object):

    def random_key():
        return "".join([chr(ord('a') + random.randint(0, 25)) 
                        for _ in range(100)])

    def __init__(self, key=random_key()):
        self.key = key

    def encode(self, text):
        return "".join(
            alphabet[(alphabet.index(text[i]) + 
                      alphabet.index(self.key[i % len(self.key)])) % 26] 
            for i in range(len(text)))

    def decode(self, text):
        return "".join(
            alphabet[(alphabet.index(text[i]) - 
                      alphabet.index(self.key[i % len(self.key)])) % 26] 
            for i in range(len(text)))
