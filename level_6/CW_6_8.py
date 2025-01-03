"""
Write a function that accepts a non-negative integer as input and returns the count of 1 bits in its binary representation.

For example:
The binary representation of 1234 is 10011010010, which contains five 1s. Therefore, the function should return 5.

Напишите функцию, которая принимает неотрицательное целое число и возвращает количество единиц в его двоичном представлении.

Например:
Двоичное представление числа 1234 — это 10011010010, где содержится пять единиц. Следовательно, функция должна вернуть 5.

https://www.codewars.com/kata/526571aae218b8ee490006f4
"""

def count_bits(number):
    binary_representation = format(number, "b")
    return binary_representation.count('1')

print(count_bits(1234))
