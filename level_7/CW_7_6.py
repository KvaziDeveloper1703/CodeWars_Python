"""
Write a program that takes a list containing non-negative integers and strings as input. The program should return a new list that includes only the integers, with all strings removed.

Напишите программу, которая принимает список, содержащий неотрицательные целые числа и строки. Программа должна вернуть новый список, содержащий только числа, из которого удалены все строки.

https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
"""

def filter_strings(input_list):
    filtered_list = []
    for item in input_list:
        if type(item) == int:
            filtered_list.append(item)
    return filtered_list

my_list = [1, 'apple', 42, 'banana', 0, 'cherry', 3]
filtered_list = filter_strings(my_list)
print(filtered_list)