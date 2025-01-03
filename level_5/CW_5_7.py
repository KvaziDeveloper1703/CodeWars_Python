"""
Implement a function to apply the ROT13 cipher to a given string. The ROT13 cipher shifts each letter of the Latin/English alphabet by 13 places.

Details:
+ Only letters from the English alphabet (A-Z and a-z) should be transformed. Non-alphabetic characters, such as numbers, spaces, and special symbols, should remain unchanged.
+ If a letter is shifted beyond the end of the alphabet, it should wrap around to the beginning (e.g., Z becomes M, and z becomes m).
+ Avoid using built-in encode or similar functions to solve the task.

Examples:
Input: "Hello, World!" → Output: "Uryyb, Jbeyq!"
Input: "ROT13 example" → Output: "EBG13 rknzcyr"
Input: "12345" → Output: "12345"

Реализуйте функцию, которая применяет шифр ROT13 к заданной строке. Шифр ROT13 сдвигает каждую букву латинского/английского алфавита на 13 позиций.

Детали:
+ Преобразованию подлежат только буквы английского алфавита (A-Z и a-z). Неалфавитные символы, такие как цифры, пробелы и специальные знаки, должны остаться без изменений.
+ Если буква при сдвиге выходит за пределы алфавита, она должна начинаться с начала (например, Z становится M, а z становится m).
+ Использование встроенных функций, таких как encode, для решения задачи не допускается.

Примеры:
Ввод: "Hello, World!" → Вывод: "Uryyb, Jbeyq!"
Ввод: "ROT13 example" → Вывод: "EBG13 rknzcyr"
Ввод: "12345" → Вывод: "12345"

https://www.codewars.com/kata/530e15517bc88ac656000716
"""

def rot13_cipher(message):
    result = []

    for char in message:
        if 'A' <= char <= 'Z':
            shifted = chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
            result.append(shifted)
        elif 'a' <= char <= 'z':
            shifted = chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)

print(rot13_cipher("Hello, World!"))
print(rot13_cipher("ROT13 example"))
print(rot13_cipher("12345"))
