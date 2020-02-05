def abbreviate(sentence):
    acronym = ''
    for cap in acrogen(sentence):
        acronym += cap
    return acronym

def acrogen(sentence):
    cur = ''
    for nxt in sentence:
        if boundary(cur, nxt):
            yield nxt.upper()
        cur = nxt

def boundary(cur, nxt):
    case = cur.islower() and nxt.isupper()
    alpha = cur != "'" and \
            nxt.isalpha() and \
            not cur.isalpha()
    return case or alpha