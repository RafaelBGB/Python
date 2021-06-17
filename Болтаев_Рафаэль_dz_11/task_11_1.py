class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def transform_to_int(cls, param):
        return [int(el) for el in param.date_str.split('-')]

    @staticmethod
    def v_num(num_list):
        return 0 < num_list[0] <= 31 and 0 < num_list[1] <= 12 and 0 < num_list[2]


x = Date('15-06-2021')
print(Date.transform_to_int(x))
print(Date.v_num(Date.transform_to_int(x)))
