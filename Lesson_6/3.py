#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
import timeit
from memory_profiler import profile

# Вариант 1 (простой)
# @profile
def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

# Вариант 2 (решето Эратосфена)
# @profile
def eratosfen(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

i = int(input('Введите порядковый номер искомого простого числа:'))
#print(simple(i))
#print(eratosfen(i))
print(timeit.timeit("simple(i)", setup="from __main__ import simple,i", number=100))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen,i", number=100))

"""
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
0.0037587000000001147
0.6719890999999998
Время работы алгоритмов для поиска 100-го простого числа 100 раз:
0.46190320000000007
0.6652361999999998
Время работы алгоритмов для поиска 200-го простого числа 100 раз:
2.3344392999999997
0.6729155000000002
Время работы алгоритмов для поиска 300-го простого числа 100 раз:
5.6165216
0.6430594999999997
Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
83.2333837
0.6620678000000026

Алгоритм решета Эратосфена эффективен для поиска простого числа с большим порядковым номером.
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
"""
'''
Line #    Mem usage    Increment   Line Contents
================================================
     8     13.2 MiB     13.2 MiB   @profile
     9                             def simple(i):
    10     13.2 MiB      0.0 MiB       count = 1
    11     13.2 MiB      0.0 MiB       n = 2
    12     13.2 MiB      0.0 MiB       while count <= i:
    13     13.2 MiB      0.0 MiB           t = 1
    14     13.2 MiB      0.0 MiB           is_simple = True
    15     13.2 MiB      0.0 MiB           while t <= n:
    16     13.2 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    17     13.2 MiB      0.0 MiB                   is_simple = False
    18     13.2 MiB      0.0 MiB                   break
    19     13.2 MiB      0.0 MiB               t += 1
    20     13.2 MiB      0.0 MiB           if is_simple:
    21     13.2 MiB      0.0 MiB               if count == i:
    22     13.2 MiB      0.0 MiB                   break
    23     13.2 MiB      0.0 MiB               count += 1
    24     13.2 MiB      0.0 MiB           n += 1
    25     13.2 MiB      0.0 MiB       return n


Line #    Mem usage    Increment   Line Contents
================================================
    28     13.2 MiB     13.2 MiB   @profile
    29                             def eratosfen(i):
    30     13.2 MiB      0.0 MiB       n = 2
    31     13.2 MiB      0.0 MiB       l = 1000
    32     13.2 MiB      0.0 MiB       sieve = [x for x in range(l)]
    33     13.2 MiB      0.0 MiB       sieve[1] = 0
    34     13.2 MiB      0.0 MiB       while n < l:
    35     13.2 MiB      0.0 MiB           if sieve[n] != 0:
    36     13.2 MiB      0.0 MiB               m = n*2
    37     13.2 MiB      0.0 MiB               while m < l:
    38     13.2 MiB      0.0 MiB                   sieve[m] = 0
    39     13.2 MiB      0.0 MiB                   m += n
    40     13.2 MiB      0.0 MiB           n += 1
    41     13.2 MiB      0.0 MiB       return [p for p in sieve if p != 0][i-1]


'''