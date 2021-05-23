import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates(value):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(site.content, 'xml')
    if not soup.find('CharCode', text=value) or not value:
        return None

    cost = str(soup.find('CharCode', text=value).find_next_sibling('Value').string).replace(',', '.')
    n = site.text.find('Date=') + 6
    date_list = site.text[n:n+10].split('.')
    date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

    return [float(cost), date]


currency = input('Введите трехбуквенную аббривиатуру валюты: ').upper()
x = currency_rates(currency)
if x:
    print(f'Курс {currency} на {x[1]}  равен {x[0]} руб.')
else:
    print(x)

