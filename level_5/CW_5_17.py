"""
Greed is a dice game played with five six-sided dice.

Your task is to implement a function that calculates the score based on the following rules:

Scoring rules:
+ Three ones (1 1 1) → 1000 points
+ Three sixes (6 6 6) → 600 points
+ Three fives (5 5 5) → 500 points
+ Three fours (4 4 4) → 400 points
+ Three threes (3 3 3) → 300 points
+ Three twos (2 2 2) → 200 points
+ A single one (1) → 100 points
+ A single five (5) → 50 points

Restrictions:
+ A single die can only be counted once per roll.
+ The input list must not be modified.

Examples:
[5, 1, 3, 4, 1]  → 250
[1, 1, 1, 3, 1]  → 1100
[2, 4, 4, 5, 4]  → 450

Greed — это игра в кости с пятью шестигранными кубиками.

Ваша задача — реализовать функцию, которая будет подсчитывать очки по следующим правилам:

Правила подсчёта очков:
+ Три единицы (1 1 1) → 1000 очков
+ Три шестёрки (6 6 6) → 600 очков
+ Три пятёрки (5 5 5) → 500 очков
+ Три четвёрки (4 4 4) → 400 очков
+ Три тройки (3 3 3) → 300 очков
+ Три двойки (2 2 2) → 200 очков
+ Одиночная единица (1) → 100 очков
+ Одиночная пятёрка (5) → 50 очков

Ограничения:
+ Один кубик можно учитывать только один раз в каждом броске.
+ Исходный массив бросков нельзя изменять.

Примеры:
[5, 1, 3, 4, 1]  → 250
[1, 1, 1, 3, 1]  → 1100
[2, 4, 4, 5, 4]  → 450
"""

def score(dice):
    triple_scores = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    single_scores = {1: 100, 5: 50}

    count = {i: 0 for i in range(1, 7)}
    for number in dice:
        count[number] += 1

    total_score = 0

    for number in range(1, 7):
        if count[number] >= 3:
            total_score += triple_scores[number]
            count[number] -= 3

        if number in single_scores:
            total_score += count[number] * single_scores[number]

    return total_score

print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
print(score([2, 4, 4, 5, 4]))
print(score([6, 6, 6, 1, 5]))
print(score([2, 3, 4, 6, 2]))