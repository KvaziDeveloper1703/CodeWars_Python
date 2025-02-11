"""
Write a program that counts vowels in the given sentence. We will consider a, e, i, o, u, y as vowels.The input string will only consist of lower case letters and/or spaces.

Напишите программу, которая подсчитывает количество гласных в заданном предложении.Мы будем считать гласными буквы a, e, i, o, u, y. Входная строка будет состоять только из строчных букв и/или пробелов.

https://www.codewars.com/kata/54ff3102c1bad923760001f3
"""

def count_vowels(given_sentence):
    counter=0
    vowels = ["a","e","i","o","u","y"]
    for character in given_sentence:
        if character in vowels:
            counter=counter + 1
    return counter

sentence = input("Write your sentence here, please: ")
number_of_vowels_in_a_sentence = count_vowels(my_sentence)
print(number_of_vowels_in_a_sentence)