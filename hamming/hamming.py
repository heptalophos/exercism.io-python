def distance(strand1, strand2):
    if len(strand1) != len(strand2) : 
        raise ValueError('Strands must be of equal length.')
    return sum(c1 != c2 for c1, c2 in zip(strand1, strand2))