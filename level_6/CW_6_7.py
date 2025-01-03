"""
The goal is to calculate the digital root of a given number n. The digital root is obtained by repeatedly summing the digits of n until the result is a single-digit number.

Examples:
16 → 1 + 6 = 7
942 → 9 + 4 + 2 = 15 → 1 + 5 = 6
132189 → 1 + 3 + 2 + 1 + 8 + 9 = 24 → 2 + 4 = 6
493193 → 4 + 9 + 3 + 1 + 9 + 3 = 29 → 2 + 9 = 11 → 1 + 1 = 2

Цель задачи — вычислить цифровой корень числа n. Цифровой корень — это результат последовательного суммирования цифр числа до тех пор, пока не останется одна цифра.

Примеры:
16 → 1 + 6 = 7
942 → 9 + 4 + 2 = 15 → 1 + 5 = 6
132189 → 1 + 3 + 2 + 1 + 8 + 9 = 24 → 2 + 4 = 6
493193 → 4 + 9 + 3 + 1 + 9 + 3 = 29 → 2 + 9 = 11 → 1 + 1 = 2

https://www.codewars.com/kata/541c8630095125aba6000c00
"""

def digital_root(number):
    while number >= 10:
        digits = [int(digit) for digit in str(number)]
        digit_sum = 0
        for digit in digits:
            digit_sum += digit
        number = digit_sum
    return number

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))