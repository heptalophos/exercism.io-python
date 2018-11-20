SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 3, 2, 1, 0


def check_lists(first, second):
    if first == [] and second:
        return SUBLIST
    if second == [] and first:
        return SUPERLIST 
    if first == second:
        return EQUAL
    first, second = ''.join(map(str, first)), ''.join(map(str, second))
    if second.find(first) > -1:
        return SUBLIST
    if first.find(second) > -1:
        return SUPERLIST
    return UNEQUAL
