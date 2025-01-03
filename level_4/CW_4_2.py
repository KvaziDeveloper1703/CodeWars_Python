"""
Write a function snail that takes an n x n matrix (a square 2D array) and returns a list of its elements arranged in a clockwise spiral order, starting from the outermost elements and moving towards the center.

Rules:
+ Begin with the top-left corner and traverse the outermost layer in a clockwise direction.
+ Continue spiraling inward, processing one layer at a time, until all elements are included.

Examples:
Input:
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input:
array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Напишите функцию snail, которая принимает квадратную матрицу размером n x n (двумерный массив) и возвращает список её элементов, упорядоченных по часовой стрелке, начиная с внешних элементов и двигаясь к центру.

Правила:
+ Начните с верхнего левого угла и обойдите внешний слой матрицы по часовой стрелке.
+ Продолжайте движение внутрь, обрабатывая один слой за раз, пока все элементы не будут включены в результат.

Примеры:
Ввод:
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
Вывод: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Ввод:
array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9]

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
"""
def snail(snail_map):
    result = []
    if not snail_map or not snail_map[0]:
        return result

    n = len(snail_map)
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(snail_map[top][j])
        top += 1

        for i in range(top, bottom + 1):
            result.append(snail_map[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(snail_map[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(snail_map[i][left])
            left += 1

    return result

print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))