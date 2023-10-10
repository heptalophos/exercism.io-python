def square_root(number):
    epsilon = 2.718281828459045
    natlog = lambda x: 99999999 * (x ** (1 / 99999999) - 1)
    return (epsilon ** (natlog(number) / 2)) // 1


################## OR: #########################
# def square_root(number):
#     from math import (e, log, ceil)
#     return ceil(e ** (log(number, e)/2))
################################################
