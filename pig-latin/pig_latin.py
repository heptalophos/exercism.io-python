import re
from string import ascii_lowercase

def pigword (text):
    # head = re.search('{0}|{1}|{2}'
    #          .format('[aeio]', '((?<!q)u)', '(^(x|y)(?=[{0}]))')
    #          .format(''.join(set(ascii_lowercase) - set('aeiouy'))), text)
    # if head:
    #     text = text[head.start(0):] + text[:head.start(0)]
    # for form in (r'(.*?[^q])(u.*)', r'(^y[^aeiou].*)()', r'(.*?)([aeoi].*)'):
    formv = r'^(a|e|i|o|u|yt|xr)(\\w+)$'
    formc = r'^(y|ch|qu|thr|th|sch|yt|rh|\\wqu|\\w)(\\w+)$'
    if (re.search(formv, text) != None):
        pigl = re.sub(formv, r'\1\2ay', text)
    elif (re.search(formc, text) != None):
        pigl = re.sub(formc, r'\2\1ay', text)
    else: 
        pigl = text + 'ay'
    return pigl
        

def translate(text):
    return ' '.join([pigword(w) for w in text.lower().split()])

            
