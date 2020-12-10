class Err(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, deliveryman, total_goods):
        self.d = deliveryman
        self.total = total_goods  # Колличество наименований товара всего

    def deliveryman(self):
        return f'{self.d} brought {self.total} types of goods'

    def dict(self):
        goods = {'product name': [], 'product price': [], 'quantity of goods': [], 'functionality': []}
        my_dict = {'product name': '', 'product price': '', 'quantity of goods': '', 'functionality': ''}
        z = 0
        while z < int(self.total):
            z += 1
            for n, i in enumerate(my_dict.keys(), 1):
                y = 0
                if n == 1:
                    while y == 0:
                        try:
                            my_property = input('What office equipment is it? ("1" - printer, "2" - scanner, '
                                                '"3" - xerox): ')
                            if int(my_property) > 3 or int(my_property) < 1:
                                raise Err("Only 1, 2 or 3!!!")
                        except Err as err:
                            print(err)
                        else:
                            my_dict[i] = my_property
                            goods[i].append(my_dict[i])
                            y = 1
                elif n == 4:
                    while y == 0:
                        try:
                            my_property = input('Is it regular or multifunctional? ("1" - regular,'
                                                ' "2" - regular or multifunctional): ')
                            if int(my_property) > 2 or int(my_property) < 1:
                                raise Err("Only 1 or 2!!!")
                        except Err as err:
                            print(err)
                        else:
                            my_dict[i] = my_property
                            goods[i].append(my_dict[i])
                            y = 1
                else:
                    my_property = input(f'Enter property value {i}: ')
                    my_dict[i] = my_property
                    goods[i].append(my_dict[i])
        return goods


class OfficeEq:

    def __init__(self, user):
        self.user = user

    def offer(self):
        return f'We can offer you {o.trans()[0]} printers ({o.trans()[1]} multifunctional),' \
               f' {o.trans()[2]} scanners ({o.trans()[3]} multifunctional) and {o.trans()[4]}' \
               f' xeroxes ({o.trans()[5]} multifunctional)' \
               f'. For total cost {o.trans()[6]}$'

    def trans(self):
        printers = 0
        mp = 0
        scanners = 0
        ms = 0
        xeroxes = 0
        mx = 0
        total_price = 0
        eq = []
        for i in w.dict().values():
            eq.append(i)
        for i, n in enumerate(eq[2]):
            if eq[0][i] == '1':
                printers += int(eq[2][int(i)])
                if eq[3][i] == '2':
                    mp += 1
            elif eq[0][i] == '2':
                scanners += int(eq[2][int(i)])
                if eq[3][i] == '2':
                    ms += 1
            elif eq[0][i] == '3':
                xeroxes += int(eq[2][int(i)])
                if eq[3][i] == '2':
                    mx += 1
        for n, i in enumerate(eq[1]):
            total_price += int(i) * int(eq[2][int(n)])
        return f'We can offer you {printers} printers ({mp} multifunctional),' \
               f' {scanners} scanners ({ms} multifunctional) and {xeroxes}' \
               f' xeroxes ({mx} multifunctional)' \
               f'. For total cost {total_price}$'


class Printer(OfficeEq):

    def printer(self):
        e = ''
        a = input('Do you need printer? ("y" - yes, "n" - no): ').lower()
        if a == 'y':
            b = input('How many?: ')
            c = input('Do you need multifunction printer? ("y" - yes, "n" - no): ').lower()
            if c == 'y':
                e += 'multifunction'
            else:
                e += 'regular'
            return f'{self.user} want to take {b} {e} printers'
        else:
            return 'see you soon!'


class Scanner(OfficeEq):
    def scanner(self):
        e = ''
        a = input('Do you need scanner? ("y" - yes, "n" - no): ').lower()
        if a == 'y':
            b = input('How many?: ')
            c = input('Do you need multifunction scanner? ("y" - yes, "n" - no): ').lower()
            if c == 'y':
                e += 'multifunction'
            else:
                e += 'regular'
            return f'{self.user} want to take {b} {e} scanners'
        else:
            return 'see you soon!'


class Xerox(OfficeEq):
    def xerox(self):
        e = ''
        a = input('Do you need xerox? ("y" - yes, "n" - no): ').lower()
        if a == 'y':
            b = input('How many?: ')
            c = input('Do you need multifunction xerox? ("y" - yes, "n" - no): ').lower()
            if c == 'y':
                e += 'multifunction'
            else:
                e += 'regular'
            return f'{self.user} want to take {b} {e} xeroxes'
        else:
            return 'see you soon!'


w = Warehouse('Upyachko', 3)
print(w.deliveryman())
o = OfficeEq('Kirill')
print(o.trans())
pr = Printer('Lida')
sc = Scanner('Yarik')
xe = Xerox('Sharik')
print(pr.printer())
print(sc.scanner())
print(xe.xerox())