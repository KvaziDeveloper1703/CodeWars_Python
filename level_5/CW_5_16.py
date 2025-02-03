"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Rules:
+ Only lowercase letters (a-z) will be used.
+ No punctuation or digits are included.
+ Performance must be considered.

Examples:
scramble('rkqodlw', 'world') → True
scramble('cedewaraaossoqqyt', 'codewars') → True
scramble('katas', 'steak') → False

Реализуйте функцию scramble(str1, str2), которая возвращает true, если из символов str1 можно составить str2, иначе false.

Правила:
+ Используются только строчные буквы (a-z).
+ Цифры и знаки препинания отсутствуют.
+ Необходимо учитывать производительность.

Примеры:
scramble('rkqodlw', 'world') → True
scramble('cedewaraaossoqqyt', 'codewars') → True
scramble('katas', 'steak') → False
"""

def scramble(string_1, string_2):

    string_1_count = {}
    for character in string_1:
        if character in string_1_count:
            string_1_count[character] += 1
        else:
            string_1_count[character] = 1

    for character in string_2:
        if character in string_1_count and string_1_count[character] > 0:
            string_1_count[character] -= 1
        else:
            return False

    return True

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('abcdefgh', 'abc'))
print(scramble('aabbcc', 'abcabc'))
print(scramble('aabbcc', 'abcbca'))