with open('file005.txt', 'w+', encoding='utf-8') as file5:
    a = input('Enter numbers with space: ').split()
    print(a, file=file5)
    b = 0
    file5.seek(0)
    for i in file5:
        for n in i:
            if n.isdigit():
                b += int(n)
            else:
                b += 0
    print(b)