class Worker:
    def __init__(self):
        self.name = 'Vanya'
        self.surname = 'Igorenko'
        self.position = 'engineer'
        self._income = {'wage': 125000, 'bonus': 5000}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{sum(self._income.values())}')


a = Position()
a.get_full_name()
a.get_total_income()
