class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, name):
        self.name_w = name
        self.amount_equipment = {'Printer': {}, 'Scanner': {}, 'Copier': {}}

    def add_to_warehouse(self, obj, amount, cost):
        if obj.model in self.amount_equipment[obj.__class__.__name__]:
            tmp = self.amount_equipment[obj.__class__.__name__][obj.model]
            tmp['amount'] += amount
            tmp['cost'] = (tmp['cost'] + cost) / 2
        else:
            self.amount_equipment[obj.__class__.__name__].setdefault(obj.model, {'amount': amount, 'cost': cost})

    def take(self, obj, amount):
        if obj.model in self.amount_equipment[obj.__class__.__name__]:
            tmp = self.amount_equipment[obj.__class__.__name__][obj.model]
            if tmp['amount'] < amount:
                print('На складее нет столько продукции')
            else:
                tmp['amount'] -= amount
                if tmp['amount'] == 0:
                    self.amount_equipment[obj.__class__.__name__].pop(obj.model)
        else:
            print('На складе нет данного товара!')

    def __str__(self):
        res = f'На складе {self.name_w} находиться следующая продукция:'
        for k, eq in self.amount_equipment.items():
            res += f'\n{k}:'
            for key, el in eq.items():
                res += f'\n    Модель: {key}, в количестве {el["amount"]}, по цене {el["cost"]}'

        return res + '\n'


class Equipment:
    def __init__(self, model):
        self.model = model


class Printer(Equipment):
    def __init__(self, model):
        super().__init__(model)


class Scanner(Equipment):
    def __init__(self, model):
        super().__init__(model)


class Copier(Equipment):
    def __init__(self, model):
        super().__init__(model)


# u_w = input('Введите название склада: ')
# w = Warehouse(u_w)
# while True:
#     try:
#         cont = input('Для выхода из программы нажмите "q"')
#         if cont == 'q':
#             break
#         u_answer = input('Для добавления продукции на склад введите "+", для выдачи со склада введите "-" ')
#         if u_answer == '+':
#             u_class = input('Введите 1 для выбора категории Printer, 2 для выбора категории Scanner, '
#                             '3 для выбора категории Copier. ')
#             if '0' < u_class < '4':
#                 u_enter = input('Введите модель, количесто и цену, через "," ')
#                 if u_class == '1':
#                     goods = Printer(u_enter.split(',')[0])
#                 elif u_class == '2':
#                     goods = Scanner(u_enter.split(',')[0])
#                 elif u_class == '3':
#                     goods = Copier(u_enter.split(',')[0])
#
#                 w.add_to_warehouse(goods, int(u_enter.split(',')[1]), float(u_enter.split(',')[2]))
#             else:
#                 raise MyException('Вы ввели неправельное значение!')
#
#         elif u_answer == '-':
#             print(w)
#             u_class = input('Введите 1 для выбора категории Printer, 2 для выбора категории Scanner, '
#                             '3 для выбора категории Copier. ')
#             if '0' < u_class < '4':
#                 u_enter = input('Введите модель из наличия на складе и количесто, через "," ')
#                 if u_class == '1':
#                     goods = Printer(u_enter.split(',')[0])
#                 elif u_class == '2':
#                     goods = Scanner(u_enter.split(',')[0])
#                 elif u_class == '3':
#                     goods = Copier(u_enter.split(',')[0])
#
#                 w.take(goods, int(u_enter.split(',')[1]))
#             else:
#                 raise MyException('Вы ввели неправельное значение!')
#
#         else:
#             raise MyException('Нужно выбрать "+" или "-"!')
#
#     except ValueError:
#         print('Вы ввели некоректное значение.')
#     except MyException as err:
#         print(err)
#     except Exception:
#         print('Что-то пошло не так...')


w1 = Warehouse('склад1')
p1 = Printer('p1')
p2 = Printer('p2')
s1 = Scanner('s1')
s2 = Scanner('s2')

w1.add_to_warehouse(p1, 100, 2000)
w1.add_to_warehouse(p1, 100, 3000)
w1.add_to_warehouse(p2, 100, 1000)
w1.add_to_warehouse(s1, 50, 800)
w1.add_to_warehouse(p1, 100, 320)

print(w1)

w1.take(s1, 50)
print(w1)


