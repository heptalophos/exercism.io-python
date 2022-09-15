from functools import reduce

colors = ['black', 'brown', 'red', 'orange', 'yellow',
          'green', 'blue', 'violet', 'grey', 'white' ]

color_code = lambda color: colors.index(color)

def value(colors: 'list[str]'):
    return reduce (
        lambda band1, band2: 10 * band1 + band2,
        map(color_code, colors[:2]) 
    )
    
