"""
Write a function that takes a string and replaces all characters except the last four with the # character.
If the string has four or fewer characters, it should remain unchanged. If the string is longer than four characters, all characters except the last four should be replaced with #.

Напишите функцию, которая принимает строку и заменяет все символы, кроме последних четырёх, на символы #.
Если строка состоит из четырёх или менее символов, она остаётся без изменений. Если строка длиннее четырёх символов, все символы, кроме последних четырёх, должны быть заменены на символы #.

https://www.codewars.com/kata/5412509bd436bd33920011bc
"""

def maskify(given_information):
    if len(given_information) <= 4:
        return given_information

    masked_part = "#" * (len(given_information) - 4)
    visible_part = given_information[-4:]
    return masked_part + visible_part

information = "4556364607935616"
masked_information = maskify(information)
print(masked_information)