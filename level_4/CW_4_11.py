'''
We define a sequence u as follows:
- u(0) = 1;
- For every element x in u, two new numbers are added:
    - 2 * x + 1;
    - 3 * x + 1.
- The sequence contains no duplicates and is sorted in ascending order.

Example: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

Write a function dbl_linear(n) that returns the n-th element of the sequence u.

Определим последовательность u так:
- u(0) = 1;
- Для каждого элемента x в u добавляем два числа:
    - 2 * x + 1;
    - 3 * x + 1.
- Последовательность не содержит повторов и отсортирована по возрастанию.

Пример: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

Нужно написать функцию dbl_linear(n), возвращающую n-й элемент последовательности.
'''

def dbl_linear(n):
    u = [1]
    i = 0
    j = 0

    while len(u) <= n:
        y = 2 * u[i] + 1
        z = 3 * u[j] + 1
        next_value = min(y, z)

        u.append(next_value)

        if next_value == y:
            i += 1
        if next_value == z:
            j += 1

    return u[n]