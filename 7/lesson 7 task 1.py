class Matrix:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        e = ''
        v = ''
        for i in self.a:
            for m, k in enumerate(i):
                v += '\t' + str(k)
            e += (v + '\n')
            v = ''
        return e

    def __add__(self, other):
        result = []
        numbers = []
        for i, z in enumerate(self.a):
            for j, x in enumerate(z):
                summa = self.a[i][j] + other.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(z):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


q = Matrix([[1, 2, 3, 5], [4, 5, 6], [7, 8]])
s = Matrix([[5, 2, 3, 5], [4, 5, 6], [7, 8]])
print(q + s)
