from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=2):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, new_value):
        if not isinstance(new_value, int):
            raise Exception("Numerator must be integer")
        self._numerator = new_value

    @denominator.setter
    def denominator(self, new_value):
        if not isinstance(new_value, int):
            raise Exception("Denominator must be integer")
        if new_value == 0:
            raise ZeroDivisionError()
        self._denominator = new_value

    def __str__(self):
        common_denominator = gcd(self.numerator, self.denominator)
        self.numerator //= common_denominator
        self.denominator //= common_denominator
        return f"{self.numerator} / {self.denominator}"

    def float_value(self):
        return self.numerator / self.denominator
