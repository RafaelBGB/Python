tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Евгений',
    'Оксна', 'Николай', 'Тарас', 'Леонид'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tup_gen = ((t, klasses[i]) if i < len(klasses) else (t, None) for i, t in enumerate(tutors))
print(type(tup_gen), *tup_gen)
print(next(tup_gen, 'Генератор пуст'))
