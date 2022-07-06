brackets = dict(zip('({[', ')}]'))

def is_paired(input_string):
    stack = []
    just_brackets = ( c for c in input_string if c in '(){}[]')
    for c in ''.join(just_brackets):
        if c in brackets:
            stack.append(brackets[c])
        elif not stack or c != stack.pop():
            return False
    return not stack
