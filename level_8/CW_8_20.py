"""
Create a function that accepts a name and returns the message:
"Hello, <name>! How are you doing today?"

Создайте функцию, которая принимает имя и возвращает сообщение:
"Hello, <имя>! How are you doing today?"
"""

def greet(name):
    return f"Hello, {name}! How are you doing today?"

name = "Viktor"
greeting = greet(name)
print(greeting)