"""
Write a function that takes a string containing multiple words and returns the length of the shortest word in the string.

Напишите функцию, которая принимает строку, содержащую несколько слов, и возвращает длину самого короткого слова в этой строке.

https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
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