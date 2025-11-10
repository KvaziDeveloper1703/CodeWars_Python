'''
There is a secret string that you don’t know. You are given a collection of triplets, each consisting of three letters.

Each triplet represents the order in which the letters appear in the secret string - meaning that in the secret string, the first letter of the triplet appears before the second, and the second appears before the third.

For example, if the secret string is "whatisup", then "whi" is a valid triplet because w comes before h, and h comes before i in the string.

Your task is to reconstruct the original secret string from the given triplets.

You may assume:
    - No letter appears more than once in the secret string;
    - All triplets are valid and together contain enough information to uniquely determine the string;
    - Every letter in the secret string appears in at least one of the triplets.

Есть секретная строка, которую нужно восстановить. Вам даны несколько триплетов - последовательностей из трёх букв.

Каждый триплет показывает относительный порядок букв в секретной строке: первая буква встречается раньше второй, а вторая - раньше третьей.

Например, если секретная строка - "whatisup", то триплет "whi" верный, потому что w идёт раньше h, а h раньше i.

Ваша задача - восстановить оригинальную секретную строку по данным триплетам.

Можно считать, что:
    - Каждая буква встречается в строке не более одного раза;
    - Все триплеты правильные и содержат достаточно информации, чтобы однозначно восстановить строку;
    - Все буквы секретной строки встречаются хотя бы в одном триплете.
'''

def recover_secret(triplets):
    secret = ''
    letters = set()
    for triplet in triplets:
        for ch in triplet:
            letters.add(ch)

    while letters:
        for letter in list(letters):
            if all(letter not in triplet[1:] for triplet in triplets):
                secret += letter
                letters.remove(letter)

                new_triplets = []
                for triplet in triplets:
                    new_triplet = []
                    for x in triplet:
                        if x != letter:
                            new_triplet.append(x)
                    new_triplets.append(new_triplet)
                triplets = new_triplets

                break
    return secret