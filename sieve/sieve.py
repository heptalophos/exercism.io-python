def primes(limit):
    limit += 1
    factors = [False for _ in range(limit)]
    factors[0:1] = [True, True]
    for s in range(2, limit):
        if  not factors[s]:
            for i in range(2*s, limit, s):
                factors[i] = True
    sieve = []
    for i in range(2, limit):
        if not factors[i]:
            sieve.append(i)
    return sieve