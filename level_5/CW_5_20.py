"""
You are given a positive number n > 1,
Find its prime factor decomposition and return a string in the following format:
(p1**n1)(p2**n2)...(pk**nk)
where:
+ p(i) are prime factors, sorted in increasing order.
+ n(i) is the exponent of the factor (omit n(i) if n(i) == 1).

Example:
n = 86240 → "(2**5)(5)(7**2)(11)"

Дано положительное число n > 1.
Найдите разложение n на простые множители и верните строку в формате:
(p1**n1)(p2**n2)...(pk**nk)
где:
+ p(i) — простые множители в возрастающем порядке.
+ n(i) — степень множителя (n(i) опускается, если n(i) == 1).

Пример:
n = 86240 → "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):

    factors = {}
    divisor = 2 

    while n % divisor == 0:
        factors[divisor] = factors.get(divisor, 0) + 1
        n //= divisor

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 2

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    result = "".join(
        f"({p}**{e})" if e > 1 else f"({p})"
        for p, e in sorted(factors.items())
    )

    return result

print(prime_factors(86240))
print(prime_factors(56))
print(prime_factors(7775460))
print(prime_factors(97))
print(prime_factors(2))