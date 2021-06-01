import requests

log = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

log_to_line = log.split('\n')
res_list = ((el.split()[0], el.split()[5][1:], el.split()[6]) for el in log_to_line if el)

spam = {}
for el in res_list:
    if el[0] in spam:
        spam[el[0]] += 1
    else:
        spam.setdefault(el[0], 1)

spammer = [0, 0]
for key in spam:
    if spam[key] > spammer[1]:
        spammer = [key, spam[key]]

print(f'IP спамера:{spammer[0]}, количество запросов: {spammer[1]}')



