def pairs(input_list):
    iterable = iter(input_list) 
    nextitem = next(iterable)
    while True:
        try:
            item, nextitem = nextitem, next(iterable)
            yield (item, nextitem)
        except StopIteration:
            return     

def proverb(*input_data, qualifier=None):
    if not input_data: return []
    prime_cause = input_data[0]
    if qualifier: prime_cause = f'{qualifier} {prime_cause}'
    verses, epilogue = [], f'And all for the want of a {prime_cause}.'
    for pair in pairs(input_data):
        (cause, result) = pair 
        premise = f'For want of a {cause} ' 
        conclusion = f'the {result} was lost.'
        verses.append(f'{premise}{conclusion}')
    verses.append(epilogue)
    return verses
