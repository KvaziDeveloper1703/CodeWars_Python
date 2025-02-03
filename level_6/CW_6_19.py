"""
Implement the function unique_in_order, which takes a sequence (string, list, or tuple) and returns a list without adjacent duplicate elements, while preserving the original order.

Examples:
unique_in_order('AAAABBBCCDAABBB')  → ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')          → ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])    → [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))    → [1, 2, 3]

Реализуйте функцию unique_in_order, которая принимает последовательность (строку, список или кортеж) и возвращает список без повторяющихся подряд элементов, сохраняя их исходный порядок.

Примеры:
unique_in_order('AAAABBBCCDAABBB')  → ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')          → ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])    → [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))    → [1, 2, 3]
"""

def unique_in_order(sequence):
    if not sequence:
        return []

    unique_list = []

    for i, element in enumerate(sequence):
        if i == 0 or element != sequence[i - 1]:
            unique_list.append(element)

    return unique_list

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
print(unique_in_order([]))
print(unique_in_order('A'))
print(unique_in_order([1, 1, 1, 1, 1]))