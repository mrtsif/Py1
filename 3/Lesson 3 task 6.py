def func(n):
    return n.title()


l = []
n = input('Enter your sentence^ ').split()
for i in n:
    l.insert(-1, func(i))
print(l)
