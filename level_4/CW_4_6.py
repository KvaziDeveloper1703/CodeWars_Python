"""
Write a function strip_comments that removes all text following specific comment markers in a given string. The function should also trim any trailing whitespace from the resulting lines.

Rules:
+ The input string may contain multiple lines separated by newline characters (\n).
+ Comment markers are provided as a list of characters. Any text following a marker on the same line should be removed.
+ Leading and trailing whitespace should be preserved, but any trailing whitespace after removing comments should be stripped.

Example:
Input:
strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
Output:
"apples, pears\ngrapes\nbananas"

Explanation:
+ In the first line, everything after # is removed, leaving "apples, pears".
+ The second line remains unchanged as it contains no comment markers.
+ In the third line, everything after ! is removed, leaving "bananas".

Напишите функцию strip_comments, которая удаляет весь текст, следующий за определёнными символами комментариев, из переданной строки. Также функция должна удалять пробелы в конце строк после обработки.

Правила:
+ Входная строка может содержать несколько строк, разделённых символами новой строки (\n).
+ Символы комментариев передаются в виде списка. Весь текст после символа комментария на одной строке должен быть удалён.
+ Начальные и конечные пробелы сохраняются, но лишние пробелы в конце строки после удаления комментариев должны быть убраны.

Пример:
Ввод:
strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
Вывод:
"apples, pears\ngrapes\nbananas"

Объяснение:
+ В первой строке всё после # удаляется, остаётся "apples, pears".
+ Вторая строка остаётся без изменений, так как в ней нет символов комментариев.
+ В третьей строке всё после ! удаляется, остаётся "bananas".

https://www.codewars.com/kata/51c8e37cee245da6b40000bd
"""

def strip_comments(text, markers):
    lines = text.split('\n')
    result = []

    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
        result.append(line.rstrip())

    return '\n'.join(result)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(strip_comments("a #b\nc!d", ["#", "!"]))