"""Варіант 12"""

a = float(input('Введіть a: '))
i = a
kv = 0
while i > 2:
    b = i**2
    kv = b + kv
    i = i - 1
    print('Сума квадратів усіх цілих чисел = ',kv)
