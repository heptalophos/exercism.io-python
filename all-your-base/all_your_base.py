invalid_base = lambda b: b < 2
valid_digits = lambda ds, b: all( 0 <= d < b for d in ds )
number = lambda ds, b: sum( d * b**i 
                            for i, d 
                            in enumerate( ds[::-1] ))
errors = [ "input base must be >= 2", 
           "output base must be >= 2", 
           "all digits must satisfy 0 <= d < input base" ]  

def rebase(input_base, digits, output_base):
    if invalid_base(input_base):
        raise ValueError(errors[0])
    if invalid_base(output_base):
        raise ValueError(errors[1])
    if not valid_digits(digits, input_base):
        raise ValueError(errors[2])
    n = number(digits, input_base)
    if n == 0:
        return [0]
    out_representation = []
    while n != 0:
        n, d = divmod(n, output_base)
        out_representation.insert(0, d)
    return out_representation