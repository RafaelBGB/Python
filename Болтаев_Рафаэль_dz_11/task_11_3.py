import re


class IsDigit(Exception):
    pass


d_list = []
while True:
    try:
        print('Для завершения программы введите "stop".')
        f = input('Введите число: ')
        if f == 'stop':
            break

        if re.search(r'(\d+[\.,]\d+)|\d+', f):
            d_list.append(float(f.replace(',', '.'))) if re.search(r'\d+[\.,]\d+|d+', f) else d_list.append(int(f))
        else:
            raise IsDigit

    except IsDigit:
        print('Вы ввели не число! Попробуйте еще раз')

print(d_list)
