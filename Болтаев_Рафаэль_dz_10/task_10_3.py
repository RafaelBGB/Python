class Cells:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return self.nucleus + other.nucleus

    def __sub__(self, other):
        return self.nucleus - other.nucleus if self.nucleus >= other.nucleus else 'Вычитание невозможно!'

    def __mul__(self, other):
        return self.nucleus * other.nucleus

    def __floordiv__(self, other):
        return self.nucleus // other.nucleus

    def __truediv__(self, other):
        return self.nucleus / other.nucleus

    def make_order(self, series):
        result = ''
        for v in range(1, self.nucleus // series + 1):
            result += '*' * series
            if v != self.nucleus // series:
                result += '\\n'

        if self.nucleus % series != 0:
            result += '\\n' + '*' * (self.nucleus - (self.nucleus // series) * series)
            
        return result


x1 = Cells(15)
x2 = Cells(8)

print(x1 + x2)
print(x1 - x2)
print(x1 * x2)
print(x1 // x2)
print(x1 / x2)

print(x1.make_order(3))
