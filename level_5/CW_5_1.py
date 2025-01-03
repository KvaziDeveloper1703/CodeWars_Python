"""
Create a function that accepts a non-negative integer representing a duration in seconds and converts it into a human-readable time format: HH:MM:SS.

Example:
Input: 0 → Output: "00:00:00"
Input: 5 → Output: "00:00:05"
Input: 3600 → Output: "01:00:00"
Input: 86399 → Output: "23:59:59"

Напишите функцию, которая принимает неотрицательное целое число, представляющее длительность в секундах, и преобразует его в человеко-читаемый формат времени: ЧЧ:ММ:СС.

Пример:
Ввод: 0 → Вывод: "00:00:00"
Ввод: 5 → Вывод: "00:00:05"
Ввод: 3600 → Вывод: "01:00:00"
Ввод: 86399 → Вывод: "23:59:59"

https://www.codewars.com/kata/52685f7382004e774f0001f7
"""

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

print(format_time(0))