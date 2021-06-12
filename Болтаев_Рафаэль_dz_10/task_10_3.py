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


x1 = Cells(2)
x2 = Cells(3)

print(x1 + x2)
print(x1 - x2)
print(x1 * x2)
print(x1 // x2)
print(x1 / x2)
