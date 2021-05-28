n = 100

# Задание 1
def yie_odd_num (num):
    for x in range(1, n+1, 2):
        yield x


print(*yie_odd_num(n))

# Задание 2
odd_num = (num for num in range(1, n+1, 2))
print(*odd_num)
