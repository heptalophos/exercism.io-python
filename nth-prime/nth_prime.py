def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes, candidate = [2], 3
    while len(primes) < number:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 2 
    return primes[-1]