"""Варіант 1"""
import math

x = float(input('Введіть x: '))

if x > 1 and x < 2:
    y = math.cos(x)**2
    print(y,'Через косинус')
if x >= 2 or x <= 0:
    y = 1 + math.sin(x)**2
    print(y,'Через синус')
