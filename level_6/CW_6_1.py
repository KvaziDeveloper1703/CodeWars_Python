"""
Write a program that returns the sum of all the multiples of 3 or 5 below the number passed in.
If the number is negative, program must return 0.

Напишите программу, которая возвращает сумму всех кратных 3 или 5 чисел, меньших заданного числа.
Если число отрицательное, программа должна вернуть 0.

https://www.codewars.com/kata/514b92a657cdc65150000006
"""

def sum_multiples_of_3_or_5(number):
    if number <= 0:
        return 0
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

my_number = input("Write your number here, please: ")
answer = sum_multiples_of_3_or_5(my_number)
print(answer)