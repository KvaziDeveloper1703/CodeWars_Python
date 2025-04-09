"""
Write a function that returns the sum of the two lowest positive numbers given an array.

Напишите функцию, которая возвращает сумму двух наименьших положительных чисел из переданного массива.

https://www.codewars.com/kata/558fc85d8fd1938afb000014
"""

def sum_of_two_smallest_numbers(given_numbers):
    sorted_numbers = sorted(given_numbers)
    return sorted_numbers[0] + sorted_numbers[1]

array = [19, 5, 42, 2, 77]
answer = sum_of_two_smallest_numbers(array)
print(answer)