from memory_profiler import profile

# Урок 2. Задача 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

@profile
def func():
    a = list(range(1000000))

    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]

    print("Два наименьших элемента:", min_num, min_num2)
    del a

if __name__ == '__main__':
    func()

'''
Интерпритаор Python 3.7  Win10 64 bit

Для запуска программы было выделено 13.1 MiB.
При создании списка "a" было выделено:
0,1 Mb = 10000 элементов
1.9 Мб = 100000 элементов
19.2 Мб = 1000000 элементов


После выполнения программы удалил список "a" , тем самым
освободил память 
0 Мб
1.3 Мб
19.1 Мб
Освобожденая память меньше чем бвло использовано на создание массива? Почему показывает погрешность?


0,1 Mb = 10000 элементов

Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func():
    10     13.2 MiB      0.1 MiB       a = list(range(10000))
    11                             
    12     13.2 MiB      0.0 MiB       min_num = a[0]
    13     13.2 MiB      0.0 MiB       min_num2 = a[1]
    14                             
    15     13.2 MiB      0.0 MiB       if min_num > min_num2:
    16                                     min_num, min_num2 = min_num2, min_num
    17                             
    18     13.2 MiB      0.0 MiB       for i in range(len(a)):
    19     13.2 MiB      0.0 MiB           if a[i] < min_num:
    20                                         min_num2 = min_num
    21                                         min_num = a[i]
    22     13.2 MiB      0.0 MiB           elif a[i] < min_num2:
    23     13.2 MiB      0.0 MiB               min_num2 = a[i]
    24                             
    25     13.2 MiB      0.0 MiB       print("Два наименьших элемента:", min_num, min_num2)
    26     13.2 MiB      0.0 MiB       del a

1.9 Мб = 100000

Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func():
    10     15.1 MiB      1.9 MiB       a = list(range(100000))
    11                             
    12     15.1 MiB      0.0 MiB       min_num = a[0]
    13     15.1 MiB      0.0 MiB       min_num2 = a[1]
    14                             
    15     15.1 MiB      0.0 MiB       if min_num > min_num2:
    16                                     min_num, min_num2 = min_num2, min_num
    17                             
    18     15.1 MiB      0.0 MiB       for i in range(len(a)):
    19     15.1 MiB      0.0 MiB           if a[i] < min_num:
    20                                         min_num2 = min_num
    21                                         min_num = a[i]
    22     15.1 MiB      0.0 MiB           elif a[i] < min_num2:
    23     15.1 MiB      0.0 MiB               min_num2 = a[i]
    24                             
    25     15.1 MiB      0.0 MiB       print("Два наименьших элемента:", min_num, min_num2)
    26     13.8 MiB      0.0 MiB       del a


19.2 Мб = 1000000

Line #    Mem usage    Increment   Line Contents
================================================
     8     13.1 MiB     13.1 MiB   @profile
     9                             def func():
    10     32.3 MiB     19.2 MiB       a = list(range(1000000))
    11                             
    12     32.3 MiB      0.0 MiB       min_num = a[0]
    13     32.3 MiB      0.0 MiB       min_num2 = a[1]
    14                             
    15     32.3 MiB      0.0 MiB       if min_num > min_num2:
    16                                     min_num, min_num2 = min_num2, min_num
    17                             
    18     32.3 MiB      0.0 MiB       for i in range(len(a)):
    19     32.3 MiB      0.0 MiB           if a[i] < min_num:
    20                                         min_num2 = min_num
    21                                         min_num = a[i]
    22     32.3 MiB      0.0 MiB           elif a[i] < min_num2:
    23     32.3 MiB      0.0 MiB               min_num2 = a[i]
    24                             
    25     32.2 MiB      0.0 MiB       print("Два наименьших элемента:", min_num, min_num2)
    26     13.1 MiB      0.0 MiB       del a

'''