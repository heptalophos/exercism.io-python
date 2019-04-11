from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer, self.denom = Rational.lowest_form(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return  Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        power = self.numer / self.denom
        return base ** power

    @staticmethod
    def lowest_form (numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        return (numer / Rational.gcd(numer, denom), denom / Rational.gcd(numer, denom)) 

    @staticmethod
    def gcd(numer, denom):
        if denom == 0:
            return numer
        return Rational.gcd(denom, numer % denom)
