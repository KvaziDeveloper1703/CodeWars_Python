"""
Given a random non-negative number, return the digits of this number in an array in reverse order.

Examples:
35231 → [1,3,2,5,3]
0 → [0]

Дано случайное неотрицательное число. Нужно вернуть массив его цифр в обратном порядке.

Примеры:
35231 → [1,3,2,5,3]
0 → [0]
"""

def digitize(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_digits = [int(digit) for digit in reversed_str]

    return reversed_digits

print(digitize(35231))
print(digitize(0))