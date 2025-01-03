"""
You are given an array of integers with a minimum length of 3. The array consists of either entirely odd numbers or entirely even numbers, except for one "outlier" integer, which is the only number of the opposite parity.
Write a function that takes the array as input and returns this outlier.

Examples:
[2, 4, 0, 100, 4, 11, 2602, 36] → 11
[160, 3, 1719, 19, 11, 13, -21] → 160

Дан массив целых чисел, длина которого как минимум равна 3. Массив состоит либо только из нечётных чисел, либо только из чётных чисел, за исключением одного "выбивающегося" числа, которое имеет противоположную чётность.
Напишите функцию, которая принимает массив в качестве входных данных и возвращает это "выбивающееся" число.

Примеры:
[2, 4, 0, 100, 4, 11, 2602, 36] → 11
[160, 3, 1719, 19, 11, 13, -21] → 160

https://www.codewars.com/kata/5526fc09a1bbd946250002dc
"""

def find_outlier(integers):
    even = 0
    odd = 0
    for integer in integers:
        if integer % 2 == 0:
            even += 1
        else:
            odd += 1
        if even == 2:
            for integer in integers:
                if integer % 2 != 0:
                    return integer
        if odd == 2:
            for integer in integers:
                if integer % 2 == 0:
                    return integer

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))