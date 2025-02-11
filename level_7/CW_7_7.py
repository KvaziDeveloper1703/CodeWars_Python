"""
Write a program that takes a word as input and returns its middle character(s).
+ If the word has an odd length, return the single middle character.
+ If the word has an even length, return the two middle characters.

Напишите программу, которая принимает слово и возвращает его средний символ или символы.
+ Если длина слова нечётная, вернуть один средний символ.
+ Если длина слова чётная, вернуть два средних символа.

https://www.codewars.com/kata/56747fd5cb988479af000028
"""

def get_the_middle(given_word):
    length = len(given_word)
    middle = length // 2

    if length % 2 == 0:
        return given_word[middle - 1:middle + 1]
    else:
        return given_word[middle]

word = input("Write your word here, please: ")
middle = get_the_middle(word)
print(middle)