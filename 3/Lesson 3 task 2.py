def info():
    gender = input('Please, enter your gender "m" or "f": ').lower()
    name = input('Please, enter your name: ')
    surname = input('Please, enter your surname: ')
    city = input('Please, enter your location: ')
    age = input('Enter your age: ')
    if name.isalpha() and surname.isalpha() and city.isalpha() and age.isdigit() and gender == 'm':
        return f'Here is {name.title()} {surname.title()}. He lives in {city.title()}. He is {age} years old'
    elif name.isalpha() and surname.isalpha() and city.isalpha() and age.isdigit() and gender == 'f':
        return f'Here is {name.title()} {surname.title()}. She lives in {city.title()}. She is {age} years old'
    else:
        return 'Incorrect data'


print(info())
