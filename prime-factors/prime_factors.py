def factors(natural_number):
    factors = []
    num = natural_number
    sqrtn = lambda n: int(n ** 0.5)
    for factor in range(2, sqrtn(num) + 1):
        while num % factor == 0:
            num //= factor
            factors.append(factor)
            if num == 1:
                break
    if num != 1:
        factors += [num]
    return factors