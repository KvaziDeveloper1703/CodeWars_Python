'''
We define a word as any sequence of uppercase English letters A–Z. For any word that contains at least two distinct letters, there exist other “words” made up of the same letters but in a different order. For example, the words STATIONARILY and ANTIROYALIST both consist of the letters AAIILNORSTTY.

We can assign a rank number to every word based on its position in an alphabetically sorted list of all unique permutations of its letters. For example, if we list all words formed by rearranging the letters of a given word in alphabetical order, the first word in the list has rank 1, the second has rank 2, and so on.

Your task is to write a function that, given a word, returns its rank number without generating all permutations explicitly. The algorithm must handle words of up to 25 letters, possibly with repeated letters, and run efficiently.

Определим слово как любую последовательность прописных букв латинского алфавита, не обязательно настоящее слово из словаря. Если в слове есть хотя бы две разные буквы, то можно составить другие слова, состоящие из тех же букв, но в другом порядке. Например, слова STATIONARILY и ANTIROYALIST содержат одинаковые буквы AAIILNORSTTY.

Каждому слову можно присвоить порядковый номер - его позицию в алфавитно отсортированном списке всех возможных перестановок его букв. Первое слово в этом списке имеет номер 1, второе - 2, и так далее.

Твоя задача - написать функцию, которая по данному слову возвращает его порядковый номер, не перебирая все перестановки. Программа должна работать быстро и поддерживать слова длиной до 25 букв, включая повторяющиеся символы.
'''

from math import factorial
from collections import Counter

def list_position(word):
    letters = list(word)
    length = len(letters)
    rank = 1
    factorials = [1] * (length + 1)
    for i in range(1, length + 1):
        factorials[i] = factorials[i - 1] * i
    for i in range(length):
        current_letter = letters[i]
        remaining_letters = Counter(letters[i:])
        for smaller_letter in sorted(set(remaining_letters)):
            if smaller_letter < current_letter:
                remaining_letters[smaller_letter] -= 1
                if remaining_letters[smaller_letter] == 0:
                    del remaining_letters[smaller_letter]
                total_permutations = factorials[len(letters) - i - 1]
                for count in remaining_letters.values():
                    total_permutations //= factorials[count]
                rank += total_permutations
                remaining_letters = Counter(letters[i:])
    return rank