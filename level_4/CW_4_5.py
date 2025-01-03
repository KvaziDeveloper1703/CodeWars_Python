"""
Detective, we need your help to crack a PIN code!

Our spy observed Robby the Robber entering a PIN on a keypad with the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

The observed PIN is 1357, but the spy mentioned that each digit might have been any adjacent digit (horizontally or vertically, but not diagonally). For example:
+ 1 could be 1, 2, or 4.
+ 5 could be 2, 4, 5, 6, or 8.

Your task:
+ Write a function getPINs (or similar, depending on the language) that generates all possible PIN variations based on the observed PIN and the possible adjacent digits for each digit.
+ The input is a string representing the observed PIN, which may have a length between 1 and 8 digits.
+ The function should return a list of strings containing all possible PIN combinations, including the original PIN.

Example:
Input: "1357"
Possible output: ["1357", "1257", "1457", "1327", "1347", "1557", ...]
Keep in mind that PINs may have leading zeros, so all PINs must be treated as strings.

Детектив, нам нужна ваша помощь, чтобы взломать код!

Наш шпион заметил, как Робби Грабитель вводил PIN-код на клавиатуре с такой раскладкой:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

Шпион заметил PIN-код 1357, но упомянул, что каждая цифра могла быть заменена на соседнюю (по горизонтали или вертикали, но не по диагонали). Например:
+ 1 может быть 1, 2 или 4.
+ 5 может быть 2, 4, 5, 6 или 8.

Ваша задача:
+ Напишите функцию getPINs (или аналогичную для вашего языка), которая генерирует все возможные варианты PIN-кода, учитывая наблюдаемый PIN и возможные соседние цифры для каждой цифры.
+ На вход подаётся строка, представляющая наблюдаемый PIN, длиной от 1 до 8 цифр.
+ Функция должна вернуть список строк, содержащих все возможные комбинации PIN, включая оригинальный PIN.

Пример:
Ввод: "1357"
Возможный вывод: ["1357", "1257", "1457", "1327", "1347", "1557", ...]
Помните, что PIN-коды могут начинаться с нуля, поэтому все коды должны обрабатываться как строки.

https://www.codewars.com/kata/5263c6999e0f40dee200059d
"""

def getPINs(observed):
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    def generate_combinations(prefix, remaining_digits):
        if not remaining_digits:
            return [prefix]

        current_digit = remaining_digits[0]
        rest = remaining_digits[1:]
        combinations = []

        for neighbor in adjacent[current_digit]:
            combinations.extend(generate_combinations(prefix + neighbor, rest))

        return combinations

    return generate_combinations("", observed)

print(getPINs("1357"))
print(getPINs("8"))