"""
Given an array of numbers, write a function to calculate the sum of all positive numbers in the array. If there are no positive numbers, return 0.

Дан массив чисел. Напишите функцию, которая вычисляет сумму всех положительных чисел в массиве. Если положительных чисел нет, вернуть 0.

https://www.codewars.com/kata/5715eaedb436cf5606000381
"""

def sum_of_positives(given_array):
    sum = 0
    for number in given_array:
        if number > 0:
            sum = sum + number
    return sum

my_array = [1, -4, 7, 12, 4, -6]

answer = sum_of_positives(my_array)
print(answer)