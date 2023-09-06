HOUR_MINUTES = 60
DAY_MINUTES = 1440

class Clock:
    def __init__(self, hour, minute):
        ms = (hour * HOUR_MINUTES + minute) % DAY_MINUTES
        self.minutes = ms

    def __repr__(self):
        hs, ms = divmod(self.minutes, HOUR_MINUTES)
        return f"Clock({hs}, {ms})"

    def __str__(self):
        hs, ms = divmod(self.minutes, HOUR_MINUTES)
        return f"{hs:02}:{ms:02}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        ms = self.minutes + minutes
        if ms < 0 or ms >= DAY_MINUTES:
            self.minutes = ms % DAY_MINUTES
        else:
            self.minutes = ms
        return self

    def __sub__(self, minutes):
        self.__add__(-minutes)
        return self
