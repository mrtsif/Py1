with open('file002.txt', 'w+', encoding='utf-8') as file2:
    file2.write(f' Фамилия: Гобачев \n Имя: Михаил \n Желаемый уровень заработной платы (Оклад + Премии): 10000 + 15000000 = {10000 + 15000000}\n +str\n i\n +str\n +str\n Python')
    file2.seek(0)
    a = 0
    for i in file2:
        b = 0
        a += 1
        #print(i, end='')
        for n in i:
            if n.isspace():
                b += 0
            else:
                b += 1
        if b > 1:
            print(f'There are {b} visible symbols in line №{a}')
        else:
            print(f'There is {b} visible symbol in line №{a}')
    if a > 1:
        print(f'There are {a} lines in file002.txt')
    else:
        print(f'There is {a} line in file002.txt')
