from itertools import cycle, count
b = ['У попа была собака', 'Он ее любил', 'Она съела кусок мяса', 'Он ее убил', 'И в землю закопал', 'И надпись написал:']
a = cycle(b)
for i in count(1):
    if i > 23:
        break
    else:
        print(next(a))
