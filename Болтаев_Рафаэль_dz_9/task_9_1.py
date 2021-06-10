import time


class TrafficLight:
    __color = [('red', 7, 31), ('yellow', 2, 33), ('green', 5, 32)]

    def running(self, s_color=0):
        if s_color < 0 or s_color > 2:
            exit('Вы ввели некоректый номер цвета.')

        print('Включаем светофор!')
        for i, val in enumerate(self.__color[s_color:]):
            print(f'\33[{val[2]}m{val[0]}\33[0m')
            time.sleep(val[1])
        print('Выключаем светофор!')


x = TrafficLight()
x.running()
s = int(input('Выберете номер цвета светофора, который хотите зажечь (1 - "red", 2 - "yellow", 3 - "green"): ')) - 1
x.running(s)

