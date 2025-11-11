'''
Write a program that calculates the Fibonacci number fib(n) defined as follows:
    - fib(0) = 0;
    - fib(1) = 1;
    - fib(n + 2) = fib(n + 1) + fib(n).

Your algorithm must:
    - Work for very large values of n (up to 2,000,000);
    - Return the exact integer result (no rounding or approximations);
    - Correctly handle negative values of n according to the recurrence relation.

Напиши программу, вычисляющую число Фибоначчи fib(n) по формулам:
    - fib(0) = 0;
    - fib(1) = 1;
    - fib(n + 2) = fib(n + 1) + fib(n).

Требования к решению:
    - Поддержка очень больших значений n (до 2 000 000);
    - Результат должен быть точным целым числом;
    - Функция должна корректно работать и для отрицательных n, в соответствии с рекуррентным законом.
'''

def fib(n):
    def fast_doubling(index):
        if index == 0:
            return (0, 1)
        fib_half, fib_half_next = fast_doubling(index // 2)
        fib_double = fib_half * ((fib_half_next * 2) - fib_half)
        fib_double_next = fib_half * fib_half + fib_half_next * fib_half_next
        if index % 2 == 1:
            return (fib_double_next, fib_double + fib_double_next)
        else:
            return (fib_double, fib_double_next)

    if n >= 0:
        return fast_doubling(n)[0]
    else:
        fib_positive = fast_doubling(-n)[0]
        return -fib_positive if n % 2 == 0 else fib_positive