"""
Write a function is_pangram that determines whether a given string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once, regardless of case.

Example:
Input: "The quick brown fox jumps over the lazy dog" → Output: True (contains all letters)
Input: "Hello World" → Output: False (missing many letters)

Напишите функцию is_pangram, которая определяет, является ли данная строка панграммой. Панграмма — это предложение, содержащее все буквы алфавита хотя бы один раз, без учёта регистра.

Пример:
Ввод: "The quick brown fox jumps over the lazy dog" → Вывод: True (содержит все буквы)
Ввод: "Hello World" → Вывод: False (многие буквы отсутствуют)
"""

def is_pangram(given_string):
    latin_letters = {
        'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False, 'J': False, 'K': False , 'L': False, 'M': False,
        'N': False, 'O': False, 'P': False, 'Q': False, 'R': False, 'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False,
    }
    for letter in given_string:
        if letter.upper() in latin_letters:
            latin_letters[letter.upper()] = True
    string_is_a_pangram = True
    for key in latin_letters:
        if latin_letters[key] == False:
            string_is_a_pangram = False
    return string_is_a_pangram