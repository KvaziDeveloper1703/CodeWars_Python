"""
You are required to replace every letter in a given string with its position in the alphabet.
+ If anything in the text isn't a letter, ignore it and don't include it in the output.

Example:
Input:  "The sunset sets at twelve o' clock."
Output: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

Вам нужно заменить каждую букву в строке её позицией в алфавите.
+ Если в тексте есть небуквенные символы, их нужно игнорировать и не включать в результат.

Пример:
Input:  "The sunset sets at twelve o' clock."
Output: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""

def alphabet_position(text):

    alphabet_dict = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6',
        'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12',
        'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18',
        's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24',
        'y': '25', 'z': '26'
    }

    text = text.lower()

    positions = []

    for character in text:
        if character in alphabet_dict:
            positions.append(alphabet_dict[character])

    return " ".join(positions)

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("Hello, World!"))