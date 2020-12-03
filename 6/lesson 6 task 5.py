class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'start drawing {self.title}')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'start drawing by pen {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'start drawing by pencil {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'start drawing by handle {self.title}')


s = Stationery('paint')
p = Pen('parker')
pcl = Pencil('bic')
h = Handle('erich')
s.draw()
p.draw()
pcl.draw()
h.draw()
