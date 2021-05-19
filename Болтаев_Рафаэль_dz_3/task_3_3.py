from random import choice


def get_jokes(n, flag_check=False):
    """Функция возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
    (по одному из каждого)"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(0, n):
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        if flag_check:
            nouns.remove(jokes[i].split()[0])
            adverbs.remove(jokes[i].split()[1])
            adjectives.remove(jokes[i].split()[2])
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                print('В списаках не хватает слов для генерации задоного количества шуток...')
                return None
    return jokes


print(get_jokes(10, True))
