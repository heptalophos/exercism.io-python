import re
from functools import reduce

def largest_product(series, size):
    
    if size < 0:
        raise ValueError("Series size cannot be negative")
    
    if len(re.sub("[^0-9]+", "", series)) != len(series):
        raise ValueError("String should contain only digits")
    
    if size > len(series):
        raise ValueError("Series size cannot be larger than containing string's length")

    partitions = [series[i:i + size] for i in range(len(series) - size + 1)]
    lists_of_size  = [[lst for lst in map(int, list(s))] for s in partitions]
    return max([reduce (lambda x, y: x * y, n, 1) for n in lists_of_size])

