"""
Write a program that return the middle character of the given word. 
If the word's length is odd, return the middle character. 
If the word's length is even, return the middle 2 characters.

Напишите программу, которая возвращает средний символ заданного слова.
Если длина слова нечётная, вернуть средний символ.
Если длина слова чётная, вернуть 2 средних символа.

https://www.codewars.com/kata/56747fd5cb988479af000028
"""

def get_the_middle(word):
    length = len(word)
    middle = length // 2

    if length % 2 == 0:
        print(middle - 1)
        print(middle + 1)
        return word[middle - 1:middle + 1]
    else:
        return word[middle]

my_word = input("Write your word here, please: ")
middle = get_the_middle(my_word)
print(middle)