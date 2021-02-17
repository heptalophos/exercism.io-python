import functools

ERROR = "Invalid input. Range is (1, 64)"

def square(integer_number):
    if valid_input(integer_number):
        return 1 << integer_number - 1
    else:
        raise ValueError(ERROR)

def total():
    return (1 << 64) - 1

def valid_input(integer_number):
    if (integer_number < 1) or (integer_number > 64):
        return False
    return True