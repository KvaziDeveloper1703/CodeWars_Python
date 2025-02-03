"""
My friend John and I are members of the "Fat to Fit Club".
John is worried because each month a list of members' weights is published, and he is always last, meaning he is the heaviest.
Since I create the list, I decided to modify the order by introducing a "weight" of numbers:
+ The weight of a number is now the sum of its digits.
+ For example:
    + 99 has a weight of 18.
    + 100 has a weight of 1.
    + So in the sorted list, 100 comes before 99.

Write a function that takes a string with weights of FFC members and sorts them by their "weight".

Additional conditions:
+ If two numbers have the same "weight", they should be sorted as strings.
+ All numbers are positive.
+ The input string may contain extra spaces.

Example:
"56 65 74 100 99 68 86 180 90" → "100 180 90 56 65 74 68 86 99"

Мой друг Джон и я состоим в клубе "Fat to Fit Club".
Джон переживает, потому что каждый месяц публикуется список весов участников, и он всегда последний, что означает, что он самый тяжелый.
Так как я составляю этот список, то решил изменить порядок и ввести "вес" чисел:

+ Вес числа теперь определяется суммой его цифр.
+ Например:
    + 99 имеет вес 18 (9 + 9 = 18).
    + 100 имеет вес 1 (1 + 0 + 0 = 1).
    + Значит, в списке 100 будет раньше, чем 99.

Напишите функцию, которая принимает строку с весами участников и сортирует их по "весу" числа.

Дополнительные условия:
+ Если у чисел одинаковый "вес", то их сравнивают как строки.
+ Все числа в списке положительные.
+ Строка может содержать лишние пробелы.

Пример:
"56 65 74 100 99 68 86 180 90" → "100 180 90 56 65 74 68 86 99"
"""

def order_weight(given_string):
    
    def weight(n):
        return sum(int(digit) for digit in n)
        
    numbers = given_string.split()

    sorted_numbers = sorted(numbers, key=lambda number: (weight(number), number))

    return " ".join(sorted_numbers)

print(order_weight("56 65 74 100 99 68 86 180 90"))  
print(order_weight("103 123 4444 99 2000"))  
print(order_weight("5 15 51"))