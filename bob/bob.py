sanitized = lambda x : x.strip()
silent    = lambda x : not x
shout     = lambda x : x.isupper() 
question  = lambda x : x.endswith('?')

def response(text):
    text = sanitized(text)
    if silent(text):
        return "Fine. Be that way!"
    if shout(text) and question(text):
        return "Calm down, I know what I'm doing!"
    if shout(text):
        return "Whoa, chill out!"
    if question(text):
        return "Sure."
    return "Whatever."