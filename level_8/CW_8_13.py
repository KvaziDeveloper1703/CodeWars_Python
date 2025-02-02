"""
Consider an array (or list) of sheep where some sheep may be missing. You need to write a function that counts the number of sheep present in the array (true means the sheep is present).

Example:
[True,  True,  True,  False,
 True,  True,  True,  True,
 True,  False, True,  False,
 True,  False, False, True,
 True,  True,  True,  True,
 False, False, True,  True]

The correct answer is 17.

Hint: Don't forget to check for bad values like null or undefined.

Дан массив (или список) овец, где некоторые из них могут отсутствовать. Необходимо написать функцию, которая подсчитает количество присутствующих овец (true означает, что овца на месте).

Пример:
[True,  True,  True,  False,
 True,  True,  True,  True,
 True,  False, True,  False,
 True,  False, False, True,
 True,  True,  True,  True,
 False, False, True,  True]

Правильный ответ: 17.

Подсказка: Не забудьте учесть возможные некорректные значения, такие как null или undefined.
"""

def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count

sheep_array = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]

print(count_sheep(sheep_array))