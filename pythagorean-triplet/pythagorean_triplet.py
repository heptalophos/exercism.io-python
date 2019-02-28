def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2:
        raise ValueError('Side should be an even integer')
    triplets = set()
    for m in range(1, number_in_triplet//2 + 2):
        for n in range(1, m+2):
            if (number_in_triplet == 2*m*n ) and euclidean_conditions(m, n):
                possible = [square(m) - square(n), number_in_triplet, square(m) + square(n)]
                if is_triplet(tuple(sorted(possible))):
                    triplets.add(tuple(sorted(possible)))
    return triplets


def triplets_in_range(range_start, range_end):
    triplets = set()
    for x in range(range_start, range_end + 1):
        for y in range(x + 1, range_end + 1):
            for z in range(y + 1, range_end + 1):
                if is_triplet((x, y, z)):
                    triplets.add(tuple(sorted((x, y, z))))
    return triplets



def is_triplet(triplet):
    return sum([square(x) for x in triplet if x != max(triplet)]) == square(max(triplet))


# Helpers

square = lambda n: n * n
odd = lambda n: n % 2 != 0
within_range = lambda n1, n2: n1 > n2 > 0
hcd = lambda n1, n2: n1 if n2 == 0 else hcd(n2, n1 % n2)
coprime = lambda n1, n2: hcd(n1, n2) == 1 
parity = lambda n: 'odd' if odd(n) else 'even'
euclidean_conditions = lambda x, y: within_range(x, y) and coprime(x, y) and parity(x) != parity(y)