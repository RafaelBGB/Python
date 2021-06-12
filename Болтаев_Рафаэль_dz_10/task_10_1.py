class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self, add_list=None):
        i_list = add_list if add_list else self.m_list
        res = ''
        for el in i_list:
            res += ''.join(str(el)) + '\n'
        return res

    def __add__(self, other):
        s_result = []
        for i, el in enumerate(self.m_list):
            if len(self.m_list) != len(other.m_list) or len(el) != len(other.m_list[i]):
                print('Сложение матриц разных размеров невозможно')
                exit()
            else:
                s_result.append([v + other.m_list[i][k] for k, v in enumerate(el)])
        return self.__str__(s_result if s_result != [] else None)


x1 = Matrix([[31, 22, 24], [37, 43, 50], [51, 86, 20]])
x2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
x3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(x1, sep='')
print(x2, sep='')
print(x3, sep='')

print(x1 + x2, sep='')
