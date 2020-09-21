def palindrome(n):
    return str(n) == str(n)[::-1]

def pairs(n, minf, maxf):
    for i in range(minf, maxf + 1):
        if n % i == 0:
            if minf <= i <= n // i <= maxf:
                yield i, n // i

def first(minf, maxf, dir):
    if dir != -1:
        possible = range(minf ** 2, maxf ** 2 + 1)
    else:
        possible = range(maxf ** 2, minf ** 2 + 1, -1)
    for p in filter(palindrome, possible):
        for i in range(minf, maxf + 1):
            if p % i == 0 and minf <= p // i <= maxf:
                return p, pairs(p, minf, maxf)
    return None, []

def smallest(min_factor, max_factor):
    if min_factor > max_factor: 
        raise ValueError("Invalid range.")
    return first(min_factor, max_factor, 1)

def largest(min_factor, max_factor):
    if min_factor > max_factor: 
        raise ValueError("Invalid range.")
    return first(min_factor, max_factor, -1)