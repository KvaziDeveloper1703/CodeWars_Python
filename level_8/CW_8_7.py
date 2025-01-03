"""
Write a program that removes the first and the last character of a string.

Напишите программу, которая удаляет первый и последний символ строки.

https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
"""

def remove_first_and_last_character(given_string):
    return given_string[1:-1]

my_string = input("Write your string here, please: ")
sliced_string = remove_first_and_last_character(my_string)
print(sliced_string)