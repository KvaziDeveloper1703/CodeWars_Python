"""
Complete the solution so that it returns true if the first string ends with the second string.

Examples:
solution('abc', 'bc') → True
solution('abc', 'd') → False

Напишите функцию, которая возвращает true, если первая строка заканчивается на вторую строку.

Примеры:
solution('abc', 'bc') → True
solution('abc', 'd') → False
"""

def solution(string, ending):
    if ending == "":
        return True

    ending_length = len(ending)

    string_ending = string[-ending_length:]  

    if string_ending == ending:
        return True
    else:
        return False

print(solution('abc', 'bc'))
print(solution('abc', 'd'))
print(solution('hello world', 'world'))
print(solution('python', 'thon'))
print(solution('python', 'py'))
print(solution('hello', ''))