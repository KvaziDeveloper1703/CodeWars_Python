"""
Write a function perimeter(n) that takes a parameter n, where n + 1 is the number of squares.
The function should return the total perimeter of all squares.

Examples:
perimeter(5)  → 80
perimeter(7)  → 216

Напишите функцию perimeter(n), которая принимает параметр n, где n + 1 — это количество квадратов.
Функция должна вернуть сумму периметров всех квадратов.

Примеры:
perimeter(5)  → 80
perimeter(7)  → 216
"""

def perimeter(n):
    if n == 0:
        return 4

    fib_sequence = [1, 1]

    for _ in range(n - 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    fib_sum = sum(fib_sequence)

    return 4 * fib_sum

print(perimeter(5))
print(perimeter(7))
print(perimeter(10))
print(perimeter(0))
print(perimeter(1))