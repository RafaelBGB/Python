import re

user_email = 'someone@geekbrains.ru'
if user_email.count('@') == 1:
    parse = re.split(r'@', user_email)
    result = {'username': parse[0], 'domain': parse[1]}
else:
    raise ValueError('Неправельный адрес электронной почты')

print(result)
