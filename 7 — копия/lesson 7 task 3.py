class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'The result is: {self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell - other.cell)
        else:
            return f'{self.cell} less than {other.cell}!!! '

    def __floordiv__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell // other.cell)
        else:
            return f'{self.cell} less than {other.cell}!!! '

    def make_order(self, raw):
        self.raw = raw
        a = ''
        b = 0
        for i in range(self.cell):
            b += 1
            if b >= self.raw:
                a += '*\n'
                b = 0
            else:
                a += '*'
        return a


cell_1 = Cell(102)
cell_2 = Cell(122)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(12))
