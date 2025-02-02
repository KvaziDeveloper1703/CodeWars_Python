"""
Create a function that returns the sum of the two lowest positive numbers given an array.

Conditions:
+ The array contains at least 4 positive integers.
+ No floats or non-positive integers will be passed.

Examples:
[19, 5, 42, 2, 77] → 7 (2 + 5)
[10, 343445353, 3453445, 3453545353453] → 3453455 (10 + 3453445)

Создайте функцию, которая возвращает сумму двух наименьших положительных чисел из переданного массива.

Условия:
+ Массив содержит минимум 4 положительных целых числа.
+ Только целые числа, без дробных и без отрицательных значений.

Примеры (вход → выход):
[19, 5, 42, 2, 77] → 7 (2 + 5)
[10, 343445353, 3453445, 3453545353453] → 3453455 (10 + 3453445)
"""

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))