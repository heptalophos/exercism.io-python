NTHDAY = [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth' ]
  
GIFTS = [ 'a Partridge in a Pear Tree',
          'two Turtle Doves',
          'three French Hens',
          'four Calling Birds',
          'five Gold Rings',
          'six Geese-a-Laying',
          'seven Swans-a-Swimming',
          'eight Maids-a-Milking',
          'nine Ladies Dancing',
          'ten Lords-a-Leaping',
          'eleven Pipers Piping',
          'twelve Drummers Drumming' ]
  
PROLOGUE = 'On the __nth__ day of Christmas my true love gave to me: '

def gifts(n):
    gifts = []
    if n > 0:
        for gift in GIFTS[n:0:-1]:
            gifts += [f'{gift},']
        gifts += [f'and {GIFTS[0]}.']
    else:
        gifts += [f'{GIFTS[0]}.']
    return gifts

def verse(n):
    return PROLOGUE.replace('__nth__', NTHDAY[n]) + ' '.join(*[gifts(n)]) 

def recite(start_verse, end_verse):
    return [verse(x - 1) for x in range(start_verse, end_verse + 1)]