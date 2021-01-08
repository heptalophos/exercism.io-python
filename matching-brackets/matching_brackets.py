brackets = dict(zip('({[', ')}]'))

def is_paired(input_string):
    just_brackets = ''.join(c for c in input_string 
                              if c in '(){}[]')
    stack = []
    for c in just_brackets:
        if c in brackets:
            stack.append(brackets[c])
        elif not stack or c != stack.pop():
            return False
    return not stack
