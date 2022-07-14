"""Варіант 11"""
import math
x = float(input('Введіть x: '))
y = float(input('Введіть y: '))

if x < 0 and y < 0:
    x = math.fabs(x)
    x = x * 10
    print('x = ',x)
    print('y = ',y)
elif x < 0 or y < 0:
    y = y + 0.5
    print('x = ', x)
    print('y = ', y)
else:
    print('x = ', x)
    print('y = ', y)