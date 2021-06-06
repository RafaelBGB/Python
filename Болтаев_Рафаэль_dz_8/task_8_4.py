def val_checker(valid_fun):
    def my_decorator(fun):
        def wrapper(*args):
            for i, el in enumerate(args, start=1):
                if not valid_fun(el):
                    raise ValueError(f'{el} меньше или ровно 0! Возведение в куб данного числа не возможно!')

                print('Вызвана функция:{0} c элементом {1} типа {2} результат: {3}'
                      .format(fun.__name__, el, type(el), fun(el)))
        return wrapper
    return my_decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(3, 2.5, 10)
