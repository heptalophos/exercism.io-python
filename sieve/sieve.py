def sieve(limit):
    limit += 1
    primes = {}
    for i in range(2, limit):
        primes[i] = True

    for i in primes:
        multiples = range(i, limit, i)
        for m in multiples[1:]:
            primes[m] = False
    
    return [x for x in primes if primes[x] == True]