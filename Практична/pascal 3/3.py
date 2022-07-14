"""Варіант 8"""
import math
a = float(input('Введіть a: '))
b = float(input('Введіть b: '))

try:
    x = (a**2-b**2) ** 0.5
    y = 1/(a**2 - b**2)
    x = format(x, '.2f')
    y = format(y, '.2f')
    print(x)
    print(y)
except:
    print('Error!!!Try again!')
