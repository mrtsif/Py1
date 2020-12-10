class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def trans(cls, date):
        a = []
        for i in date.split('-'):
            a.append(int(i))
        cls(date)
        return a

    @staticmethod
    def valid():
        for n, i in enumerate(Data(d).date):
            if n == 0 and 1 > i or n == 0 and i > 31:
                return f'Incorrect date ({i})'
            elif n == 1 and 1 > i or n == 1 and i > 12:
                return f'Incorrect date ({i})'
            elif n == 2 and 1800 > i or n == 2 and i > 2240:
                return f'Incorrect date ({i})'
        return 'Correct date!'


d = Data.trans('12-11-2020')
print(*d, sep=', ')
print(Data.valid())
