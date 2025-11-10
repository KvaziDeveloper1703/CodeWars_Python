'''
Pyramids are fascinating - both in architecture and in mathematics!

You are given a pyramid of numbers represented as a list of lists (each inner list is one row of the pyramid).

Write a function that takes a pyramid (a list of lists of integers) and returns the maximum slide down sum.

Пирамиды удивительны - и в архитектуре, и в математике!

Дана числовая пирамида, представленная в виде списка списков (каждый вложенный список - это один ряд пирамиды).

Напиши функцию, которая принимает пирамиду (список списков целых чисел) и возвращает максимальную сумму пути вниз - то есть наибольшую сумму чисел от вершины до основания, если на каждом шаге можно двигаться к одному из двух соседних чисел следующего ряда.
'''

def longest_slide_down(pyramid):
    for row in range(len(pyramid) - 2, -1, -1):
        for column in range(len(pyramid[row])):
            pyramid[row][column] += max(pyramid[row + 1][column], pyramid[row + 1][column + 1])

    return pyramid[0][0]