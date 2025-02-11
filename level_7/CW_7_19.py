"""
Take two strings string_1 and string_2, containing only letters from 'a' to 'z'.
+ Return a new sorted string (in alphabetical ascending order), containing distinct letters taken from string_1 or string_2.
+ Each letter should appear only once.

Examples:
string_1 = "xyaabbbccccdefww"
string_2 = "xxxxyyyyabklmopq"
process(string_1, string_2) → "abcdefklmopqwxy"

Даны две строки string_1 и string_2, содержащие только буквы от 'a' до 'z'.
+ Верните новую отсортированную строку (в алфавитном порядке, по возрастанию), содержащую уникальные буквы, которые встречаются в string_1 или string_2.
+ Каждая буква должна встречаться только один раз.

Примеры:
string_1 = "xyaabbbccccdefww"
string_2 = "xxxxyyyyabklmopq"
process(string_1, string_2) → "abcdefklmopqwxy"
"""

def process(string_1, string_2):
    combined = string_1 + string_2
    unique_characters = []
    
    for character in combined:
        if character not in unique_characters:
            unique_characters.append(character)
    
    return "".join(sorted(unique_chars))

first_string = "xyaabbbccccdefww"
second_string ="xxxxyyyyabklmopq"
answer = process(first_string, second_string)
print(answer)