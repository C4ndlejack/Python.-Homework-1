quart = int(input("Введите цифру, обозначающую номер четверти: "))
if quart == 1:
    print("Диапазон четверти - x > 0, y > 0")
elif quart == 2:
    print("Диапазон четверти - x < 0, y > 0")
elif quart == 3:
    print("Диапазон четверти - x < 0, y < 0")
elif quart == 4:
    print("Диапазон четверти - x > 0, y < 0")
else:
    print("Четверть не существует!")