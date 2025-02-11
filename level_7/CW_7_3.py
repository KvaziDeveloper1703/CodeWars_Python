"""
Write a program that squares each digit of a number and combines them.
For example, an input of 765 will return 493625.

Напишите программу, которая возводит в квадрат каждую цифру числа и объединяет их.
Например, ввод числа 765 вернёт 493625.

https://www.codewars.com/kata/546e2562b03326a88e000020
"""

def square_digits(given_number):
    number_as_an_integer = given_number
    processed_number_as_a_string = ""
    number_as_a_string = str(number_as_an_integer)
    for digit_as_a_string in number_as_a_string:
        digit_as_an_integer = int(digit_as_a_string) 
        squared_digit_as_an_integer = digit_as_an_integer**2
        squared_digit_as_a_string = str(squared_digit_as_an_integer)
        processed_number_as_a_string = processed_number_as_a_string + squared_digit_as_a_string
    processed_number_as_an_integer=int(processed_number_as_a_string)
    return processed_number_as_an_integer

number = input("Write your number here, please: ")
processed_number = square_digits(number)
print(processed_number)