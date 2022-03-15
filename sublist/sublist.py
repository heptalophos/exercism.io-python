from collections import deque

SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 3, 2, 1, 0

def sublist(l1, l2):
    if l1 == [] and l2:
        return SUBLIST
    if l2 == [] and l1:
        return SUPERLIST
    if len(l1) == len(l2):
        return EQUAL * int(l1 == l2)
    if len(l1) < len(l2):
        sub, sup = l1, l2 
    else:
        sub, sup = l2, l1
    ls = deque([], len(sub))
    try:
        for x in sup:
            ls.append(x)
            if list(ls) == sub:
                return SUBLIST if sub == l1 else SUPERLIST
    except:
        return EQUAL
    finally:
        return UNEQUAL