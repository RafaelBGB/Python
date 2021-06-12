from abc import abstractmethod, ABC


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Jacket(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return self.h * 2 + 0.3


x1 = Coat(52)
x2 = Coat(48)
x3 = Jacket(167)
x4 = Jacket(180)

print(x1.consumption + x2.consumption + x3.consumption + x4.consumption)
