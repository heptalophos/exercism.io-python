def is_armstrong_number(number):
    digits = ( int(digit)**len(str(number)) 
               for digit in str(number) )
    return sum( digits ) == number