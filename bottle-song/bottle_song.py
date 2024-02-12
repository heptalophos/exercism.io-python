How_Many = 'no|one|two|three|four|five|six|seven|eight|nine|ten'.split('|')

def bottles(num: int, cap=False) -> str:
    s = 's' if num != 1 else ''
    this_many = How_Many[num].capitalize() if cap else How_Many[num]
    return f'{this_many} green bottle{s}'

def prologue(num: int) -> list[str]:
    return [f'{bottles(num, True)} hanging on the wall,', 
            f'{bottles(num, True)} hanging on the wall,']

def premise():
    return f'And if {bottles(1, False)} should accidentally fall,'

def conclusion(num: int) -> list[str]:
    return f'There\'ll be {bottles(num - 1, False)} hanging on the wall.'

def recite(start, take=1):
    song = list()
    for n in range(start, start - take, -1):
        song += [*prologue(n), premise(), conclusion(n)]
        if n > start - take + 1:
            song += ['']
    return song