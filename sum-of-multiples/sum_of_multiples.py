def sum_of_multiples(limit, multiples):
    return sum(
            set(x for m in multiples 
                  if not m == 0
                  for x in range(0, limit, m)))