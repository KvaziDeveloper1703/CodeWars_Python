"""
Given a random non-negative number, return the digits of this number in an array in reverse order.

Дано случайное неотрицательное число. Нужно вернуть массив его цифр в обратном порядке.

https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""

def digitize(given_number):
    number_as_a_string = str(given_number)
    reversed_string = number_as_a_string[::-1]
    reversed_digits = []
    for digit in reversed_string:
        reversed_digits.append(int(digit))

    return reversed_digits

number = 1234
answer = digitize(number)
print(answer)