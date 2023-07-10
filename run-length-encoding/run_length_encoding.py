from re import sub
from itertools import groupby

def decode(text):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), text)

def encode(text):
   return ''.join(x if cnt <= 1 else "%d%s" % (cnt, x) 
                    for x, cnt 
                    in map(lambda x: (x[0], len(list(x[1]))), groupby(text)))