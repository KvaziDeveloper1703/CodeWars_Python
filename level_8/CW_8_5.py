"""
Write a program that takes a boolean value and return a "Yes" string for True, or a "No" string for False.

Напишите программу, которая принимает логическое значение и возвращает строку "Yes" для True или строку "No" для False.

https://www.codewars.com/kata/53369039d7ab3ac506000467
"""

def bool_to_yes_or_no(given_boolean):
    if given_boolean == True:
        return "Yes"
    else:
        return "No"

my_boolean = input("Write True or False here, please: ")

if my_boolean == "True":
    my_boolean = True

if my_boolean == "False":
    my_noolean = False
    
answer = bool_to_yes_or_no(my_boolean)
print(answer)