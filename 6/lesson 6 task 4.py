class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_police

    def go(self):
        print("let's start")

    def stop(self):
        print('stop!')

    def turn(self):
        a = input('Where do you want to turn?'
                  ' Enter "R" to turn right, enter "L" to turn left, enter "F" to keep going').lower()
        if a == 'l':
            print('The car turned left')
        elif a == 'r':
            print('The car turned right')
        elif a == 'f':
            print('The car is keep going')
        else:
            print('There was a car crash')

    def show_speed(self):
        print(f'Your speed is {self.s}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.s > 60:
            print('you got over speed')
        else:
            print(f'Your speed is {self.s}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.s > 40:
            print('you got over speed')
        else:
            print(f'Your speed is {self.s}')


class PoliceCar(Car):
    pass


c = Car(43, 'gray', 'lada')
t = TownCar(55, 'red', 'dodge')
s = SportCar(110, 'gray', 'ferrari')
w = WorkCar(60, 'gray', 'gazel')
p = PoliceCar(109, 'white', 'ford')
c.go()
t.turn()
t.show_speed()
s.show_speed()
w.show_speed()
