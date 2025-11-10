'''
Write a function that, given a string of text (possibly with punctuation and line breaks), returns an array of the top 3 most frequent words, in descending order of occurrence count.

Assumptions:
- A word is a sequence of letters A–Z (case-insensitive) that may contain apostrophes ' anywhere - at the start, middle, or end;
- Any other characters (#, /, ., \n, etc.) are treated as separators;
- Matching is case-insensitive;
- The words in the result should be lowercased;
- If there are fewer than three unique words, return only the available ones (1 or 2);
- If there are no valid words, return an empty array;
- Ties may be broken arbitrarily.

Напиши функцию, которая принимает строку текста (возможно с пунктуацией и переносами строк) и возвращает массив из трёх самых часто встречающихся слов, в порядке убывания частоты.

Условия:
- Слово - это последовательность букв A–Z (без учёта регистра), в которой могут встречаться апострофы ' в начале, середине или конце.
- Все остальные символы (#, /, ., пробелы, переводы строк и т.д.) считаются разделителями;
- Сравнение слов выполняется без учёта регистра;
- В результирующем массиве все слова должны быть в нижнем регистре;
- Если уникальных слов меньше трёх, вернуть только доступные (1 или 2);
- Если текст не содержит слов, вернуть пустой массив;
- При равной частоте порядок слов может быть произвольным.
'''

import re
from collections import Counter

def top_3_words(text):
    text = text.lower()

    words = re.findall(r"[a-zA-Z']+", text)

    clean_words = []
    for w in words:
        if re.search(r"[a-z]", w):
            clean_words.append(w)

    counts = Counter(clean_words)

    top_three = counts.most_common(3)

    result = []
    for pair in top_three:
        word = pair[0]
        result.append(word)

    return result