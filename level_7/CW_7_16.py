"""
Create a function that returns the sum of the two lowest positive numbers given an array.

Создайте функцию, которая возвращает сумму двух наименьших положительных чисел из переданного массива.
"""

def sum_of_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

array = [19, 5, 42, 2, 77]
answer = sum_of_two_smallest_numbers(array)
print(answer)