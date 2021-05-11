def div_to_7(number):
    if number % 7 == 0:
        return True
    else:
        return False


def sum_numbers(numb):
    result = 0
    for n in numb:
        sum_digit = 0
        check = n
        while check // 10 != 0:
            sum_digit += check % 10
            check //= 10
        else:
            sum_digit += check % 10

        if div_to_7(sum_digit):
            result += n

    print(result)


odd_list = []
for i in range(1, 1000, 2):
    odd_list.append(i ** 3)

sum_numbers(odd_list)

for p in range(len(odd_list)):
    odd_list[p] += 17

sum_numbers(odd_list)
