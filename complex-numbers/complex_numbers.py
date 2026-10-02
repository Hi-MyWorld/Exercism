# +
import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        add_real = self.real + other.real
        add_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(add_real, add_imaginary)

    def __mul__(self, other):
        mul_real = self.real * other.real - self.imaginary * other.imaginary
        mul_imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(mul_real, mul_imaginary)

    def __sub__(self, other):
        sub_real = self.real - other.real
        sub_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(sub_real, sub_imaginary)

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary

        div_real = (a * c + b * d) / (c**2 + d**2)
        div_imaginary = (b * c - a * d) / (c**2 + d**2)
        return ComplexNumber(div_real, div_imaginary)

    def __abs__(self):
        abso = (self.real**2 + self.imaginary**2) ** (1 / 2)
        return abso

    def conjugate(self):
        conjugate_real = self.real
        conjugate_imaginary = -self.imaginary
        return ComplexNumber(conjugate_real, conjugate_imaginary)

    def exp(self):
        e = math.e
        export_real = e**self.real * math.cos(self.imaginary)
        export_imaginary = e**self.real * math.sin(self.imaginary)
        return ComplexNumber(export_real, export_imaginary)


# -
