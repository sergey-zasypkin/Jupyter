# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
print(f'Сумма элементов, стоящих на нечетной позиции = {sum((list_new :=[randint(0, 10) for _ in range(int(input("Введите количество чисел в списке: ")))])[1::2])}')