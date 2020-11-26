l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
p = [i for i in l if l.count(i) < 2]
print(p)