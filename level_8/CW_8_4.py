"""
Write a program that takes a string as input and returns the reversed version of the string.

Напишите программу, которая принимает строку на вход и возвращает её перевёрнутую версию.

https://www.codewars.com/kata/5168bb5dfe9a00b126000018
"""

def reverse(given_string):
    reversed_string = ''
    for i in range(len(my_string) - 1, -1, -1):
        reversed_string = reversed_string + my_string[i]
    return reversed_string

my_string = input("Write your string here, please: ")
reversed_string = reverse_string(my_string)
print(reversed_string)