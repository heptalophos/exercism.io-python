from math import sqrt

square = lambda n: n * n
odd = lambda n: n % 2 != 0
within_range = lambda n1, n2: n1 > n2 > 0
hcd = lambda n1, n2: n1 if n2 == 0 else hcd(n2, n1 % n2)
coprime = lambda n1, n2: hcd(n1, n2) == 1 
parity = lambda n: 'odd' if odd(n) else 'even'


def primitive_triplets(number_in_triplet):
    pass


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return square(a) + square(b) == square(c)
