import random

def private_key(p):
    return random.choice(range(2, p))


def public_key(p, g, private):
    return modexp(g, private, p)


def secret(p, public, private):
    return modexp(public, private, p)


def modexp(base, exp, modulus):
    p = 1
    while exp > 0:
        if exp & 1 == 1:
            p *= base
            p %= modulus
        exp >>= 1
        base *= base
        base %= modulus
    return p