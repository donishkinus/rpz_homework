from random import randint
numbers = {'a' : [] ,'b' : [] }
n = int(input('Введіть кількість чисел в списках:'))

numbers['a'] = [randint(-100, 100) for i in range(n)]
numbers['b'] = [randint(-100, 100) for i in range(n)]

sum_a = sum(numbers.get('a'))
sum_b = sum(numbers.get('b'))

print(numbers)
print('----------------------------------------')
if sum_a > sum_b :
    print('Сума більшого словника =',sum_a, '|Ключ словника = ','"a"')
else :
    print('Сума більшого словника =',sum_b, '|Ключ словника = ','"b"')

