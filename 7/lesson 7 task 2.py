class Clothes:
    def __init__(self, name):
        self.n = name


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def func(self):
        return f'{self.n} requires {round(self.v / 6.5 + 0.5, 2)} m2 of textile'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 10:
            self.__height = 10
        elif height > 100:
            self.__height = 100
        else:
            self.__height = height

    def func(self):
        return f'{self.n} requires {round(2 * self.height + 0.3, 2)} m2 of textile'


c = Coat('Softy', 10)
s = Suit('Tighty', 1)
print(c.func)
print(s.func())
