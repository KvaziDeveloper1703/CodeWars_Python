"""
Write a program that takes a string as input and returns a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Напишите программу, которая принимает строку и возвращает новую строку с удалёнными гласными.
Например, строка "This website is for losers LOL!" станет "Ths wbst s fr lsrs LL!".

https://www.codewars.com/kata/52fba66badcd10859f00097e
"""

def remove_vowels(given_comment):
    original_comment = given_comment
    processed_comment = ""
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    for character in original_comment:
        if character not in vowels:
            processed_comment = processed_comment + character
            
    return processed_comment

troll_comment = input("Write any inappropriate comment here, please: ")
processed_comment = remove_vowels(troll_comment)
print(processed_comment)