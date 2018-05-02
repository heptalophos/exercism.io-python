def sieve(limit):
    limit += 1
    factors = [False for _ in range(limit)]
    factors[0:1] = [True, True]
    for s in range(2, limit):
        if  not factors[s]:
            for i in range(2*s, limit, s):
                factors[i] = True
    primes = []
    for i in range(2, limit):
        if not factors[i]:
            primes.append(i)
    return primes