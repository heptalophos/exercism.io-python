import functools

def on_square(integer_number):
    if valid_input(integer_number):
        return 2 ** (integer_number - 1)
    else:
        raise ValueError("Invalid input. Range is (1, 64)")

def total_after(integer_number):
    if valid_input(integer_number):
        return sum(map(on_square, range(1, integer_number + 1)))
    else:
        raise ValueError("Invalid input. Range is (1, 64)")

def valid_input(integer_number):
    if (integer_number < 1) or (integer_number > 64):
        return False
    return True