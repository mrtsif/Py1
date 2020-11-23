def div(arg1, arg2):
    try:
        print(f'Division result is: {round(arg1 / arg2, 3)}')
    except ZeroDivisionError:
        print('Error')


div(int(input('Please, enter first number')), int(input('Please, enter second number')))
