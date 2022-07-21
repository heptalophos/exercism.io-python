def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    _steps = 0
    while number != 1:
        if number % 2:
            number *= 3
            number += 1
        else:
            number >>= 1
        _steps += 1
    return _steps