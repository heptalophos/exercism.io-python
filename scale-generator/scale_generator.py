class Scale:
    S_FLATS = 'A Bb B C Db D Eb E F Gb G Ab'.split()
    S_SHARP = 'A A# B C C# D D# E F F# G G#'.split()
    T_FLATS = 'F Bb Eb Ab Db Gb d g c f bb eb'.split()

    def __init__(self, tonic: str):
        self.scale = self.S_FLATS if tonic in self.T_FLATS else self.S_SHARP
        self.tonic = tonic.capitalize()

    def chromatic(self) -> list[str]:
        scale, index = self.scale, self.scale.index(self.tonic)
        return scale[index:] + scale[:index]

    def interval(self, intervals: str) -> list[str]:
        chromatic, notes, index = self.chromatic(), [], 0
        steps = {'m': 1, 'M': 2, 'A': 3}
        for i in intervals:
            try:
                notes += [chromatic[index]]
                index += steps[i] % len(chromatic)
            except:
                raise ValueError("Not a valid interval")
        notes += [chromatic[0]]
        return notes


