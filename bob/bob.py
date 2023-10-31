def response(text):
    smalltalk = sanitized(text)
    if silent(smalltalk):
        return "Fine. Be that way!"
    if yelling(smalltalk):
        return "Calm down, I know what I'm doing!"
    if shouting(smalltalk):
        return "Whoa, chill out!"
    if question(smalltalk):
        return "Sure."
    return "Whatever."

sanitized = lambda x : x.strip()
silent    = lambda x : not x
shouting  = lambda x : x.isupper() 
question  = lambda x : x.endswith('?')
yelling   = lambda x : shouting(x) and question(x)