"""
Write a function that converts a two-word name into initials, outputting two capital letters separated by a dot.

Напишите функцию, которая преобразует имя из двух слов в инициалы, выводя две заглавные буквы, разделённые точкой.
"""

def abbreviation(name):
    words = name.split()

    first_initial = words[0][0]
    last_initial = words[1][0]

    first_initial = first_initial.upper()
    last_initial = last_initial.upper()

    initials = f"{first_initial}.{last_initial}"

    return initials

name = "patrick feeney"
answer = abbreviation(name)
print(answer)