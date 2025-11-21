'''
You have an a × b grid filled with integers from 0 to m−1.
Your goal is to make all cells equal to 0.

Rules:
    - The value 0 represents the “up” direction;
    - Clicking a cell rotates that cell and all of its neighbors;
    - Each rotation increases the cell’s value by 1 (mod m);
    - If a cell has value m−1, rotating it wraps it back to 0;
    - Edge and corner cells affect only the neighbors that exist within the grid.

У вас есть поле размером a × b, заполненное числами от 0 до m−1.
Цель - сделать так, чтобы все клетки стали равны 0.

Правила:
    - Значение 0 соответствует направлению «вверх»;
    - Нажатие на клетку поворачивает её и всех соседей;
    - Каждый поворот увеличивает значение клетки на 1 (по модулю m);
    - Если клетка имеет значение m−1, после поворота она становится 0;
    - Для клеток на краю или углу поворачиваются только существующие соседи. 
'''

from typing import List, Tuple

def solve(board: List[List[int]], modulus: int) -> List[Tuple[int, int, int]]:
    height: int = len(board)
    width: int = len(board[0])

    number_of_cells: int = height * width
    equations: List[dict[int, int]] = []
    right_hand_side: List[int] = []

    def cell_index(row_index: int, column_index: int) -> int:
        return row_index * width + column_index

    for row_index in range(height):
        for column_index in range(width):
            equation_row: dict[int, int] = {}
            for delta_row in (-1, 0, 1):
                for delta_column in (-1, 0, 1):
                    neighbor_row: int = row_index + delta_row
                    neighbor_column: int = column_index + delta_column
                    if 0 <= neighbor_row < height and 0 <= neighbor_column < width:
                        index: int = cell_index(neighbor_row, neighbor_column)
                        equation_row[index] = 1
            equations.append(equation_row)
            right_hand_side.append((-board[row_index][column_index]) % modulus)

    pivot_row_for_column: List[int] = [-1] * number_of_cells

    for column_index in range(number_of_cells):
        pivot_row_index: int = -1
        for current_row_index in range(column_index, number_of_cells):
            coefficient_value: int = equations[current_row_index].get(column_index, 0) % modulus
            if coefficient_value != 0:
                pivot_row_index = current_row_index
                break
        if pivot_row_index == -1:
            continue

        equations[column_index], equations[pivot_row_index] = equations[pivot_row_index], equations[column_index]
        right_hand_side[column_index], right_hand_side[pivot_row_index] = right_hand_side[pivot_row_index], right_hand_side[column_index]

        pivot_row_for_column[column_index] = column_index

        pivot_coefficient: int = equations[column_index][column_index]
        inverse_value: int = pow(pivot_coefficient, -1, modulus)

        for key_index in list(equations[column_index].keys()):
            equations[column_index][key_index] = (equations[column_index][key_index] * inverse_value) % modulus
        right_hand_side[column_index] = (right_hand_side[column_index] * inverse_value) % modulus

        for current_row_index in range(number_of_cells):
            if current_row_index == column_index:
                continue
            factor_value: int = equations[current_row_index].get(column_index, 0)
            if factor_value == 0:
                continue
            for key_index, value in equations[column_index].items():
                new_value: int = (equations[current_row_index].get(key_index, 0) - factor_value * value) % modulus
                if new_value == 0:
                    if key_index in equations[current_row_index]:
                        del equations[current_row_index][key_index]
                else:
                    equations[current_row_index][key_index] = new_value
            right_hand_side[current_row_index] = (right_hand_side[current_row_index] - factor_value * right_hand_side[column_index]) % modulus
            if column_index in equations[current_row_index]:
                del equations[current_row_index][column_index]

    solution_clicks_flat: List[int] = [0] * number_of_cells
    for cell in range(number_of_cells):
        pivot_row_index = pivot_row_for_column[cell]
        if pivot_row_index != -1:
            solution_clicks_flat[cell] = right_hand_side[pivot_row_index] % modulus

    result_moves: List[Tuple[int, int, int]] = []
    for row_index in range(height):
        for column_index in range(width):
            index: int = cell_index(row_index, column_index)
            click_count: int = solution_clicks_flat[index] % modulus
            if click_count != 0:
                result_moves.append((row_index, column_index, click_count))

    return result_moves