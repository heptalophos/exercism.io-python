def factors(natural_number):
    factors = []
    number = natural_number
    for factor in range(2, int(number ** 0.5) + 1):
        while number % factor == 0:
            number //= factor
            factors += [factor]
            if number == 1:
                break
    if number != 1:
        factors += [number]
    return factors