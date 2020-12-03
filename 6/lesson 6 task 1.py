import time
import turtle
from itertools import cycle


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']
    def __running(self):
        window = turtle.Screen()
        c = 0
        for i in cycle(TrafficLight.__color):
            c += 1
            if c > 7:
                break
            turtle.pensize(100)
            turtle.color(i)
            turtle.circle(100)
            if i == 'red':
                time.sleep(7)
            elif i == 'green':
                time.sleep(1)
            else:
                time.sleep(2)


tl = TrafficLight()
tl._TrafficLight__running()
print(tl._TrafficLight__running())