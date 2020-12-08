dict = {}
with open("text_6.txt", 'r+', encoding='utf8') as tf1:
    for i in tf1:
        name, info = i.split(':')
        result = sum(map(int, ''.join([n for n in info if n == ' ' or '9' >= n >= '0']).split()))
        dict[name] = result
print(f'{dict}')