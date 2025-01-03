"""
A traveler is given a series of directions to navigate through a mountainous desert. The directions are provided as a list of strings: "NORTH", "SOUTH", "EAST", and "WEST". Opposite directions, such as "NORTH" and "SOUTH", cancel each other out, as do "EAST" and "WEST".

Your task is to simplify the list of directions by removing any pairs of opposite directions that follow one another or can be reduced. The goal is to provide the traveler with an optimized route that minimizes unnecessary backtracking.

For example:
Input: ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
Output: ["WEST"]

Путнику дали маршрут, состоящий из последовательности направлений через горную пустыню. Направления представлены в виде списка строк: "NORTH", "SOUTH", "EAST", "WEST". Противоположные направления, такие как "NORTH" и "SOUTH", а также "EAST" и "WEST", взаимно уничтожаются.

Ваша задача — упростить маршрут, удалив пары противоположных направлений, которые идут друг за другом или могут быть сокращены. Цель — предоставить путешественнику оптимизированный маршрут, исключив ненужные движения назад.

Например:
Ввод: ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
Вывод: ["WEST"]

https://www.codewars.com/kata/550f22f4d758534c1100025a
"""

def simplify_directions(directions):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []

    for direction in directions:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack

print(simplify_directions(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(simplify_directions(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))
