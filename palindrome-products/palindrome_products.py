def pairs(n, minf, maxf):
    for i in range(minf, maxf + 1):
        if n % i == 0:
            if minf <= i <= n // i <= maxf:
                yield i, n // i

def first(minf, maxf, direction):
    if minf > maxf: 
        raise ValueError("Invalid range.")
    palindrome = lambda x : str(x) == str(x)[::-1]
    possible = range(minf ** 2, maxf ** 2 + 1)
    if direction == -1:
        possible = range(maxf ** 2, minf ** 2 + 1, -1)
    for p in filter(palindrome, possible):
        for i in range(minf, maxf + 1):
            if p % i == 0 and minf <= p // i <= maxf:
                return p, pairs(p, minf, maxf)
    return None, []

def smallest(min_factor, max_factor):
    return first(min_factor, max_factor, 1)

def largest(min_factor, max_factor):
    return first(min_factor, max_factor, -1)