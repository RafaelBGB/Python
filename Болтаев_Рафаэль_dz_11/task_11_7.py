class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        r_num = self.a + other.a
        i_num = self.b + other.b
        return f'{r_num} + {i_num}i' if i_num > 0 else f'{r_num} {i_num}i'

    def __mul__(self, other):
        r_num = (self.a * other.a - self.b * other.b)
        i_num = self.a * other.b + other.a * self.b
        return f'{r_num} + {i_num}i' if i_num > 0 else f'{r_num} {i_num}i'


x1 = Complex(1, -1)
x2 = Complex(3, 6)
print(x1 + x2)
print(x1 * x2)
