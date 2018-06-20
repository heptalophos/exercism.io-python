def prime_factors(natural_number):
    factors = []
    for factor in range(2, int(natural_number ** 0.5) + 1):
        while natural_number % factor == 0:
            natural_number //= factor
            factors.append(factor)
            if natural_number == 1:
                break
    if natural_number != 1:
        factors += [natural_number]
    return factors
