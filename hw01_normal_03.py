# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите число а: '))
print('a = ', a)
b = int(input('Введите число b: '))
print('b = ', b)
c = int(input('Введите число b: '))
print('c = ', c)

print('\n')

disc = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(disc)) / (2 * a)
x2 = (-b - math.sqrt(disc)) / (2 * a)

print('x1 = ', x1)
print('x2 = ', x2)
