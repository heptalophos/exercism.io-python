def sieve(limit):
    
    non_primes = set()
    primes = []
    if limit == 1:
        return []
    
    primes.append(2)

    for i in range(3, limit+1, 2):
        if i not in non_primes:
            primes.append(i)
            non_primes.update(range(i**2, limit, i))
    return primes       