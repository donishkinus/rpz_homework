"""Варіант 9"""
from random import randint

amount = 10
numbers = []

for i in range(amount):
    numbers.append(randint(-20, 20))

print(numbers)
print(numbers[0])
print(numbers[1], numbers[2])
print(numbers[3], numbers[4], numbers[5])
print(numbers[6], numbers[7], numbers[8], numbers[9])