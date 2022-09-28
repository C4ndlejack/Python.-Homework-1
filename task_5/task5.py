from cmath import sqrt


print("Первая точка: ")
x1 = int(input("Введите значение координаты x: "))
y1 = int(input("Введите значение координаты y: "))
print("Вторая точка: ")
x2 = int(input("Введите значение координаты x: "))
y2 = int(input("Введите значение координаты y: "))
dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f"Расстояние между точками равно: {round(dist.real, 3)}")