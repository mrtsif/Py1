with open('file001.txt', 'w+', encoding='utf-8') as file1:
    file1.write(f' Фамилия: Гобачев \n Имя: Михаил \n Желаемый уровень заработной платы (Оклад + Премии): 10000 + 15000000 = {10000 + 15000000}\n')
    file1.seek(0)
    content = file1.read()
    print(content)
