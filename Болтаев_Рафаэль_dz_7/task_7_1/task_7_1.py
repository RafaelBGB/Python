import os

with open('config.yaml', 'r', encoding='utf-8') as f:
    try:
        fol_list = [el.strip().split('|--')[-1] for el in f]
        os.mkdir(fol_list[0])
        os.chdir(fol_list[0])
        for el in fol_list[1:]:
            os.mkdir(el)

    except FileExistsError:
        print('Такая папка уже существует')
