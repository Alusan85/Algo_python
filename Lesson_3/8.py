"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

M = 5
N = 4
array_a = []

for i in range(N):
    array_b = []
    sum = 0
    print("Введите числа {} строки :".format(i+1))
    for j in range(M - 1):
        n = int(input())
        sum += n
        array_b.append(n) # помещаем 4 элемента (числа)
    array_b.append(sum) # помещаем сумму 5 элементов в 5 элемент массива

    array_a.append(array_b) # помещаем массив в массив
print("Полученная матрица :")
for i in array_a:
    print(i)


