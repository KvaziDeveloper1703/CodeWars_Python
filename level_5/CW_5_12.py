"""
Write a function first_non_repeating_letter that takes a string and returns the first character that is not repeated anywhere in the string.

Examples:
first_non_repeating_letter('stress')  → 't'
first_non_repeating_letter('sTreSS')  → 'T'

Напишите функцию first_non_repeating_letter, которая принимает строку и возвращает первый символ, который нигде в строке не повторяется.

Примеры:
first_non_repeating_letter('stress')  → 't'
first_non_repeating_letter('sTreSS')  → 'T'
"""

def first_non_repeating_letter(given_string):

    lower_string = given_string.lower()

    character_count = {}

    for character in lower_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    for index, character in enumerate(lower_string):
        if character_count[character] == 1:
            return given_string[index]

    return ""

print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter("aabbcc"))
print(first_non_repeating_letter("abcABC"))