def valid_input(integer_number):
    return 1 <= integer_number and integer_number <= 64

ERROR = "square must be between 1 and 64"

def square(integer_number):
    if valid_input(integer_number):
        return 1 << integer_number - 1
    else:
        raise ValueError(ERROR)

def total():
    return (1 << 64) - 1
    