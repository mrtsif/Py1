number = int(input('Enter number of month'))
if 0 < number <= 12:
    result = number // 3
    month = {1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter', 0: 'winter'}
    print(month.get(result))
else:
    print('Error')
