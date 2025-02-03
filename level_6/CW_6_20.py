"""
Some numbers have interesting properties. For example:
89 → 81 + 92 = 89 * 1
695 → 62 + 93 + 5**4 = 695 * 2
46288 → 43 + 64 + 25 + 86 + 8**7 = 46288 * 51

Given two positive numbers n and p, the task is to find an integer k, if it exists, such that: a**p + b**(p+1) + c**(p+2) + ... = n*k, where a, b, c, d ... are the digits of the number n.
+ If such a k exists → return it.
+ If it does not exist → return -1.

Examples:
n = 89, p = 1 → 1
n = 92, p = 1 → -1
n = 695, p = 2 → 2
n = 46288, p = 3 → 51

Note: n and p are always positive integers.

Некоторые числа обладают интересными свойствами. Например:
+ 89 → 8**1 + 9**2 = 89 * 1
+ 695 → 6**2 + 9**3 + 5**4 = 695 * 2 
+ 46288 → 4**3 + 6**4 + 2**5 + 8**6 + 8**7 = 46288 * 51

Даны два положительных числа n и p. Нужно найти целое число k, если оно существует, такое что: a**p + b**(p+1) + c**(p+2) + ... = n*k, где a, b, c, d ... — это цифры числа n.
+ Если такое k существует → вернуть его.
+ Если не существует → вернуть -1.

Примеры:
n = 89, p = 1  →  1
n = 92, p = 1  → -1
n = 695, p = 2 →  2
n = 46288, p = 3 → 51

Примечание: n и p всегда положительные целые числа.
"""

def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    sum_of_powers = sum(digit ** (p + i) for i, digit in enumerate(digits))

    if sum_of_powers % n == 0:
        return sum_of_powers // n
    else:
        return -1

print(dig_pow(89, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
print(dig_pow(123, 1))
print(dig_pow(10, 1))