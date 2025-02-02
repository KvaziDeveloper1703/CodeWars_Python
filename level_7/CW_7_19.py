"""
Take two strings s1 and s2, containing only letters from 'a' to 'z'.
+ Return a new sorted string (in alphabetical ascending order), containing distinct letters taken from s1 or s2.
+ Each letter should appear only once.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) → "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) → "abcdefghijklmnopqrstuvwxyz"

Даны две строки s1 и s2, содержащие только буквы от 'a' до 'z'.
+ Верните новую отсортированную строку (в алфавитном порядке, по возрастанию), содержащую уникальные буквы, которые встречаются в s1 или s2.
+ Каждая буква должна встречаться только один раз.

Примеры:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) → "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) → "abcdefghijklmnopqrstuvwxyz"
"""

def longest(string_1, string_2):
    combined = string_1 + string_2
    unique_chars = []
    
    for char in combined:
        if char not in unique_chars:
            unique_chars.append(char)
    
    return "".join(sorted(unique_chars))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))