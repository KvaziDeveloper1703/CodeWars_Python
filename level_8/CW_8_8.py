"""
Write a program that returns the sum of the squares of all numbers in an array.

Напишите программу, которая удаляет первый и последний символ строки.

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