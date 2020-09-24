def pfactors(number):
    if number == 1:
        yield 1
        return
    for i in range(2, number + 1):
        if number % i == 0:
            yield i 
            yield from pfactors(number // k)
                 
def aliquot(number):
    return number == sum(pfactors(number))

def classify(number):
    if (number < 1):
        raise ValueError("Not a natural")
    return "abundant" if aliquot(number) > number \
            else "perfect" if aliquot(number) == number \
            else "deficient"
