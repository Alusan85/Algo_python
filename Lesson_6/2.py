# Урок 3. Задача 2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from memory_profiler import profile

@profile
def func2():
    a = list(range(1000000))
    b = []

    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(i+1)

    del a
    return b

if __name__ == '__main__':
    func2()

"""
Интерпритатор Python 3.7  Win10 64 bit

Для запуска программы было выделено 13.1 MiB.
При создании списка "a" было выделено:
0,2 Mb = 10000 элементов
1.9 Мб = 100000 элементов
19.2 Мб = 1000000 элементов


После выполнения программы удалил список "a" , тем самым
освободил память 
0 Мб
1.9 Мб
19 Мб


Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func2():
    10     13.3 MiB      0.2 MiB       a = list(range(10000))
    11     13.3 MiB      0.0 MiB       b = []
    12                             
    13     13.4 MiB      0.1 MiB       for i in range(len(a)):
    14     13.4 MiB      0.0 MiB           if a[i] % 2 == 0:
    15     13.4 MiB      0.0 MiB               b.append(i+1)
    16                             
    17     13.4 MiB      0.0 MiB       del a
    18     13.4 MiB      0.0 MiB       return b



Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func2():
    10     15.0 MiB      1.9 MiB       a = list(range(100000))
    11     15.0 MiB      0.0 MiB       b = []
    12                             
    13     16.5 MiB      0.1 MiB       for i in range(len(a)):
    14     16.5 MiB      0.0 MiB           if a[i] % 2 == 0:
    15     16.5 MiB      0.1 MiB               b.append(i+1)
    16                             
    17     14.6 MiB      0.0 MiB       del a
    18     14.6 MiB      0.0 MiB       return b



Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func2():
    10     32.3 MiB     19.2 MiB       a = list(range(1000000))
    11     32.3 MiB      0.0 MiB       b = []
    12                             
    13     45.6 MiB      0.1 MiB       for i in range(len(a)):
    14     45.6 MiB      0.0 MiB           if a[i] % 2 == 0:
    15     45.6 MiB      0.2 MiB               b.append(i+1)
    16                             
    17     26.6 MiB      0.0 MiB       del a
    18     26.6 MiB      0.0 MiB       return b
"""