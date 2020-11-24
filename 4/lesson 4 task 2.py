from random import randint
or_list = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
print(f'Original list is: {or_list}')
new_list = [or_list[n] for n, i in enumerate(or_list) if or_list[n] > or_list[n-1] and n != 0]

print(new_list)
