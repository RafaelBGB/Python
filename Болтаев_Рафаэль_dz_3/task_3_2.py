def thesaurus(*args):
    name_list = list(args)
    name_dic = {}
    for i, el in enumerate(name_list):
        if el[0] in name_dic:
            name_dic[el[0]].append(el)
        else:
            name_dic.setdefault(el[0], list(name_list[i].split()))
    return name_dic


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


def thesaurus_adv(*args):
    user_list = list(args)
    name = list(map(lambda n: n.split()[0], user_list))
    surname = list(map(lambda n: n.split()[1], user_list))
    fam_dic = {}
    for i, e in enumerate(surname):
        if e[0] in fam_dic:
            if name[i][0] in fam_dic[e[0]]:
                fam_dic[e[0]][name[i][0]].append(user_list[i])
            else:
                fam_dic.setdefault(e[0], {})
                fam_dic[e[0]].setdefault(name[i][0], list(user_list[i].split(',')))
        else:
            fam_dic.setdefault(e[0], {})
            fam_dic[e[0]].setdefault(name[i][0], list(user_list[i].split(',')))
    return fam_dic


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print('Неотсортированный словарь', result)

sort_result = {}
for f_k in sorted(result.keys()):
    sort_result.setdefault(f_k, {})
    for s_k in sorted(result[f_k].keys()):
        sort_result[f_k].setdefault(s_k, result[f_k][s_k])
print('Отсортированный словарь', sort_result)
