# 4.	Определить, какое число в массиве встречается чаще всего.

import random
N = 15
array = [0]*N
for i in range(N):
    array[i] = int(random.randint(1,20))
    print(array[i],end=' ')
print()

num = array[0]
max_frq = 1

for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Нет повторений')