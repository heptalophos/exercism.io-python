SCORES = {
    1: 'aeioulnrst',
    2: 'dg',
    3: 'bcmp',
    4: 'fhvwy',
    5: 'k',
    8: 'jx',
    10: 'qz',
    }

SCORES = {letter.upper(): score
         for score in SCORES
         for letter in SCORES[score]}

def score(word):
    if word.isalpha():
        return sum(SCORES[c] 
                   for c in word.upper())
    return 0
    