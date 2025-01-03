"""
Create a function that counts the number of distinct characters in a string (case-insensitive) that appear more than once. The input string will only contain alphabetic characters (both uppercase and lowercase) and numeric digits.

For example:
"abcde" → 0 (no character repeats)
"aabbcde" → 2 ('a' and 'b')
"aabBcde" → 2 ('a' occurs twice and 'b' twice, considering 'b' and 'B' as the same)
"indivisibility" → 1 ('i' occurs six times)
"Indivisibilities" → 2 ('i' occurs seven times and 's' twice)
"aA11" → 2 ('a' and '1')
"ABBA" → 2 ('A' and 'B' each occur twice)

Напишите функцию, которая подсчитывает количество различных символов в строке (без учета регистра), которые встречаются более одного раза. Входная строка будет содержать только буквы (заглавные и строчные) и цифры.

Например:
"abcde" → 0 (нет повторяющихся символов)
"aabbcde" → 2 ('a' и 'b')
"aabBcde" → 2 ('a' встречается дважды, и 'b' тоже дважды, считая 'b' и 'B' одинаковыми)
"indivisibility" → 1 ('i' встречается шесть раз)
"Indivisibilities" → 2 ('i' встречается семь раз, а 's' дважды)
"aA11" → 2 ('a' и '1')
"ABBA" → 2 ('A' и 'B' встречаются по два раза)

https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
"""

def count_repeated_characters(given_string):
    given_string = given_string.lower()
    char_count = {}

    for char in given_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    repeated_count = 0
    for count in char_count.values():
        if count > 1:
            repeated_count += 1

    return repeated_count

print(count_repeated_characters("aA11"))
print(count_repeated_characters("abcde"))
print(count_repeated_characters("aabbccdd"))
