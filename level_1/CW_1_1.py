'''
The N Queens Puzzle is a classic problem in combinatorial chess: you must place N queens on an N×N chessboard so that no two queens attack each other - that is, no two queens share the same row, column, or diagonal.

You are given:
    - An integer N, representing the size of the board;
    - A mandatory queen position (row, column) - the coordinates (0-based) of a queen that must be placed on the board:
        - 0 <= row < N;
        - 0 <= column < N;
        - The top-left corner of the board has coordinates {0, 0}.

Your task is to find one valid arrangement of N queens that satisfies all conditions, including the fixed queen position. If a solution exists, return it as a string, where:
    - '.' represents an empty square;
    - 'Q' represents a queen;
    - Each row ends with a newline character '\n'.

If no solution exists for the given parameters, return None.

Задача N ферзей - это классическая комбинаторная задача: нужно расставить N ферзей на шахматной доске размером N×N так, чтобы ни один ферзь не атаковал другого, то есть ни два ферзя не стояли в одной строке, колонке или диагонали.

Дано:
Число N - размер доски;
Координаты обязательной позиции ферзя (row, column) - ферзь, который уже стоит на доске:
    - 0 <= row < N;
    - 0 <= column < N;
    - Верхний левый угол доски имеет координаты {0, 0}.

Нужно найти одно возможное решение, удовлетворяющее всем условиям, включая положение заданного ферзя. Если решение существует, вернуть его в виде строки, где:
    - '.' обозначает пустую клетку,
    - 'Q' обозначает ферзя,
    - каждая строка заканчивается символом перевода строки '\n'.

Если решения нет, вернуть None.
'''

def solve_n_queens(size, fixed_queen_position):
    fixed_row, fixed_column = fixed_queen_position

    if size in (2, 3):
        return None

    occupied_columns = set()
    occupied_main_diagonals = set()
    occupied_anti_diagonals = set()
    queen_columns_by_row = [-1] * size
    queen_columns_by_row[fixed_row] = fixed_column

    occupied_columns.add(fixed_column)
    occupied_main_diagonals.add(fixed_row - fixed_column)
    occupied_anti_diagonals.add(fixed_row + fixed_column)

    def search_solution(row_index):
        if row_index == size:
            return True
        if row_index == fixed_row:
            return search_solution(row_index + 1)

        for column_index in range(size):
            if (column_index in occupied_columns or
                row_index - column_index in occupied_main_diagonals or
                row_index + column_index in occupied_anti_diagonals):
                continue

            queen_columns_by_row[row_index] = column_index
            occupied_columns.add(column_index)
            occupied_main_diagonals.add(row_index - column_index)
            occupied_anti_diagonals.add(row_index + column_index)

            if search_solution(row_index + 1):
                return True

            occupied_columns.remove(column_index)
            occupied_main_diagonals.remove(row_index - column_index)
            occupied_anti_diagonals.remove(row_index + column_index)
            queen_columns_by_row[row_index] = -1
        return False

    if not search_solution(0):
        return None

    board_rows = []
    for row_index in range(size):
        row_cells = ['.'] * size
        if queen_columns_by_row[row_index] != -1:
            row_cells[queen_columns_by_row[row_index]] = 'Q'
        board_rows.append(''.join(row_cells))
    return '\n'.join(board_rows) + '\n'