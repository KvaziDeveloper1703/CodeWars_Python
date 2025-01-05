"""
Write a program that takes an integer and a string as input, then returns the string repeated the number of times specified by the integer.

Напишите программу, которая принимает целое число и строку, а затем возвращает эту строку, повторённую количество раз, указанное в целом числе.

https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
"""

def repeat_the_string(given_number, given_string):
    return given_string * given_number

my_number = int(input("Write your number here, please: "))
my_string = input("Write your string here, please: ")

repeated_string = repeat_the_string(my_number, my_string)
print(repeated_string)