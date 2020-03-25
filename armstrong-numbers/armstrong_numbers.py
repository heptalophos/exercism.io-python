def is_armstrong_number(number):
    power_digits = (int(digit)**len(str(number)) 
                    for digit in str(number) )
    return sum(power_digits) == number