"""
Your task is to sort a given string.
+ Each word in the string contains a single number, which indicates its position in the result.
+ Numbers can be from 1 to 9.
+ If the input string is empty, return an empty string.
+ The input will always contain valid and consecutive numbers.

Examples:
"is2 Thi1s T4est 3a" → "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" → "Fo1r the2 g3ood 4of th5e pe6ople"
"" → ""

Ваша задача — отсортировать заданную строку.
+ Каждое слово в строке содержит одну цифру, которая указывает позицию слова в результате.
+ Числа могут быть от 1 до 9.
+ Если входная строка пустая, вернуть пустую строку.
+ Входные данные всегда содержат валидные и последовательные номера.

Примеры:
"is2 Thi1s T4est 3a" → "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" → "Fo1r the2 g3ood 4of th5e pe6ople"
"" → ""
"""

def order(sentence):

    if not sentence:
        return ""

    words = sentence.split()
    words_with_numbers = []

    for word in words:
        for character in word:
            if character.isdigit():
                number = int(character)
                words_with_numbers.append((number, word))
                break

    sorted_words = sorted(words_with_numbers, key=lambda x: x[0])

    result = [word for _, word in sorted_words]

    return " ".join(result)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
print(order("test5 simple1 a3 is2"))