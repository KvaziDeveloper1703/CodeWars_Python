"""
Make a program that filters a list of strings and returns a list containing only your friends' names.
+ If a name has exactly 4 letters, you can be sure it's a friend!
+ If the length is not 4, you can be sure they're not.
+ Keep the original order of names in the output.
+ Input strings will only contain letters (no digits or symbols).

Examples:
["Ryan", "Kieran", "Jason", "Yous"] → ["Ryan", "Yous"]
["Peter", "Stephen", "Joe"] → []

Создайте программу, которая фильтрует список строк и возвращает список, содержащий только имена ваших друзей.
+ Если имя содержит ровно 4 буквы, это ваш друг!
+ Если длина имени не равна 4, то этот человек не ваш друг.
+ Порядок имён в выходном списке должен сохраниться.
+ Входные строки содержат только буквы (без цифр и символов).

Примеры:
["Ryan", "Kieran", "Jason", "Yous"] → ["Ryan", "Yous"]
["Peter", "Stephen", "Joe"] → []
"""

def friend(names):

    filtered_names = []

    for name in names:
        if len(name) == 4:
            filtered_names.append(name)

    return filtered_names

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(friend(["Peter", "Stephen", "Joe"]))
print(friend(["Mark", "John", "Paul", "Anna"]))