class MyDivExc(Exception):
    pass


try:
    x = int(input('Введите число: '))
    if x == 0:
        raise MyDivExc

except ValueError:
    print('Вы ввели не число!!!')
except MyDivExc:
    print('Делить на ноль нельзя!!!')
else:
    print(100 / x)


