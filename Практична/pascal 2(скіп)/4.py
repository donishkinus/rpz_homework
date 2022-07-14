import math

a = float(input('Введіть чисельник: '))
b = float(input('Введіть знаменник: '))
aa = int(a)
bb = int(b)
print('')

n = a / b
x = n / 2
xx = ((n+1)/2)
xn = int(x)
xxn = int(xx)

if (n / 2) is xn:
    print('True - число натуральне')
    print(n)
elif ((n+1)/2) is xxn:
    print('True - число натуральне')
    print(n)
else:
    print('false - Число ненатуральне')
    print(n)
