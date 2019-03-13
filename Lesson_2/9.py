# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def recursion(n, m, result = 0):
    if m == 1:
        result = n % 10 + result
        return result
    elif len(str(m)) == len(str(n)):
        number = n // m
        result = number + result
        return recursion(n, int(m / 10), result)
    else:
        number = (n % (m * 10)) // m
        result = number + result
        return recursion(n, int(m / 10), result)

num1 = input('Введите число 1: ')
num2 = input('Введите число 2: ')

divider1 = str(1) + '0' * (len(num1) - 1)
divider2 = str(1) + '0' * (len(num2) - 1)

sum1 = recursion(int(num1), int(divider1))
sum2 = recursion(int(num2), int(divider2))

if sum1 > sum2:
    print('Сумма цифр числа {} = {}'.format(num1, sum1))
else:
    print('Сумма цифр числа {} = {}'.format(num2, sum2))