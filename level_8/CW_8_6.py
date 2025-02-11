"""
Write a program that converts a number to a string.

Напишите программу, которая преобразует число в строку.

https://www.codewars.com/kata/5265326f5fda8eb1160004c8
"""

def number_to_string(given_number):
    given_number_as_a_string = str(given_number)
    return given_number_as_a_string

number = input("Write your number here, please: ")
number_as_a_string = number_to_string(number)
print(number_as_a_string)