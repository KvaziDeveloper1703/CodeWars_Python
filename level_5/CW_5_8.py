"""
Create a function to generate hashtags based on input text. The function should follow these rules:
+ The output must start with a hashtag (#).
+ Each word in the input must have its first letter capitalized.
+ If the final result exceeds 140 characters, the function should return false.
+ If the input text is empty or results in an empty hashtag, the function should return false.

Examples:
Input: "hello world" → Output: "#HelloWorld"
Input: " " → Output: false
Input: "a very long string that exceeds one hundred and forty characters..." → Output: false

Создайте функцию для генерации хэштегов на основе введённого текста. Функция должна соблюдать следующие правила:
+ Результат должен начинаться с символа хэштега (#).
+ Каждое слово во входном тексте должно начинаться с заглавной буквы.
+ Если итоговый результат превышает 140 символов, функция должна вернуть false.
+ Если введённый текст пустой или результатом является пустой хэштег, функция должна вернуть false.

Примеры:
Ввод: "hello world" → Вывод: "#HelloWorld"
Ввод: " " → Вывод: false
Ввод: "очень длинная строка, превышающая сто сорок символов..." → Вывод: false

https://www.codewars.com/kata/52449b062fb80683ec000024
"""

def generate_hashtag(text):
    stripped_text = text.strip()

    if not stripped_text:
        return False

    words = stripped_text.split()

    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())

    hashtag = '#' + ''.join(capitalized_words)

    if len(hashtag) > 140:
        return False

    return hashtag

print(generate_hashtag("hello world"))
print(generate_hashtag(" "))
print(generate_hashtag("a" * 139))
print(generate_hashtag("a" * 140))