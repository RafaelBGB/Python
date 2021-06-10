class Stationery:
    def __init__(self, u_title):
        self.title = u_title

    def draw(self):
        print('Запуск отрисовки класса Stationery')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки класса Pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки класса Pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки класса Handle')


s = Stationery('title')
s.draw()

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

p = Handle('маркер')
p.draw()

