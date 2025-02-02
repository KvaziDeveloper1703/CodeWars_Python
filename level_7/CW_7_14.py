"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells. It carries the "instructions" for the development and functioning of living organisms.
+ In DNA strings, symbols "A" and "T" are complements of each other, as are "C" and "G".
+ Your function receives one side of the DNA (as a string) and must return the complementary strand.
+ The DNA strand is never empty and is always valid.

Examples:
"ATTGC" → "TAACG"
"GTAT" → "CATA"

Дезоксирибонуклеиновая кислота (ДНК) — это химическое соединение, находящееся в ядре клеток. Оно несёт «инструкции» для развития и функционирования живых организмов.
+ В строках ДНК символы "A" и "T" являются дополняющими друг друга, как и "C" и "G".
+ Ваша функция получает одну сторону ДНК (в виде строки) и должна вернуть комплементарную ей сторону.
+ ДНК-строка никогда не будет пустой и всегда будет корректной.

Примеры:
"ATTGC" → "TAACG"
"GTAT" → "CATA"
"""

def dna_strand(dna):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    complementary_dna = ""

    for nucleotide in dna:
        complement_nucleotide = complement[nucleotide]
        complementary_dna += complement_nucleotide

    return complementary_dna

print(dna_strand("ATTGC"))
print(dna_strand("GTAT"))
print(dna_strand("AGCT"))
print(dna_strand("CGCG"))