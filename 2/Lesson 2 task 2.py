a = input('Enter value with space').split()
b = 1
c = 0
for i in a[0::2]:
    a.pop(c)
    a.insert(b, i)
    b += 2
    c += 2
print(a)
