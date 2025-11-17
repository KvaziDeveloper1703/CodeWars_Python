'''
Gerrymander.
The practice of dividing a state, county, or region into electoral districts in a way that gives one political party a majority in many districts, while concentrating the opposing party’s voters into as few districts as possible.

Objective:
You are given a 5×5 region populated by 25 citizens. Write a function that divides this region into 5 districts under the following conditions:
    - 10 citizens support your candidate, and 15 support the opponent;
    - Your candidate must win the majority in at least 3 out of the 5 districts;
    - Each district must contain the same number of voters, i.e., exactly 5 cells;
    - Each district must be contiguous, meaning all cells in a district must form one connected region (orthogonally adjacent: up/down/left/right).

Concept Overview:
    - The input is a 5×5 matrix, each being:
        - 'O' - a voter for your candidate;
        - 'X' - a voter for the opponent.

Panels illustrate possible district divisions:
    - Panel B: Proportionate results;
    - Panel C: Disproportionate - one party wins all;
    - Panel D: Disproportionate - your candidate wins the majority despite the opponent having more total supporters.

Your task is to implement Panel D behavior.

Gerrymander.
Разделение территории на избирательные округа таким образом, чтобы обеспечить преимущество одной политической партии, концентрируя избирателей оппозиции в меньшем числе округов.

Цель задания:
Дано поле 5×5, содержащее 25 избирателей.Нужно написать функцию, которая делит это поле на 5 округов при соблюдении условий:
    - 10 человек голосуют за вашего кандидата, 15 - за оппонента;
    - Ваш кандидат должен победить минимум в 3 из 5 округов;
    - Каждый округ должен содержать ровно 5 клеток;
    - Каждый округ должен быть связным: все клетки округа должны соприкасаться по сторонам (вверх, вниз, влево, вправо).

Описание:
На вход подаётся поле 5×5, где:
    - 'O' - избиратель за вашего кандидата;
    - 'X' - избиратель за соперника.

Существует несколько способов разметки округов. Необходимо реализовать вариант, аналогичный панели D (когда ваш кандидат выигрывает большинство округов при меньшем общем числе сторонников).
'''

from itertools import combinations

GRID_SIZE = 5
TOTAL_CELLS = GRID_SIZE * GRID_SIZE

cell_coordinates = [(row_index, column_index)
                    for row_index in range(GRID_SIZE)
                    for column_index in range(GRID_SIZE)]

position_index_by_coordinates = {
    cell_coordinates[i]: i for i in range(TOTAL_CELLS)
}

neighbor_indices_by_cell = [[] for _ in range(TOTAL_CELLS)]
for index, (row_index, column_index) in enumerate(cell_coordinates):
    for delta_row, delta_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row = row_index + delta_row
        neighbor_column = column_index + delta_column
        if 0 <= neighbor_row < GRID_SIZE and 0 <= neighbor_column < GRID_SIZE:
            neighbor_indices_by_cell[index].append(
                position_index_by_coordinates[(neighbor_row, neighbor_column)]
            )

def subset_is_connected(cell_indices_subset):
    subset_set = set(cell_indices_subset)
    stack = [cell_indices_subset[0]]
    visited = {cell_indices_subset[0]}
    while stack:
        current = stack.pop()
        for neighbor in neighbor_indices_by_cell[current]:
            if neighbor in subset_set and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return len(visited) == len(cell_indices_subset)

connected_regions_of_five = []
for combination in combinations(range(TOTAL_CELLS), 5):
    if subset_is_connected(combination):
        connected_regions_of_five.append(combination)

regions_by_cell_index = [[] for _ in range(TOTAL_CELLS)]
for region_index, region_cells in enumerate(connected_regions_of_five):
    for cell_index in region_cells:
        regions_by_cell_index[cell_index].append(region_index)

def gerrymander(s):
    rows = s.split("\n")
    if len(rows) != GRID_SIZE or any(len(row) != GRID_SIZE for row in rows):
        return None

    flat_voters = "".join(rows)
    if any(ch not in ("O", "X") for ch in flat_voters):
        return None

    region_is_won_by_candidate = []
    for region_cells in connected_regions_of_five:
        number_of_supporters = sum(
            1 for cell_index in region_cells if flat_voters[cell_index] == "O"
        )
        region_is_won_by_candidate.append(number_of_supporters >= 3)

    cell_is_assigned = [False] * TOTAL_CELLS
    chosen_regions = []
    result_string_holder = [None]

    def depth_first_search(number_of_winning_regions):
        if result_string_holder[0] is not None:
            return True

        number_of_chosen_regions = len(chosen_regions)
        if number_of_winning_regions + (5 - number_of_chosen_regions) < 3:
            return False

        if number_of_chosen_regions == 5:
            if not all(cell_is_assigned):
                return False
            if number_of_winning_regions >= 3:
                district_labels = ["0"] * TOTAL_CELLS
                for district_index, region_index in enumerate(chosen_regions, start=1):
                    for cell_index in connected_regions_of_five[region_index]:
                        district_labels[cell_index] = str(district_index)
                output_rows = []
                for row_index in range(GRID_SIZE):
                    start = row_index * GRID_SIZE
                    end = start + GRID_SIZE
                    output_rows.append("".join(district_labels[start:end]))
                result_string_holder[0] = "\n".join(output_rows)
                return True
            return False

        try:
            first_unassigned_cell = next(
                i for i, assigned in enumerate(cell_is_assigned) if not assigned
            )
        except StopIteration:
            return False

        for region_index in regions_by_cell_index[first_unassigned_cell]:
            region_cells = connected_regions_of_five[region_index]
            if any(cell_is_assigned[cell_index] for cell_index in region_cells):
                continue

            chosen_regions.append(region_index)
            for cell_index in region_cells:
                cell_is_assigned[cell_index] = True

            new_number_of_winning_regions = number_of_winning_regions + (
                1 if region_is_won_by_candidate[region_index] else 0
            )

            if depth_first_search(new_number_of_winning_regions):
                return True

            for cell_index in region_cells:
                cell_is_assigned[cell_index] = False
            chosen_regions.pop()

        return False

    depth_first_search(0)
    return result_string_holder[0]