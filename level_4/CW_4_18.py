'''
Your task is to convert a string representation of a number into an integer.

The input is a string that spells out a number in English words.

Examples:
Input: "one"
Output: 1

Input: "twenty"
Output: 20

Ваша задача - преобразовать число, записанное словами на английском языке, в целое число.

На вход подаётся строка, в которой число записано словами.

Примеры:
Ввод: "one"
Вывод: 1

Ввод: "twenty"
Вывод: 20 
'''

def parse_int(string):
    words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    multipliers = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }

    string = string.replace("-", " ").replace(" and ", " ")
    parts = string.split()

    result = 0
    current = 0

    for word in parts:
        if word in words:
            current += words[word]
        elif word == "hundred":
            current *= 100
        elif word == "thousand":
            result += current * 1000
            current = 0
        elif word == "million":
            result += current * 1000000
            current = 0

    return result + current