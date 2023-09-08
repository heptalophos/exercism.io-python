SUPERLIST, EQUAL, SUBLIST, UNEQUAL = 3, 2, 1, 0

def flip_args(func):
    def flip(first, second):
        if first == second:
            return 2
        if len(first) >= len(second):
            return 3 * func(second, first)
        else:
            return func(first, second)
    return flip

@flip_args
def sublist(sub, sup):
    for i in range(len(sup) - len(sub) + 1):
        if sub == sup[i:i + len(sub)]:
            return 1
    return 0