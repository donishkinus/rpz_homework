"""Варіант 2"""
print('Введіть вектор а')
ax = int(input('Введіть вектор аx: '))
ay = int(input('Введіть вектор аy: '))
az = int(input('Введіть вектор аz: '))
print('')
print('Введіть вектор b')
bx = int(input('Введіть вектор bx: '))
by = int(input('Введіть вектор by: '))
bz = int(input('Введіть вектор bz: '))
print('Вектор а = ', ax, ay, az)
print('Вектор b = ', bx, by, bz)

sk = ax*bx + ay*by + az*bz
print('Скалярний добуток векторів = ', sk)

vec_dob_a = ay*bz - az*by
vec_dob_b = az*bx - ax*bz
vec_dob_z = ax*by - ay*bx

print('Векторний добуток = ', vec_dob_a, vec_dob_b, vec_dob_z)