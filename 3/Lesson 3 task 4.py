def f():
    a = int(input('Please, enter positive number'))
    b = int(input('Please, enter negative number'))
    if a > 0 and b < 0:
        n = -1
        while n < abs(b - 2):
            a *= a
            return round((1 / a), 4)
    else:
        return 'Look at the task'


print(f())
