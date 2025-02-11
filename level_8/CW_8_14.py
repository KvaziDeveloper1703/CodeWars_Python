"""
We need a function that can transform a string into a number.

Нужно написать функцию, которая преобразует строку в число.
"""

def string_to_number(given_string):
    return int(given_string)

string = "1234"
number = string_to_number(string)
print(number)