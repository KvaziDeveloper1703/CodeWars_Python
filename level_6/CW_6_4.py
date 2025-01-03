"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Вы, вероятно, знакомы с системой "лайков" из Facebook и других платформ. Люди могут "лайкать" посты в блогах, фотографии или другие объекты. Мы хотим создать текст, который будет отображаться рядом с таким объектом.
Реализуйте функцию, которая принимает массив с именами людей, которые лайкнули объект. Функция должна возвращать текст для отображения, как показано в примерах:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""

def likes(given_names):
    N = len(given_names)
    if N == 0:
        return "no one likes this"
    elif N == 1:
        return given_names[0] + " likes this"
    elif N == 2:
        return given_names[0] + " and " + given_names[1] + " like this"
    elif N == 3:
        return given_names[0] + ", " + given_names[1] + " and " + given_names[2] + " like this"
    else:
        return given_names[0] + ", " + given_names[1] + " and " + str(N - 2) + " others like this"

names = ["Mike", "John", "Artur"]
generated_test = likes(names)
print(generated_test)