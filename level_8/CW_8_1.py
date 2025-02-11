"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

Создайте функцию, которая принимает целое число в качестве аргумента и возвращает "Even" для четных чисел или "Odd" для нечетных.

https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
"""

def even_or_odd(given_number):
    if given_number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = input("Enter your number here, please: ")
answer = even_or_odd(number)
print(answer)