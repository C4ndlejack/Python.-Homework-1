day = int(input("Введите цифру, обозначающую день недели: "))
if day == 6 or day == 7:
    print("Это выходной день!")
elif day <= 5 and day >= 1: 
    print("Это рабочий день.")
else:
    print("Некорректное число!")