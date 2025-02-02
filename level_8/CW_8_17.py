"""
Given a year, return the century it belongs to.

Examples:
1705 → 18
1900 → 19
1601 → 17

Дан год. Необходимо определить, к какому веку он относится.

Примеры:
1705 → 18
1900 → 19
1601 → 17
"""

def century(year):
    century = (year + 99) // 100
    return century

print(century(1705))
print(century(1900))
print(century(1601))