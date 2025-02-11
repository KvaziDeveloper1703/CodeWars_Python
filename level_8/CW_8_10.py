"""
Write a program that takes a positive integer greater than 0 as input and calculates the sum of all numbers from 1 to the given number.

Напишите программу, которая принимает положительное целое число, большее 0, и вычисляет сумму всех чисел от 1 до указанного числа.

https://www.codewars.com/kata/55d24f55d7dd296eb9000030
"""

def summation(given_number):
    sum = 0
    for i in range(given_number+1):
        sum = sum + i
    return sum

number = int(input("Write your number here, please: "))
sum = summation(number)
print(sum)