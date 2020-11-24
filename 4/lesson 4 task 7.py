def fact(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    yield a


for n in fact(int(input('Enter your number: '))):
    print(n)
