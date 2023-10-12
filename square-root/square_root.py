def square_root(number: int) -> int:
    '''
    Function uses approximations of e, to 15 significant places (epsilon) and 
    of the natural logarithm (nat_log) of the integer input to approximate its 
    square root using the root-computing formula: 
        (nth-root of S = e raised to (1/n of ln(S))).
    It then returns the integer part of the formula's output. 

    '''
    epsilon  = 2.718281828459045
    nat_log  = lambda x: 99999999 * (x ** (1 / 99999999) - 1)
    return epsilon ** (0.5 * nat_log(number)) // 1


## OR -with better precision, but less fun 🙂- ##
#################################################
# def square_root(number):
#     from math import (e, log, ceil)
#     return ceil(e ** (log(number, e)/2))
#################################################
