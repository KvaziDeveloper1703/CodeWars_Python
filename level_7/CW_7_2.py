"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the troll's comments, neutralizing the threat.
Write a program that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Тролли атакуют ваш раздел комментариев!
Обычный способ справиться с этой ситуацией — удалить все гласные из комментариев троллей, нейтрализуя угрозу.
Напишите программу, которая принимает строку и возвращает новую строку с удалёнными гласными.
Например, строка "This website is for losers LOL!" станет "Ths wbst s fr lsrs LL!".

https://www.codewars.com/kata/52fba66badcd10859f00097e
"""

def vowel_buster(given_comment):
    original_comment=given_comment
    processed_comment=""
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    for character in original_comment:
        if character not in vowels:
            processed_comment=processed_comment+character
            
    return processed_comment

troll_comment = input("Write any inappropriate comment here, please: ")
processed_comment = vowel_buster(troll_comment)
print(processed_comment)