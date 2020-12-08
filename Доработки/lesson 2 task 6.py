goods = []
my_dict = {'product name': '', 'product price': '', 'quantity of goods': '', 'product unit': ''}
analytics_dict = {'product name': [], 'product price': [], 'quantity of goods': [], 'product unit': []}
number = 0
while True:
    number += 1
    if input('Enter "q" to quit or anything else to continue: ').lower() == 'q':
        break
    else:
        for i in my_dict.keys():
            my_property = input(f'Enter property value {i}: ')
            my_dict[i] = my_property
            analytics_dict[i].append(my_dict[i])
        goods.append((number, my_dict))
print(f'goods: \n{goods}')
print(f'analytics: \n{analytics_dict}')


