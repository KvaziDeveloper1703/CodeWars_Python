"""
Write a function that takes two strings representing integers and returns their sum as a string.

Rules:
+ The input strings will only contain numerical characters ("0" to "9").
+ The function must handle very large numbers (e.g., up to a million digits), so converting the input to integers is not allowed.

Example:
Input: sumStrings('1', '2')
Output: '3'

Input: sumStrings('123456789', '987654321')
Output: '1111111110'

Напишите функцию, которая принимает две строки, представляющие целые числа, и возвращает их сумму в виде строки.

Правила:
+ Входные строки содержат только числовые символы ("0"–"9").
+ Функция должна корректно обрабатывать очень большие числа (например, до миллиона цифр), поэтому преобразование строк в числа использовать нельзя.

Пример:
Ввод: sumStrings('1', '2')
Вывод: '3'

Ввод: sumStrings('123456789', '987654321')
Вывод: '1111111110'

https://www.codewars.com/kata/5324945e2ece5e1f32000370
"""

def sum_strings(a, b):

    a = a.lstrip('0')
    b = b.lstrip('0')

    carry = 0
    result = []

    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    for i in range(max_length - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

    if carry:
        result.append(str(carry))

    if ''.join(result[::-1]) == '':
        return '0'
    else:
        return ''.join(result[::-1])

print(sum_strings('1', '2'))
print(sum_strings('123456789', '987654321'))
print(sum_strings('0000123', '456'))
print(sum_strings('500', '500'))
