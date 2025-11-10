'''
Write a function that takes a square matrix (N × N 2D array) and returns its determinant.

Напишите функцию, которая принимает квадратную матрицу (N × N двумерный массив) и возвращает её определитель (детерминант).
'''

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant_value = 0

    for column in range(len(matrix)):
        minor = [row[:column] + row[column+1:] for row in matrix[1:]]
        sign = (-1) ** column
        determinant_value += sign * matrix[0][column] * determinant(minor)

    return determinant_value