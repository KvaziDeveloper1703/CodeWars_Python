"""
Complete the method/function so that it converts dash (-) and underscore (_) delimited words into camel case.
Transformation rules:
+ The first word remains in its original case if it was lowercase (lower camelCase).
+ If the first word was capitalized, it remains capitalized (PascalCase).
+ All following words must be capitalized.

Examples:
"the-stealth-warrior" → "theStealthWarrior"
"The_Stealth_Warrior" → "TheStealthWarrior"
"The_Stealth-Warrior" → "TheStealthWarrior"

Допишите функцию так, чтобы она конвертировала строку с разделителями (- или _) в camelCase.
Правила преобразования:
+ Первое слово остается в исходном регистре, если оно начиналось с маленькой буквы (это lower camelCase).
+ Если первое слово начиналось с заглавной буквы, оно остается заглавным (это PascalCase).
+ Все остальные слова всегда пишутся с заглавной буквы.

Примеры:
"the-stealth-warrior"   → "theStealthWarrior"
"The_Stealth_Warrior"   → "TheStealthWarrior"
"The_Stealth-Warrior"   → "TheStealthWarrior"
"""

def to_camel_case(text):
    if not text:
        return ""

    words = text.replace("-", " ").replace("_", " ").split()

    if not words:
        return ""

    first_word = words[0]
    if first_word[0].islower():  
        result = first_word + "".join(word.capitalize() for word in words[1:])
    else:
        result = "".join(word.capitalize() for word in words)

    return result

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case("hello_world"))
print(to_camel_case("snake_case-text-here"))
print(to_camel_case(""))