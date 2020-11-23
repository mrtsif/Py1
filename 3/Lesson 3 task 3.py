def my_func():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + c
    else:
        return a + b


print(my_func())
