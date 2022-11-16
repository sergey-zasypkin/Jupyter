#Напишите программу, 
#которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Error! Введите целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5) # При округлении до 2 знаков после запятой результат будет 5,10, а не 5,09.
    lengthSegment = int(lengthSegment * 100) # Поэтому взял это решение в стороках 24 и 25.
    lengthSegment = float(lengthSegment/100) 
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")