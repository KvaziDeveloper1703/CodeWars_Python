"""
You get an array of numbers, return the sum of all of the positive ones.

Вам дан массив чисел, верните сумму всех положительных чисел.

https://www.codewars.com/kata/5715eaedb436cf5606000381
"""

def sum_of_positives(given_array):
    sum = 0
    for number in given_array:
        if number > 0:
            sum = sum + number
    return sum

my_array = [1, -4, 7, 12, 4, -6]

answer = sum_of_positives(my_array)
print(answer)