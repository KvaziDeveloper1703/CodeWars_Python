"""
You live in the city of Cartesia, where all roads are laid out in a perfect grid.
You arrived 10 minutes early to an appointment and decided to take a walk. The city provides a Walk Generating App, which sends you an array of direction letters ('n', 's', 'w', 'e').
+ Each letter represents moving one block in that direction, and it takes 1 minute to walk one block.
+ Your task is to write a function that returns true if the walk takes exactly 10 minutes and returns you to your starting point.
+ If either condition is not met, return false.

Examples:
['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] → True
['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'] → True
['n', 'n', 'n', 's', 's', 's', 'e', 'e', 'w', 'w'] → False
['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 'e'] → False

Вы живёте в городе Картезия, где все дороги расположены в виде идеальной сетки.
Вы пришли на встречу на 10 минут раньше и решили прогуляться. В городе есть приложение для генерации прогулок, которое отправляет вам массив строк с направлениями ('n', 's', 'w', 'e').
+ Каждая буква — это одно направление (один квартал), и переход через один квартал занимает 1 минуту.
+ Ваша задача — написать функцию, которая вернёт true, если прогулка занимает ровно 10 минут и приводит обратно в начальную точку.
+ Если хоть одно из условий не выполняется, функция должна вернуть false.

Примеры:
['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] → True
['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'] → True
['n', 'n', 'n', 's', 's', 's', 'e', 'e', 'w', 'w'] → False
['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 'e'] → False
"""

def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')