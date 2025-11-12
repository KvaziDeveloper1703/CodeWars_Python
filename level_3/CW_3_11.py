'''
The goal of this kata is to write a program that performs algebraic expansion.

You need to write a function expand that takes an expression of the form (ax + b)^n, where:
    - a and b are integers (positive or negative),
    - x is a single-character variable,
    - n is a natural number (n ≥ 0).

Rules:
    - If a = 1, the coefficient 1 is not shown;
    - If a = -1, only a "-" is shown before x.

The function must return the expanded polynomial as a string in the format:
    ax^b + cx^d + ex^f + ...

where:
    - the powers (b, d, f, …) are in decreasing order,
    - terms with a zero coefficient are omitted,
    - if a coefficient is 1, it is not shown,
    - if a coefficient is -1, only "-" is shown,
    - if the power is 0, only the coefficient is shown,
    - if the power is 1, omit the caret (^) and exponent.

Цель задачи - написать программу, которая выполняет алгебраическое раскрытие скобок.

Нужно написать функцию expand, которая принимает выражение вида (ax + b)^n, где:
    - a и b - целые числа (могут быть отрицательными),
    - x - переменная, состоящая из одного символа,
    - n - натуральное число (n ≥ 0).

Правила форматирования:
    - Если a = 1, коэффициент 1 не указывается перед x;
    - Если a = -1, перед x ставится только "-".

Результат возвращается в виде строки — раскрытый многочлен:
    ax^b + cx^d + ex^f + ...
где степени (b, d, f, …) указаны в порядке убывания.

Дополнительные правила:
    - Термы с коэффициентом 0 пропускаются;
    - Если коэффициент равен 1, он не пишется;
    - Если коэффициент равен -1, пишется только "-";
    - Если степень равна 0, пишется только число (без x);
    - Если степень равна 1, символ ^ и показатель не пишутся.
'''

import math

def expand(expression: str) -> str:
    right_parenthesis_index = expression.index(')')
    inner_expression = expression[1:right_parenthesis_index]
    exponent_n = int(expression[right_parenthesis_index + 2:])

    variable_character_index = None
    variable_character = None
    for current_index, current_character in enumerate(inner_expression):
        if current_character.isalpha():
            variable_character_index = current_index
            variable_character = current_character
            break

    coefficient_a_string = inner_expression[:variable_character_index]
    if coefficient_a_string == '':
        coefficient_a = 1
    elif coefficient_a_string == '-':
        coefficient_a = -1
    else:
        coefficient_a = int(coefficient_a_string)

    coefficient_b_string = inner_expression[variable_character_index + 1:]
    coefficient_b = int(coefficient_b_string) if coefficient_b_string else 0

    result_terms_strings = []
    for exponent_of_variable in range(exponent_n, -1, -1):
        exponent_of_b = exponent_n - exponent_of_variable
        binomial_coefficient = math.comb(exponent_n, exponent_of_b)
        term_coefficient = (
            binomial_coefficient
            * (coefficient_a ** exponent_of_variable)
            * (coefficient_b ** exponent_of_b)
        )

        if term_coefficient == 0:
            continue

        if exponent_of_variable == 0:
            term_body_string = str(abs(term_coefficient))
        else:
            absolute_coefficient = abs(term_coefficient)
            if absolute_coefficient == 1:
                coefficient_part_string = ''
            else:
                coefficient_part_string = str(absolute_coefficient)

            if exponent_of_variable == 1:
                variable_part_string = variable_character
            else:
                variable_part_string = f"{variable_character}^{exponent_of_variable}"

            term_body_string = coefficient_part_string + variable_part_string

        if not result_terms_strings:
            sign_part_string = '-' if term_coefficient < 0 else ''
        else:
            sign_part_string = '-' if term_coefficient < 0 else '+'

        result_terms_strings.append(sign_part_string + term_body_string)

    if not result_terms_strings:
        return "0"

    return "".join(result_terms_strings)