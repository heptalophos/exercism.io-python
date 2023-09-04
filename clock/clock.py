HOURminutes = 60
DAYminutes = 1440

class Clock:
    def __init__(self, hour, minute):
        ms = (hour * HOURminutes + minute) % DAYminutes
        self.minutes = ms

    def __repr__(self):
        hs, ms = divmod(self.minutes, HOURminutes)
        return f"Clock({hs}, {ms})"

    def __str__(self):
        hs, ms = divmod(self.minutes, HOURminutes)
        return f"{hs:02}:{ms:02}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        ms = self.minutes + minutes
        if ms < 0 or ms >= DAYminutes:
            self.minutes = ms % DAYminutes
        else:
            self.minutes = ms
        return self

    def __sub__(self, minutes):
        self.__add__(-minutes)
        return self
