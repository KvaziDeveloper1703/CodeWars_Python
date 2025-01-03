"""
Create a set of functions to perform calculations using a unique functional syntax. Each number from 0 to 9 should have its own function, and each operation (addition, subtraction, multiplication, division) should also have its own function.

Rules:
+ Provide a function for each digit: zero(), one(), ..., nine().
+ Provide a function for each operation: plus(), minus(), times(), divided_by().
+ Each calculation will consist of exactly one operation and two numbers.
+ The outer function represents the left operand, while the inner function represents the right operand.
+ Division should be performed as integer division (e.g., 6 divided by 4 should return 1).

Examples:
seven(times(five())) → returns 35
four(plus(nine())) → returns 13
eight(minus(three())) → returns 5
six(divided_by(two())) → returns 3

Создайте набор функций для выполнения вычислений с использованием уникального функционального синтаксиса. Каждое число от 0 до 9 должно иметь свою функцию, а также каждая операция (сложение, вычитание, умножение, деление) должна быть реализована через функцию.

Правила:
+ Реализуйте функцию для каждой цифры: zero(), one(), ..., nine().
+ Реализуйте функцию для каждой операции: plus(), minus(), times(), divided_by().
+ Каждое вычисление должно состоять ровно из одной операции и двух чисел.
+ Внешняя функция представляет левый операнд, внутренняя функция — правый операнд.
+ Деление должно быть целочисленным (например, 6 делить на 4 должно возвращать 1).

Примеры:
seven(times(five())) → возвращает 35
four(plus(nine())) → возвращает 13
eight(minus(three())) → возвращает 5
six(divided_by(two())) → возвращает 3

https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""

def zero(func=None):
    return 0 if func is None else func(0)

def one(func=None):
    return 1 if func is None else func(1)

def two(func=None):
    return 2 if func is None else func(2)

def three(func=None):
    return 3 if func is None else func(3)

def four(func=None):
    return 4 if func is None else func(4)

def five(func=None):
    return 5 if func is None else func(5)

def six(func=None):
    return 6 if func is None else func(6)

def seven(func=None):
    return 7 if func is None else func(7)

def eight(func=None):
    return 8 if func is None else func(8)

def nine(func=None):
    return 9 if func is None else func(9)

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x // y

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))