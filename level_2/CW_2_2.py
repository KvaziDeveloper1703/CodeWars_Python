'''
You are given the top row of a colored triangle, where each position is either: R (red), G (green), or B (blue).

Each next row is formed by combining pairs of adjacent colors from the row above:
    - If the two colors are the same, the resulting color is the same;
    - If the two colors are different, the resulting color is the third one.

This process continues until only one color remains - that final color is the result.

Дана верхняя строка цветного треугольника, где каждый символ - это: R (красный), G (зелёный) или B (синий).

Каждая следующая строка строится из пар соседних цветов предыдущей строки:
    - Если цвета одинаковые, то внизу записывается тот же цвет;
    - Если цвета разные, то записывается третий цвет, которого нет среди пары {R, G, B}.

Процесс продолжается, пока не останется один цвет — он и является результатом.
'''

def triangle(row):
    color_to_number = {'R': 0, 'G': 1, 'B': 2}
    number_to_color = ['R', 'G', 'B']

    numeric_row = [color_to_number[color] for color in row]
    row_length = len(numeric_row)

    def combination_count(total, index):
        result = 1
        while total > 0 or index > 0:
            total_mod = total % 3
            index_mod = index % 3
            if index_mod > total_mod:
                return 0
            if index_mod == 1 and total_mod == 2:
                result *= 2
            total //= 3
            index //= 3
        return result % 3

    total_color_value = 0
    for position in range(row_length):
        binomial_coefficient = combination_count(row_length - 1, position)
        total_color_value += binomial_coefficient * numeric_row[position]
    total_color_value %= 3

    if (row_length - 1) % 2 == 1:
        total_color_value = (-total_color_value) % 3

    return number_to_color[total_color_value]