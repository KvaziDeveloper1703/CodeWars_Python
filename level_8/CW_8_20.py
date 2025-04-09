"""
Write a function that accepts a name and returns the message:
"Hello, <name>! How are you doing today?"

Напишите функцию, которая принимает имя и возвращает сообщение:
"Hello, <имя>! How are you doing today?"

https://www.codewars.com/kata/55a70521798b14d4750000a4
"""

def greet(given_name):
    return f"Hello, {given_name}! How are you doing today?"

name = "Viktor"
greeting = greet(name)
print(greeting)