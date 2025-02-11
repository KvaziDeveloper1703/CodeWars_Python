"""
An isogram is a word that has no repeating letters. 
Write a program that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram and ignore the letter case.

Изограмма — это слово, в котором нет повторяющихся букв.
Напишите программу, которая определяет, является ли строка, содержащая только буквы, изограммой.
Предположим, что пустая строка является изограммой, и игнорируйте регистр букв.

https://www.codewars.com/kata/54ba84be607a92aa900000f1
"""

def is_isogram(given_string):
    given_string = given_string.lower()
    seen_letters = set()
    for character in given_string:
        if character in seen_letters:
            return False
        seen_letters.add(character)
    return True
    

word = input("Write your word here, please: ")
answer = is_isogram(word)
print(answer)