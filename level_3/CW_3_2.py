"""
Write a function sudoku that solves a 9x9 Sudoku puzzle. The function will take a 2D array as input, where 0 represents an unknown square, and it should return the completed Sudoku grid.

Rules:
+ The Sudoku grid is a 9x9 array.
+ Each row, column, and 3x3 sub-grid must contain the numbers 1 through 9, without repetition.
+ The input puzzles are guaranteed to be solvable without guessing or backtracking, so a brute-force approach will suffice.

Example:
Input:
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
Output:
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

Напишите функцию sudoku, которая решает головоломку Судоку размером 9x9. Функция принимает в качестве входных данных двумерный массив, где 0 обозначает неизвестную ячейку, и возвращает завершённую таблицу Судоку.

Правила:
+ Поле Судоку состоит из массива 9x9.
+ Каждая строка, столбец и 3x3 подмассив должны содержать числа от 1 до 9 без повторений.
+ Входные головоломки гарантированно решаемы без предположений или перебора, поэтому можно использовать метод "в лоб".

Пример:
Ввод:
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
Вывод:
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

https://www.codewars.com/kata/5296bc77afba8baa690002d7
"""

def sudoku(puzzle):
    
    # Checks if placing a number in a specific position is valid.
    # Проверяет, является ли размещение числа в конкретной позиции допустимым.
    def is_valid(num, row, col):

        # Check the row
        # Проверяем строку
        if num in puzzle[row]:
            return False

        # Check the column
        # Проверяем столбец
        for r in range(9):
            if puzzle[r][col] == num:
                return False

        # Check the 3x3 sub-grid
        # Проверяем подгрид 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if puzzle[r][c] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                
                # Find an empty cell
                # Ищем пустую клетку
                if puzzle[row][col] == 0:  
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            
                            # Place the number
                            # Размещаем число
                            puzzle[row][col] = num  
                            if solve():
                                return True
                            
                            # Backtrack
                            # Откатываемся назад
                            puzzle[row][col] = 0
                    
                    # No valid number found
                    # Не найдено подходящего числа
                    return False  
        
        # Puzzle is solved
        # Судоку решено
        return True  

    solve()
    return puzzle

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_puzzle = sudoku(puzzle)
for row in solved_puzzle:
    print(row)