'''
A Carmichael number is defined as a composite number N that nevertheless passes Fermat’s primality test, that is: for every integer M that is relatively prime to N, the value of M raised to the power (N minus 1) is congruent to 1 modulo N.

Find a Carmichael number that satisfies the following conditions:
    + It is the product of exactly seven prime numbers;
    + Each prime factor lies between ten million (10^7) and one billion (10^9).

Submit the prime factorization of such a number.

Число Кармайкла — это составное число N, которое тем не менее проходит тест простоты Ферма, то есть: для любого целого числа M, взаимно простого с N, значение M в степени (N минус 1) сравнимо с 1 по модулю N.

Найдите число Кармайкла, которое удовлетворяет следующим условиям:
    + Оно является произведением ровно семи простых чисел;
    + Каждый простой множитель находится в диапазоне от десяти миллионов (10^7) до одного миллиарда (10^9).

Необходимо представить разложение этого числа на простые множители.
'''

from math import prod, gcd

primes = [
    13501351,
    14581459,
    16201621,
    17281729,
    58325833,
    64806481,
    77767777
]

candidate_composite_number = prod(primes)

are_all_prime_factors_unique = len(set(primes)) == len(primes)

def does_number_satisfy_korselt_condition(number_to_check, list_of_prime_factors):
    for single_prime_factor in list_of_prime_factors:
        if (number_to_check - 1) % (single_prime_factor - 1) != 0:
            return False
    return True

is_korselt_condition_satisfied = does_number_satisfy_korselt_condition(
    candidate_composite_number,
    primes
)

def does_number_satisfy_fermat_condition_for_base(number_to_check, base_value):
    if gcd(base_value, number_to_check) != 1:
        return None
    modular_exponentiation_result = pow(base_value, number_to_check - 1, number_to_check)
    return modular_exponentiation_result == 1

list_of_test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]

fermat_condition_results_by_base = {}
for current_base in list_of_test_bases:
    result_for_base = does_number_satisfy_fermat_condition_for_base(
        candidate_composite_number,
        current_base
    )
    fermat_condition_results_by_base[current_base] = result_for_base

print(primes)
print(candidate_composite_number)
print(are_all_prime_factors_unique)
print(is_korselt_condition_satisfied)

for current_base in list_of_test_bases:
    print(current_base, fermat_condition_results_by_base[current_base])