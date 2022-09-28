sanitized = lambda x : x.strip()
silent    = lambda x : not x
shouting  = lambda x : x.isupper() 
question  = lambda x : x.endswith('?')
yelling   = lambda x : shouting(x) and question(x)

def response(text):
    text = sanitized(text)
    if silent(text):
        return "Fine. Be that way!"
    if yelling(text):
        return "Calm down, I know what I'm doing!"
    if shouting(text):
        return "Whoa, chill out!"
    if question(text):
        return "Sure."
    return "Whatever."