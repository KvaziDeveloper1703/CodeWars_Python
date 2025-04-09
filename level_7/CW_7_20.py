"""
Complete the solution so that it returns true if the first string ends with the second string.

Напишите функцию, которая возвращает true, если первая строка заканчивается на вторую строку.

https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
"""

def solution(given_string, given_ending):
    if given_ending == "":
        return True

    ending_length = len(given_ending)

    string_ending = given_string[-ending_length:]  

    if string_ending == given_ending:
        return True
    else:
        return False

string = "python"
ending = "thon"

answer = solution(string, ending)
print(answer)