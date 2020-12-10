class Err(Exception):
    def __init__(self, text):
        self.text = text


divider = 0#int(input('Please, enter positive number: '))
try:
    if divider == 0:
        raise Err('Only positive!!')
    a = 100 // divider
except Err as err:
    print(err)
else:
    print('the end')
