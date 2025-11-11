'''
Write a function that returns True if the second array has the same nesting structure and the same lengths of nested arrays as the first one. Otherwise, return False.

Two arrays are considered to have the same structure if:
    - They contain the same number of elements;
    - For every corresponding element, either both are not arrays, or both are arrays that have the same internal structure recursively.

Напишите функцию, которая возвращает True, если второй массив имеет такую же структуру вложенности и такие же длины вложенных массивов, как и первый. В противном случае функция должна вернуть False.

Два массива считаются одинаковыми по структуре, если:
    - Они содержат одинаковое количество элементов;
    - Для каждой пары соответствующих элементов: либо оба не являются массивами, либо оба являются массивами, которые имеют одинаковую внутреннюю структуру (рекурсивно).
'''

def same_structure_as(original, other):
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    if len(original) != len(other):
        return False

    for a, b in zip(original, other):
        if isinstance(a, list) and isinstance(b, list):
            if not same_structure_as(a, b):
                return False
        elif isinstance(a, list) != isinstance(b, list):
            return False

    return True