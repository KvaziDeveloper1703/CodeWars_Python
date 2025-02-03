"""
Write a function persistence that takes in a positive integer num and returns its multiplicative persistence.
Multiplicative persistence is the number of times you must multiply the digits in num until you reach a single digit.

Examples:
39  → 3
999 → 4
4   → 0

Напишите функцию persistence, которая принимает положительное число num и возвращает его мультипликативную устойчивость.
Мультипликативная устойчивость — это количество шагов, за которое нужно перемножать цифры числа, пока в результате не останется одна цифра.

Примеры:
39  → 3
999 → 4
4   → 0
"""

def persistence(number):
    if number < 10:
        return 0

    steps = 0
    while number >= 10:
        digits = [int(digit) for digit in str(number)]
        product = 1
        for digit in digits:
            product *= digit
        number = product
        steps += 1

    return steps

print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(25))
print(persistence(77))