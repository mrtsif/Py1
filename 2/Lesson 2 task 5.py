rate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_rate = int(input('Enter your rate'))
a = 0
for i in rate:
    if new_rate <= i:
        a += 1
rate.insert(a, new_rate)
print(rate)
