def square_root(number: int) -> int:
    if number == 0 or number == 1:
        return number
    root, bit = 0, 1
    # Find the highest bit needed
    while bit * bit <= number:
        bit <<= 1
    bit >>= 1
    while bit != 0:
        temp = root + bit
        if temp * temp <= number:
            root += bit
        bit >>= 1
    # Return -1 if n not a perfect square
    return root if root * root == number else -1

############################################################
# '''
# Function uses approximations of e and of the 
# natural logarithm (nat_log) of the integer input. 
# It then produce a sufficient approximation of sqrt 
# using the exponential identity : 
#    (nth-root of S = e raised to (1/n of ln(S))). 
# '''
# epsilon  = 2.718281828459045
# nat_log  = lambda x: 99999999 * (x ** (1 / 99999999) - 1)
# return epsilon ** (nat_log(number) / 2) // 1
#############################################################

## OR -with better precision, but less fun 🙂- ##
#################################################
# def square_root(number):
#     from math import (e, log, ceil)
#     return ceil(e ** (log(number, e)/2))
#################################################


# OR,if the Analyzer won't allow the use of exponentiation ##
# as in other tracks, or -I don't know- multiplication 😄  ##
#############################################################
# def square_root(number: int) -> int:
# 	min1, max1, sqr = 0, number, 0 
# 	while sqr != number:
# 		mid = (min1 + max1) / 2  
# 		sqr = mid * mid  
# 		if sqr > number:      
# 			max1 = mid
# 		else:          
# 			min1 = mid
# 	return mid
#############################################################