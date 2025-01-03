"""
Write a program that finds the number that appears an odd number of times in a given array of integers.
There will always be only one integer that appears an odd number of times.

Напишите программу, которая находит число, которое встречается нечётное количество раз в заданном массиве целых чисел.
Всегда будет только одно число, которое встречается нечётное количество раз.

https://www.codewars.com/kata/54da5a58ea159efa38000836
"""

def find_odd_occurrence(given_array):
    counts = {}
    for number in given_array:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1
    for number, count in counts.items():
        if count % 2 != 0:
            return number

my_array = [3,1,1,2,2]
desired_number = find_odd_occurrence(my_array)
print(desired_number)