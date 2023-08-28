from functools import reduce

colors = ['black', 'brown', 'red', 'orange', 'yellow',
          'green', 'blue', 'violet', 'grey', 'white' ]

color_code = lambda color: colors.index(color)

def label(colors: 'list[str]'):
    zeros = color_code(colors[2])
    value = reduce (lambda band1, band2: 10 * band1 + band2,
                    map(color_code, colors[:2]))
    resistance = value * 10 ** zeros
    ohms, magn = 0, ''
    if resistance > 1e9:
        ohms, magn = int(resistance // 1e9), 'giga'
    elif resistance > 1e6:
        ohms, magn = int(resistance // 1e6), 'mega'
    elif resistance > 1e3:
        ohms, magn = int(resistance // 1e3), 'kilo'
    elif resistance > 1e0:
        ohms = resistance
    else:
        ohms = 0
    return f'{ohms} {magn}ohms'
    ###### OR:
    # match resistance:
    #     case r if r > 1e9:
    #         ohms, magn = int(resistance // 1e9), 'giga'
    #     case r if r > 1e6:
    #         ohms, magn = int(resistance // 1e6), 'mega'
    #     case r if r > 1e3:
    #         ohms, magn = int(resistance // 1e3), 'kilo'
    #     case r if r > 1e0:
    #         ohms = resistance
    #     case _:
    #         ohms = 0
    # return f'{ohms} {magn}ohms'
    ###### Only works with python >= 3.10
    