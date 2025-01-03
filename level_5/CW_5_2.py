"""
Write a function that takes an array and rearranges it so that all the zeros are moved to the end of the array, while maintaining the relative order of the non-zero elements.

Example:
Input: [1, 0, 2, 0, 3] → Output: [1, 2, 3, 0, 0]
Input: [0, 0, 0, 1] → Output: [1, 0, 0, 0]

Напишите функцию, которая принимает массив и переставляет его элементы так, чтобы все нули были перемещены в конец массива, сохраняя порядок остальных элементов.

Пример:
Ввод: [1, 0, 2, 0, 3] → Вывод: [1, 2, 3, 0, 0]
Ввод: [0, 0, 0, 1] → Вывод: [1, 0, 0, 0]

https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""

def move_zeros(arr):
    non_zeros = []
    zeros = []
    
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    
    return non_zeros + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))