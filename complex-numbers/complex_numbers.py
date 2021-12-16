import math

def complexify(f):
    def inner(_, n): 
        if not isinstance(n, ComplexNumber):
            n = ComplexNumber(n, 0)
        return f(_, n)
    return inner

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    @complexify
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    @complexify
    def __radd__(self, other):
        return other + self

    @complexify
    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(r, i)

    @complexify
    def __rmul__(self, other):
        return other * self

    @complexify
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    @complexify
    def __rsub__(self, other):
        return other - self

    @complexify
    def __truediv__(self, other):
        denom = other.real ** 2 + other.imaginary ** 2
        realn = self.real * other.real + self.imaginary * other.imaginary 
        imagn = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber(realn / denom, imagn / denom)

    @complexify
    def __rtruediv__(self, other):
        return other / self
    
    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        xr = math.exp(self.real)
        i = self.imaginary
        return ComplexNumber(xr * math.cos(i), xr * math.sin(i))

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
