"""
The goal of this exercise is to convert a string into a new string following these rules:
Each character in the new string:
+ ( if that character appears only once in the original string.
+ ) if that character appears more than once in the original string.

Ignore capitalization when determining if a character is a duplicate.

Examples:
"din"      →  "((("  
"recede"   →  "()()()"  
"Success"  →  ")())())"  
"(( @"     →  "))(("  

Цель этого упражнения — преобразовать строку в новую строку по следующим правилам:
Каждый символ в новой строке:
+ ( — если этот символ встречается только один раз в исходной строке.
+ ) — если этот символ встречается более одного раза в исходной строке.

Регистр букв игнорируется при определении повторяющихся символов.

Примеры:
"din"      →  "((("  
"recede"   →  "()()()"  
"Success"  →  ")())())"  
"(( @"     →  "))(("  
"""

def duplicate_encode(word):
    word = word.lower()
    encoded_string = ""

    for character in word:
        character_count = word.count(character)

        if character_count == 1:
            encoded_string += "("
        else:
            encoded_string += ")"

    return encoded_string

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
