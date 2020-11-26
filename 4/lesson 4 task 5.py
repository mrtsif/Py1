from functools import reduce


def func(el1, el2):
    return el1 + el2


my_list = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(func, l))
