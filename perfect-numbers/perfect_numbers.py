def factors(number):
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            yield i 

aliquot = lambda number: sum(factors(number))

def classify(number):
    if (number < 1):
        raise ValueError("Not a natural number")
    if number > aliquot(number):
        return "deficient"
    elif number < aliquot(number):
        return "abundant"
    else:
        return "perfect"
