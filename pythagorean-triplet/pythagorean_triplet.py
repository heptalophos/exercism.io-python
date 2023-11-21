def triplets_with_sum(number):
    triplets = []
    a = b = c = 0 
    m = 2
    while a + b + c <= 6 * number:
        for n in range(1, m):
            a = square(m) - square(n)
            b = 2 * m * n
            c = square(m) + square(n)
            if coprime(a, b) and  number % (a + b + c) == 0:
                if within_range(a, b):
                    a, b = b, a
                triplet = list(map(
                        lambda x: x * (number // (a + b + c)), 
                        [a, b, c]))
                if not triplet in triplets:
                    triplets.append(triplet)
        m += 1
    return triplets

# Helpers
square = lambda n: n * n
odd = lambda n: n % 2 != 0
within_range = lambda n1, n2: n1 > n2 > 0
hcd = lambda n1, n2: n1 if n2 == 0 else hcd(n2, n1 % n2)
coprime = lambda n1, n2: hcd(n1, n2) == 1 
# parity = lambda n: 'odd' if odd(n) else 'even'
# euclidean_conditions = lambda x, y: \
#     within_range(x, y) and coprime(x, y) and parity(x) != parity(y)