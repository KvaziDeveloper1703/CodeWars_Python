"""
Write a program that takes a number and makes it negative if it is not negative yet.

Напишите программу, которая принимает число и делает его отрицательным, если оно ещё не является отрицательным.

https://www.codewars.com/kata/55685cd7ad70877c23000102
"""

def make_negative(given_number):
    return -abs(given_number)

number = input("Enter your number here, please: ")
answer = make_negative(number)
print(answer)