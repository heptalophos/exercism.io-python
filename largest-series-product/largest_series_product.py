import re
from functools import reduce

errors = [ 
    "span must not be negative",
    "digits input must only contain digits",
    "span must be smaller than string length"
    ]

def largest_product(series, size):
    if size < 0:
        raise ValueError(errors[0])
    if len(re.sub("[^0-9]+", "", series)) != len(series):
        raise ValueError(errors[1])
    if size > len(series):
        raise ValueError(errors[2])
    slices = [series[i:i + size] for i in range(len(series) - size + 1)]
    slice_vectors = [[d for d in map(int, list(s))] for s in slices]
    products = [reduce (lambda x, y: x * y, v, 1) for v in slice_vectors]
    return max(products)