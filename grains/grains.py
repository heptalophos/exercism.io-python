def valid_input(integer_number):
    if (integer_number < 1):
        return False
    if (integer_number > 64):
        return False
    return True

ERROR = "square must be between 1 and 64"

def square(integer_number):
    if valid_input(integer_number):
        return 1 << integer_number - 1
    else:
        raise ValueError(ERROR)

def total():
    return (1 << 64) - 1
    