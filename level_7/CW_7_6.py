"""
Write a program that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Напишите программу, которая принимает список неотрицательных целых чисел и строк, и возвращает новый список, из которого удалены все строки.

https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
"""

def filter_strings(input_list):
    filtered_list = []
    for item in input_list:
        if isinstance(item, int):
            filtered_list.append(item)
    return filtered_list

my_list = [1, 'apple', 42, 'banana', 0, 'cherry', 3]
filtered_list = filter_strings(my_list)
print(filtered_list)