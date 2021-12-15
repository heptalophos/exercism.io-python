import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def _ensure_complex(f):
        def wrapper(self, n): 
            if not isinstance(n, ComplexNumber):
                number = ComplexNumber(n, 0)
            return f(self, n)
        return wrapper

    @_ensure_complex
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    @_ensure_complex
    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(r, i)

    @_ensure_complex
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    @_ensure_complex
    def __truediv__(self, other):
        denom = other.real ** 2 + other.imaginary ** 2
        realn = self.real * other.real + self.imaginary * other.imaginary 
        imagn = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber(realn / denom, imagn / denom)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        xr = math.exp(self.real)
        i = self.imaginary
        return ComplexNumber(xr * math.cos(i), xr * math.sin(i))

    @_ensure_complex
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
