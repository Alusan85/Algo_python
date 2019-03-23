"""
7.  В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random as rnd

ls_src = [rnd.randint(0, 10) for x in range(10000)]


def two_mins():
    """способ 1. 
    Поиск 2х минимумов 
    Сложность O(N)
    """
    min1 = float('inf')
    min2 = float('inf')
    ls = [*ls_src]

    for x in ls:
        if x < min1:
            min2 = min1
            min1 = x
            continue
        elif x < min2:
            min2 = x
    
    return [min1, min2]


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
            [arr[0]] + \
            qsort([x for x in arr[1:] if x >= arr[0]])


def with_qsort(mins_count=2):
    """способ 2. 
    Поиск любое кол-во минимумов
    O(N*log(N)).
    """
    sorted_list = qsort([*ls_src])
    return sorted_list[:mins_count]


def test_performance():
    import cProfile
    cProfile.run('two_mins()')
    cProfile.run('with_qsort()')


if __name__ == '__main__':
    test_performance()
