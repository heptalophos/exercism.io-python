import re
from functools import reduce

errors = [ 
    "Series size cannot be negative",
    "String should contain only digits",
    "Series size cannot be larger than containing string's length"
    ]

def largest_product(series, size):
    
    if size < 0:
        raise ValueError(errors[0])
    
    if len(re.sub("[^0-9]+", "", series)) != len(series):
        raise ValueError(errors[1])
    
    if size > len(series):
        raise ValueError(errors[2])

    slices = [series[i:i + size] 
              for i in range(len(series) - size + 1)]
    prods  = [[prods 
              for prods in map(int, list(s))] 
              for s in slices]
    return max([reduce (lambda x, y: x * y, n, 1) 
                for n in prods])