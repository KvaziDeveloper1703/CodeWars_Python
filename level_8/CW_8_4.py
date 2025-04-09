"""
Write a program that takes a string as input and returns the reversed version of the string.

Напишите программу, которая принимает строку на вход и возвращает её перевёрнутую версию.

https://www.codewars.com/kata/5168bb5dfe9a00b126000018
"""

def reverse_string(given_string):
    reversed_string = ''
    for i in range(len(given_string) - 1, -1, -1):
        reversed_string = reversed_string + given_string[i]
    return reversed_string

string = input("Write your string here, please: ")
reversed_string = reverse_string(string)
print(reversed_string)