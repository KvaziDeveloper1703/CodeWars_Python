"""
Consider an array of sheep where some sheep may be missing. You need to write a function that counts the number of sheep present in the array (true means the sheep is present).

Example:
[True,  True,  True,  False, True,  True,  True,  True, True,  False, True,  False, True,  False, False, True, True,  True,  True,  True, False, False, True,  True]

Answer: 17.

Дан массив овец, где некоторые из них могут отсутствовать. Необходимо написать функцию, которая подсчитает количество присутствующих овец (true означает, что овца на месте).

Пример:
[True,  True,  True,  False, True,  True,  True,  True, True,  False, True,  False, True,  False, False, True, True,  True,  True,  True, False, False, True,  True]

Ответ: 17.
"""

def count_sheeps(sheeps):
    count = 0
    for sheep in sheeps:
        if sheep is True:
            count += 1
    return count

array = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]
answer = count_sheeps(array)
print(answer)