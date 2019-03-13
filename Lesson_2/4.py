# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def recursion(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return recursion(n - 1) + 1 / 2**n
    else:
        return recursion(n - 1) - 1 / 2**n

n = int(input('Введите длину ряда:'))
print("Сумма ряда = ",recursion(n - 1))