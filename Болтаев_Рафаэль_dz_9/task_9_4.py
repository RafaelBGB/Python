class Car:
    def __init__(self, speed, color, name, is_police):
        self.c_speed = speed
        self.c_color = color
        self.c_name = name
        self.c_is_police = is_police

    def go(self):
        print('Начинаем движение.')

    def stop(self):
        print('Останавливаемся.')

    def turn(self, direction):
        print(f'Поворачиваем {direction}')

    def show_speed(self):
        print(f'Скорость Car {self.c_speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость TownCar {self.c_speed}')
        if self.c_speed > 60:
            print('Внимание! Снизте скорость до 60!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость WorkCar {self.c_speed}')
        if self.c_speed > 40:
            print('Внимание! Снизте скорость до 40!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


c1 = Car(30, 'red', 'Volvo', 0)
c1.go()
c1.turn('left')
c1.show_speed()
c1.stop()
print()

t = TownCar(90, 'red', 'Lada', 0)
t.go()
t.turn('right')
t.show_speed()
t.stop()
print()

s = SportCar(200, 'black', 'Porsche', 0)
s.go()
s.turn('right')
s.show_speed()
s.stop()
print()

w = WorkCar(60, 'yellow', 'БелАЗ', 0)
w.go()
w.turn('right')
w.show_speed()
w.stop()
print()

p = PoliceCar(60, 'white', 'Bentley', 0)
p.go()
p.turn('right')
p.show_speed()
p.stop()
print()
