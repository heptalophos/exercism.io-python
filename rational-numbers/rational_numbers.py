from __future__ import division

class Rational(object):
    def __init__(self, numer, denom):
        self.numer, self.denom = Rational.lowest_form(numer, denom)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        else:
            return (self.numer / self.denom) == other

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, \
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, \
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer * self.denom == 0:
            raise ValueError("Division by zero")
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return  Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0 or isinstance(power, float):
            return Rational(self.numer ** power, self.denom ** power)
        else:
            power = abs(power)
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        power = self.numer / self.denom
        return base ** power

    @staticmethod
    def lowest_form (numer, denom):
        if denom == 0:
            raise ValueError("Division by zero")
        return (numer / Rational.gcd(numer, denom), denom / Rational.gcd(numer, denom)) 

    @staticmethod
    def gcd(numer, denom):
        if denom == 0:
            return numer
        return Rational.gcd(denom, numer % denom)
