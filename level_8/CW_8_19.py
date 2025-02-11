"""
Given a random non-negative number, return the digits of this number in an array in reverse order.

Дано случайное неотрицательное число. Нужно вернуть массив его цифр в обратном порядке.
"""

def digitize(given_number):
    number_as_a_string = str(given_number)
    reversed_string = number_as_a_string[::-1]
    reversed_digits = [int(digit) for digit in reversed_string]

    return reversed_digits

number = 1234
answer = digitize(number)
print(answer)