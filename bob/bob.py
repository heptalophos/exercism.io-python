import re

def normal(text):
    return re.sub(r"([^A-Za-z0-9_?:) ])+",'', text).strip()

def silent(text):
    return text is None or text == ''

def shout(text):
    return text == text.upper() and re.search("[A-Z]+", text) 
    
def question(text):
    return text.endswith('?')

def hey(text):
    text = normal(text)
    if silent(text):
        return "Fine. Be that way!"
    if not shout(text) and question(text):
        return "Sure."
    if shout(text):
        return "Whoa, chill out!"
    return "Whatever."

