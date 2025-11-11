'''
Complete the function same_structure_as(original, other) that returns True if the second array has the same structure as the first one.

Two arrays have the same structure if:
    - They have the same nesting pattern;
    - Each corresponding array has the same length at each nesting level.

The actual values inside the arrays do not matter - only the structure does.

Дополните функцию same_structure_as(original, other), которая возвращает True, если второй список имеет такую же структуру, как и первый.

Два списка считаются одинаковыми по структуре, если:
    - У них одинаковое вложение списков;
    - На каждом уровне вложенности количество элементов совпадает.

Значения внутри списков не имеют значения — важна только структура.
'''

def same_structure_as(original, other):
    if not isinstance(original, list) and not isinstance(other, list):
        return True
    if isinstance(original, list) != isinstance(other, list):
        return False
    if len(original) != len(other):
        return False
    for x, y in zip(original, other):
        if not same_structure_as(x, y):
            return False
    return True