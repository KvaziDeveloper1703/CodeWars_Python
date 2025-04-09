"""
Write a function that converts a two-word name into initials, outputting two capital letters separated by a dot.

Напишите функцию, которая преобразует имя из двух слов в инициалы, выводя две заглавные буквы, разделённые точкой.

https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
"""

def make_abbreviation(given_name):
    words = given_name.split()

    first_initial = words[0][0]
    last_initial = words[1][0]

    first_initial = first_initial.upper()
    last_initial = last_initial.upper()

    initials = f"{first_initial}.{last_initial}"

    return initials

name = "Viktor Sbruev"
answer = make_abbreviation(name)
print(answer)