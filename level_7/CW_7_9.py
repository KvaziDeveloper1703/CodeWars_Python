"""
Write a program that checks whether a given integer is a perfect square.
For example, is_square(4) returns True, while is_square(3) returns False.

Напишите программу, которая проверяет, является ли заданное целое число идеальным квадратом.
Например, is_square(4) возвращает True, а is_square(3) возвращает False.

https://www.codewars.com/kata/54c27a33fb7da0db0100040e
"""

def is_square(given_number):
    if given_number < 0:
        return False
    i = 0
    while i * i <= given_number:
        if i * i == given_number:
            return True
        i += 1
    return False

number = input("Write your number here, please: ")
answer = is_square(number)
print(answer)