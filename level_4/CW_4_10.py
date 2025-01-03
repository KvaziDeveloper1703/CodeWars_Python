"""
Your task is to write a function that generates all possible permutations of a non-empty input string. If duplicates are present, ensure that the output contains only unique permutations.

Rules:
+ The input is a non-empty string.
+ Generate all possible unique arrangements ("shufflings") of the string's characters.
+ The order of the permutations in the output does not matter.

Examples:
Input: "a"
Output: ["a"]

Input: "ab"
Output: ["ab", "ba"]

Input: "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

Input: "aabb"
Output: ["aabb", "abab", "abba", "baab", "baba", "bbaa"]

Ваша задача — написать функцию, которая создаёт все возможные перестановки символов непустой входной строки. Если в строке есть повторяющиеся символы, в выводе должны быть только уникальные комбинации.

Правила:
+ На вход подаётся непустая строка.
+ Генерируйте все возможные уникальные комбинации ("перемешивания") символов строки.
+ Порядок перестановок в выводе не имеет значения.

Примеры:
Ввод: "a"
Вывод: ["a"]

Ввод: "ab"
Вывод: ["ab", "ba"]

Ввод: "abc"
Вывод: ["abc", "acb", "bac", "bca", "cab", "cba"]

Ввод: "aabb"
Вывод: ["aabb", "abab", "abba", "baab", "baba", "bbaa"]

https://www.codewars.com/kata/5254ca2719453dcc0b00027d
"""

def unique_permutations(s):

    def permute(chars, path, used, result):
        if len(path) == len(chars):
            result.add(''.join(path))
            return

        for i in range(len(chars)):
            if used[i]:
                continue

            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(chars[i])

            permute(chars, path, used, result)

            path.pop()
            used[i] = False

    chars = sorted(s)
    result = set()
    used = [False] * len(chars)

    permute(chars, [], used, result)

    return list(result)

print(unique_permutations("a"))
print(unique_permutations("ab"))
print(unique_permutations("abc"))