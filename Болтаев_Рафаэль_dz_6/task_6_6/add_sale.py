def add_sale(argv):
    program, i = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(f'{i} \n')


if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))
