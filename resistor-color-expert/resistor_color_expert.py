COLORS = "black brown red orange yellow green blue violet grey white".split()
color_code = lambda color: COLORS.index(color)

TOLERANCES = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
    }

def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1: return f'{color_code(colors[0])} ohms'
    zeros = color_code(colors[-2])
    tolerance = color_code(colors[-1])
    b2, b3 = color_code(colors[-4]), color_code(colors[-3])
    if len(colors) == 4: b1 = 0
    else: b1 = color_code(colors[-5])
    value = (b1 * 100 + b2 * 10 + b3) * 10 ** zeros
    ohms, magn = 0, ''
    if value > 1e9: ohms, magn = int(value // 1e9), 'giga'
    elif value > 1e6: ohms, magn = int(value // 1e6), 'mega'
    elif value > 1e3: ohms, magn = int(value // 1e3), 'kilo'
    elif value > 1e0: ohms = value
    else: ohms = 0
    units = f'{ohms} {magn}ohms'
    return f'{value:g} {units} ±{TOLERANCES[tolerance]}%'