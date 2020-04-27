def sum_of_multiples(limit, multiples):
    return sum( set(value 
                    for m in multiples 
                    if not m == 0 
                    for value in range(0, limit, m)))