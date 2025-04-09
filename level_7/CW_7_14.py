"""
Deoxyribonucleic acid is a chemical found in the nucleus of cells. It carries the "instructions" for the development and functioning of living organisms.
+ In DNA strings, symbols "A" and "T" are complements of each other, as are "C" and "G".
+ Your function receives one side of the DNA and must return the complementary strand.
+ The DNA strand is never empty and is always valid.

Examples:
Input: "ATTGC"
Output: "TAACG"

Input: "GTAT"
Output: "CATA"

Дезоксирибонуклеиновая кислота — это химическое соединение, находящееся в ядре клеток. Оно несёт «инструкции» для развития и функционирования живых организмов.
+ В строках ДНК символы "A" и "T" являются дополняющими друг друга, как и "C" и "G".
+ Ваша функция получает одну сторону ДНК и должна вернуть комплементарную ей сторону.
+ ДНК-строка никогда не будет пустой и всегда будет корректной.

Примеры:
Ввод: "ATTGC"
Вывод: "TAACG"

Ввод: "GTAT"
Вывод: "CATA"

https://www.codewars.com/kata/554e4a2f232cdd87d9000038
"""

def complementary_dna_strand(given_dna_strand):

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    complementary_dna = ""

    for nucleotide in given_dna_strand:
        complement_nucleotide = complement[nucleotide]
        complementary_dna += complement_nucleotide

    return complementary_dna

dna_strand = "ATTGC"
complementary_dna_strand = complementary_dna_strand(dna_strand)
print("Complementary DNA strand: " + complementary_dna_strand)