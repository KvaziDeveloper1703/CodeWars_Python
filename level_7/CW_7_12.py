"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). He is also known for some of his philosophy that he shares on Twitter. When writing on Twitter, Jaden almost always capitalizes every word.
Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized correctly.

Example:
Not Jaden-Cased:
"How can mirrors be real if our eyes aren't real"

Jaden-Cased:
"How Can Mirrors Be Real If Our Eyes Aren't Real"

Джейден Смит, сын Уилла Смита, известен своими ролями в фильмах «Каратэ-пацан» (2010) и «После нашей эры» (2013). Он также прославился своими философскими мыслями, которые публикует в Twitter. Когда Джейден пишет в Twitter, он почти всегда делает каждое слово с заглавной буквы.
Ваша задача — преобразовать строку так, как это сделал бы Джейден Смит. Строки представляют собой его реальные цитаты, но в них отсутствует правильная капитализация.

Пример:
До преобразования:
"How can mirrors be real if our eyes aren't real"

После преобразования:
"How Can Mirrors Be Real If Our Eyes Aren't Real"
"""

def to_jaden_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]  
    jaden_case_string = " ".join(capitalized_words)  

    return jaden_case_string

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))  
print(to_jaden_case("hello world this is python"))  