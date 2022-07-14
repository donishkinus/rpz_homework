"""Варіант 3"""
print('Введіть Матрицю А')
a11 = int(input('Введіть a11 :'))
a12 = int(input('Введіть a12 :'))
a13 = int(input('Введіть a13 :'))
a21 = int(input('Введіть a21 :'))
a22 = int(input('Введіть a22 :'))
a23 = int(input('Введіть a23 :'))
a31 = int(input('Введіть a31 :'))
a32 = int(input('Введіть a32 :'))
a33 = int(input('Введіть a33 :'))

print('')
print('Введіть Матрицю B')
b11 = int(input('Введіть b11 :'))
b12 = int(input('Введіть b12 :'))
b13 = int(input('Введіть b13 :'))
b21 = int(input('Введіть b21 :'))
b22 = int(input('Введіть b22 :'))
b23 = int(input('Введіть b23 :'))
b31 = int(input('Введіть b31 :'))
b32 = int(input('Введіть b32 :'))
b33 = int(input('Введіть b33 :'))

c11 = a11*b11 + a12*b21 + a13*b31
c12 = a11*b12 + a12*b22 + a13*b32
c13 = a11*b13 + a12*b23 + a13*b33
c21 = a21*b11 + a22*b21 + a23*b31
c22 = a21*b12 + a22*b22 + a23*b32
c23 = a21*b13 + a22*b23 + a23*b33
c31 = a31*b11 + a32*b21 + a33*b31
c32 = a31*b12 + a32*b22 + a33*b32
c33 = a31*b13 + a32*b23 + a33*b33

print('Добуток матриць А та B = ')
print(c11, c12, c13)
print(c21, c22, c23)
print(c31, c32, c33)