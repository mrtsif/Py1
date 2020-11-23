a = input('Enter your sentence').split()
b = 1
for us in a:
    print(f'{b}. {us[0:10:1]}')
    b += 1
# Через enumerate перестает работать срез, почему-то
