"""
Given a string of words, return the length of the shortest word in the string.
+ The string will never be empty.
+ You do not need to handle different data types.

Example:
"The quick brown fox" → 3 (shortest word: "The", length 3)
"Hello world" → 5 (shortest word: "world", length 5)

Дана строка, содержащая несколько слов. Найдите длину самого короткого слова в строке и верните это значение.
+ Гарантируется, что строка не будет пустой.
+ Не нужно обрабатывать другие типы данных.

Пример:
"The quick brown fox" → 3 (самое короткое слово — "The", длина 3)
"Hello world" → 5 (самое короткое слово — "world", длина 5)
"""

def find_short(given_string):
    words = given_string.split()  
    min_length = float('inf')

    for word in words:
        word_length = len(word)
        if word_length < min_length:
            min_length = word_length

    return min_length

print(find_short("The quick brown fox"))
print(find_short("Hello world"))
print(find_short("Python is amazing"))
print(find_short("I love programming"))