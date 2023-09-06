SUPERLIST, EQUAL, SUBLIST, UNEQUAL = 3, 2, 1, 0

def swapper(func):
    """Wrapper that ensures the first argument 
       is smaller then the second"""
    def swap(first, second):
        """swaps first and second argument 
           if the second is smaller"""
        if first == second:
            return EQUAL
        if len(first) > len(second):
            return SUPERLIST * func(second, first)
        else:
            return func(first, second)
    return swap

@swapper
def sublist(sub, sup):
    for i in range(len(sup) - len(sub) + 1):
        if sub == sup[i:i + len(sub)]:
            return SUBLIST
    return UNEQUAL