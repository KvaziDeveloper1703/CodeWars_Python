"""
Write a function that transforms each word in a sentence by moving its first letter to the end of the word, followed by adding "ay" at the end. Words are defined as sequences of letters, and any punctuation marks or spaces should remain unchanged.

Examples:
Input: "Hello world!" → Output: "elloHay orldway!"
Input: "This is a test." → Output: "hisTay siay aay esttay."

Напишите функцию, которая преобразует каждое слово в предложении, перемещая его первую букву в конец слова, после чего добавляет "ay" в конец. Слова — это последовательности букв, а знаки пунктуации и пробелы должны остаться неизменными.

Примеры:
Ввод: "Hello world!" → Вывод: "elloHay orldway!"
Ввод: "This is a test." → Вывод: "hisTay siay aay esttay."

https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""

def pig_it(text):
    words = text.split()
    
    transformed_words = []
    
    for word in words:
        if word.isalpha():
            transformed_word = word[1:] + word[0] + "ay"
        else:
            transformed_word = word
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words)

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))