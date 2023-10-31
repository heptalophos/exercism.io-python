rhyme = """ the horse and the hound and the horn \
that belonged to, the farmer sowing his corn \
that kept, the rooster that crowed in the morn \
that woke, the priest all shaven and shorn \
that married, the man all tattered and torn \
that kissed, the maiden all forlorn \
that milked, the cow with the crumpled horn \
that tossed, the dog \
that worried, the cat \
that killed, the rat \
that ate, the malt that lay in """.split(',')


def recite(start_verse: int, end_verse: int) -> list[str]:
    all_the = lambda x: ' ' if x == 1 else ''.join(rhyme[1-x::1])
    recital = lambda things_in:\
            f"This is{all_the(things_in)}the house that Jack built."
    return [recital(n) for n in range(start_verse, end_verse + 1)]
