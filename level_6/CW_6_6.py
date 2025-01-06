"""
Your task is to create a function called array_diff that takes two lists, a and b, and returns a new list that excludes all elements from a that are present in b. The order of elements in the resulting list must remain unchanged.

For example:
array_diff([1, 2], [1]) should return [2].
array_diff([1, 2, 2, 2, 3], [2]) should return [1, 3].

If an element appears multiple times in b, all occurrences of it in a should be removed.

Ваша задача — написать функцию array_diff, которая принимает два списка, a и b, и возвращает новый список, исключив из a все элементы, присутствующие в b. Порядок элементов в результирующем списке должен сохраняться.

Например:
array_diff([1, 2], [1]) должно вернуть [2].
array_diff([1, 2, 2, 2, 3], [2]) должно вернуть [1, 3].

Если элемент встречается в b несколько раз, все его вхождения в a должны быть удалены.

https://www.codewars.com/kata/523f5d21c841566fde000009
"""

def array_diff(a, b):
    result = []

    for element in a:
        if element not in b:
            result.append(element)

    return result

print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))