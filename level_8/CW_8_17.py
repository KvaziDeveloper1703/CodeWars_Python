"""
Given a year, determine the century it belongs to.

Дан год, определите, к какому веку он относится.
"""

def get_century(given_year):
    if given_year % 100 == 0:
        return given_year // 100
    else:
        return (given_year // 100) + 1

year = 1703
century = get_century(year)
print(century)