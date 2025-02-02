"""
Write a function that removes all spaces from a string and returns the resulting string.

Examples (Input → Output):
+ "8 j 8 mBliB8g imjB8B8 jl B" → "8j8mBliB8gimjB8B8jlB"
+ "8 8 Bi fk8h B 8 BB8B B B B888 c hl8 BhB fd" → "88Bifk8hB8BB8BBBB888chl8BhBfd"
+ "8aaaaa dddd r " → "8aaaaaddddr"

Напишите функцию, которая удаляет все пробелы из строки и возвращает получившуюся строку.

Примеры (вход → выход):
+ "8 j 8 mBliB8g imjB8B8 jl B" → "8j8mBliB8gimjB8B8jlB"
+ "8 8 Bi fk8h B 8 BB8B B B B888 c hl8 BhB fd" → "88Bifk8hB8BB8BBBB888chl8BhBfd"
+ "8aaaaa dddd r " → "8aaaaaddddr"
"""

def no_space(given_string):
    return given_string.replace(" ", "")

print(no_space("8 j 8 mBliB8g imjB8B8 jl B"))
print(no_space("8 8 Bi fk8h B 8 BB8B B B B888 c hl8 BhB fd"))
print(no_space("8aaaaa dddd r "))