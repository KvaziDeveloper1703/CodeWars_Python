"""
Welcome to Fibonacci’s bigger brother — Tribonacci! It works just like Fibonacci, but instead of summing the last two numbers, it sums the last three numbers to generate the next one.

For example, if we start with [1, 1, 1] as a signature, we get:
[1,1,1,3,5,9,17,31,...]

If the signature is [0, 0, 1], we get:
[0,0,1,1,2,4,7,13,24,...]

Write a function tribonacci that takes:
+ signature — an array of three numbers (starting values).
+ n — the number of elements to return.

Guaranteed conditions:
+ signature always contains 3 numbers.
+ n is always a non-negative number.
+ If n == 0, return an empty array.
+ Be prepared for any other unspecified input cases.

Examples:
tribonacci([1, 1, 1], 10)  
→ [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

tribonacci([0, 0, 1], 10)  
→ [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

tribonacci([0, 1, 1], 10)  
→ [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]

tribonacci([1, 2, 3], 0)  
→ []

Добро пожаловать в «старшего брата» Фибоначчи — Трибоначчи! Он работает похоже на последовательность Фибоначчи, но вместо суммы двух предыдущих чисел для вычисления следующего, он складывает три предыдущих числа.

Например, если начальное значение (signature) — [1, 1, 1], то последовательность будет:
[1,1,1,3,5,9,17,31,...]

Если начальное значение [0, 0, 1], то получится:
[0,0,1,1,2,4,7,13,24,...]

Напишите функцию tribonacci, которая принимает:
+ signature — массив из трёх чисел (начальные значения последовательности).
+ n — количество элементов, которые нужно вернуть.

Гарантии:
+ signature всегда содержит 3 числа.
+ n всегда неотрицательное число.
+ Если n == 0, вернуть пустой массив.
+ Будьте готовы к любым входным данным, не указанным явно.

Примеры:
tribonacci([1, 1, 1], 10)  
→ [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

tribonacci([0, 0, 1], 10)  
→ [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

tribonacci([0, 1, 1], 10)  
→ [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]

tribonacci([1, 2, 3], 0)  
→ []
"""

def tribonacci(signature, n):
    if n == 0:
        return []

    if n <= 3:
        return signature[:n]

    tribonacci_sequence = signature[:]

    for i in range(3, n):
        next_value = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]

        tribonacci_sequence.append(next_value)

    return tribonacci_sequence

print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 2, 3], 0))
print(tribonacci([1, 2, 3], 2))