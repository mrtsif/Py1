class Err(Exception):
    def __init__(self, text):
        self.text = text


a = []
while True:
    try:
        b = input('Enter the number or "q" to exit: ')
        if b.isdigit():
            a.append(int(b))
        elif b == 'q':
            break
        else:
            raise Err('What the...')
    except Err as err:
        print(err)
print(a)
