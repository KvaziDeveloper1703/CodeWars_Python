'''
Given a height map represented as a 2D array of integers. Each value in the array represents the ground elevation at that position.

Determine the total volume of liquid that the height map can contain if water is poured over it until it stabilizes.

Rules:
    + Water can only escape off the edges of the height map;
    + Water cannot pass through diagonal cracks — only through horizontal or vertical neighbors;
    + Heights may be negative (imagine pits below ground level);
    + The map is always a rectangular grid (not ragged).

Example:
Heightmap:
8 8 8 8 6 6 6 6
8 0 0 8 6 0 0 6
8 0 0 8 6 0 0 6
8 8 8 8 6 6 6 0

Filled with water:
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 0

Дан рельеф местности в виде двумерного массива целых чисел. Каждое значение массива показывает высоту земли в данной точке.

Нужно найти общий объём жидкости (воды), который может удержать рельеф, если на него налить воду до максимального уровня заполнения.

Правила:
    + Вода может вытекать только через границы массива;
    + Вода не может протекать по диагонали — только через соседей сверху, снизу, слева и справа;
    + Высоты могут быть отрицательными (ямы ниже уровня земли);
    + Высота карты всегда задаётся прямоугольной таблицей.

Пример:
Высоты:
8 8 8 8 6 6 6 6
8 0 0 8 6 0 0 6
8 0 0 8 6 0 0 6
8 8 8 8 6 6 6 0

После заполнения водой:
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 6
8 8 8 8 6 6 6 0
'''

import heapq

def volume(heightmap):
    if not heightmap or len(heightmap[0]) == 0:
        return 0

    total_rows, total_columns = len(heightmap), len(heightmap[0])
    if total_rows < 3 or total_columns < 3:
        return 0

    visited_matrix = [[False] * total_columns for _ in range(total_rows)]
    min_heap_boundary = []

    def add_boundary_cell_to_heap(row_index, column_index):
        visited_matrix[row_index][column_index] = True
        heapq.heappush(min_heap_boundary, (heightmap[row_index][column_index], row_index, column_index))

    for column_index in range(total_columns):
        add_boundary_cell_to_heap(0, column_index)
        add_boundary_cell_to_heap(total_rows - 1, column_index)
    for row_index in range(1, total_rows - 1):
        add_boundary_cell_to_heap(row_index, 0)
        add_boundary_cell_to_heap(row_index, total_columns - 1)

    trapped_water_volume = 0
    neighbor_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while min_heap_boundary:
        current_height, current_row, current_column = heapq.heappop(min_heap_boundary)
        for delta_row, delta_column in neighbor_directions:
            neighbor_row, neighbor_column = current_row + delta_row, current_column + delta_column
            if not (0 <= neighbor_row < total_rows and 0 <= neighbor_column < total_columns):
                continue
            if visited_matrix[neighbor_row][neighbor_column]:
                continue
            visited_matrix[neighbor_row][neighbor_column] = True
            neighbor_height = heightmap[neighbor_row][neighbor_column]

            if neighbor_height < current_height:
                trapped_water_volume += current_height - neighbor_height
                effective_height = current_height
            else:
                effective_height = neighbor_height

            heapq.heappush(min_heap_boundary, (effective_height, neighbor_row, neighbor_column))

    return trapped_water_volume