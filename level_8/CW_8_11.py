"""
Given an array of integers, your solution should find the smallest integer in the array.

Дан массив целых чисел. Необходимо найти наименьшее число в этом массиве.
"""

def find_smallest_int(given_array):
    smallest_number = given_array[0]
    for number in given_array:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

array = [34, 15, 88, 2]
smallest_number = find_smallest_int(array)
print(smallest_number)