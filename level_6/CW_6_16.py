"""
A Narcissistic Number (or Armstrong Number) is a positive number that is equal to the sum of its own digits, each raised to the power of the number of digits in a given base.

Write a function that returns true or false, depending on whether the given number is Narcissistic in base 10.

Нарциссическое число (или число Армстронга) — это положительное число, которое равно сумме своих цифр, возведённых в степень, равную количеству цифр в числе.

Напишите функцию, которая возвращает true или false, в зависимости от того, является ли число нарциссическим.
"""

def narcissistic(number):
    digits_str = str(number)
    num_digits = len(digits_str)

    sum_of_powers = 0
    for digit_char in digits_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits

    return sum_of_powers == number

print(narcissistic(153))
print(narcissistic(1652))
print(narcissistic(9474))
print(narcissistic(9475))
print(narcissistic(9))
print(narcissistic(370))