"""
Given two integers, which can be positive or negative:
+ Find the sum of all integers between them (inclusive) and return it;
+ If the two numbers are equal, return either of them;
+ The numbers are not ordered.

Даны два целых числа, которые могут быть положительными или отрицательными.
+ Найти сумму всех целых чисел между ними (включительно) и вернуть этот результат;
+ Если числа равны, вернуть любое из них;
+ Числа могут быть переданы в любом порядке.

https://www.codewars.com/kata/55f2b110f61eb01779000053
"""

def get_sum(given_number_1, given_number_2):
    lower_bound = min(given_number_1, given_number_2)
    upper_bound = max(given_number_1, given_number_2)

    numbers = list(range(lower_bound, upper_bound + 1))

    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum

first_number = 64
second_number = 27
answer = get_sum(first_number, second_number)
print(answer)