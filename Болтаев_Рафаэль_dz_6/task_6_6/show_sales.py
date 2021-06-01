import itertools


def show_sales(argv):
    program, *i = argv
    start = (int(i[0]) - 1 if i else 0)
    stop = (int(i[1]) if i and len(i) > 1 else None)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(*itertools.islice(f, start, stop))


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))
