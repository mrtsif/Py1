class Complex:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return f'{self.n1} + {self.n2}j'

    def __add__(self, other):
        return Complex(self.n1 + other.n1, self.n2 + other.n2)

    def __mul__(self, other):
        return Complex(self.n1 * self.n2 - other.n1 * other.n2, self.n1 * other.n2 + other.n1 * other.n2)




a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a * b)