"""
Given two strings s1 and s2, create a function mix to compare the frequency of lowercase letters (a to z) in each string and produce a formatted string summarizing the differences.

Rules:
+ Count the frequency of each lowercase letter in both strings.
+ Ignore letters with a maximum occurrence of 1 or less in both strings.
+ For each remaining letter:
    + If it appears more often in s1, prefix it with 1:.
    + If it appears more often in s2, prefix it with 2:.
    + If it appears equally often in both strings, prefix it with =:.
+ Sort the substrings:
    + By decreasing order of their length.
    + If lengths are equal, sort lexicographically by their prefix and letter.
+ Combine the substrings into a single string, separated by /.

Examples:
Input:
s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
Output: "1:aaaa/2:bbb"

Input:
s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"

Output: "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

Даны две строки s1 и s2. Напишите функцию mix, которая сравнивает частоту появления строчных букв (a–z) в каждой строке и возвращает форматированную строку, описывающую различия.

Правила:
+ Подсчитайте частоту каждой строчной буквы в обеих строках.
+ Игнорируйте буквы, которые встречаются не более 1 раза в обеих строках.
+ Для каждой оставшейся буквы:
    + Если она чаще встречается в s1, добавьте префикс 1:.
    + Если она чаще встречается в s2, добавьте префикс 2:.
    + Если она встречается одинаково часто, добавьте префикс =: (или E: в некоторых языках).
+ Отсортируйте подстроки:
    + По убыванию длины.
    + Если длины равны, по лексикографическому порядку префикса и буквы.
+ Объедините подстроки в одну строку, разделяя их через /.

Примеры:
Ввод:
s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"

Вывод: "1:aaaa/2:bbb"

Ввод:
s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"

Вывод: "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

https://www.codewars.com/kata/5629db57620258aa9d000014
"""

def mix(s1, s2):
    def count_letters(s):
        counts = {}
        for char in s:
            if char.islower():
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
        return counts

    count1 = count_letters(s1)
    count2 = count_letters(s2)

    differences = []

    unique_chars = set(count1.keys()).union(set(count2.keys()))

    for char in unique_chars:
        freq1 = count1.get(char, 0)
        freq2 = count2.get(char, 0)

        if max(freq1, freq2) > 1:
            if freq1 > freq2:
                differences.append((1, char, freq1))
            elif freq2 > freq1:
                differences.append((2, char, freq2))
            else:
                differences.append(("=", char, freq1))

    differences.sort(key=lambda x: (-x[2], str(x[0]) + x[1]))

    result = []
    for prefix, char, count in differences:
        result.append(f"{prefix}:{char * count}")

    return "/".join(result)

s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
print(mix(s1, s2))

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1, s2))