"""
The Fibonacci sequence is defined as follows:
+ F(0)=1
+ F(1)=1
+ F(n)=F(n−1)+F(n−2)

Write a function that, given a number prod, finds two consecutive Fibonacci numbers F(n) and F(n+1) such that:

+ F(n)×F(n+1)=prod If such numbers exist, return them along with true. If no such numbers exist, return the closest pair F(n) and F(n+1) where F(n)×F(n+1)>prod, along with false.

The function should return a tuple or array: (F(n),F(n+1),boolean).

Examples:
Input: 714 → Output: (21, 34, true)
Explanation: 
F(8)=21, F(9)=34, and 21×34=714.

Input: 800 → Output: (34, 55, false)
Explanation: 
F(8)=21, F(9)=34, F(10)=55, and 21×34<800<34×55.

Последовательность чисел Фибоначчи определяется следующим образом:
+ F(0)=1
+ F(1)=1
+ F(n)=F(n−1)+F(n−2)

Напишите функцию, которая для заданного числа prod находит два последовательных числа Фибоначчи F(n) и F(n+1), такие что: 

+ F(n)×F(n+1)=prod Если такие числа существуют, верните их вместе с true. Если таких чисел нет, верните ближайшую пару F(n) и F(n+1), где F(n)×F(n+1)>prod, вместе с false.

Функция должна возвращать кортеж или массив: (F(n),F(n+1),boolean).

Примеры:
Ввод: 714 → Вывод: (21, 34, true)
Объяснение: 
F(8)=21, F(9)=34, и 21×34=714.

Ввод: 800 → Вывод: (34, 55, false)
Объяснение: 
F(8)=21, F(9)=34, F(10)=55, и 21×34<800<34×55.

https://www.codewars.com/kata/5541f58a944b85ce6d00006a
"""

def product_fib(prod):
    a, b = 0, 1

    while a * b < prod:
        a, b = b, a + b

    return [a, b, a * b == prod]

print(product_fib(714))
print(product_fib(800))