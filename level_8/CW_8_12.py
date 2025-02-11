"""
Write a function that removes all spaces from a string and returns the resulting string.

Напишите функцию, которая удаляет все пробелы из строки и возвращает получившуюся строку.
"""

def no_space(given_string):
    return given_string.replace(" ", "")

string = "8 j 8 mBliB8g imjB8B8 jl B"
answer = no_space(string)
print(answer)