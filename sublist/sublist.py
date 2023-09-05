SUPERLIST, EQUAL, SUBLIST, UNEQUAL = 3, 2, 1, 0

def swapper(func):
    """Wrapper that ensures the first argument is smaller then the seconds"""
    def swap(first, second):
        """swaps first and second argument if the second is smaller"""
        if first == second:
            return 2
        if len(first) > len(second):
            return SUPERLIST * func(second, first)
        else:
            return func(first, second)
    return swap

@swapper
def sublist(small_list, big_list):
    """Checks if first list is a sublist of the seconds"""
    for i in range(len(big_list) - len(small_list) + 1):
        if small_list == big_list[i: i+len(small_list)]:
            return SUBLIST
    return UNEQUAL