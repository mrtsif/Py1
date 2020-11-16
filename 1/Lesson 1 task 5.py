income = float(input('Enter your income'))
costs = float(input('Enter your costs'))
profit = income - costs
if income > costs:
    print(f'Your firm is profitable. Return on equity is: {profit / income}')
elif income == costs:
    print('You did not earn anything')
else:
    print(f'Your firm is not profitable. Net loss is: {profit}')
staff = int(input('Enter the number of staff'))
print(f'Revenue per employee is: {profit / staff}')
