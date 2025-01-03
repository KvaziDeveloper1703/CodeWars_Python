"""
The task is to write a function that converts a list of integers into a formatted string. The formatting rules are as follows:

+ Use a comma-separated list to express the integers.
+ Consecutive integers that form a sequence of at least three numbers should be represented as a range, with the start and end of the range separated by a dash (-).
+ Integers that do not belong to a range should be listed individually.
+ The input list will always be sorted in increasing order.

Examples:
Input: [12, 13, 15, 16, 17] → Output: "12,13,15-17"
Input: [1, 2, 3, 5, 7, 8, 9, 10] → Output: "1-3,5,7-10"
Input: [1, 3, 4, 5, 7, 9] → Output: "1,3-5,7,9"

Задача состоит в написании функции, которая преобразует список целых чисел в форматированную строку. Правила форматирования следующие:

+ Используйте список, разделённый запятыми, для представления чисел.
+ Последовательные числа, образующие последовательность из как минимум трёх чисел, должны быть представлены в виде диапазона, где начальное и конечное число диапазона разделены дефисом (-).
+ Числа, не принадлежащие диапазону, должны быть указаны отдельно.
+ Входной список всегда отсортирован по возрастанию.

Примеры:
Ввод: [12, 13, 15, 16, 17] → Вывод: "12,13,15-17"
Ввод: [1, 2, 3, 5, 7, 8, 9, 10] → Вывод: "1-3,5,7-10"
Ввод: [1, 3, 4, 5, 7, 9] → Вывод: "1,3-5,7,9"

https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
"""

def solution(args):
    ranges = []
    start = args[0]
    current = args[0]

    for num in args[1:]:
        if num == current + 1:
            current = num
        else:
            if current - start >= 2:
                ranges.append(f"{start}-{current}")
            else:
                ranges.extend(map(str, range(start, current + 1)))
            start = current = num

    if current - start >= 2:
        ranges.append(f"{start}-{current}")
    else:
        ranges.extend(map(str, range(start, current + 1)))

    return ",".join(ranges)

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))