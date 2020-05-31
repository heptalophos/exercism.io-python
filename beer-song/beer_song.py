def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        verses += verse(i) + ['']
    verses.pop()
    return verses

def verse(n):
    s = 's' if n > 1 else ''
    z = 's' if n != 2 else ''
    it = 'it' if n == 1 else 'one'
    more = str(n - 1) * (n > 1) + 'no more' * ( n == 1)
    if n == 0:
        return [("No more bottles of beer on the wall,"
                 " no more bottles of beer."),
                ("Go to the store and buy some more, " 
                "99 bottles of beer on the wall.")]
    else:
        return [(f'{n} bottle{s} of beer on the wall,' 
                 f' {n} bottle{s} of beer.'),
                (f'Take {it} down and pass it around, '
                 f'{more} bottle{z} of beer on the wall.')]
