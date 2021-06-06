def type_logger(fun):
    def wrapper(*args):
        for i, el in enumerate(args, start=1):
            if i != len(args):
                print('Вызвана функция:{0} c элементом {1} типа {2} результат: {3}'
                      .format(fun.__name__, el, type(el), fun(el)), end=', ')
            else:
                print('Вызвана функция:{0} c элементом {1} типа {2} результат: {3}'
                      .format(fun.__name__, el, type(el), fun(el)))

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3.5, 3, 5, 1)

