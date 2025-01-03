"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

Напишите программу, которая вычисляет сумму всех чисел от 1 до num. Число всегда будет положительным целым числом, большим 0.

https://www.codewars.com/kata/55d24f55d7dd296eb9000030
"""

def summation(given_number):
    sum = 0
    for i in range(given_number+1):
        sum = sum + i
    return sum

my_number = int(input("Write your number here, please: "))
my_sum = summation(my_number)
print(my_sum)