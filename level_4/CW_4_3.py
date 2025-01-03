"""
Write a function that converts a duration in seconds into a human-readable string.

Rules:
+ If the input is 0, return "now".
+ Use the units: years, days, hours, minutes, and seconds.
    + 1 year = 365 days;
    + 1 day = 24 hours;
    + 1 hour = 60 minutes; 
    + 1 minute = 60 seconds.
+ Skip units with a value of 0.
+ Separate components with ", " and " and " for the last two.
+ Use singular or plural for units (e.g., "1 second" vs "2 seconds").
+ Use the largest possible units (e.g., 61 seconds → "1 minute and 1 second").

Examples:
62 → "1 minute and 2 seconds"
3662 → "1 hour, 1 minute and 2 seconds"

Напишите функцию, которая преобразует длительность в секундах в читаемую строку.

Правила:
+ Если ввод 0, вернуть "now".
+ Используйте единицы: годы, дни, часы, минуты, секунды.
    + 1 год = 365 дней;
    + 1 день = 24 часа;
    + 1 час = 60 минут;
    + 1 минута = 60 секунд.
+ Пропустите единицы с нулевым значением.
+ Разделяйте компоненты через ", " и " and " для последних двух.
+ Учитывайте единственное и множественное число (например, "1 second" и "2 seconds").
+ Используйте самые крупные возможные единицы (например, 61 seconds → "1 minute and 1 second").

Примеры:
62 → "1 minute and 2 seconds"
3662 → "1 hour, 1 minute and 2 seconds"

https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""

def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]

    parts = []

    for unit in time_units:
        name = unit[0]
        count = unit[1]

        value = seconds // count
        if value > 0:
            seconds -= value * count

            if value == 1:
                parts.append(f"{value} {name}")
            else:
                parts.append(f"{value} {name}s")

    if len(parts) > 1:
        formatted_time = ', '.join(parts[:-1]) + ' and ' + parts[-1]
    else:
        formatted_time = parts[0]

    return formatted_time

print(format_duration(0))
print(format_duration(62))
print(format_duration(3662))