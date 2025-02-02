"""
Nathan loves cycling.Because he knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
Given the time in hours, return the number of litres Nathan will drink, rounded down to the smallest value.

Examples:
time = 3 → litres = 1
time = 6.7 → litres = 3
time = 11.8 → litres = 5

Нейтан любит кататься на велосипеде. Так как он знает, что важно поддерживать водный баланс, он выпивает 0.5 литра воды в час катания.
Дано время в часах, нужно вернуть количество литров воды, которые Нейтан выпьет, округлённое в меньшую сторону.

Примеры:
time = 3 → litres = 1
time = 6.7 → litres = 3
time = 11.8 → litres = 5
"""

import math

def litres(time):
    water_per_hour = 0.5
    total_water = time * water_per_hour
    litres = math.floor(total_water)

    return litres

print(litres(3))
print(litres(6.7))
print(litres(11.8))