"""
Check if a string has the same amount of 'x' and 'o'.
+ The function must return a boolean (true or false).
+ It must be case insensitive.
+ The string can contain any characters.

Examples:
xo("ooxx") → true
xo("xooxx") → false
xo("ooxXm") → true
xo("zpzpzpp") → true
xo("zzoo") → false

Проверьте, содержит ли строка одинаковое количество символов 'x' и 'o'.
+ Функция должна возвращать булево значение (true или false).
+ Проверка не чувствительна к регистру.
+ Строка может содержать любые символы.

Примеры:
xo("ooxx") → true
xo("xooxx") → false
xo("ooxXm") → true
xo("zpzpzpp") → true
xo("zzoo") → false
"""

def xo(given_string):
    given_string = given_string.lower()
    return given_string.count('x') == given_string.count('o')

string = "ooxXm"
answer = xo(string)
print(answer)