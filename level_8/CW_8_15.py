"""
Your task is to create a function that performs four basic mathematical operations.

The function should take three arguments:
+ operation (string) — mathematical operation,
+ value1 (number) — first number,
+ value2 (number) — second number.

The function should return the result of applying the chosen operation to the numbers.

Examples (operator, value1, value2) → output:
my_function('+', 4, 7) → 11
my_function('-', 15, 18) → -3
my_function('*', 5, 5) → 25
my_function('/', 49, 7) → 7

Напишите функцию, которая выполняет четыре базовые математические операции.

Функция должна принимать три аргумента:
+ operation (строка) — математическая операция,
+ value1 (число) — первое число,
+ value2 (число) — второе число.

Функция должна возвращать результат выполнения указанной операции над числами.

Примеры (оператор, число1, число2) → результат:
my_function('+', 4, 7) → 11
my_function('-', 15, 18) → -3
my_function('*', 5, 5) → 25
my_function('/', 49, 7) → 7
"""

def my_function(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2 if value2 != 0 else "Division by zero!"
    else:
        return "Invalid operation!"

print(my_function('+', 4, 7))
print(my_function('-', 15, 18))
print(my_function('*', 5, 5))
print(my_function('/', 49, 7))