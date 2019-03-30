'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
'''

import random

def median(array, k):
    if len(array) == 1:
        return array[0]

    center = random.choice(array) # начинаем от случайной точки

    left_el = [el for el in array if el < center]
    right_el = [el for el in array if el > center]
    center = [el for el in array if el == center]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(center):
        return center[0]
    else:
        return median(right_el, k - len(left_el) - len(center))


M = 7
lst = [random.randint(0, 20) for _ in range(2 * M + 1)]
print("Список: ", lst)
print("Медиана: ", median(lst, len(lst) / 2))

lst.sort() # Проверка всроенными функциями
print("Список после сортировки:", lst)
print("Медиана: ", lst[len(lst) // 2])