class Road:
    def __init__(self, u_length, u_width):
        self._length = u_length
        self._width = u_width

    def mass_calc(self):
        # В расчете взяли вес асфальта равный 25 кг 1 кадратный метр толщиной 1 см, а толщина дорожного покрытия 5 см.
        return self._length * self._width * 25 * 5 / 1000


length = 5000
width = 10
x = Road(length, width)
print(f'Для покрытия дороги длиной {length} метров и шириной {width} метров потребуется {x.mass_calc()} тонн асфальта')
