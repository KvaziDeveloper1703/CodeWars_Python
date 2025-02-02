"""
Given two integers a and b, which can be positive or negative:
+ Find the sum of all integers between them (inclusive) and return it.
+ If the two numbers are equal, return a or b.
+ The numbers are not ordered! (a can be greater than b).

Examples:
(1, 0) → 1
(1, 2) → 3
(0, 1) → 1
(1, 1) → 1
(-1, 0) → -1
(-1, 2) → 2

Даны два целых числа a и b, которые могут быть положительными или отрицательными.
+ Найти сумму всех целых чисел между ними (включительно) и вернуть этот результат.
+ Если числа равны, вернуть a или b (так как сумма будет равна самому числу).
+ Числа могут быть переданы в любом порядке (то есть a может быть больше b).

Примеры:
(1, 0) → 1
(1, 2) → 3
(0, 1) → 1
(1, 1) → 1
(-1, 0) → -1
(-1, 2) → 2
"""

def get_sum(a, b):
    lower_bound = min(a, b)
    upper_bound = max(a, b)

    numbers = list(range(lower_bound, upper_bound + 1))

    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum

print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))