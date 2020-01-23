def distance(x, y):
    if len(x) != len(y) : 
        raise ValueError('DNA strands must be of equal length.')
    return sum(c1 != c2 for c1, c2 in zip(x, y))