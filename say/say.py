LITERALS = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (100, 'hundred'),
    (90, 'ninety'),
    (80, 'eighty'),
    (70, 'seventy'),
    (60, 'sixty'),
    (50, 'fifty'),
    (40, 'forty'),
    (30, 'thirty'),
    (20, 'twenty'),
    (19, 'nineteen'),
    (18, 'eighteen'),
    (17, 'seventeen'),
    (16, 'sixteen'),
    (15, 'fifteen'),
    (14, 'fourteen'),
    (13, 'thirteen'),
    (12, 'twelve'),
    (11, 'eleven'),
    (10, 'ten'),
    (9, 'nine'),
    (8, 'eight'),
    (7, 'seven'),
    (6, 'six'),
    (5, 'five'),
    (4, 'four'),
    (3, 'three'),
    (2, 'two'),
    (1, 'one')
    )

def say_rec(number, prefix):
    for num, word in LITERALS:
        upper = number // num
        lower = number % num
        if upper == 0:
            continue
        suffix = '-' if num < 100 else ' and ' 
        tail = lower and say_rec(lower, suffix) or ''
        if num < 100:
            return '{}{}{}'.format(prefix, word, tail)
        head = say_rec(upper, prefix and ' ' or '')
        return '{} {}{}'.format(head, word, tail)
    return 'zero'

def say(number):
    if number < 0 or number >= 1e12:
        raise AttributeError
    return say_rec(number, '')
