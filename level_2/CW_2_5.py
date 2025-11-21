'''
The key difficulty of this kata comes from the extremely large size of the input strings that your function must process.

For comparison, the test cases in Bubbler’s Insane version go up to 100,000 characters. In this kata, the limit is increased to 1,000,000,000 characters - that is 10,000 times more.

Because of such enormous input sizes, the challenge is not about micro-optimizing code execution, but about significantly reducing the algorithmic complexity.

Note that the test cases are randomly generated, so the execution time can vary between attempts. However, a well-designed solution should pass within the time limit in 99% of runs.

Главная сложность этого ката связана с огромным размером входных строк, которые должна обработать ваша функция.

Для сравнения: в «Insane»-версии от Bubbler тестовые случаи достигают 100 000 символов. В этой задаче ограничение увеличено до 1 000 000 000 символов - то есть в 10 000 раз больше.

При таких гигантских размерах входных данных задача состоит не в ускорении исполнения кода на уровне операций, а в радикальном уменьшении алгоритмической сложности.

Обратите внимание, что тесты генерируются случайным образом, поэтому время выполнения может немного отличаться от запуска к запуску. Тем не менее, хорошее решение должно укладываться в лимит примерно в 99% случаев.
'''

def triangle(row: str) -> str:
    length = len(row)
    if length == 1:
        return row[0]

    color_to_number = {'R': 0, 'G': 1, 'B': 2}
    number_to_color = ('R', 'G', 'B')
    color_values = [color_to_number[color] for color in row]

    combination_index = length - 1
    combination_index_digits_base3 = []
    while combination_index:
        combination_index_digits_base3.append(combination_index % 3)
        combination_index //= 3

    total_value = 0

    for position, color_value in enumerate(color_values):
        index_value = position
        digit_position = 0
        count_two_factor_parity = 0
        is_nonzero_coefficient = True

        while index_value > 0 or digit_position < len(combination_index_digits_base3):
            digit_n = combination_index_digits_base3[digit_position] if digit_position < len(combination_index_digits_base3) else 0
            digit_k = index_value % 3

            if digit_k > digit_n:
                is_nonzero_coefficient = False
                break

            if digit_n == 2 and digit_k == 1:
                count_two_factor_parity ^= 1

            index_value //= 3
            digit_position += 1

        if not is_nonzero_coefficient:
            continue

        coefficient_mod3 = 2 if count_two_factor_parity else 1
        total_value = (total_value + coefficient_mod3 * color_value) % 3

    if length % 2 == 0:
        total_value = (total_value * 2) % 3

    return number_to_color[total_value]