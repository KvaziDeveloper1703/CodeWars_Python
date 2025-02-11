"""
Write a program that can take any non-negative integer as an argument and return it with its digits in descending order.

Напишите программу, которая принимает любое неотрицательное целое число в качестве аргумента и возвращает его с цифрами, расположенными в порядке убывания.

https://www.codewars.com/kata/5467e4d82edf8bbf40000155
"""

def descending_order(given_number):
    given_number_as_a_string = str(given_number)
    sorted_digits = sorted(given_number_as_a_string, reverse=True)
    highest_number = int(''.join(sorted_digits))
    return highest_number

number = input("Write your number here, please: ")
print(descending_order(number))