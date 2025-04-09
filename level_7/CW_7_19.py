"""
Take two strings containing only letters from 'a' to 'z'.
+ Return a new sorted string, containing distinct letters taken from string_1 or string_2;
+ Each letter should appear only once.

Example:
Input: string_1 = "xyaabbbccccdefww", string_2 = "xxxxyyyyabklmopq"
Output: "abcdefklmopqwxy"

Даны две строки содержащие только буквы от 'a' до 'z'.
+ Верните новую отсортированную строку, содержащую уникальные буквы, которые встречаются в string_1 или string_2;
+ Каждая буква должна встречаться только один раз.

Пример:
Ввод: string_1 = "xyaabbbccccdefww", string_2 = "xxxxyyyyabklmopq"
Вывод: "abcdefklmopqwxy"

https://www.codewars.com/kata/5656b6906de340bd1b0000ac
"""

def process_strings(given_string_1, given_string_2):
    combined = given_string_1 + given_string_2
    unique_characters = []
    
    for character in combined:
        if character not in unique_characters:
            unique_characters.append(character)
    
    return "".join(sorted(unique_characters))

first_string = "xyaabbbccccdefww"
second_string ="xxxxyyyyabklmopq"
answer = process_strings(first_string, second_string)
print(answer)