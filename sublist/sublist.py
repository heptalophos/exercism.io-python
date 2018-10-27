SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 3, 2, 1, 0

def check_lists(first_list, second_list):
    if first_list == [] and second_list:
        return SUBLIST
    if second_list == [] and first_list:
        return SUPERLIST 
    if first_list == second_list:
        return EQUAL
    first_list, second_list = ''.join(map(str, first_list)), ''.join(map(str, second_list))
    if second_list.find(first_list) > -1:
        return SUBLIST
    if first_list.find(second_list) > -1:
        return SUPERLIST
    return UNEQUAL
