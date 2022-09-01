def square_of_sum(count):
    return sum( i for i in range(count + 1) ) ** 2

def sum_of_squares(count):
    return sum( i**2 for i in range(count + 1) )

def difference_of_squares(count):
    return square_of_sum(count) - sum_of_squares(count)