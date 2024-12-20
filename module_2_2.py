first = int(input('Введи превое число: '))
second = int(input('Введи второе число: '))
third = int(input('Введи третье число:'))

if first != second and first != third and second != third:
    print(0)
elif first == second and first == third and first == second:
    print(3)
else:
    print(2)
