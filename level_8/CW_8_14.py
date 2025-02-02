"""
We need a function that can transform a string into a number.

Examples:
"1234" → 1234
"605" → 605

Нужно написать функцию, которая преобразует строку в число.

Примеры:
"1234" → 1234
"605" → 605
"""

def string_to_number(given_string):
    return int(given_string)

print(string_to_number("1234")) 
print(string_to_number("605"))