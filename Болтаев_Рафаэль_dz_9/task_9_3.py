class Worker:
    def __init__(self, u_name, u_surname, u_position, u_wage, u_bonus):
        self.name = u_name
        self.surname = u_surname
        self.position = u_position
        self._income = {'wage': u_wage, 'bonus': u_bonus}


class Position(Worker):
    def __init__(self, u_name, u_surname, u_position, u_wage, u_bonus):
        super().__init__(u_name, u_surname, u_position, u_wage, u_bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


x = Position('Борис', 'Иванов', 'Слесарь', 100, 10)
print(x.name, x.surname, x.position, x._income)
print(x.get_full_name())
print(x.get_total_income())
