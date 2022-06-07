def pig_latin(word):
    if word.startswith (('a', 'e', 'i', 'o', 'u')):
        return word + 'ay'
    if word.startswith (('thr', 'sch', 'squ')):
        return word[3:] + word[:3] + 'ay'
    if word.startswith (('ch', 'qu', 'th', 'rh')):
        return word[2:] + word[:2] + 'ay'
    if word.startswith (('ye', 'xe')):
        return word[1:] + word[:1] + 'ay'
    if word.startswith (('yt', 'xr')):
        return word + 'ay'
    return word[1:] + word[:1] + 'ay'
        
def translate(sentence):
    return ' '.join([pig_latin(w) for w in sentence.lower().split()])
