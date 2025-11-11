'''
You are given a 6×6 Skyscraper puzzle.

Your task is to place skyscrapers of heights 1 to 6 in each square of the grid according to the following rules:
    - Each row and each column must contain all numbers from 1 to 6 exactly once;
    - The clues around the grid indicate how many skyscrapers are visible from that side;
        - A taller skyscraper blocks the view of any shorter ones behind it;
        - For example, if you see clue 4 from the left, you must be able to see four buildings when looking across that row from that direction.
    - You must fill the grid so that all clues are satisfied.

Your program should be able to solve any valid 6×6 puzzle given the clues.

Дана головоломка «Небоскрёбы» размером 6×6.

Необходимо расставить небоскрёбы высотой от 1 до 6 в каждой клетке таблицы, соблюдая следующие правила:
    - В каждой строке и каждом столбце должны быть все числа от 1 до 6 без повторений;
    - Подсказки по краям поля показывают, сколько небоскрёбов видно с этой стороны;
        - Более высокий небоскрёб закрывает вид на более низкие, стоящие за ним.
        - Например, если слева указана подсказка 4, значит, из этой точки видны четыре здания в этом ряду;
    - Нужно заполнить сетку так, чтобы все подсказки выполнялись.

Программа должна уметь решать любую корректную головоломку 6×6 по данным подсказкам.
'''

import itertools

def solve_puzzle(clues):
    grid_size = 6
    all_possible_rows = list(itertools.permutations(range(1, grid_size + 1)))

    def count_visible_buildings(row_sequence):
        visible_count = 0
        current_max_height = 0
        for building_height in row_sequence:
            if building_height > current_max_height:
                current_max_height = building_height
                visible_count += 1
        return visible_count

    def is_row_valid_for_clues(row_sequence, left_clue, right_clue):
        if left_clue and count_visible_buildings(row_sequence) != left_clue:
            return False
        if right_clue and count_visible_buildings(row_sequence[::-1]) != right_clue:
            return False
        return True

    top_clues = clues[:grid_size]
    right_clues = clues[grid_size:2 * grid_size]
    bottom_clues = clues[2 * grid_size:3 * grid_size][::-1]
    left_clues = clues[3 * grid_size:][::-1]

    possible_rows_for_each_index = [
        [
            row_candidate
            for row_candidate in all_possible_rows
            if is_row_valid_for_clues(row_candidate, left_clue_value, right_clue_value)
        ]
        for left_clue_value, right_clue_value in zip(left_clues, right_clues)
    ]

    remaining_numbers_in_columns = [set(range(1, grid_size + 1)) for _ in range(grid_size)]
    current_grid = [None] * grid_size
    solution_grid = None

    def solve_with_backtracking(row_index):
        nonlocal solution_grid
        if solution_grid:
            return
        if row_index == grid_size:
            for column_index in range(grid_size):
                column_values = [current_grid[row][column_index] for row in range(grid_size)]
                if len(set(column_values)) != grid_size:
                    return
                if top_clues[column_index] and count_visible_buildings(column_values) != top_clues[column_index]:
                    return
                if bottom_clues[column_index] and count_visible_buildings(column_values[::-1]) != bottom_clues[column_index]:
                    return
            solution_grid = tuple(tuple(row_values) for row_values in current_grid)
            return

        for row_candidate in possible_rows_for_each_index[row_index]:
            if all(
                row_candidate[column_index] in remaining_numbers_in_columns[column_index]
                for column_index in range(grid_size)
            ):
                for column_index in range(grid_size):
                    remaining_numbers_in_columns[column_index].remove(row_candidate[column_index])
                current_grid[row_index] = row_candidate
                solve_with_backtracking(row_index + 1)
                for column_index in range(grid_size):
                    remaining_numbers_in_columns[column_index].add(row_candidate[column_index])
            if solution_grid:
                return

    solve_with_backtracking(0)
    return solution_grid