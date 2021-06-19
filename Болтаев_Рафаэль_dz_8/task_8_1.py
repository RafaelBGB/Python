import re


def email_parse(email):
    parse = re.split(r'@', email)
    if email.count('@') == 1 and parse[1].count('.'):
        return {'username': parse[0], 'domain': parse[1]}
    else:
        raise ValueError('Неправельный адрес электронной почты')


print(email_parse('someone@geekbrains.ru'))
