"""
Write a function to convert a name into initials.
Input: two words with a single space between them.
Output: two capital letters separated by a dot.

Examples:
"Sam Harris" → "S.H"
"patrick feeney" → "P.F"

Напишите функцию, которая преобразует имя в инициалы.
Входные данные: два слова, разделённые одним пробелом.
Выходные данные: две заглавные буквы, разделённые точкой.

Примеры:
"Sam Harris" → "S.H"
"patrick feeney" → "P.F"
"""

def abbrev_name(name):
    words = name.split()

    first_initial = words[0][0]
    last_initial = words[1][0]

    first_initial = first_initial.upper()
    last_initial = last_initial.upper()

    initials = f"{first_initial}.{last_initial}"

    return initials

print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feeney"))
