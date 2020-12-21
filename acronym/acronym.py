def abbreviate(sentence):
    acronym = ''
    for capital in acrogen(sentence):
        acronym += capital
    return acronym

def acrogen(sentence):
    current = ''
    for next in sentence:
        if boundary(current, next):
            yield next.upper()
        current = next

def boundary(current, next):
    case = current.islower() and \
           next.isupper()
    alpha = current != "'" and \
            next.isalpha() and \
            not current.isalpha()
    return case or alpha