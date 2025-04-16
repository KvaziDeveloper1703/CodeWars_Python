'''
A "word" is defined as any sequence of uppercase letters A–Z (not necessarily a valid dictionary word). For example, "STATIONARILY" and "ANTIROYALIST" are two different words, but they are made up of the same letters — both are anagrams of the sorted sequence "AAIILNORSTTY".
For any word that contains at least two different letters, there are other permutations (words) made up of the same letters but in a different order.
Your task is to write a function that takes a word and returns its rank — the position of the word in the list of all unique permutations of its letters sorted in lexicographic (alphabetical) order. The rank should start from 1 (i.e., the first word in sorted order has rank 1).

Constraints:
+ The input word will be no more than 25 characters long;
+ The word can contain repeated letters;
+ The function should return the rank as an integer;
+ Your solution must be optimized to run in less than 500 milliseconds even for large words.

Examples:
"ABAB" → 2
"AAAB" → 1
"BAAA" → 4
"QUESTION" → 24572
"BOOKKEEPER" → 10743

«Словом» считается любая последовательность заглавных латинских букв от A до Z (не обязательно из словаря). Например, "STATIONARILY" и "ANTIROYALIST" — это разные слова, но они состоят из одинаковых букв, то есть являются анаграммами отсортированной последовательности "AAIILNORSTTY".
Для любого слова, содержащего хотя бы две разные буквы, можно составить и другие перестановки (слова) из тех же букв, но в другом порядке.
Ваша задача — написать функцию, которая принимает слово и возвращает его ранг — позицию этого слова в списке всех уникальных перестановок его букв, отсортированных в лексикографическом (алфавитном) порядке. Ранг должен начинаться с 1 (то есть первое по алфавиту слово имеет ранг 1).

Ограничения:
+ Длина входного слова не превышает 25 символов;
+ Слово может содержать повторяющиеся буквы;
+ Функция должна возвращать ранг в виде целого числа;
+ Решение должно быть оптимизировано и работать менее чем за 500 миллисекунд даже для длинных слов.

Примеры:
"ABAB" → 2
"AAAB" → 1
"BAAA" → 4
"QUESTION" → 24572
"BOOKKEEPER" → 10743

https://www.codewars.com/kata/53e57dada0cb0400ba000688
'''

from math import factorial
from collections import Counter

def permutations_count(counter):
    total = sum(counter.values())
    result = factorial(total)
    for count in counter.values():
        result //= factorial(count)
    return result
    
def list_position(word):
    rank = 1
    counter = Counter(word)
    
    for i, letter in enumerate(word):
        for smaller in sorted(counter):
            if smaller >= letter:
                break
            if counter[smaller] > 0:
                counter[smaller] -= 1
                rank += permutations_count(counter)
                counter[smaller] += 1
        counter[letter] -= 1

    return rank