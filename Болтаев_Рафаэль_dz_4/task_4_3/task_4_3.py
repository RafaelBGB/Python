import untils


currency = input('Введите трехбуквенную аббривиатуру валюты: ').upper()
x = untils.currency_rates(currency)
if x:
    print(f'Курс {currency} на {x[1]}  равен {x[0]} руб.')
else:
    print(x)
