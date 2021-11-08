def is_armstrong_number(number):
    raised_digits = [int(digit) ** len(str(number)) 
                    for digit in str(number)]
    return sum(raised_digits) == number