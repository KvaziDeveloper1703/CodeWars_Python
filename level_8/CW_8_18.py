"""
Nathan loves cycling.Because he knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
Given the time in hours, return the number of litres Nathan will drink, rounded down to the smallest value.

Нейтан любит кататься на велосипеде. Так как он знает, что важно поддерживать водный баланс, он выпивает 0.5 литра воды в час катания.
Дано время в часах, нужно вернуть количество литров воды, которые Нейтан выпьет, округлённое в меньшую сторону.
"""

def time_to_litres(given_time):
    water_per_hour = 0.5
    litres_of_water = given_time * water_per_hour
    return int(litres_of_water)

time = 6.7
answer = time_to_litres(time)
print(answer)