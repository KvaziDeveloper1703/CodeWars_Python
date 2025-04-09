"""
Write a function that filters a list of strings and returns a list containing only your friends' names.
+ If a name has exactly 4 letters, you can be sure it's a friend;
+ If the length is not 4, you can be sure they're not;
+ Keep the original order of names in the output;
+ Input strings will only contain letters.

Example:
Input: ["Ryan", "Kieran", "Jason", "Yous"]
Output: ["Ryan", "Yous"]

Напишите функцию, которая фильтрует список строк и возвращает список, содержащий только имена ваших друзей.
+ Если имя содержит ровно 4 буквы, это ваш друг;
+ Если длина имени не равна 4, то этот человек не ваш друг;
+ Порядок имён в выходном списке должен сохраниться;
+ Входные строки содержат только буквы.

Примеры:
Ввод: ["Ryan", "Kieran", "Jason", "Yous"]
Вывод: ["Ryan", "Yous"]

https://www.codewars.com/kata/55b42574ff091733d900002f
"""

def filter_friend(given_names):

    filtered_names = []

    for name in given_names:
        if len(name) == 4:
            filtered_names.append(name)

    return filtered_names

names = ["Ryan", "Kieran", "Jason", "Yous"]
answer = filter_friend(names)
print(answer)