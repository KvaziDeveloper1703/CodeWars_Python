"""
Write a program that calculates the number of trailing zeros in the factorial of a given number N.

Be careful!
1000! has 2568 digits, so direct computation of factorial may not be efficient.

Напишите программу, которая вычисляет количество завершающих нулей в факториале заданного числа N.

Будьте внимательны!
1000! содержит 2568 цифр, поэтому прямое вычисление факториала может быть неэффективным.
"""

def zeros(n):
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5

    return count

print(count_trailing_zeros(5))
print(count_trailing_zeros(10))
print(count_trailing_zeros(25))
print(count_trailing_zeros(100))
print(count_trailing_zeros(1000))
print(count_trailing_zeros(5000))