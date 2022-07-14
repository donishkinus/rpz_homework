"""Варіант 1"""
from random import randint

amount = 100
numbers = []
for i in range(amount):
    numbers.append(randint(-100, 100))
print(numbers)
print(max(numbers))
print(min(numbers))
x = max(numbers) - min(numbers)
print('Різниця між максимальним та мінімальним числом = ', x)