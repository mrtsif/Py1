class Road:

    def __init__(self, _length, _width):
        self.l = _length
        self.w = _width
        print(f'{_length}м * {_width}м * 25кг * 5см = {round(_length * _width * 0.025 * 5, 2)}тн')

r = Road(20, 5000)
