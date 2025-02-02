"""
Your task is to create a function that performs four basic mathematical operations.

The function should take three arguments:
+ operation (string/char) — mathematical operation,
+ value1 (number) — first number,
+ value2 (number) — second number.

The function should return the result of applying the chosen operation to the numbers.

Examples (operator, value1, value2) → output:
('+', 4, 7) → 11
('-', 15, 18) → -3
('*', 5, 5) → 25
('/', 49, 7) → 7

Напишите функцию, которая выполняет четыре базовые математические операции.

Функция должна принимать три аргумента:
+ operation (строка/символ) — математическая операция,
+ value1 (число) — первое число,
+ value2 (число) — второе число.

Функция должна возвращать результат выполнения указанной операции над числами.

Примеры (оператор, число1, число2) → результат:
('+', 4, 7) → 11
('-', 15, 18) → -3
('*', 5, 5) → 25
('/', 49, 7) → 7
"""

def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2 if value2 != 0 else "Division by zero!"
    else:
        return "Invalid operation"

print(basic_math('+', 4, 7))
print(basic_math('-', 15, 18))
print(basic_math('*', 5, 5))
print(basic_math('/', 49, 7))