"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers.

Example:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])  

Conditions:
+ Easy case — if the list consists only of positive numbers, the maximum sum is the sum of the entire array.
+ If the list consists only of negative numbers, return 0.
+ An empty list is considered to have a maximum sum of zero.
+ An empty list or array is a valid sublist/subarray.

Задача о максимальной сумме подмассива заключается в поиске максимальной суммы непрерывной подпоследовательности в массиве или списке целых чисел.

Пример:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])  

Условия:
+ Простой случай — если массив состоит только из положительных чисел, максимальная сумма будет равна сумме всего массива.
+ Если массив состоит только из отрицательных чисел, вернуть 0.
+ Пустой массив считается имеющим нулевую максимальную сумму.
+ Пустой массив — это также допустимый подмассив.
"""

def max_sequence(given_array):
    if not given_array:
        return 0

    max_sum = 0
    current_sum = 0

    for number in given_array:
        current_sum += number

        if current_sum < 0:
            current_sum = 0

        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([1, 2, 3, 4, 5]))
print(max_sequence([-1, -2, -3, -4]))
print(max_sequence([]))
print(max_sequence([3, -2, 5, -1]))