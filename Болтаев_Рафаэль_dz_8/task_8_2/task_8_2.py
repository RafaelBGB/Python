import re

with open('nginx_logs.txt') as f, open('result.txt', 'w', encoding='utf-8') as f_result:
    r_add = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    r_datetime = re.compile(r'(\[(.*)\])')
    r_type = re.compile(r'(?:")([A-Z]*)(?:\s)')
    r_resource = re.compile(r'(?:\s)(/\S*)')
    r_size = re.compile(r'(?:"\s\d*\s)(\d*)')
    r_code = re.compile(r'(?:"\s)(\d{1,10})')
    for i, el in enumerate(f, start=1):
        result = (r_add.search(el).group(1), r_datetime.search(el).group(1), (r_type.search(el).group(1)),
                  r_resource.search(el).group(1), r_size.search(el).group(1), r_code.search(el).group(1))
        print(i, result, file=f_result)
