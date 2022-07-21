"""Варіант 12"""

amount = int(input('Введіть кількість товарів в магазині:'))

name = []
unit = []
price = []
number = []

for i in range(amount):
    name.append(input('Введіть назву:'))
    unit.append(input('Введіть одиницю виміру:'))
    price.append(input('Введіть ціну:'))
    number.append(input('Введіть кількість товару:'))

print('')
for i in range(amount):
    print(name[i], unit[i], price[i], number[i])
    i +=1