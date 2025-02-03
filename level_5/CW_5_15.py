"""
Your task is to write a function that increments a numerical suffix in a string, creating a new string.

Rules:
+ If the string ends with a number, the number should be incremented by 1.
+ If the string does not end with a number, append "1" to the new string.
+ Attention! If the number has leading zeros, the number of digits should be preserved.

Examples:
"foo"       → "foo1"
"foobar23"  → "foobar24"
"foo0042"   → "foo0043"
"foo9"      → "foo10"
"foo099"    → "foo100"

Ваша задача — написать функцию, которая увеличивает числовой суффикс строки и возвращает новую строку.

Правила:
+ Если строка заканчивается числом, это число нужно увеличить на 1.
+ Если строка не заканчивается числом, к строке добавляется "1".
+ Важно! Если число содержит ведущие нули, количество цифр должно сохраниться.

Примеры:
"foo"       → "foo1"
"foobar23"  → "foobar24"
"foo0042"   → "foo0043"
"foo9"      → "foo10"
"foo099"    → "foo100"
"""

def increment_string(given_string):
    if not given_string:
        return "1"

    i = len(given_string)
    while i > 0 and given_string[i - 1].isdigit():
        i -= 1

    text_part = given_string[:i]
    number_part = given_string[i:]

    if not number_part:
        return given_string + "1"

    incremented_number = str(int(number_part) + 1)
    padded_number = incremented_number.zfill(len(number_part))

    return text_part + padded_number

print(increment_string("foo"))
print(increment_string("foobar23"))
print(increment_string("foo0042"))
