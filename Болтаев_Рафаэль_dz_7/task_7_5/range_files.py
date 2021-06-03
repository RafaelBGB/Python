import os
import random

folder = 'some_data'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
ext_list = ['txt', 'bin', 'py', 'csv']
for _ in range(100):
    f_ext = random.choice(ext_list)
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255)
    for _ in range(random.randrange(100)))
    with open(os.path.join(folder, f'{f_name}.{f_ext}'), 'wb') as f:
        f.write(f_content)
