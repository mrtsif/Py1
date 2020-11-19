def sum():
    a = 0
    while True:
        n = input('please enter any numbers with space or "q" to exit: ').lower().split()
        if n[-1] == 'q':
            for i in n[0:-1:]:
                a += int(i)
            print(a)
            break
        elif n[1] == 'q':
            break
        else:
            for i in n[0::1]:
                if i.isdigit():
                    a += int(i)
                else:
                    print(f"I don't understand what is {i}")
            print(a)


sum()