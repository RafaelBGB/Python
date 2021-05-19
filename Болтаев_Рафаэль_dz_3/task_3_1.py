def num_translate(eng_n, trans):
    print(trans.get(eng_n))


def num_translate_adv(eng_num, translate):
    if eng_num.istitle():
        print(translate.get(eng_num.lower()).title())
    else:
        print(translate.get(eng_num))


translate_dic = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'дестять'
    }

user_num = input('Введите число на англиском языке: ')
num_translate(user_num, translate_dic)
num_translate_adv(user_num, translate_dic)

