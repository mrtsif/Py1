from googletrans import Translator
def func(a):
    translator = Translator()
    result = translator.translate(a, src='en', dest='ru')
    return result.text

file4upd = open("file004upd.txt", 'w', encoding='utf-8')
with open('file004.txt', 'r+', encoding='utf-8') as file4:
    try:
        for i in file4:
            a = ''
            b = ''
            for n in i:
                n = n.lower()
                if n.isalpha():
                    a += n
                elif n.isspace():
                    n = ' '
                else:
                    b += n
            end = str(func(a) + b)
            print(end, file=file4upd)
    except AttributeError:
        print('Проблема в блоке googletrans. Попробуйте еще раз!')
file4upd.close()