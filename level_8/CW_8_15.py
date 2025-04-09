"""
Write a function that performs basic math operations. The function should take three arguments:
+ operation — the math operation (+, -, *, /);
+ value_1 — the first number;
+ value_2 — the second number.

The function should return the result of the operation.

Напишите функцию для базовых математических операций. Функция должна принимать три аргумента:
+ operation — математическая операция (+, -, *, /);
+ value_1 — первое число;
+ value_2 — второе число.

Функция должна возвращать результат операции.

https://www.codewars.com/kata/57356c55867b9b7a60000bd7
"""

def my_function(operation, value_1, value_2):
    if operation == '+':
        return value_1 + value_2
    elif operation == '-':
        return value_1 - value_2
    elif operation == '*':
        return value_1 * value_2
    elif operation == '/':
        return value_1 / value_2 if value_2 != 0 else "Division by zero!"
    else:
        return "Invalid operation!"

print(my_function('+', 4, 7))
print(my_function('-', 15, 18))
print(my_function('*', 5, 5))
print(my_function('/', 49, 7))