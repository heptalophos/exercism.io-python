def is_armstrong(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number