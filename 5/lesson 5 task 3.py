with open('file003.txt', 'r', encoding='utf-8') as file3:
    infernal_salary = int(20000)
    total_salary = 0
    people = 0
    poor_guys = []
    for i in file3:
        name = ''
        salary = 0
        for n in i.split():
            if n.isspace():
                n = 0
            elif n.isalpha():
                name += n
            else:
                try:
                    if float(n):
                        salary += float(n)
                except ValueError:
                    n = 0
        if salary <= infernal_salary:
            poor_guys.append(name)
        total_salary += salary
        people += 1
    if total_salary / people > 40000:
        print(f'Your average salary is okay ({total_salary / people}), but some of your employees are gonna become bums ({", ".join(poor_guys)})')
    else:
        print(
            f'Your average salary is not okay ({total_salary / people}). Some of your employees are gonna become bums ({", ".join(poor_guys)}). You are monster!')
