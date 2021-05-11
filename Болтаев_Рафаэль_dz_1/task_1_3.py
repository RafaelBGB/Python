amount_proc = int(input('Введите количество процентов (от 0 до 20): '))

if amount_proc == 0 or 5 <= amount_proc <= 20:
    print(f'{amount_proc} процентов')
elif 1 < amount_proc < 5:
    print(f'{amount_proc} процента')
elif amount_proc == 1:
    print(f'{amount_proc} процент')
