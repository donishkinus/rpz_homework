"""Варіант 4"""
import math

x = float(input('Введіть x: '))
y = float(input('Введіть y: '))
z = float(input('Введіть z: '))

a = y + (z / (y**2) + math.fabs((x**2) / y + (x**2)))
b = (1 + math.tan(z/2)**2)**2

print('Рівняння a= ', a)
print('Рівняння b= ', b)
