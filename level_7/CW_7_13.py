"""
Given a string of words, return the length of the shortest word in the string.

Дана строка, содержащая несколько слов. Найдите длину самого короткого слова в строке и верните это значение.
"""

def the_shortest(given_string):
    words = given_string.split()  
    min_length = float('inf')

    for word in words:
        word_length = len(word)
        if word_length < min_length:
            min_length = word_length

    return min_length

string = "Python is amazing"
answer = the_shortest(string)
print(answer)