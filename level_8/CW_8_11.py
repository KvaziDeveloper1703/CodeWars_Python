"""
Given an array of integers, your solution should find the smallest integer in the array.

Examples:
+ Given [34, 15, 88, 2], the result should be 2.
+ Given [34, -345, -1, 100], the result should be -345.

You can assume that the provided array will not be empty.

Дан массив целых чисел. Необходимо найти наименьшее число в этом массиве.

Примеры:
+ Для массива [34, 15, 88, 2] результатом должно быть 2.
+ Для массива [34, -345, -1, 100] результатом должно быть -345.

Можно считать, что массив не будет пустым.
"""
def find_smallest_int(given_array):
    smallest_number = given_array[0]
    for number in given_array:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(find_smallest([34, 15, 88, 2]))
print(find_smallest([34, -345, -1, 100]))