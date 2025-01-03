"""
Write me a program that takes a number and makes it negative if it is not negative yet.

Напишите программу, которая принимает число и делает его отрицательным, если оно ещё не является отрицательным.

https://www.codewars.com/kata/55685cd7ad70877c23000102
"""

def make_negative(number):
    return -abs(number)

my_number = input("Enter your number here, please: ")
answer = make_negative(my_number)
print(answer)