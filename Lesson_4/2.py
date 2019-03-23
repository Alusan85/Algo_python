"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import time
import timeit

start = timeit.default_timer()

def ne_resheto(n, d):
    number=[]
    for i in range (d+1):
        number.append(i)
    lst=[]
    for i in range(2, d+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[n-1]

def resheto(n, d):
    a = []
    for i in range (d+1):
        a.append(i)
    lst = []

    i = 2
    while i <= d:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, d+1, i):
                a[j] = 0
        i += 1
    return lst[n-1]

n = int(input("Введите номер простого числа - "))
d = int(input("Введите количество чисел - "))

print("{} простое число  - это число {}".format(n, ne_resheto(n,d)))
print("{} простое число  - это число {}".format(n, resheto(n,d)))

print("Время без решета ", timeit.timeit("ne_resheto(n, d)", setup="from __main__ import ne_resheto, n, d"))
print("Время с решетом ", timeit.timeit("resheto(n, d)", setup="from __main__ import resheto, n, d"))

stop = timeit.default_timer()
execution_time = stop - start

print("Общее время выполнения программы: ", execution_time)

"""
Введите номер простого числа - 1
Введите количество чисел - 5
Время без решета  5.008579600000001
Время с решетом  4.892189499999999

Введите номер простого числа - 1
Введите количество чисел - 10
Время без решета  9.0746573
Время с решетом  7.682746199999999

Введите номер простого числа - 1
Введите количество чисел - 15
Время без решета  14.278084800000002
Время с решетом  10.9597233

Введите номер простого числа - 1
Введите количество чисел - 20
Время без решета  21.0703526
Время с решетом  14.441801900000002

Введите номер простого числа - 2
Введите количество чисел - 50
Время без решета  64.886644
Время с решетом  30.5402081

Вывод: Решете Эратосфена выиграет при использовании больших чисел
"""

