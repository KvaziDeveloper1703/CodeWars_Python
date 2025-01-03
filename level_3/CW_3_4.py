"""
Create two functions to encode and decode a string using the Rail Fence Cipher.

Rules:

Encoding:
+ Write the string in a zigzag pattern across a given number of "rails."
+ Start at the top rail, move diagonally down until the bottom rail, then reverse direction and move diagonally up until the top rail again.
+ Repeat until all characters in the string are placed.
+ Read the characters row by row to form the encoded string.

Example (3 rails):
Input string: "WEAREDISCOVEREDFLEEATONCE"
Zigzag pattern:
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N   
Encoded string: "WECRLTEERDSOEEFEAOCAIVDEN"

Decoding:
+ Reverse the zigzag pattern to reconstruct the original string.
+ Use the same number of rails as was used for encoding.

The functions should:
+ Accept a string and the number of rails as arguments.
+ Handle strings containing spaces, punctuation, and special characters without filtering them.
+ Return an empty string for an empty input.
+ Assume the number of rails is always greater than or equal to 2.

Examples:
Encoding:
encode("HELLO WORLD", 3) → "HOLELWRDLO"
Decoding:
decode("HOLELWRDLO", 3) → "HELLO WORLD"

Создайте две функции для кодирования и декодирования строки с использованием Шифра Забора (Rail Fence Cipher).

Правила:

Кодирование:
+ Запишите строку зигзагом по заданному количеству "рельсов."
+ Начните с верхнего рельса, двигайтесь по диагонали вниз до нижнего рельса, затем измените направление и двигайтесь по диагонали вверх к верхнему рельсу.
+ Повторяйте, пока не разместите все символы строки.
+ Считайте символы по рядам, чтобы сформировать закодированную строку.

Пример (3 рельса):
Входная строка: "WEAREDISCOVEREDFLEEATONCE"
Зигзаг:
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
Закодированная строка: "WECRLTEERDSOEEFEAOCAIVDEN"

Декодирование:
+ Воссоздайте зигзаг, чтобы восстановить исходную строку.
+ Используйте то же количество рельсов, что и при кодировании.

Функции должны:
+ Принимать строку и количество рельсов в качестве аргументов.
+ Обрабатывать строки с пробелами, знаками препинания и спецсимволами без их фильтрации.
+ Возвращать пустую строку для пустого ввода.
+ Предполагать, что количество рельсов всегда больше или равно 2.

Примеры:
Кодирование:
encode("HELLO WORLD", 3) → "HOLELWRDLO"
Декодирование:
decode("HOLELWRDLO", 3) → "HELLO WORLD"

https://www.codewars.com/kata/58c5577d61aefcf3ff000081
"""

def encode_rail_fence_cipher(string, n):
    if not string or n < 2:
        return string

    # Create an array of empty strings for each rail
    # Создаем массив пустых строк для каждой рейки
    rails = ['' for _ in range(n)]

    # Determine the direction and populate the rails
    # Определяем направление и заполняем рейки
    direction = 1
    current_rail = 0

    for char in string:
        rails[current_rail] += char
        current_rail += direction

        if current_rail == 0 or current_rail == n - 1:
            direction *= -1

    # Combine all rails into one encoded string
    # Объединяем все рейки в одну закодированную строку
    return ''.join(rails)

def decode_rail_fence_cipher(string, n):
    if not string or n < 2:
        return string

    # Determine the length of each rail in the encoded text
    # Определяем длину каждой рейки в закодированном тексте
    rail_lengths = [0] * n
    direction = 1
    current_rail = 0

    for _ in string:
        rail_lengths[current_rail] += 1
        current_rail += direction

        if current_rail == 0 or current_rail == n - 1:
            direction *= -1

    # Split the encoded text into parts based on rail lengths
    # Разделяем закодированный текст на части в зависимости от длины реек
    rails = []
    start = 0
    for length in rail_lengths:
        rails.append(string[start:start + length])
        start += length

    # Reconstruct the original string
    # Восстанавливаем исходную строку
    result = []
    current_positions = [0] * n
    direction = 1
    current_rail = 0

    for _ in string:
        result.append(rails[current_rail][current_positions[current_rail]])
        current_positions[current_rail] += 1
        current_rail += direction

        if current_rail == 0 or current_rail == n - 1:
            direction *= -1

    return ''.join(result)