def is_valid(isbn):
    digits = list(isbn.replace('-', '')
                      .replace('_', ''))
    if digits and digits[-1] == 'X':
        digits[-1] = '10'
    exist_nondigits = any(not d.isdigit() 
                          for d in digits) 
    if len(digits) != 10 or exist_nondigits:
        return False
    countdown = list(range(10, 0, -1))
    csum = sum(int(d) * c  
               for d, c in zip(digits, countdown))  
    return  csum % 11 == 0