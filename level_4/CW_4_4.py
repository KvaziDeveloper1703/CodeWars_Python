"""
Write a function that takes a positive integer as input and returns the next largest number that can be formed by rearranging its digits.

Rules:
+ If it is possible to rearrange the digits to form a larger number, return that number.
+ If no larger number can be formed, return -1.

Examples:
12 → 21
513 → 531
2017 → 2071
9 → -1 (no larger number possible)
111 → -1
531 → -1

Напишите функцию, которая принимает положительное целое число и возвращает следующее большее число, которое можно составить из его цифр.

Правила:
+ Если возможно переставить цифры так, чтобы получилось большее число, вернуть это число.
+ Если большее число составить невозможно, вернуть -1.

Примеры:
12 → 21
513 → 531
2017 → 2071
9 → -1 (большее число невозможно)
111 → -1
531 → -1

https://www.codewars.com/kata/55983863da40caa2c900004e
"""

def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1

    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break

    digits[i], digits[j] = digits[j], digits[i]

    left_part = digits[:i + 1]
    right_part = sorted(digits[i + 1:])

    digits = left_part + right_part

    return int("".join(digits))

print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))