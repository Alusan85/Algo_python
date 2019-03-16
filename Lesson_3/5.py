#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random
N = 10
array = [0]*N
for i in range(N):
    array[i] = int(random.randint(-20,20))
    print(array[i],end=' ')
print()

i = 0
poss = -1
while i < N:
    if array[i] < 0 and poss == -1:
        poss = i
    elif array[i] < 0 and array[i] > array[poss]:
        poss = i
    i += 1

print(poss + 1, ':', array[poss])