# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random.randint(1,100))
        b.append(n)
        print('%5d' % n, end='') # собрали массив (строку)
    a.append(b)                  # поместили массив в массив
    print()

mx = -1
for j in range(M):
    mn = 100 # задаем границу для максимальных элементов
    for i in range(N):
        if a[i][j] < mn: # идем по столбцам, сначала 1 элемент из массива массивов
            mn = a[i][j]
    if mn > mx:
        mx = mn

print("Максимальный среди минимальных: ", mx)
