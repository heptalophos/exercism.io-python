from functools import reduce

iadd = lambda x, y : x + y
isub = lambda x, y : x - y
imul = lambda x, y : x * y
idiv = lambda x, y : x // y

validOps = {'plus'       : iadd, 
            'minus'      : isub, 
            'multiplied' : imul, 
            'divided'    : idiv }

def curry(func, var):
    y = var
    def f(x):
        return func(x, y)
    return f

def calculate(question):
    question = question.lstrip('What is').rstrip('?')
    tokens = [t if t in validOps else int(t) 
              for t in question.split(' ') if t != 'by']
    if len(tokens) == 0:
       raise ValueError('invalid question: no numbers here') 
    if len(tokens) == 1:
        return int(tokens[0])
    try:
        curries = [curry(validOps[op], num) 
                   for (op, num) in zip(tokens[1::2], tokens[2::2])]
        if (len(curries) * 2 != len(tokens) - 1):
            raise ValueError('invalid question: operands not matched')
    except:
            raise ValueError('invalid sequence of operands')
    return reduce (lambda num, op: op(num), curries, int(tokens[0]))