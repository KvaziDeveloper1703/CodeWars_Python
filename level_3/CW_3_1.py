"""
Write a function that validates a given 10x10 Battleship game board. The function should return true if the board setup is valid according to the rules of the game, and false otherwise. The board is represented as a 2D array, where 0 indicates an empty cell, and 1 indicates a cell occupied by a ship.

Rules:
+ The board must contain:
    + 1 battleship (4 cells in a straight line).
    + 2 cruisers (3 cells each in a straight line).
    + 3 destroyers (2 cells each in a straight line).
    + 4 submarines (1 cell each).
+ Ships must not overlap or touch each other, even diagonally.
+ Each ship must be a straight line (horizontal or vertical), except for submarines, which are single cells.
+ No additional ships or missing ships are allowed.

Example:
Input:
board = [
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  ...
]
Output: true (if the setup follows the rules).

Напишите функцию, которая проверяет заданное поле для игры «Морской бой» размером 10x10. Функция должна возвращать true, если расстановка кораблей на поле соответствует правилам игры, и false в противном случае. Поле представлено в виде двумерного массива, где 0 означает пустую клетку, а 1 — клетку, занятую кораблём.

Правила:
+ На поле должны быть:
    + 1 линкор (4 клетки в одну линию).
    + 2 крейсера (по 3 клетки в одну линию).
    + 3 эсминца (по 2 клетки в одну линию).
    + 4 подводные лодки (по 1 клетке каждая).
+ Корабли не могут пересекаться или соприкасаться, даже по диагонали.
+ Каждый корабль должен быть прямой линией (горизонтальной или вертикальной), кроме подводных лодок, которые занимают одну клетку.
+ Недостающие или лишние корабли не допускаются.

Пример:
Ввод:
board = [
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  ...
]
Вывод: true (если расстановка соответствует правилам).

https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
"""

def valid_battleship_board(board):
    def mark_ship(x, y):
        # Traverses the cells of a ship and marks them as visited.
        # Обходит клетки корабля и помечает их как посещённые.
        ship_cells = []

        # Check if the cell is a valid starting point of a ship
        # Проверяем, является ли клетка начальной точкой корабля
        if x < 0 or y < 0 or x >= 10 or y >= 10 or board[x][y] != 1:
            return []

        # Stack for traversing the ship cells
        # Стек для обхода клеток корабля
        stack = [(x, y)]

        while stack:
            i, j = stack.pop()

            # Validate the cell boundaries and status
            # Проверяем границы и статус клетки
            if i < 0 or j < 0 or i >= 10 or j >= 10 or board[i][j] != 1:
                continue

            # Mark the cell as visited
            # Помечаем клетку как посещённую
            board[i][j] = -1
            ship_cells.append((i, j))

            # Add neighboring cells to the stack
            # Добавляем соседние клетки в стек
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))

        return ship_cells

    def is_valid_ship(ship_cells):
        if not ship_cells:
            return False

        # Check if the ship is horizontal
        # Проверяем, является ли корабль горизонтальным
        if all(x == ship_cells[0][0] for x, y in ship_cells):
            ship_cells.sort(key=lambda cell: cell[1])
            for k in range(1, len(ship_cells)):
                if ship_cells[k][1] != ship_cells[k - 1][1] + 1:
                    return False

        # Check if the ship is vertical
        # Проверяем, является ли корабль вертикальным
        elif all(y == ship_cells[0][1] for x, y in ship_cells):
            ship_cells.sort(key=lambda cell: cell[0])
            for k in range(1, len(ship_cells)):
                if ship_cells[k][0] != ship_cells[k - 1][0] + 1:
                    return False
        else:
            return False

        # Check the surrounding cells for the absence of other ships
        # Проверяем окружение корабля на отсутствие других кораблей
        for x, y in ship_cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 1:
                        return False

        return True

    # Initialize the ship count by lengths
    # Инициализируем счётчик кораблей по их длинам
    ship_count = {4: 0, 3: 0, 2: 0, 1: 0}

    # Traverse all cells of the board
    # Проходим по всем клеткам поля
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                # Identify the current ship's cells
                # Определяем клетки текущего корабля
                ship_cells = mark_ship(i, j)

                # Check if the ship is valid
                # Проверяем, валиден ли корабль
                if not is_valid_ship(ship_cells):
                    return False

                # Check the ship's length
                # Проверяем длину корабля
                ship_length = len(ship_cells)
                if ship_length in ship_count:
                    ship_count[ship_length] += 1
                else:
                    return False

    # Verify the correct number of ships
    # Проверяем корректность количества кораблей
    return ship_count == {4: 1, 3: 2, 2: 3, 1: 4}

board = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(valid_battleship_board(board))