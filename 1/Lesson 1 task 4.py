i = int(input('Enter your number'))
a = i % 10
b = 1
c = 10
while b > 0:
    b = i // c % 10
    if b > a:
        a = b
    else:
        c *= 10
print(a)
