LITERALS = {1: 'one', 
            2: 'two', 
            3: 'three', 
            4: 'four', 
            5: 'five', 
            6: 'six', 
            7: 'seven', 
            8: 'eight', 
            9: 'nine', 
            10: 'ten', 
            11: 'eleven', 
            12: 'twelve', 
            13: 'thirteen', 
            14: 'fourteen', 
            15: 'fifteen', 
            16: 'sixteen', 
            17: 'seventeen', 
            18: 'eighteen', 
            19: 'nineteen', 
            20: 'twenty', 
            30: 'thirty', 
            40: 'forty', 
            50: 'fifty', 
            60: 'sixty', 
            70: 'seventy', 
            80: 'eighty', 
            90: 'ninety', 
            100: 'hundred', 
            1000: 'thousand', 
            1000000: 'million'}


tens = lambda n: n//10*10

hundreds = lambda n: n//100*100

def chunks(num, size=3):
    return [int(str(num)[::-1][i:i+size][::-1]) 
            for i in range(0, len(str(num)), size)]

def lit_chunk(num, acc=""):
    if num == 0:
        return acc
    if 100 <= num < 1000:
        acc += LITERALS[int(num // 100)] + " hundred"
        num -= hundreds(num)
        if num:
            acc += " "
    elif 20 < num < 100:
        acc += LITERALS[tens(num)]
        num -= tens(num)
        if num:
            acc += '-'
    else:
        acc += LITERALS[num]
        num = 0
    return lit_chunk(num, acc) 

def elucidate(lst):
    out = ""
    if 'billion' in lst:
        out = lst['billion'] + " billion"
    if 'million' in lst and lst['million']:
        if out:
            out += " "
        out += lst['million'] + " million"
    if 'thousand' in lst and lst['thousand']:
        if out:
            out += " "
        out += lst['thousand'] + " thousand"
    if lst['hundred']:
        if out:
            out += " "
            if 'hundred' not in lst or not lst['thousand']:
                out += " "
        out += lst['hundred']
    return out

def say(number):
    number = int(number)
    if number == 0:
        return "zero"
    elif number < 0 or number >= 1e12:
        raise ValueError("Number out of range")
    lst = [lit_chunk(n) 
           for n in chunks(number)]
    lst = dict(zip(['hundred', 
                    'thousand', 
                    'million', 
                    'billion'], 
               lst))
    return elucidate(lst)