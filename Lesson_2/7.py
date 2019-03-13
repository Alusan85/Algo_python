# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# # 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def sum_n(n):
    if n == 1:
        return 1
    else:
        return sum_n(n - 1) + n

n = int(input('Введите верхнюю границу множества: '))

for i in range(1, n + 1):
    if sum_n(i) != ((i * (i + 1)) / 2):
        print('Утверждение неверно для n = ', i)
    if i == n:
        print('Для множеств до n = {} утверждение верно!'.format(i))