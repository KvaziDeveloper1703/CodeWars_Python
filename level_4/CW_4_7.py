"""
Write a function sum_of_intervals that takes an array of intervals and returns the total length of all intervals, merging overlapping ones.

Rules:
+ Intervals are arrays [a, b] where a < b. Length = b - a.
+ Merge overlapping intervals before calculating the total length.

Examples:
[[1, 2], [6, 10], [11, 15]] → 9
[[1, 4], [7, 10], [3, 5]] → 7
[[1, 5], [10, 20], [1, 6]] → 19
[[0, 20], [-100000000, 10]] → 100000030

Напишите функцию sum_of_intervals, которая принимает массив интервалов и возвращает их общую длину, объединяя перекрывающиеся.

Правила:
+ Интервалы задаются как [a, b], где a < b. Длина = b - a.
+ Перекрывающиеся интервалы объединяются.

Примеры:
[[1, 2], [6, 10], [11, 15]] → 9
[[1, 4], [7, 10], [3, 5]] → 7
[[1, 5], [10, 20], [1, 6]] → 19
[[0, 20], [-100000000, 10]] → 100000030

https://www.codewars.com/kata/52b7ed099cdc285c300001cd
"""

def sum_of_intervals(intervals):

    if not intervals:
        return 0

    intervals.sort(key=lambda x: (x[0], x[1]))

    merged_intervals = []

    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end

    merged_intervals.append((current_start, current_end))

    total_length = 0
    for start, end in merged_intervals:
        length = end - start
        total_length += length

    return total_length

print(sum_intervals([[1, 2], [6, 10], [11, 15]]))
print(sum_intervals([[1, 4], [7, 10], [3, 5]]))
print(sum_intervals([[1, 5], [10, 20], [1, 6]]))
print(sum_intervals([[0, 20], [-100000000, 10]]))