"""
Write a function that takes a year and returns the century it belongs to.

Напишите функцию, которая принимает год и возвращает век, к которому этот год относится.

https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
"""

def get_century(given_year):
    if given_year % 100 == 0:
        return given_year // 100
    else:
        return (given_year // 100) + 1

year = 1703
century = get_century(year)
print(century)