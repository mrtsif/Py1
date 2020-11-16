a = float(input('Enter the first-day distance'))
b = float(input('Enter the target distance'))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f"Sportsmen's result reach {b} kilometers at {i} day")
