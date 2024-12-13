COLORS = """black brown red orange yellow 
            green blue violet grey white""".split()
TOLERANCES = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
              'brown': 1, 'red': 2, 'gold': 5, 'silver': 10, }

def resistor_label(colors: list[str]) -> str:
    r_code = lambda c: COLORS.index(c)
    t_code = lambda c: TOLERANCES[c]
    n_bands = len(colors)
    if n_bands in range(2, 4) or n_bands > 5:
        raise ValueError("invalid number of bands for this problem")
    if n_bands == 1: return f'{r_code(colors[0])} ohms'
    tolerance = t_code(colors[-1])
    zeros = r_code(colors[-2])
    band3 = r_code(colors[-3])
    band2 = r_code(colors[-4])
    if n_bands == 5: band1 = r_code(colors[-5])
    else: band1 = 0
    resistance = (band1 * 100 + band2 * 10 + band3) * 10 ** zeros
    ohms, magn = 0, ''
    if resistance   > 1e9: ohms, magn = resistance / 1e9, 'giga'
    elif resistance > 1e6: ohms, magn = resistance / 1e6, 'mega'
    elif resistance > 1e3: ohms, magn = resistance / 1e3, 'kilo'
    elif resistance > 1e0: ohms = resistance
    else: ohms = 0
    return f'{ohms:g} {magn}ohms ±{tolerance}%'