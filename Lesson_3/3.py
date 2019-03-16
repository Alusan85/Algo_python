#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random
N = 10
array = [0]*N
for i in range(N):
    array[i] = int(random.randint(1,100))
    print(array[i],end=' ')
print()

mn = min(array)
mx = max(array)
imn = array.index(mn)
imx = array.index(mx)

print("Минимальный  элемент [{}], Максимальный элемент [{}]".format (mn, mx))

array[imn],array[imx] = array[imx],array[imn]

for i in range(N):
    print(array[i],end=' ')
print()