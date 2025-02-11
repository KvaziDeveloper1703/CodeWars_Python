"""
Given two integers a and b, which can be positive or negative:
+ Find the sum of all integers between them (inclusive) and return it.
+ If the two numbers are equal, return a or b.
+ The numbers are not ordered! (a can be greater than b).

Даны два целых числа a и b, которые могут быть положительными или отрицательными.
+ Найти сумму всех целых чисел между ними (включительно) и вернуть этот результат.
+ Если числа равны, вернуть a или b (так как сумма будет равна самому числу).
+ Числа могут быть переданы в любом порядке (то есть a может быть больше b).
"""

def get_sum(number_1, number_2):
    lower_bound = min(number_1, number_2)
    upper_bound = max(number_1, number_2)

    numbers = list(range(lower_bound, upper_bound + 1))

    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum

first_number = 64
second_number = 27
answer = get_sum(first_number, second_number)
print(answer)