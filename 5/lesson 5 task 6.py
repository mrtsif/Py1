with open('file006.txt', 'r+', encoding='utf-8') as file6:
    a = ''
    for i in file6:
        for n in i:
            if n.isdigit():
                a += n
            elif n.isalnum() or n == ' ':
                a += n
    b = a.lower()
    b = a.split()
    с = []
    print(b)
