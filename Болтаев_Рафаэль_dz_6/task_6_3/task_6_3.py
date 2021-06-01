import sys

with open('users.csv', 'r', encoding='utf-8') as f_users, open('hobby.csv', 'r', encoding='utf-8') as f_hobby:

    users = (el.replace(',', ' ').replace('\ufeff', '').strip() for el in f_users)
    hobby = (vol.replace('\ufeff', '').strip() for vol in f_hobby)
    users_dict = {u: next(hobby, None) for u in users}

    if next(hobby, None):
        sys.exit(1)

    print(users_dict)

