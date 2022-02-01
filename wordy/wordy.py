from functools import reduce

wadd = lambda x, y : x + y
wsub = lambda x, y : x - y
wmul = lambda x, y : x * y
wdiv = lambda x, y : x // y

validOps = {'plus'       : wadd, 
            'minus'      : wsub, 
            'multiplied' : wmul, 
            'divided'    : wdiv }

def curry(func, var):
    y = var
    def f(x):
        return func(x, y)
    return f

def convertToInt(lst, err):
    for x in lst:
        try:
            yield int(x)
        except:
            raise ValueError(err) 

def answer(question):
    if not question.startswith('What is'):
        raise ValueError('unknown operation')
    question = question.lstrip('What is').rstrip('?')
    if question == '':
        raise ValueError('syntax error')
    tokens = [t for t in question.split(' ') if t != 'by']
    if len(tokens) == 0:
        raise ValueError('unknown operation') 
    if len(tokens) == 1:
        return int(tokens[0])
    operators = [x for x in tokens 
                   if tokens.index(x) % 2 == 1 
                      and x in list(validOps.keys())]
    arguments = [x for x in tokens 
                   if tokens.index(x) % 2 == 0]
    if (len(operators) + 1 != len(arguments)):
        raise ValueError('syntax error')
    operants = [x for x 
                  in convertToInt(arguments, 'syntax error')]
    try:
        curries = [curry(validOps[op], num) 
                   for (op, num) 
                   in zip(operators[0::1], operants[1::1])]
        if (len(curries) == 0):
            raise ValueError('unknown operation')
        if (len(curries) * 2 != len(tokens) - 1):
            raise ValueError('syntax error')
    except KeyError:
        raise ValueError('syntax error')
    return reduce (lambda num, op: op(num), curries, int(tokens[0]))
    