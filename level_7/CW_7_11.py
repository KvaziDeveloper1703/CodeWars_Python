"""
Write a function that checks if a given string contains the same number of 'x' and 'o' characters.

Examples:
Input: "ooxx"
Output: True

Input: "xooxx"
Output: False

Input: "ooxXm"
Output: True

Напишите функцию, которая проверяет, содержит ли заданная строка одинаковое количество символов 'x' и 'o'.

Примеры:
Ввод: "ooxx"
Вывод: True

Ввод: "xooxx"
Вывод: False 

Ввод: "ooxXm"
Вывод: True

https://www.codewars.com/kata/55908aad6620c066bc00002a
"""

def xo(given_string):
    given_string = given_string.lower()
    return given_string.count('x') == given_string.count('o')

string = "ooxXm"
answer = xo(string)
print(answer)