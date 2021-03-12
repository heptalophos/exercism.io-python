def factors(n):
    yield 1    
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            yield x
            if x ** 2 < n:
                yield n // x

aliquot = lambda n: 0 if n == 1 else sum(factors(n))

def classify(n):
    if (n < 1):
        raise ValueError("Not a natural number")
    if n - aliquot(n) > 0:
        return 'deficient'
    if n - aliquot(n) < 0:
        return 'abundant'
    return 'perfect'