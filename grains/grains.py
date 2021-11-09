def valid_input(int_number):
    if (int_number < 1) or (int_number > 64):
        return False
    return True

ERROR = "square must be between 1 and 64"

def square(int_number):
    if valid_input(int_number):
        return 1 << int_number - 1
    else:
        raise ValueError(ERROR)

def total():
    return (1 << 64) - 1
    