from random import randint
numbers = []*10
for i in range(10):
    numbers.append(randint(-10, 10))
print(numbers)

i = 0
summax = 0
summin = 0
while i < len(numbers):
    if numbers[i] >= 0:
        summax = summax + numbers[i]
        print(summax,'+')
        i = i + 1
    else:
        summin = summin + numbers[i]
        print(summin,'-')
        i = i + 1

if abs(summax) > abs(summin):
    print('plus bilshe')
else :
    print('minus bilshe')
