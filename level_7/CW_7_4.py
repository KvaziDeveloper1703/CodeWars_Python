"""
Write a program that finds the highest and the lowest number in a given space separated string.

Напишите программу, которая находит самое большое и самое маленькое число в заданной строке, где числа разделены пробелами.

https://www.codewars.com/kata/554b4ac871d6813a03000035
"""

def highest_and_lowest(given_numbers):
    array_of_string_numbers=given_numbers.split()
    array_of_int_numbers=[]
    for number in array_of_string_numbers:
        array_of_int_numbers.append(int(number))

    maximum=max(array_of_int_numbers)
    minimum=min(array_of_int_numbers)

    return str(maximum) + " " + str(minimum)

my_string_of_numbers = input("Write your string of numbers here, please: ")
string_with_the_highest_and_the_lowest_number = highest_and_lowest(my_string_of_numbers)
print(string_with_the_highest_and_the_lowest_number)