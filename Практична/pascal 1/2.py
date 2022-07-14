"""Варіант 7"""
import math

g = 9.8
h = float(input('Введіть h(Висоту з якої падати): '))
v = float(input('Введіть швидкість падіння: '))

a = g / 2
b = v
c = -h

x1 = (-1 * b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
print('')
print(x1)
