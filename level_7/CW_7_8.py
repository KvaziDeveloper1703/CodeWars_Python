"""
Write a program that takes a string as input and transforms it by repeating each character based on its position in the string. The first repetition should be capitalized, and the results should be joined with hyphens.
For example, the input "abcd" should return "A-Bb-Ccc-Dddd".

Напишите программу, которая принимает строку и преобразует её, повторяя каждый символ столько раз, сколько соответствует его позиции в строке. Первая повторяющаяся буква должна быть заглавной, а результаты соединяются с помощью дефисов.
Например, для строки "abcd" программа должна вернуть "A-Bb-Ccc-Dddd".

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
"""

def transformator(given_string):
    result = []
    for i in range(len(given_string)):
        part = given_string[i].upper() + given_string[i].lower() * i
        result.append(part)
    return '-'.join(result)

string = input("Write your string here, please: ")
transformed_string = transformator(string)
print(transformed_string)