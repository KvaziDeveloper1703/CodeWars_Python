'''
You are given a list of integers (positive or negative): I = [i1, i2, ..., in]

Your task is to create and return a list of lists of the form: [[p, S(p)], ...]

Where:
    - p is a prime number that divides at least one element of I,
    - S(p) is the sum of all elements in I that are divisible by p.

The result list must be sorted in ascending order of the prime numbers p.

Вам дан список целых чисел (положительных или отрицательных): I = [i1, i2, ..., in]

Ваша задача — создать и вернуть список списков следующего вида: [[p, S(p)], ...]

Где:
    - p это простое число, которое является делителем хотя бы одного элемента списка I,
    - S(p) это сумма всех элементов списка I, которые делятся на p.

Результирующий список должен быть отсортирован по возрастанию простых чисел p.
'''

def sum_for_list(lst):
    from math import sqrt

    def prime_factors(n):
        n = abs(n)
        factors = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            factors.add(n)
        return factors

    all_primes = set()
    number_factors = {}

    for number in lst:
        f = prime_factors(number)
        number_factors[number] = f
        all_primes |= f

    result = []
    for p in sorted(all_primes):
        s = sum(number for number in lst if p in number_factors[number])
        result.append([p, s])
    return result