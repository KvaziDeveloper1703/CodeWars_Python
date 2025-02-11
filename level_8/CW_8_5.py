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

boolean = input("Write True or False here, please: ")

if boolean == "True":
    boolean = True

if boolean == "False":
    noolean = False
    
answer = bool_to_yes_or_no(boolean)
print(answer)