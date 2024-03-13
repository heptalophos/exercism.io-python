COLORS = """black brown red orange yellow 
            green blue violet grey white""".split()
TOLERANCES = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
              'brown': 1, 'red': 2, 'gold': 5, 'silver': 10, }
r_code = lambda color: COLORS.index(color)
t_code = lambda color: TOLERANCES[color]

def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1: 
        return f'{r_code(colors[0])} ohms'
    tolerance = t_code(colors[-1])
    zeros     = r_code(colors[-2])
    band2     = r_code(colors[-4])
    band3     = r_code(colors[-3])
    if len(colors) == 4: 
        band1 = 0
    else: 
        band1 = r_code(colors[-5])
    resistance = (band1 * 100 + band2 * 10 + band3) * 10 ** zeros
    ohms, magn = 0, ''
    if resistance   > 1e9: ohms, magn = resistance / 1e9, 'giga'
    elif resistance > 1e6: ohms, magn = resistance / 1e6, 'mega'
    elif resistance > 1e3: ohms, magn = resistance / 1e3, 'kilo'
    elif resistance > 1e0: ohms = resistance
    else: ohms = 0
    return f'{ohms:g} {magn}ohms ±{tolerance}%'