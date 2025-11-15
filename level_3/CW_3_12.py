'''
You are given a 3×3 grid of points, labeled as follows:
    A B C
    D E F
    G H I

Your task is to implement a function count_patterns_from(first_point, length) that returns the number of valid screen-lock patterns that:
    - Start from the given point;
    - Have exactly the given length.

A pattern is a sequence of distinct points connected by a continuous swipe. The function should return only the number of valid patterns - not the patterns themselves.

Rules for Valid Patterns:
    - No point may be used more than once;
    - You may draw a line between two points if the connection is:
        - Horizontal (e.g., A → B),
        - Vertical (e.g., D → G),
        - Diagonal (e.g., I → E),
        - OR passes over another point only if that point has already been used.

У вас есть сетка 3×3 с точками, обозначенными так:
    A B C
    D E F
    G H I

Нужно реализовать функцию count_patterns_from(first_point, length), которая возвращает количество возможных узоров-патов, которые:
    - Начинаются с указанной точки;
    - Имеют строго заданную длину.

Узор - это последовательность различных точек, соединённых непрерывным движением пальца. Функция должна вернуть только число таких узоров, а не сами последовательности.

Правила построения узоров:
    - Нельзя использовать одну точку дважды;
    - Можно соединять две точки линией, если соединение является:
        - горизонтальным (например, A → B),
        - вертикальным (например, D → G),
        - диагональным (например, I → E),
        - или проходит через промежуточную точку только если эта точка уже была использована ранее.
'''

def count_patterns_from(first_point, pattern_length):
    if pattern_length <= 0:
        return 0
    if pattern_length == 1:
        return 1

    coordinates_by_point = {
        'A': (0, 0), 'B': (1, 0), 'C': (2, 0),
        'D': (0, 1), 'E': (1, 1), 'F': (2, 1),
        'G': (0, 2), 'H': (1, 2), 'I': (2, 2)
    }

    intermediate_points_map = {
        ('A', 'C'): 'B', ('C', 'A'): 'B',
        ('A', 'G'): 'D', ('G', 'A'): 'D',
        ('C', 'I'): 'F', ('I', 'C'): 'F',
        ('G', 'I'): 'H', ('I', 'G'): 'H',
        ('B', 'H'): 'E', ('H', 'B'): 'E',
        ('D', 'F'): 'E', ('F', 'D'): 'E',
        ('A', 'I'): 'E', ('I', 'A'): 'E',
        ('C', 'G'): 'E', ('G', 'C'): 'E'
    }

    def can_move(from_point, to_point, used_points):
        if (from_point, to_point) in intermediate_points_map:
            intermediate_point = intermediate_points_map[(from_point, to_point)]
            return intermediate_point in used_points
        return True

    def depth_first_search(current_point, remaining_length, used_points):
        if remaining_length == 0:
            return 1

        total_count = 0
        for next_point in coordinates_by_point.keys():
            if next_point not in used_points and can_move(current_point, next_point, used_points):
                total_count += depth_first_search(
                    next_point,
                    remaining_length - 1,
                    used_points | {next_point}
                )
        return total_count

    return depth_first_search(first_point, pattern_length - 1, {first_point})