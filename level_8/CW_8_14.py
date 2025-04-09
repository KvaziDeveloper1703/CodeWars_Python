"""
Write a function that can transform a string into a number.

Напишите функцию, которая преобразует строку в число.

https://www.codewars.com/kata/544675c6f971f7399a000e79
"""

def string_to_number(given_string):
    return int(given_string)

string = "1234"
number = string_to_number(string)
print(number)