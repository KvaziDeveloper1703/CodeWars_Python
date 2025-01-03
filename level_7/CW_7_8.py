"""
Write a program that transforms a string by repeating each character based on its position, capitalizing the first repetition, and joining them with hyphens. 
For example, "abcd" should return "A-Bb-Ccc-Dddd".

Напишите программу, которая преобразует строку, повторяя каждый символ в соответствии с его позицией, делая первую повторяющуюся букву заглавной, и соединяет результаты с помощью дефисов.
Например, строка "abcd" должна вернуть "A-Bb-Ccc-Dddd".

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
"""

def transformator(given_string):
    result = []
    for i in range(len(given_string)):
        part = given_string[i].upper() + given_string[i].lower() * i
        result.append(part)
    return '-'.join(result)

my_string = input("Write your string here, please: ")
transformed_string = transformator(my_string)
print(transformed_string)