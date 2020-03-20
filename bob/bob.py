import re

def normal(text):
    return re.sub(r"([^A-Za-z0-9_?:) ])+",'', text).strip()

def silent(text):
    return text is None or text == ''

def shout(text):
    return text == text.upper() and re.search("[A-Z]+", text) 
    
def question(text):
    return text.endswith('?')

def response(text):
    text = normal(text)
    if silent(text):
        return "Fine. Be that way!"
    if shout(text) and question(text):
        return "Calm down, I know what I'm doing!"
    if shout(text):
        return "Whoa, chill out!"
    if question(text):
        return "Sure."
    return "Whatever."