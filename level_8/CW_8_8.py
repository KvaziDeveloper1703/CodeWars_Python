"""
Write a program that takes an array of numbers as input and calculates the sum of the squares of all the numbers in the array.

Напишите программу, которая принимает массив чисел и вычисляет сумму квадратов всех чисел в массиве.

https://www.codewars.com/kata/515e271a311df0350d00000f
"""

def sum_of_all_squared_numbers(given_array):
    sum = 0
    for number in given_array:
        sum = sum + (number*number)
    return sum

my_array = [3,6,1,2,5]

answer = sum_of_all_squared_numbers(my_array)
print(answer)